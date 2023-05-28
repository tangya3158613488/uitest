import time
from common.config.read_config import get_value


class TestLoginPage:
    def test_login_by_password(self, login):
        userid = get_value("changba", "changba_id")
        password = get_value("changba", "password")
        assert login.login_by_password(userid=userid,password=password).try_to_cannel_popUpWindows()





