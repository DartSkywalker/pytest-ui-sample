from loguru import logger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from pages.locators.sign_up_locators import *
from utils.constants import DEFAULT_WAIT
from utils.email_helper import EmailHelper


class SignUp:
    """
    Login page - registration tab actions
    """

    def __init__(self, browser):
        self.browser = browser

    @staticmethod
    def __get_registration_code():
        eh = EmailHelper()
        return eh.get_registration_code()

    def get(self):
        self.browser.get(SIGN_UP_URL)
        logger.info(f'Loading registration page - {SIGN_UP_URL}')

    def enter_first_name(self, first_name):
        self.browser.find_element(*FIRST_NAME_INPUT).send_keys(first_name)
        logger.info(f'First Name - {first_name}')

    def enter_last_name(self, last_name):
        self.browser.find_element(*LAST_NAME_INPUT).send_keys(last_name)
        logger.info(f'Last Name - {last_name}')

    def enter_email(self, email):
        self.browser.find_element(*EMAIL_INPUT).send_keys(email)
        logger.info(f'User email - {email}')

    def enter_password(self, password):
        self.browser.find_element(*PASSWORD_INPUT).send_keys(password)
        logger.info('User password - *SECURITY ISSUE FOUND*')

    def submit_policy(self):
        policy_confirm = self.browser.find_element(*POLICY_CONFIRM_CHECKBX)
        ActionChains(self.browser).move_to_element(policy_confirm).click(policy_confirm).perform()
        logger.info('Security policy submitted')

    def click_sign_up_btn(self):
        sign_up_btn = self.browser.find_element(*SIGN_UP_BTN)
        ActionChains(self.browser).move_to_element(sign_up_btn) \
            .click_and_hold(sign_up_btn) \
            .click(sign_up_btn) \
            .perform()
        logger.info('Sign Up button clicked')

    def if_confirm_code_input_appears(self):
        if WebDriverWait(self.browser, DEFAULT_WAIT).until(ec.visibility_of_element_located(CONFIRM_CODE)):
            logger.info('Confirmation code input is found')
            return True
        else:
            logger.critical('Confirmation code input is not found!')
            return False

    def enter_registration_code(self):
        code = self.__get_registration_code()
        self.browser.find_element(*CONFIRM_CODE).send_keys(code)
        logger.info(f'Used confirmation code - {code}')
