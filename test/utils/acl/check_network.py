#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys, os


# ??Ό ?€?
print os.getcwd()
data = open("ACL_CHECK_SERVER_LIST.txt", "r")

# ?λ²? ?¬?Έ κ΅¬λΆ? (tuple)
separator_list = (' ', ':')

# ?λ²? ? λ³? ??±
for server_info in data:
    if len(server_info) > 0:
        # ?λ²? ?¬?Έ κ΅¬λΆ? ??Έ ? ??±
        for separator in separator_list:
            if server_info.find(separator) > -1:
                server = server_info.split(separator)
                break

        host = server[0]
        ip = int(server[1])

        try:
            # ?μΌ? ??±
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)

            # ?μΌ? ?°κ²? ??Έ
            s.connect((host, ip))

            # ?±κ³? λ‘κ·Έ
            print "Checking Host : %s:%s ==> Connection Successed" % (host, ip)

        except Exception, e:
            print "Checking Host : %s:%s ==> Connection Failed" % (host, ip)
        finally:
            s.close()

data.close()
print("Done!!")