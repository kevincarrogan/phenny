#!/usr/bin/env python

import requests, re

def fc(phenny, input):
    response = requests.get('http://api.fortunekookie.com/fortune_server.php?code=b76846205c5aa65043c4fa5b8ef75f4f')
    reply = re.search('<front>(.*)\.</front>', response.content).groups()[0] + ' in bed.'
    phenny.say(reply)
fc.commands = ['fc']
fc.example = '.fc'

if __name__ == '__main__':
	print __doc__.strip()
