import unittest
import time
from Inittest import InitTest


class record_voice(InitTest):

    # 录音实时转写,普通话录音时可保存成功
    def test_luyin(self):
        self.luyin.click_luyin()
        self.luyin.luyin_button()
        title = self.luyin.get_title()
        time.sleep(15)
        self.luyin.luyin_stop()
        time.sleep(2)
        self.luyin.luyin_save()
        time.sleep(4)
        title1 = self.luyin.get_title()
        self.assertEqual(title, title1)

    #录音实时转写暂停编辑
    def test_edit(self):
        self.luyin.click_luyin()
        self.luyin.luyin_button()
        time.sleep(15)
        self.luyin.luyin_stop()
        where = self.luyin.click_luyin_text()
        text = where.text
        self.luyin.send_key(where, "测试测试")
        self.luyin.driver.back()
        time.sleep(2)
        self.luyin.luyin_save()
        time.sleep(4)
        where1 = self.luyin.noVIP_wenjian()
        text1 = where1.text
        self.assertIn("测试测试", text1)



if __name__ == '__main__':
    unittest.main(verbosity=2)