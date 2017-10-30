# -*- coding: utf-8 -*-

import requests

def get_content(url):
    print "url: " + url
    res = requests.get(url)
    print "status: "
    print res.status_code
    return res.text

if __name__ == "__main__":
    url = "http://en.wikipedia.org/wiki/Nobel_Prize"
    print get_content(url)


