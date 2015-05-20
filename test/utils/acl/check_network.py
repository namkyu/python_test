#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys, os


# ?ŒŒ?¼ ?˜¤?”ˆ
print os.getcwd()
data = open("ACL_CHECK_SERVER_LIST.txt", "r")

# ?„œë²? ?¬?Š¸ êµ¬ë¶„?ž (tuple)
separator_list = (' ', ':')

# ?„œë²? ? •ë³? ?ŒŒ?‹±
for server_info in data:
    if len(server_info) > 0:
        # ?„œë²? ?¬?Š¸ êµ¬ë¶„?ž ?™•?¸ ?›„ ?ŒŒ?‹±
        for separator in separator_list:
            if server_info.find(separator) > -1:
                server = server_info.split(separator)
                break

        host = server[0]
        ip = int(server[1])

        try:
            # ?†Œì¼? ?ƒ?„±
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)

            # ?†Œì¼? ?—°ê²? ?™•?¸
            s.connect((host, ip))

            # ?„±ê³? ë¡œê·¸
            print "Checking Host : %s:%s ==> Connection Successed" % (host, ip)

        except Exception, e:
            print "Checking Host : %s:%s ==> Connection Failed" % (host, ip)
        finally:
            s.close()

data.close()
print("Done!!")