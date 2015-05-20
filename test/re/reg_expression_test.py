# -*- coding: utf-8 -*-

import re

line = "Cats are smarter then dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
	print "matchObj.group() : ", matchObj.group()
	print "matchObj.group(1) : ", matchObj.group(1)
	print "matchObj.group(2) : ", matchObj.group(2)
else:
	print "No match!!"

# Matching, Searching 테스트
print("\n\n")
matchObj2 = re.match(r'dogs', line, re.M | re.I)
if matchObj2:
	print "match --> matchObj2.group() : ", matchObj2.group()
else:
	print "No match!"

searchObj = re.search(r'dogs', line, re.M | re.I)
if searchObj:
	print "search --> searchObj.group() : ", searchObj.group()
else:
	print "No match!"