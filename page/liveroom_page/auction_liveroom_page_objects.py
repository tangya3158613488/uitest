from appium.webdriver.common.mobileby import MobileBy
from page.liveroom_page import base_liveroom_page_objects


class Android(base_liveroom_page_objects.Android):
    # 工具箱元素
    toolbox_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tool_box_button")'
    # 竞拍模式主持席
    auction_live_host_seat=MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.changba:id/image_seat")'
    # 主持席用户
    auction_live_host_seat_name=MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.changba:id/ktv_auction_live_host_name")'
    # 贵宾席1号
    vip_seat=MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.changba:id/vip_seat_num_one")'

class IOS(base_liveroom_page_objects.IOS):
    # '更多'按钮元素
    more_btn_id = MobileBy.IOS_PREDICATE, 'label = "更多"'
    # '榜单'按钮元素
    rank_btn_id = MobileBy.IOS_PREDICATE, 'label = "排行榜"'
    # '房间'id元素
    room_id_text = MobileBy.IOS_PREDICATE, 'label CONTAINS "房间:" AND type = "XCUIElementTypeStaticText"'
