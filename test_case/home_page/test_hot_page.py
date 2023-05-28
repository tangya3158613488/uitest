import pytest

from page.home_page.hot_page import HotPage
from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector

"""
check 
1.点击投稿跳转到投稿页
2. 断言有小火车，断言点击小火车，跳转到直播、ktv页面
3. 断言点击热门推荐的作品进入作品播放页，歌曲名和播放页歌曲名相同
4. 断言进入全局播放页
"""


class TestHotPage:

    # 该case在my_page.py下编写
    def test_goto_submit_work_page(self, hot_page: HotPage):
        """
        进入投稿页
        :return:
        """
        submit_work_page_obj = hot_page.submit_work_btn_click()
        assert submit_work_page_obj.title() == submit_work_page_obj.assert_title

    def test_check_train_card_displayed(self, hot_page: HotPage):
        """
        测试热门tab小火车是否显示,android 点击头像进到直播页或包房页
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            assert hot_page.train_card_displayed()
        else:
            if hot_page.train_displayed():
                card_type = hot_page.get_state_card()
                print("card is %s" % card_type)
                if card_type == hot_page.LIVE:
                    username = hot_page.get_train_username()[0:2]
                    print("username%s" % username)
                    live_page_obj = hot_page.go_to_train_userhome()
                    if live_page_obj.know_displayed():
                        live_page_obj.know_click()
                    print("live name %s" % live_page_obj.get_live_page_name())
                    live_name = live_page_obj.get_live_page_name()[0:2]
                    live_page_obj.close_live()
                    assert username in live_name
                else:
                    # ktv_page_obj = hot_page.go_to_ktv()
                    # assert ktv_page_obj.is_ktv_room()
                    # ktv_page_obj.quit_ktv_room()
                    pass


if __name__ == "__main__":
    pytest.main(["-s", "test_hot_page.py"])
