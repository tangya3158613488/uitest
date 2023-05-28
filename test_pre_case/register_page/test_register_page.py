from page.register_page.register_page import RegisterPage



class TestRegisterPage:
    def test_register_page(self,register_page:RegisterPage):
        register_page.register_by_phonenumber()
        # register_page.register_by_phonenumber().try_to_cannel_popUpWindows()
