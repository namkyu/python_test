#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
import shutil
import zipfile, os, glob

################################
# function zip 생성
################################
def make_zip(dest_path, backup_file_path):
	zip_file_name = dest_path + "/" + os.path.basename(backup_file_path)
	zip_file = zipfile.ZipFile(zip_file_name + ".zip", "w")
	print "zip_file_name : %s" % zip_file_name

	mode = zipfile.ZIP_DEFLATED

	## 디렉토리인 경우
	if os.path.isdir(backup_file_path):
		print "is directory ==>", backup_file_path
		for path, dir, files in os.walk(backup_file_path):
			for file in files:
				zip_file.write(os.path.join(path, file), os.path.join(path, file), mode)

	## 파일인 경우
	elif os.path.exists(backup_file_path):
		print "is file ==>", backup_file_path
		for name in glob.glob(backup_file_path):
			zip_file.write(name, os.path.basename(name), mode)

	## zip file close
	zip_file.close()

# ===========================================
# execute backup
# ===========================================
def execute_backup():
	# xml file read
	dom_tree = xml.dom.minidom.parse("backup_info.xml")
	collection = dom_tree.documentElement

	backups = collection.getElementsByTagName("backup")
	for backup_info in backups:
		print "####### backup info ######"

		backup_file_path = backup_info.getElementsByTagName('path')[0].childNodes[0].data
		dest_path = backup_info.getElementsByTagName('dest_path')[0].childNodes[0].data
		description = backup_info.getElementsByTagName('description')[0].childNodes[0].data

		print "backup_file_path : %s" % backup_file_path
		print "dest_path : %s" % dest_path
		print "description : %s" % description

		## zip 생성
		make_zip(dest_path, backup_file_path)

# ===========================================
# main
# ===========================================
if __name__ == "__main__":
	execute_backup()