from splinter import Browser


def test_get_countries(browser):
    """Test asynchronous."""

    url = "http://127.0.0.1:8000/get_countries"
    browser = Browser("chrome", headless=True)
    browser.visit(url)

    browser.find_by_id("get-countries-button").click()

    assert browser.is_text_present("Christmas Island", wait_time=10) is True
