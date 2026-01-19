import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import re
import module_other_stx_app
import login_stx_app
import var_stx_app
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller
keyboard = Controller()
import math
wait = WebDriverWait(var_stx_app.driver, 10)






class promotion:



    def use_now(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(2)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.promotion).click()
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.promotion).click()
        time.sleep(2)
        name_promotion = var_stx_app.driver.find_element(By.XPATH, var_stx_app.promotion_code).text
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.use_now1).click()
        time.sleep(2)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_pick_up_point).click()
        time.sleep(3.5)

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Khuyến Mãi(g7)",
                                                      var_stx_app.order_car_promotion, name_promotion, "_KhuyenMai_DungNgay.png")

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_car_back).click()
            time.sleep(2.5)
        except:
            pass
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_car_back).click()
            time.sleep(2.5)
        except:
            pass


    def check_info_promotion(self, code, eventname, result, path_check, name_image):
        var_stx_app.driver.implicitly_wait(0.3)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_promotion)
        except:
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.promotion).click()
                time.sleep(2)
            except:
                pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_promotion)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.promotion).click()
            time.sleep(2)

        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Khuyến Mãi(g7)",
                                                      path_check, "", name_image)


        if name_image == "_KhuyenMai_SoLanSuDung.png":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.promotion_back).click()
            time.sleep(2)
            module_other_stx_app.close_app()



