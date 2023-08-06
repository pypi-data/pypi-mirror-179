#!/usr/bin/python3
# @Time    : 2019-08-21
# @Author  : Kevin Kong (kfx2007@163.com)

import base64
from hashlib import md5
from lxml import etree
import inspect
from itertools import zip_longest
from functools import partial

import requests
import uuid
import time
from copy import copy
import json

URL = "https://bspgw.sf-express.com/std/service"
HKURL = "https://sfapi-hk.sf-express.com/std/service"
SANDBOXURL = "https://sfapi-sbox.sf-express.com/std/service"
TOKEN_URL = "https://sfapi.sf-express.com/oauth2/accessToken"
TOKEN_SANDBOXURL = "https://sfapi-sbox.sf-express.com/oauth2/accessToken"


class BaseService(object):

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return partial(self.__call__, instance)

    def __call__(self, *args, **kwargs):
        # 获取方法的默认值
        vals = tuple(list(args) + list(inspect.getfullargspec(
            self.func).defaults if inspect.getfullargspec(self.func).defaults else []))
        data = {}
        data["service"] = self.__name__
        ags = inspect.getfullargspec(self.func).args
        vdata = dict(zip_longest(ags, vals))
        vdata.update(kwargs)
        if self.options is None:
            vdata = {key: str(value) for key,
                     value in vdata.items() if value and key != 'self'}
        else:
            vdata.pop("self")
            vdata = {k: v for k, v in vdata.items() if v}
            key, start = self.options
            parent_keys = list(vdata.keys())[:start]
            child_keys = list(vdata.keys())[start:]
            vdata.update({key: str(vdata[key])
                          for key in parent_keys if vdata[key] is not None and key != 'self'})
            vdata[key] = {key: str(vdata[key])
                          for key in child_keys if vdata[key] and key != 'self'}
        data.update({
            "data": {
                self.key: vdata
            }
        })
        return args[0].post(data)


class Service(type):

    def __init__(cls, *args, **kwargs):
        pass

    def __new__(cls, name, key=None, options=None):
        attrs = {}
        attrs['__name__'] = name
        attrs["key"] = key if key else name.split("Service")[0]
        attrs["options"] = options
        return type.__new__(cls, name, (BaseService,), attrs)


class Comm(object):
    """封装公共请求"""

    def __get__(self, instance, owner):
        self._clientcode = instance.clientcode
        self._checkword = instance.checkword
        self._sandbox = instance.sandbox
        self.get_access_token()
        return self

    def get_access_token(self):
        """获取AccessToken"""
        url = f"{TOKEN_SANDBOXURL if self._sandbox else TOKEN_URL}?partnerID={self._clientcode}&secret={self._checkword}&grantType=password"
        res = requests.post(url,headers={
            "content-type":"application/x-www-form-urlencoded;charset=UTF-8"
        }).json()
        if res['apiResultCode'] == "A1000":
            self._access_token = res['accessToken']
        else:
            self._access_token = None
        return self._access_token

    def get_public_params(self):
        """获取公共参数"""
        data = {
            "partnerID": self._clientcode,
            "requestID": str(uuid.uuid4()),
            "timestamp": int(time.time()),
            "accessToken": self._access_token
        }
        return data    

    def post(self,service, data):
        """
        提交请求

        param data: 数据结构
        """

        post_data = self.get_public_params()
        copy_data = copy(data)

        for key,value in copy_data.items():
            if value is None:
                data.pop(key)

        post_data.update({
            "serviceCode": service,
            "msgData": json.dumps(data)
        })

        headers = {
            "content-type":"application/x-www-form-urlencoded"
        }

        url = SANDBOXURL if self._sandbox else URL
        res =  requests.post(url, data=post_data, headers=headers).json()
        if res['apiResultCode'] != 'A1000':
            return res
        return json.loads(res['apiResultData'])