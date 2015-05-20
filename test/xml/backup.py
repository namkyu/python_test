#!/usr/bin/python
# -*- coding: utf-8 -*-

import shutil
from xml.dom.minidom import parse
import xml.dom.minidom
import zipfile, os, glob


################################
# function zip ?Éù?Ñ±
################################
def make_zip(dest_path, backup_file_path):
	zip_file_name = dest_path + "/" + os.path.basename(backup_file_path)
	zip_file = zipfile.ZipFile(zip_file_name + ".zip", "w")

	mode = zipfile.ZIP_DEFLATED

	## ?îî?†â?Ü†Î¶¨Ïù∏ Í≤ΩÏö∞
	if os.path.isdir(backup_file_path):
		for path, dir, files in os.walk(backup_file_path):
			for file in files:
				zip_file.write(os.path.join(path, file), os.path.join(path, file), mode)

	## ?åå?ùº?ù∏ Í≤ΩÏö∞
	elif os.path.exists(backup_file_path):
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
		print("####### backup info ######")

		backup_file_path = backup_info.getElementsByTagName('path')[0].childNodes[0].data
		dest_path = backup_info.getElementsByTagName('dest_path')[0].childNodes[0].data
		description = backup_info.getElementsByTagName('description')[0].childNodes[0].data

		print("backup_file_path : %s" % backup_file_path)
		print("dest_path : %s" % dest_path)
		print("description : %s" % description)
		print("\n")

		## zip ?Éù?Ñ±
		make_zip(dest_path, backup_file_path)

# ===========================================
# main
# ===========================================
if __name__ == "__main__":
	execute_backup()