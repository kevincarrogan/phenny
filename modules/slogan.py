#!/usr/bin/env python
"""
slogan.py - Phenny Slogan Module
Copyright (c) 2011 Dafydd Crosby - http://www.dafyddcrosby.com

Licensed under the Eiffel Forum License 2.
"""

import re
import web

uri = 'http://www.sloganizer.net/en/outbound.php?slogan=%s'

def sloganize(word): 
    bytes = web.get(uri % web.urllib.quote(word.encode('utf-8')))
    return bytes

def slogan(phenny, input): 
    word = input.group(2)
    slogan = sloganize(word)

    # Remove HTML tags    
    remove_tags = re.compile(r'<.*?>')
    slogan = remove_tags.sub('', slogan)
    
    if not slogan:
      phenny.say("Looks like an issue with sloganizer.net")
      return
    phenny.say(slogan)

slogan.commands = ['slogan']
slogan.example = '.slogan Granola'

if __name__ == '__main__': 
   print __doc__.strip()
