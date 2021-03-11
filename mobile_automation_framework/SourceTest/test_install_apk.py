#test cases for install .apk file into connected adb device
import unittest
from install_apk import m_install_apk as ins

class Test_install_apk(unittest.TestCase):
    def test_1_path(self):
        exp=True
        act=ins(apk_file_path)
        self.assertEqual(act,exp,'failed  test1')
    def test_2_path(self):
        exp=Exception
        act=ins(apk_file_path1)
        self.assertEqual(act,exp,'failed  test2')

if __name__=="__main__":
    apk_file_path='C:\\Andriod\\platform-tools\\cal.apk'
    apk_file_path1='C:\\Andriod\\platform-tools\\cal.a'
    
    unittest.main()
    

        
        
