from playwright.sync_api import expect

def test_login(login_page_f):
    login_page_f.login("customer@practicesoftwaretesting.com", "welcome01")
    expect(login_page_f.page).to_have_url("https://practicesoftwaretesting.com/account")