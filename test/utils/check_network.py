#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys, os


# check?  ??? ?λ²? λ¦¬μ€?Έ ?? ₯ λ°κΈ°
print("===============================================================================")
print("please write server list")
print("and then if you finish writing server list you have to press CTRL+D !!")
print("===============================================================================")
data = sys.stdin.read()

# ?λ²? ?¬?Έ κ΅¬λΆ? (tuple)
separator_list = (' ', ':')

# ?λ²? ? λ³? ??±
server_info_list = data.split("\n")
for server_info in server_info_list:
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

print("Done!!")