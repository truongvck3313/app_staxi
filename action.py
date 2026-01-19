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
from appium.webdriver.extensions.android.nativekey import AndroidKey





def send_keys1(driver, text_input):
    driver.execute_script("mobile: type", {"text": text_input})



def clear_only(driver, locator, max_length=30, time_wait=30):
    wait = WebDriverWait(driver, time_wait)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
    element.click()
    try:
        element.click()
        time.sleep(1)
        driver.press_keycode(AndroidKey.MOVE_END)
        time.sleep(0.5)
        for _ in range(max_length):  # bấm DEL dư để chắc chắn xoá hết
            driver.press_keycode(AndroidKey.DEL)
    except Exception as e:
        print(f"Không clear được input: {e}")



def wait_for(driver, locator, time_wait=30):
    wait = WebDriverWait(driver, time_wait)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))



def click(driver, locator, time_wait=30):
    wait = WebDriverWait(driver, time_wait)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
    element.click()



def send_keys(driver, locator, text, time_wait=30):
    wait = WebDriverWait(driver, time_wait)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
    element.clear()
    element.send_keys(text)
    print(f"Nhập thành công: '{text}' vào phần tử: '{locator}'")


def delete(driver, locator, time_wait=30):
    wait = WebDriverWait(driver, time_wait)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
    element.send_keys(Keys.CONTROL, "a")



def clear(driver, locator, time_wait=30):
    wait = WebDriverWait(driver, time_wait)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
    element.clear()



def get_text(driver, locator, time_wait=30):
    wait = WebDriverWait(driver, time_wait)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
    text = element.text
    print(text)
    return text






def swipe(driver, startX, startY, endX, endY, duration):
    try:
        driver.swipe(startX, startY, endX, endY, duration)
    except NoSuchElementException:
        print(f"Không thể swipe các điểm  startX: {startX}, startY: {startY}, endX: {endX}, endY: {endY}, duration: {duration}")


def tap(driver, x, y):
    try:
        driver.tap([(x, y)])
    except NoSuchElementException:
        print(f"Không thể tap vào điểm  startX: {x}, startY: {y}")


def zoom(driver, type_zoom, number):
    driver.implicitly_wait(1)
    # Tạo các đối tượng hành động cho thu nhỏ
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    i = 0
    if type_zoom == "Thu nhỏ":
        for i in range(number):
            i = i + 1
            # Ngón tay thứ nhất kéo từ xa về gần trung tâm
            action1.press(x=890, y=270).move_to(x=500, y=700).release()

            # Ngón tay thứ hai kéo từ xa về gần trung tâm
            action2.press(x=50, y=1400).move_to(x=400, y=900).release()

            # Kết hợp hai hành động thành MultiAction
            pinch_action = MultiAction(driver)
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
            pinch_action = MultiAction(driver)
            pinch_action.add(action1, action2)
            pinch_action.perform()
            time.sleep(1)
            print(f"Đã phóng to {i} lần")









