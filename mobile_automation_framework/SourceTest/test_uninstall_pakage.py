#test cases for uninstall app or application in the device using adb command line
import unittest
from uninstall_pakage import m_uninstall_pak as unins

class Test_uninstall_pakage(unittest.TestCase):
    def test_1_pakage(self):
        expect=True
        actual=unins(pkg_name)
        self.assertEqual(actual,expect,"failed test1")

if __name__=="__main__":
    pkg_name='com.bak.mnr.calculatrice'
    unittest.main()
