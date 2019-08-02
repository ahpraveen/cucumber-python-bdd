from behave import *
from pages import seleniumhq_home_page

@given('launch browser and go to about link page')
def step_search(self):
    self.driver = seleniumhq_home_page.launch_browser("chrome")
    seleniumhq_home_page.click_about_link(self.driver)

@when('enter search input and click go')
def step_2(self):
    seleniumhq_home_page.enter_search(self.driver,"Automation")
    seleniumhq_home_page.click_go(self.driver)

@then('google custom search page is displayed')
def step_3(self):
    assert "Google Custom Search" == self.driver.title