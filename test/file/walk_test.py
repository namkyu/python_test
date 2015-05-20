import os, zipfile


Z = zipfile.ZipFile('E:/test/python/backup_dir/teste.zip', 'w')
for path, directory, files in os.walk('E:/test/python/src_dir'):
	for ff in files:
		Z.write(os.path.join(path, ff), os.path.join(path, ff))
Z.close()

Z1 = zipfile.ZipFile('E:/test/python/backup_dir/teste1.zip', 'w')
for path, directory, files in os.walk('E:/test/python/src_dir/test2.txt'):
	for ff in files:
		Z1.write(os.path.join(path, ff), os.path.join(path, ff))
Z1.close()


for root, dirs, files in os.walk("E:/test/python/src_dir", topdown=False):
	for name in files:
		print(os.path.join(root, name))
	for name in dirs:
		print(os.path.join(root, name))