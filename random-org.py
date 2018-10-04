#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by onlymyflower on 2018年10月04日22:06:43
# FileName: random-org.py

import requests
import json

url = "https://api.random.org/json-rpc/1/invoke"

def readFileToLine(filePath):
    import os
    file = open(filePath, 'r')
    l = ""
    for line in file.readlines():
        l += line.rstrip('\n').rstrip('\r')
    return l

def postRequest():
    toPost = readFileToLine("post.json")
    # print(toPost)
    # print(json.dumps(toPost))
    # data = requests.post(url, data=json.dumps(toPost)).text
    data = requests.post(url, data=toPost).text
    return data

def main():
    # print(readFileToLine("post.json"))
    print(postRequest())


if __name__ == '__main__':
    main()