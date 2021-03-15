from loguru import logger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.locators.side_bar_locators import *
from pages.locators.sign_up_locators import *
from utils.constants import DEFAULT_WAIT


class Sidebar:
    """
    Main page's sidebar actions
    """

    def __init__(self, browser):
        self.browser = browser

    def open_my_account_dd(self):
        """
        Click on the "My Account" dropdown on the main page
        """
        WebDriverWait(self.browser, DEFAULT_WAIT).until(EC.visibility_of_element_located(MY_ACCOUNT_DD))
        my_account_drop_down = self.browser.find_element(*MY_ACCOUNT_DD)
        ActionChains(self.browser).move_to_element(my_account_drop_down).click().perform()
        logger.info('Clicked on "My Account dropdown"')

    def logout(self):
        """
        Click on the Logout list element in the "My Account" dropdown
        """
        WebDriverWait(self.browser, DEFAULT_WAIT).until(EC.visibility_of_element_located(LOGOUT_BTN))
        self.browser.find_element(*LOGOUT_BTN).click()
        logger.info('Signing out from the system')

    def if_correct_email_in_my_account(self, email):
        """
        Check if the correct user email appears in the User Data in "My Account" dropdown
        :param email: string
        :return: boolean
        """
        if WebDriverWait(self.browser, DEFAULT_WAIT)\
                .until(lambda email_text: self.browser.find_element(*EMAIL_DIV).text == email):
            logger.info('Verified the correct email in user data')
            return True
        else:
            logger.critical(f'Getting {self.browser.find_element(*EMAIL_DIV).text} in user data instead of {email}')
            return False

    def if_logout_successful(self):
        """
        Check if user successfully logged out by the current email
        :return: boolean
        """
        if WebDriverWait(self.browser, DEFAULT_WAIT)\
                .until(lambda browser: self.browser.current_url == SIGN_UP_URL):
            logger.info('Successfully logged out from the system')
            return True
        else:
            logger.critical(f'Failed to log out - currently on {self.browser.current_url} page')
            return False
