import pytest
from page.public_page.client_utils_page import ClientUtilsPage
from page.sing_page.sing_page import SingPage


@pytest.fixture()
def sing_page(client_utils_page: ClientUtilsPage):
    """
    sing tab页
    :param client_utils_page:
    :return:
    """
    return client_utils_page.go_to_tab_bar_master().sing_tab_click()


@pytest.fixture()
def sing_page_need_into_ktv(client_utils_page: ClientUtilsPage):
    """
    sing tab页
    :param client_utils_page:
    :return:
    """
    return client_utils_page.go_to_tab_bar().sing_tab_click()


@pytest.fixture()
def search_page(sing_page: SingPage):
    """
    搜索页面
    :param client_utils_sing_page:
    :return:
    """
    return sing_page.search_frame_click()


@pytest.fixture()
def ordered_page(sing_page: SingPage):
    """
    已点页面
    :param client_utils_sing_page:
    :return:
    """
    return sing_page.ordered_btn_click()


@pytest.fixture()
def song_details_page(sing_page: SingPage):
    """
    歌曲详情页
    :param client_utils_sing_page:
    :return:
    """
    return sing_page.song_cell_click()


@pytest.fixture()
def singer_page(sing_page: SingPage):
    """
    歌手页
    :param client_utils_sing_page:
    :return:
    """
    return sing_page.singer_btn_click()

@pytest.fixture()
def singer_details_page(sing_page: SingPage):
    """
    歌手详情页
    :param client_utils_sing_page:
    :return:
    """
    return sing_page.singer_btn_click().hot_see_more_btn_click().click_single_cell()


@pytest.fixture(autouse=True)
def tear_down_sing_page(client_utils_page: ClientUtilsPage):
    """
    自动返回点歌台页面
    :param client_utils_page:
    :return:
    """
    yield
