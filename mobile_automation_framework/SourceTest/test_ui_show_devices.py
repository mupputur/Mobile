#test cases for create user interface to click the button to display adb command response
import unittest
from ui_show_devices import show_dev

class Test_ui_show_devices(unittest.TestCase):
    def test_1_device(self):
        expect=True
        actual=show_dev(cmd,button_name)
        self.assertEqual(actual,expect,"failed test1")

if __name__=="__main__":
        cmd='adb devices'
        button_name="show devices"
        unittest.main()
