#!/usr/bin/env python

def stache(phenny, input):
    """Responds when someone mentions the bot nickname"""
    inp = input.group()

    phenny.say(input.nick + ": " + 'http://mustachify.me/?src=' + inp)
stache.rule = r'(https?:\/\/[^ #]+\.(?:png|jpg|jpeg))(?:[#]\.png)?'
stache.priority = 'low'
