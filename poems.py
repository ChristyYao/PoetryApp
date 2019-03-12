#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:27:19 2019

@author: christyyao
"""

import http.client

conn = http.client.HTTPSConnection("www.poemist.com")
conn.request("GET", "/api/v1/randompoems")
res = conn.getresponse()
data = res.read()
print(data)