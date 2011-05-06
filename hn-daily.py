#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from xml.etree.ElementTree import parse
import re

url = "http://www.daemonology.net/hn-daily/index.rss"

f = urllib.urlopen(url)
tree = parse(f)
root = tree.getroot()
channel = root.find('channel')
item = channel.find('item')
title = item.find('title')
print title.text

desc = item.find('description')
stories = re.findall('<span class="storylink"><a href="(.*)">(.*)</a>', desc.text)
comments = re.findall('<span class="commentlink"><a href="(.*)">.*</a>', desc.text)
if stories and comments:
    i = 0
    for story in stories:
        print ("%2d: %s\n    link: %s" % (i+1, story[1], story[0])).encode('utf-8')
        print "    comment: %s\n" % comments[i]
        i += 1

