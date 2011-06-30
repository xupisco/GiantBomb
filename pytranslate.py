#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import urllib
import re

langCode={ "arabic":"ar", "bulgarian":"bg", "chinese":"zh-CN", "croatian":"hr", "czech":"cs", "danish":"da", "dutch":"nl", "english":"en", "finnish":"fi", "french":"fr", "german":"de", "greek":"el", "hindi":"hi", "italian":"it", "japanese":"ja", "korean":"ko", "norwegian":"no", "polish":"pl", "portuguese":"pt", "romanian":"ro", "russian":"ru", "spanish":"es", "swedish":"sv", "galician": "gl" }

def setUserAgent(userAgent):
    urllib.FancyURLopener.version = userAgent
    pass

def translate(text, fromLang="English", toLang="Portuguese"):
    # urllib.FancyURLopener.version = "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008070400 SUSE/3.0.1-0.1 Firefox/3.0.1"
    setUserAgent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008070400 SUSE/3.0.1-0.1 Firefox/3.0.1")
    try:
        post_params = urllib.urlencode({"langpair":"%s|%s" %(langCode[fromLang.lower()],langCode[toLang.lower()]), "text":text,"ie":"UTF8", "oe":"UTF8"})
    except KeyError, error:
        print "Currently we do not support %s" %(error.args[0])
        return
        
    page = urllib.urlopen("http://translate.google.com/translate_t", post_params)
    content = page.read()
    page.close()
    match = re.search("'#fff'\">(.*?)</span>", content)
    value = match.groups()[0]
    return value.decode('utf-8')