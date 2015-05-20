# -*- coding: utf-8 -*-

import ftplib
import os
import sys


# ?””? ‰?† ë¦? ?´?™
print os.getcwd()
os.chdir("E:/test/python")


def gettext(ftp, filename, outfile=None):
    # fetch a text file
    if outfile is None:
        outfile = sys.stdout
    # use a lambda to add newlines to the lines read from the server
    ftp.retrlines("RETR " + filename, lambda s, w=outfile.write: w(s+"\n"))

def getbinary(ftp, filename, outfile=None):
    # fetch a binary file
    if outfile is None:
        outfile = sys.stdout
    ftp.retrbinary("RETR " + filename, outfile.write)

def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    print("ext : " + ext)
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file, "rb"))
    else:
		ftp.storbinary("STOR " + file, open(file, "rb"), 1024)

# FTP ë¡œê·¸?¸
ftp = ftplib.FTP("lnk1982.cafe24.com")
ftp.login("nklee", "rbdn2001")

# FTP ?„œë²? ?Š¹? • ?ŒŒ?¼ ?‚´?š© ì¶œë ¥
gettext(ftp, "test/python/ftp_test.txt")

# FTP ?„œë²? ?””? ‰?† ë¦? ë¦¬ìŠ¤?Š¸ ì¶œë ¥
data = []
ftp.dir(data.append)
for line in data:
    print "-", line

# FTP ?ŒŒ?¼ ?—…ë¡œë“œ
#upload(ftp, "upload_test.txt")



# ftp ?‚˜ê°?ê¸?
ftp.quit()