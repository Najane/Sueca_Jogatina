from behave import given, when, then
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time


caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "7e1c07d9"
caps["appPackage"] = "com.riva.sueca"
caps["appActivity"] = "com.riva.sueca.activity.SplashActivity"
caps["automationName"] = "UiAutomator2"
caps["ensureWebviewsHavePages"] = True
caps["locale"] = "BR"
caps["language"] = "pt"


@given('que eu esteja na pagina Home')
def go_to_page(context):
    context.driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub", caps)
    print("awaint 15s before skipping google accounts")
    time.sleep(15)
    TouchAction(context.driver).tap(x=521, y=489).perform()
    print("\n Google Account skipped await 5 seconds to next step")
    time.sleep(5)


@when('o idioma do device esta em Português')
def create_todo(context):
    assert caps["language"] == "pt"


@then('existe um botao com o texto "{texto}"')
def check_todo(context, texto):
    el1 = context.driver.find_element_by_id(
        "com.riva.sueca:id/buttonSinglePlayer")

    time.sleep(15)
    result = el1.text
    el1.click()
    context.driver.quit()
    assert texto == result
