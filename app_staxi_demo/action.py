from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from appium.options.common import AppiumOptions
import var_stx_app
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException




def find_element(locator):
    try:
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(0.5)
    except TimeoutException:
        print(f"Không tìm thấy phần tử: {locator}")


def click(locator):
    try:
        time.sleep(0.5)
        wait = WebDriverWait(var_stx_app.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        element.click()
        time.sleep(0.5)
    except TimeoutException:
        print(f"Không click được vào phần tử: {locator}")


def send_keys(locator, text):
    try:
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(0.5)
        element.clear()
        element.send_keys(text)
        print(f"Nhập thành công: '{text}' vào phần tử: '{locator}'")
        time.sleep(0.5)
    except TimeoutException:
        print(f"Không nhập được: '{text}' \nDo không tìm thấy hoặc không thể thao tác trên phần tử: '{locator}'")


def delete(locator):
    try:
        time.sleep(0.5)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        element.send_keys(Keys.CONTROL, "a")
        time.sleep(0.5)
    except TimeoutException:
        print(f"Không xóa được text phần tử: {locator}")


def clear(locator):
    try:
        time.sleep(0.5)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        element.clear()
        time.sleep(0.5)
    except TimeoutException:
        print(f"Không xóa được text phần tử: {locator}")


def print_text(locator):
    try:
        time.sleep(0.5)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        text = var_stx_app.driver.find_element(By.XPATH, locator).text
        return text
        # print(f"text: {text}")
    except NoSuchElementException:
        print(f"Không tìm thấy phần tử: {locator}")


def wail_until(locator, time_s):
    wait = WebDriverWait(var_stx_app.driver, time_s)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
    time.sleep(0.5)
    # try:
    #     wait = WebDriverWait(var_stx_app.driver, time_s)
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
    #     time.sleep(1)
    # except NoSuchElementException:
    #     print(f"Không tìm thấy phần tử: {locator}")
    #     return None


def swipe(startX, startY, endX, endY, duration):
    try:
        var_stx_app.driver.swipe(startX, startY, endX, endY, duration)
        time.sleep(0.5)
    except NoSuchElementException:
        print(f"Không thể swipe các điểm  startX: {startX}, startY: {startY}, endX: {endX}, endY: {endY}, duration: {duration}")


def tap(x, y):
    try:
        var_stx_app.driver.tap([(x, y)])
        time.sleep(0.5)
    except NoSuchElementException:
        print(f"Không thể tap vào điểm  startX: {x}, startY: {y}")


def zoom(type_zoom, number):
    var_stx_app.driver.implicitly_wait(1)
    # Tạo các đối tượng hành động cho thu nhỏ
    action1 = TouchAction(var_stx_app.driver)
    action2 = TouchAction(var_stx_app.driver)
    i = 0
    if type_zoom == "Thu nhỏ":
        for i in range(number):
            i = i + 1
            # Ngón tay thứ nhất kéo từ xa về gần trung tâm
            action1.press(x=890, y=270).move_to(x=500, y=700).release()

            # Ngón tay thứ hai kéo từ xa về gần trung tâm
            action2.press(x=50, y=1400).move_to(x=400, y=900).release()

            # Kết hợp hai hành động thành MultiAction
            pinch_action = MultiAction(var_stx_app.driver)
            pinch_action.add(action1, action2)
            pinch_action.perform()
            time.sleep(1)
            print(f"Đã thu nhỏ {i} lần")


    if type_zoom == "Phóng to":
        for i in range(number):
            i = i + 1
            # Ngón tay thứ nhất kéo từ xa về gần trung tâm
            action1.press(x=500, y=700).move_to(x=890, y=270).release()

            # Ngón tay thứ hai kéo từ xa về gần trung tâm
            action2.press(x=400, y=900).move_to(x=50, y=1400).release()

            # Kết hợp hai hành động thành MultiAction
            pinch_action = MultiAction(var_stx_app.driver)
            pinch_action.add(action1, action2)
            pinch_action.perform()
            time.sleep(1)
            print(f"Đã phóng to {i} lần")









