from selenium.webdriver.common.by import By

from Create_project_QA.pages.base_page import BasePage


button_selector = ("link text", "Click")
# button_selector = (By.XPATH, "//a[@href='#']")
result_selector = ("id", 'result-text')


class LikeAButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://www.qa-practice.com/elements/button/like_a_button")

    @property
    def button(self):
        return self.find(button_selector)

    @property
    def button_is_displayed(self):
        return self.button.is_displayed()

    def click_button(self):
        self.button.click()

    @property
    def result(self):
        return self.find(result_selector)

    @property
    def result_text(self):
        return self.result.text
