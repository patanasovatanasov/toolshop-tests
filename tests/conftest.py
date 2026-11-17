import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page_f(page):
    lp = LoginPage(page)
    lp.open()
    return lp