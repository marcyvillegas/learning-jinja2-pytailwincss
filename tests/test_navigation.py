from splinter import Browser


def test_navigation(browser):
    """Test asynchronous."""

    url = "http://127.0.0.1:8000/navigation"
    browser = Browser("chrome", headless=True)
    browser.visit(url)

    browser.find_by_id("go-to-countries").click()

    assert browser.url == "http://127.0.0.1:8000/get_countries"
