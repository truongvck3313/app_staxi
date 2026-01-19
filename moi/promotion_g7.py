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
import var_stx_app
wait = WebDriverWait(var_stx_app.driver_customer, 10)
import action





class promotion:



    def use_now(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.promotion, time_wait=1)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.promotion)

        try:
            name_promotion = action.get_text(var_stx_app.driver_customer, var_stx_app.promotion_code, time_wait=1)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_back1)
            action.click(var_stx_app.driver_customer, var_stx_app.promotion)

        name_promotion = action.get_text(var_stx_app.driver_customer, var_stx_app.promotion_code)
        action.click(var_stx_app.driver_customer, var_stx_app.use_now1)
        action.click(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.PROMOTION1, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Khuyến Mãi(g7)",
                                                      var_stx_app.PROMOTION1, name_promotion, "_KhuyenMai_DungNgay.png")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.order_car_back, time_wait=1)
            time.sleep(2)
        except:
            pass
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.order_car_back, time_wait=1)
            time.sleep(2)
        except:
            pass




    def check_info_promotion(self, code, eventname, result, path_check, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.promotion_code, time_wait=1)
        except:
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.promotion, time_wait=2)
                time.sleep(2)
            except:
                pass


        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.promotion_code, time_wait=1.5)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.promotion)


        try:
            action.wait_for(var_stx_app.driver_customer, path_check, time_wait=5)
        except:
            pass


        module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_customer, code, eventname, result, "Khuyến Mãi(g7)",
                                                      path_check, "", name_image)


        if name_image == "_KhuyenMai_SoLanSuDung.png":
            action.click(var_stx_app.driver_customer, var_stx_app.promotion_back)
            time.sleep(1.5)
            # module_other_stx_app.reset_app_image()





