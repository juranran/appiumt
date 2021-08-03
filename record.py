from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction


class Luyin():
    def __init__(self, plateformname, palatformversion, devicename):
        self.desired_caps={"platformName": plateformname,
                           "platformVersion": palatformversion,
                           "deviceName": devicename,
                           "appPackage": 'com.hudun.androidrecorder',
                           "appActivity": 'com.hudun.androidrecorder.module.start.activity.WelcomeNewActivity',
                           "noReset": "True"}
        #self.desired_caps['platformName']=plateformname

        #模拟器设备
        #self.desired_caps['platformVersion']=palatformversion
        #self.desired_caps['deviceName']=devicename
        #self.desired_caps['app']=r'F:\学习资料\第四章软件\App\kaoyan3.1.0.apk'

        #self.desired_caps['appPackage']='com.hudun.androidrecorder'
        #self.desired_caps['appActivity']='com.hudun.androidrecorder.module.start.activity.WelcomeNewActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(5)
        #self.app_name=self.driver.find_element_by_accessibility_id("录音转文字")
        #self.app_name.click()
        # self.driver.implicitly_wait(2)
        # self.yinsi = self.driver.find_element_by_id("com.hudun.androidrecorder:id/agreenView")
        # self.yinsi.click()
        # self.driver.implicitly_wait(4)
        # self.libao = self.driver.find_element_by_id("com.hudun.androidrecorder:id/btn_cancel")
        # self.libao.click()
        # self.back = self.driver.find_element_by_id("com.hudun.androidrecorder:id/btn_close")
        # self.back.click()


    #点击录音实时转写
    def click_luyin(self):
        luyin_shishi = self.driver.find_element_by_id("com.hudun.androidrecorder:id/record_translate_img")
        luyin_shishi.click()
    #申请权限
    def allow_cunchu(self):
        cunchu = self.driver.find_element_by_id("com.hudun.androidrecorder:id/btn_right")
        cunchu.click()
    #系统权限
    def sys_allow(self):
        print(self.driver.page_source)
        sys = self.driver.find_element_by_id("com.lbe.security.miui:id/permission_allow_foreground_only_button")
        sys.click()

    #点击录音按钮
    def luyin_button(self):
        luyin = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout"
                                                  "/android.widget.LinearLayout/android.widget.FrameLayout"
                                                  "/android.widget.RelativeLayout/android.widget.RelativeLayout"
                                                  "/android.widget.LinearLayout/android.widget.LinearLayout"
                                                  "/android.widget.RelativeLayout[2]")
        luyin.click()
        #TouchAction(self.driver).press(x=229, y=1763).move_to(x=214, y=1987).release().perform()

    #暂停按钮
    def luyin_stop(self):
        stop = self.driver.find_element_by_id("com.hudun.androidrecorder:id/cb_record_btn")
        stop.click()
    #点击选择语言
    def click_language(self):
        language = self.driver.find_element_by_id("com.hudun.androidrecorder:id/tv_scene_and_language")
        language.click()
    #语言选择框
    def select_language(self):
        cancel = self.driver.find_element_by_id("com.hudun.androidrecorder:id/btnCancel")
        changjing_title = self.driver.find_element_by_id("com.hudun.androidrecorder:id/tvTitle")
        queren = self.driver.find_element_by_id("com.hudun.androidrecorder:id/btnSubmit")
        select_changjing = self.driver.find_elements_by_id("com.hudun.androidrecorder:id/options1")
        select_yuzhong = self.driver.find_elements_by_id("com.hudun.androidrecorder:id/options2")
        select_yuyan = self.driver.find_elements_by_id("com.hudun.androidrecorder:id/options3")
        for x in select_yuzhong:
            print(x.text)
        print(select_changjing.text, select_yuyan.text, select_yuzhong.text)
    #点击开通会员
    def huiyuan_button(self):
        huiyuan = self.driver.find_element_by_id("com.hudun.androidrecorder:id/no_vip_hint_txt")
        huiyuan.click()
    #获取标题
    def get_title(self):
        title = self.driver.find_element_by_id("com.hudun.androidrecorder:id/title_bar_text")
        return title.text

    #录音权限
    def allow_luyin(self):
        click_luyin = self.driver.find_element_by_id("com.hudun.androidrecorder:id/btn_right")
        click_luyin.click()
    #录音文本区
    def click_luyin_text(self):
        luyin_text = self.driver.find_element_by_id("com.hudun.androidrecorder:id/et_recognize_result")
        luyin_text.click()
        return luyin_text
    #录音文本区输入测试内容
    def send_key(self, where, words):
        where.send_keys(words)

    #录音保存
    def luyin_save(self):
        save = self.driver.find_element_by_id("com.hudun.androidrecorder:id/btn_save")
        save.click()
    #非VIP文件详情
    def noVIP_wenjian(self):
        wenjian = self.driver.find_element_by_id("com.hudun.androidrecorder:id/edit_recognize_result")
        return wenjian
    #点击外部导入
    def audio_import(self):
        audioimport = self.driver.find_element_by_id('com.hudun.androidrecorder:id/import_audio_img')
        audioimport.click()
    #分类名
    def sort_name(self):
        sorts = self.driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                   '/android.widget.FrameLayout/android.view.ViewGroup'
                                                   '/android.widget.HorizontalScrollView/android.widget.LinearLayout'
                                                   '/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView')
        sort_name_dict = {}
        for x in sorts:
            name = x.text[:x.text.find('(')]
            sort_name_dict[name] = x
        return sort_name_dict
    #小提示
    def point(self):
        small_point = self.driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                         '/android.widget.FrameLayout/android.view.ViewGroup'
                                                         '/android.view.ViewGroup[2]/android.widget.TextView')
        Point = ""
        for x in small_point:
            Point = Point+x.text
        #小提示：1.找到文件，分享到"录音转文字助手"，也能导入哦~2.目前支持的音频格式有：MP3、WAV、M4A、AMR、WMA、OGG、AAC、FLAC，单个文件大小不得超过800M及3小时。
        return Point

    #点击排序
    def sort_click(self):
        sort = self.driver.find_element_by_id('com.hudun.androidrecorder:id/iv_title_bar_right2')
        sort.click()

    #获取排序文本
    def sort_text(self):
        text = self.driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout'
                                              '/android.widget.FrameLayout/android.widget.LinearLayout'
                                              '/android.widget.FrameLayout/android.widget.LinearLayout'
                                              '/android.widget.RelativeLayout/android.widget.TextView')
        sorttext = {}
        for x in text:
            sorttext[x.text] = x
        return sorttext

    #文件日期
    def file_time(self):
        filetime = self.driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                      '/android.widget.FrameLayout/android.view.ViewGroup'
                                                      '/androidx.viewpager.widget.ViewPager/android.view.ViewGroup'
                                                      '/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView'
                                                      '/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]')
        time_list = []
        for x in filetime:
            time_list.append(x.text)

        return time_list
    #文件大小
    def file_size(self):
        filesize = self.driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                      '/android.widget.FrameLayout/android.view.ViewGroup'
                                                      '/androidx.viewpager.widget.ViewPager/android.view.ViewGroup'
                                                      '/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView'
                                                      '/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[3]')
        size_list = []
        for x in filesize:
            size_list.append(x.text)
        return size_list

if __name__ == '__main__':
    luyin = Luyin('Android', '7.1.2', '127.0.0.1:62001')
    luyin.audio_import()
    luyin.point()

