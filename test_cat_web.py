#/usr/bin/env python
# -*- coding=utf-8 -*-
 
import urllib.request #Import urllib.request instead of urllib.

def post(url, data):
    req = urllib.request.urlopen(url)
    data = urllib.urlencode(data)
    #enable cookie
    opener = urllib.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data)
    return response.read()

def main():
    posturl = "http://wjw.sysu.edu.cn/sign_in"
    data = {'username':'12353235', 'password':'01020010'}
    print (post(posturl, data))

if __name__ == '__main__':
    main()
