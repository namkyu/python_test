# -*- coding: utf-8 -*-

import unittest
import os
import glob, shutil, time

from kyu.utils.release import execute_main, hot_deploy_releae

class ReleaseTest(unittest.TestCase):

    @unittest.skip("skip")
    def test_rc(self):
        param = "mode=release#profile_active=rc#project_name=project,project2#gportal_path=E:/test/python/release/gportal#java_home=C:/jdk1.7.0_25#war_home=E:/test/python/release#tar_path=E:/test/python/release/project.tar.gz"
        execute_main(param)
    
    @unittest.skip("skip")
    def test_op(self):
        param = "mode=release#profile_active=op#project_name=project,project2#gportal_path=E:/test/python/release/gportal#java_home=C:/jdk1.7.0_25#war_home=E:/test/python/release/%s"
        execute_main(param)
        
    @unittest.skip("skip")
    def test_other(self):
        param = "ROOT#5.war"
        print(param.split(".")[0])
        
    def test_directory(self):
        root_files = []
        for root, dirs, files in os.walk("E:/test/war/", topdown=False):
            root_files = files
        
        wab_app_path = "test/aa/ROOT"
        print(wab_app_path.rfind("/"))
        print(wab_app_path[0:wab_app_path.rfind("/")])
        print("wab_app_path=" + wab_app_path)
        
        default_version = 1
        if not root_files:
            print "List is empty"
            new_version = default_version  
            print(new_version)          
        else:        
            root_files.sort()
            print(root_files)
    
            latest_war_file = max(root_files)
            start_num = latest_war_file.rfind("#") + 1
            end_num = latest_war_file.rfind(".")
            version = int(latest_war_file[start_num:end_num])
            new_version = default_version + 1
            print("## 기존 최신 버전")
            print(version)
            print("## 신규 버전")
            print(new_version)
        
        original_war_name = "TestApp-Front.war"
        rename_war_name = "ROOT##%d.war" % new_version
        print(rename_war_name)
        
        shutil.copy2("E:/test/war/war_home/" + original_war_name, "E:/test/war/" + rename_war_name)
        print("source=" + ("E:/test/war/war_home/" + original_war_name) + ", dest=" + ("E:/test/war/" + rename_war_name))
        
        time.sleep(5)
        for idx, file in enumerate(root_files):
            if file != rename_war_name:                
                print(file)
                os.remove("E:/test/war/" + file)
                shutil.rmtree("E:/test/war/" + file.split(".")[0]) # war 파일이 deploy되면서 풀린 folder 삭제
        
        if os.path.isdir("E:/test/war/ROOT"):
            shutil.rmtree("E:/test/war/ROOT")
            
            
        os.makedirs("E:/test/war/webapps/ROOT")
