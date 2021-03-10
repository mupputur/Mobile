#test cases for reboot the connected device through adb
import unittest
from reboot_device import reboot_dev as rdev

class Test_reboot_device(unittest.TestCase):
    def test_1_device(self):
        expect=True
        actual=rdev(cmd_list)
        self.assertEqual(actual,expect,"failed test1")

if __name__=="__main__":
        cmd_list=['adb devices','adb reboot']
        unittest.main()
