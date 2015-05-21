# -*- coding: utf-8 -*-

import unittest

from kyu.utils.release import execute_main

class ReleaseTest(unittest.TestCase):

    def rc_test(self):
        param = "mode=release#profile_active=rc#project_name=project,project2#gportal_path=E:/test/python/release/gportal#java_home=C:/jdk1.7.0_25#war_home=E:/test/python/release#tar_path=E:/test/python/release/project.tar.gz"
        execute_main(param)
        
    def op_test(self):
        param = "mode=release#profile_active=op#project_name=project,project2#gportal_path=E:/test/python/release/gportal#java_home=C:/jdk1.7.0_25#war_home=E:/test/python/release/%s"
        execute_main(param)