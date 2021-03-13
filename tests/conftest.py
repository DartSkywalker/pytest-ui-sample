import logging
from datetime import datetime

import pytest
from loguru import logger
from selenium import webdriver
from _pytest.logging import caplog as _caplog


@pytest.fixture
def caplog(_caplog):
    class PropogateHandler(logging.Handler):
        def emit(self, record):
            logging.getLogger(record.name).handle(record)

    handler_id = logger.add(PropogateHandler(), format="{message} {extra}")
    logger.add(f'actions-{datetime.now().strftime("%m%d%Y-%H:%M:%S")}.log')
    yield _caplog
    logger.remove(handler_id)


def pytest_namespace():
    return {'reg_email': None}


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver
    driver.quit()
