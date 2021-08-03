import copy
import unittest
from Inittest import InitTest


class record_import(InitTest):
    def test_audio_import(self):
        #验证分类名字展示正确
        #点击导入音频
        self.luyin.audio_import()
        sort_name_dict = self.luyin.sort_name()
        sort_name = []
        for x in sort_name_dict.keys():
            sort_name.append(x)
        true_sort_name = ['全部音频', '文件库', '微信', 'QQ', '系统录音']
        self.assertEqual(sort_name, true_sort_name)
        #验证提示正确
        point = self.luyin.point()
        true_text = '小提示：1.找到文件，分享到"录音转文字助手"，也能导入哦~2.目前支持的音频格式有：MP3、WAV、M4A、AMR、WMA、OGG、AAC、FLAC，单个文件大小不得超过800M及3小时。'
        self.assertEqual(point, true_text)
    #验证排序
    def test_sort(self):
        #点击导入音频
        self.luyin.audio_import()
        #点击排序
        self.luyin.sort_click()
        #获取排序文本
        sorttext = self.luyin.sort_text()

        sorttext_list = []
        for x in sorttext.keys():
            sorttext_list.append(x)
        true_sort_text = ['新文件优先', '旧文件优先', '大文件优先', '小文件优先', '取消']
        self.assertEqual(true_sort_text, sorttext_list)
        #新文件优先
        sorttext.get(sorttext_list[0]).click()
        time_list = self.luyin.file_time()
        true_time_list = copy.copy(time_list)
        true_time_list.sort(reverse=True)
        self.assertEqual(true_time_list,time_list)
        #旧文件优先
        self.luyin.sort_click()
        sorttext = self.luyin.sort_text()
        sorttext.get(sorttext_list[1]).click()
        time_list = self.luyin.file_time()
        true_time_list = copy.copy(time_list)
        true_time_list.sort(reverse=False)
        self.assertEqual(true_time_list,time_list)
        #大文件优先
        self.luyin.sort_click()
        sorttext = self.luyin.sort_text()
        sorttext.get(sorttext_list[2]).click()
        size_list = self.luyin.file_size()
        list3 = []
        for x in size_list:
            if 'MB' in x:
                x = float(x[:-2]) * 1024
            elif 'KB' in x:
                x = float(x[:-2])
            list3.append(x)

        true_size_list = copy.copy(list3)
        true_size_list.sort(reverse=True)
        self.assertEqual(true_size_list, list3)
        #小文件优先
        self.luyin.sort_click()
        sorttext = self.luyin.sort_text()
        sorttext.get(sorttext_list[3]).click()
        size_list = self.luyin.file_size()
        list3 = []
        for x in size_list:
            if 'MB' in x:
                x = float(x[:-2]) * 1024
            elif 'KB' in x:
                x = float(x[:-2])
            list3.append(x)
        true_size_list = copy.copy(list3)
        true_size_list.sort(reverse=False)
        self.assertEqual(true_size_list, list3)





if __name__ == '__main__':
    unittest.main(verbosity=2)