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


@given('que esteja na pagina de Preferências')
def go_to_page(context):
    context.driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub", caps)
    time.sleep(20)
    TouchAction(context.driver).tap(x=537, y=436).perform()
    time.sleep(5)

    el1 = context.driver.find_element_by_id(
        "com.riva.sueca:id/buttonSettings")
    el1.click()
    time.sleep(10)


@when('arrasto a tela até o fim da página')
def step_impl(context):
    TouchAction(context.driver).press(x=816, y=1455).move_to(
        x=786, y=629).release().perform()
    # el1.click()
    time.sleep(5)


@when(u'vejo a versão do App')
def check_todo(context):
    el2 = context.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[9]/android.widget.RelativeLayout")
    el2.click()
    time.sleep(15)


@then(u'valido se a versão é "{texto}"')
def step_impl(context, texto):
    el3 = context.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[9]/android.widget.RelativeLayout/android.widget.TextView[2]")
    el3.click()
    time.sleep(5)
    result = el3.text
    el3.click()
    context.driver.quit()
    assert texto == result
