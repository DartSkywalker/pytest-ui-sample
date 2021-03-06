from loguru import logger
from selenium.webdriver.common.action_chains import ActionChains

from pages.locators.sign_in_locators import *


class SignIn:
    """
    Login page - sign in tab
    """

    def __init__(self, browser):
        self.browser = browser

    def get(self):
        """
        Navigate to the login page
        """
        self.browser.get(SIGN_IN_URL)
        logger.info(f'Loading login page - {SIGN_IN_URL}')

    def enter_email(self, email):
        """
        Enter user email in the corresponding field on the login tab
        :param email: string
        """
        self.browser.find_element(*EMAIL_AUTH).send_keys(email)
        logger.info(f'User email - {email}')

    def enter_password(self, password):
        """
        Enter user password in the corresponding field on the login tab
        :param password: string
        """
        self.browser.find_element(*PASS_AUTH).send_keys(password)
        logger.info(f'User password - do not even hope :)')

    def click_sign_in_btn(self):
        """
        Click on the Sign In button on the login tab
        """
        sign_up_btn = self.browser.find_element(*SIGN_IN_BTN)
        ActionChains(self.browser).move_to_element(sign_up_btn) \
            .click_and_hold(sign_up_btn) \
            .click(sign_up_btn) \
            .perform()
        logger.info('Sign In button clicked')
