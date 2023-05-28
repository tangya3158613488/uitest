import pytest

from page.sing_page.sing_page import SingPage


class TestClassifyPage:

    def test_into_mandarin_classify_page(self, sing_page: SingPage):
        """
        进入国语分类二级页面
        :return:
        """
        mandarin_classify_page_obj = sing_page.classify_btn_click().mandarin_classify_btn_click()
        page_title_txt = mandarin_classify_page_obj.get_page_title()
        assert (page_title_txt == '国语') is True


if __name__ == "__main__":
    pytest.main(["-s", "test_classify_page.py"])
