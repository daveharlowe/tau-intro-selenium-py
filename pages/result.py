"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

class DuckDuckGoResultPage:

    RESULTS_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    def ___init___(self, browser):
        self.browser = browser

    def result_link_titles(self):
        # TODO
        return []

    def search_input_value(self):
        # TODO
        return ""

    def title(self):
        # TODO
        return ""