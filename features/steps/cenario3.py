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


@given(u'que eu esteja na pagina de Preferências')
def step_impl(context):
    context.driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub", caps)
    time.sleep(20)
    TouchAction(context.driver).tap(x=537, y=436).perform()
    time.sleep(10)

    el1 = context.driver.find_element_by_id(
        "com.riva.sueca:id/buttonSettings")
    el1.click()
    time.sleep(10)


@given('troque a Ordem dos jogadores para Sentido Anti-Horário')
def step_impl(context):
    el2 = context.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.RelativeLayout")
    el2.click()
    time.sleep(5)
    el3 = context.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]")
    el3.click()
    time.sleep(3)


@when('estiver selecionado')
def step_impl(context):
    el4 = context.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.RelativeLayout")
    el4.click()
    time.sleep(5)
    el5 = context.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").is_selected()
    time.sleep(5)
    # el5.click()


@then('foi feita a troca')
def step_impl(context):
    context.driver.quit()
