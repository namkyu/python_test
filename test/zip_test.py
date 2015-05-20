import glob, os
import zipfile


# file = zipfile.ZipFile("E:/test/python/zip_test/test.zip", "w")
#
# for name in glob.glob("E:/test/python/src_dir/*"):
# 	print name
# 	print os.path.basename(name)
# 	file.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
#
# file.close()
print "######## os.path.basename TEST"
print os.path.basename("c:/test/test.txt")
print os.path.basename("c:/test/")

