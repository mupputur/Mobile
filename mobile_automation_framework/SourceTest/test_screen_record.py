#test cases for To connect adb device to perform screen record store in device and pull to our system one copy
import unittest
from screen_record import screen_rec as srec

class Test_screen_record(unittest.TestCase):
    def test_1_device(self):
        expect=True
        actual=srec(cmd_list,s_path_filename,d_path_filename,d_filename)
        self.assertEqual(actual,expect,"failed test1")

if __name__=="__main__":
    cmd_list=['adb devices','adb shell screenrecord ','adb pull ']
    s_path_filename='//sdcard//s_record.mp4 '
    d_path_filename='D:\\adb_fastboot\\d_record.mp4'
    d_filename="d_record.mp4"
    unittest.main()
