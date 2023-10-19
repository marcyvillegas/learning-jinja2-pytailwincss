from splinter import Browser

def test_some_browser_stuff(browser):
    """Test using real browser."""
    url = "http://127.0.0.1:8000/sample_macro"
    browser = Browser('chrome')
    browser.visit(url)

    assert browser.is_text_present('This is a content') is True