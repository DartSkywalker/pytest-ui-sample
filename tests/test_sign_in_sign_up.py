import pytest

from pages.sidebar import Sidebar
from pages.sign_in import SignIn
from pages.sign_up import SignUp
from utils.constants import *
from utils.data_generator import DataGenerator


@pytest.mark.dependency()
def test_user_registration(browser, caplog):
    """
    The test case automated to verify the ability to create a new user in the system
    Objectives:
        1. Validate the ability to enter registration parameters
        2. Validate the confirmation code was send to a mentioned email
        3. Validate the correct email displayed in user data
        4. Validate the ability to log out from the system after signing up
    """

    su = SignUp(browser)
    sb = Sidebar(browser)

    # Data generation (not the best way)
    dg = DataGenerator(EMAIL_USER)
    reg_email = dg.get_login_data()
    pytest.reg_email = reg_email

    # Enter parameters
    su.get()
    su.enter_first_name(USER_FIRST_NAME)
    su.enter_last_name(USER_LAST_NAME)
    su.enter_email(reg_email)
    su.enter_password(USER_PASSWORD)
    su.submit_policy()
    su.click_sign_up_btn()

    # Assert whether the input for the email confirmation appears
    assert su.if_confirm_code_input_appears()

    # Gathering data from the confirmation email
    su.enter_registration_code()

    # Verify that the correct email displayed in user data
    sb.open_my_account_dd()
    assert sb.if_correct_email_in_my_account(reg_email)

    # Logout from the system
    sb.logout()
    assert sb.if_logout_successful()


@pytest.mark.dependency(depends=['test_user_registration'])
def test_user_auth(browser, caplog):
    """
    The test case automated to verify the ability to login into a system with a newly registered user
    Chained with the registration test case 'test_user_registration'
    Objectives:
        1. Validate the ability to enter registration parameters
        2. Validate the correct email displayed in user data
    """
    si = SignIn(browser)
    sb = Sidebar(browser)

    # Enter user credentials
    si.get()
    si.enter_email(pytest.reg_email)
    si.enter_password(USER_PASSWORD)
    si.click_sign_in_btn()

    # Verify that the correct email displayed in user data
    sb.open_my_account_dd()
    assert sb.if_correct_email_in_my_account(pytest.reg_email)
