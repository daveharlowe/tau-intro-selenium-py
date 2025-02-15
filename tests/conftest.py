"""
This module contains shared fixtures
"""
import webbrowser

import pytest
import selenium.webdriver

@pytest.fixture

def browser():

    # Initialise the Chromedriver instance
    b = selenium.webdriver.Chrome()

    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(10)

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()
