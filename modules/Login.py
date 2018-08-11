from robotpageobjects import Page
from robot.utils import asserts


class Login(Page):

    def __init__(self):
        Page.__init__(self)

    selectors = {
        "username_input":   "css=#username",
        "user_password":    "css=#password",
        "login_button":     "css=#submit",
        "lets_go_jquery":   '$(".center.btn.btn-primary.width-full")[0].click();',
        "register_jquery":  "$('p.mt-md a')[0].click();",
        "continue_jquery":  '$(".btn.btn-primary.btn-block.uppercase.next").click();',
    }

    def login_to_outfittery(self, username, password, isValid=True):
        self._open_browser_page("https://www.outfittery.com/login/auth")
        self.input_text("username_input", username)
        self.input_text("user_password", password)
        self.click_button("login_button")
        if isValid:
            # assert if My orders is present when logged in with valid user
            asserts.assert_true(self._is_text_present("My orders"))
        else:
            # assert if expected message is shown when logged in with invalid credentials
            asserts.assert_true(self._is_text_present("The combination of e-mail and password is not correct."))
        return self

    def validate_lets_go(self):
        self._open_browser_page("https://www.outfittery.com/")
        self.execute_javascript(self.selectors['lets_go_jquery'])
        # Check if clicking on 'lets' go takes to leisure choice selection
        asserts.assert_true(self._is_text_present('LEISURE STYLES'))
        return self

    def validate_atleast_one_leisure_selection_alert(self):
        self._open_browser_page("https://www.outfittery.com/login/auth")
        self.execute_javascript(self.selectors['register_jquery'])
        self.execute_javascript(self.selectors['continue_jquery'])
        # Check if clicking on continue without leisure choice selection gives expected message
        asserts.assert_true(self._is_text_present('Please select at least 1 option.'))
        return self

    def _open_browser_page(self, url):
        self.open(url)
        self.maximize_browser_window()
