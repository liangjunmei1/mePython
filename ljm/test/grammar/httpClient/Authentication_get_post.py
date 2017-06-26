#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
身份认证
"""
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
import requests

"""基本认证"""
r = requests.get("https://api.github.com/user",auth=HTTPBasicAuth('liangjunmei1','liangjunmei0'))
r = requests.get("https://api.github.com/user",auth=('liangjunmei1','liangjunmei0'))

"""摘要认证"""
url = "http://httpbin.org/digest-auth/auth/user/pass"
r = requests.get(url,auth=HTTPDigestAuth('liangjunmei1','liangjunmei0'))
print r.status_code

