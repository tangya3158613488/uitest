#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
from page.my_page.customer_my_page import CustomerMyPage


class TestCustommerMyPage:

    def test_click_fans_number_btn(self, customer_my_page: CustomerMyPage):
        """
        点击粉丝
        :param my_page:
        :return:
        """
        fans_page = customer_my_page.click_fans_number_btn()
        assert fans_page.in_my_fans_page()

    def test_click_my_group_btn(self, customer_my_page: CustomerMyPage):
        """
        点击Ta的群组
        :param my_page:
        :return:
        """
        my_group_page = customer_my_page.click_my_group_btn()
        assert my_group_page.in_other_group_page()

    def test_click_song_list_btn(self, customer_my_page: CustomerMyPage):
        """
        点击歌单
        :param customer_my_page:
        :return:
        """
        song_list_page = customer_my_page.click_song_list_btn()
        assert song_list_page.in_song_list_page()

    def test_click_data_tab_btn(self, customer_my_page: CustomerMyPage):
        """
        点击资料tab
        :param click_data_tab_btn:
        :return:
        """
        customer_my_page.click_data_tab_btn()
        assert customer_my_page.data_tab_show()

    def test_click_photo_btn(self, customer_my_page: CustomerMyPage):
        """
        点击资料tab下的相册
        :param customer_my_page:
        :return:
        """
        photo_album = customer_my_page.click_photo_btn()
        assert photo_album.in_photo_album_page()

    def test_click_dynamic_tab_btn(self, customer_my_page: CustomerMyPage):
        """
        点击动态tab
        :param customer_my_page:
        :return:
        """
        customer_my_page.click_dynamic_tab_btn()
        print(customer_my_page.appium_driver.get_page_source())
        assert customer_my_page.dynamic_cell_show()

    def test_click_more_btn(self, customer_my_page: CustomerMyPage):
        """
        点击更多按钮
        :return:
        """
        # customer_my_page.click_more_btn()
        assert customer_my_page.more_cell_show()
