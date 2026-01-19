import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import homepage_driver
import homepage_g7
import var_stx_app
import module_other_stx_app
from retry import retry
import action
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from pynput.keyboard import Key, Controller
keyboard = Controller()

path_user = var_stx_app.checklistpath
username = path_user.split("/")[2]
print(username)

# from var_stx_app import var_stx_app.driver_driver, var_stx_app.driver_customer
import var_stx_app




def login_driverg7(self, type):
    if username == "truongtq.BA":  # Máy Truongtq
        # driver_g7.logout_driver_g7(self)
        if type == "Xe thường":
            driver_g7.login_driver_g7(self, "auto409", "atgmj123", "29E04479")
        if type == "Xe sân bay":
            print("n11")
            driver_g7.login_driver_g7(self, "auto383", "atgmj123", "29A96320")   #29A1240(test)    #29A96320(staging)   ĐINH MẠNH CƯỜNG
    else:
        if type == "Xe thường":
            driver_g7.login_driver_g7(self, "auto82", "atgmj123", "30E05364")
        if type == "Xe sân bay":
            driver_g7.login_driver_g7(self, "auto376", "atgmj123", "30A76818")  #30E48956(test)    #30A76818(staging)








class g7:

    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def login_g7(self, phone):
        # var_stx_app.reset_app(var_stx_app.driver_customer)
        var_stx_app.open_app(var_stx_app.driver_customer)
        homepage_g7.homepage_g7_back()
        n = 0
        while (n < 5):
            n = n + 1
            n = str(n)
            try:
                action.wait_for(var_stx_app.driver_customer, var_stx_app.favorite_spot, time_wait=10)
                break
            except:
                pass

            try:
                action.clear_only(var_stx_app.driver_customer, var_stx_app.login_phone, time_wait=1)
            except:
                # var_stx_app.reset_app(var_stx_app.driver_customer)
                var_stx_app.open_app(var_stx_app.driver_customer)

                try:
                    action.wait_for(var_stx_app.driver_customer, var_stx_app.favorite_spot, time_wait=10)
                    break
                except:
                    pass
            action.clear_only(var_stx_app.driver_customer, var_stx_app.login_phone)
            time.sleep(0.5)
            action.send_keys1(var_stx_app.driver_customer, phone)
            time.sleep(1)
            action.click(var_stx_app.driver_customer, var_stx_app.continue1)


            action.send_keys(var_stx_app.driver_customer, var_stx_app.otp1, "9")
            action.send_keys(var_stx_app.driver_customer, var_stx_app.otp2, "9")
            action.send_keys(var_stx_app.driver_customer, var_stx_app.otp3, "9")
            action.send_keys(var_stx_app.driver_customer, var_stx_app.otp4, "9")
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.confirm, time_wait=1)
            except:
                var_stx_app.driver_customer.back()
                time.sleep(1)
                action.click(var_stx_app.driver_customer, var_stx_app.confirm)



            try:
                action.wait_for(var_stx_app.driver_customer, var_stx_app.home_page, time_wait=10)
                time.sleep(1)
                break
            except:
                # var_stx_app.reset_app(var_stx_app.driver_customer)
                var_stx_app.open_app(var_stx_app.driver_customer)

            try:
                action.click(var_stx_app.driver_customer, var_stx_app.confirm, time_wait=1)
                time.sleep(2)
            except:
                pass
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.allow, time_wait=1)
                time.sleep(1)
            except:
                pass
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.ALLOW, time_wait=1)
                time.sleep(1)
            except:
                pass
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.allow, time_wait=1)
                time.sleep(1)
            except:
                pass
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.SKIP, time_wait=1)
                time.sleep(1)
            except:
                pass
            n = int(n)



    def login_g7_close_app(self, phone):
        n = 0
        while (n < 5):
            n = n + 1
            n = str(n)
            if n == "1":
                # var_stx_app.reset_app(var_stx_app.driver_customer)
                var_stx_app.open_app(var_stx_app.driver_customer)
                try:
                    action.wait_for(var_stx_app.driver_customer, var_stx_app.login_phone, 6)
                except:
                    # var_stx_app.reset_app(var_stx_app.driver_customer)
                    var_stx_app.open_app(var_stx_app.driver_customer)
            try:
                action.wait_for(var_stx_app.driver_customer, var_stx_app.home_page, 7)
                break
            except:
                try:
                    action.clear_only(var_stx_app.driver_customer, var_stx_app.login_phone)
                    time.sleep(0.5)
                    action.clear_only(var_stx_app.driver_customer, var_stx_app.login_phone)
                    time.sleep(0.5)
                    action.send_keys1(var_stx_app.driver_customer, phone)
                except:
                    action.clear_only(var_stx_app.driver_customer, var_stx_app.login_phone)
                    time.sleep(0.5)
                    action.send_keys1(var_stx_app.driver_customer, phone)
                time.sleep(1)
                action.click(var_stx_app.driver_customer, var_stx_app.continue1)
                time.sleep(7)
                action.send_keys(var_stx_app.driver_customer, var_stx_app.otp1, "9")
                action.send_keys(var_stx_app.driver_customer, var_stx_app.otp2, "9")
                action.send_keys(var_stx_app.driver_customer, var_stx_app.otp3, "9")
                action.send_keys(var_stx_app.driver_customer, var_stx_app.otp4, "9")
                action.click(var_stx_app.driver_customer, var_stx_app.confirm)
                try:
                    action.wait_for(var_stx_app.driver_customer, var_stx_app.home_page, 7)
                except:
                    break
            n = int(n)



    def display_login_g7(self):
        n = 0
        while (n < 3):
            n = n + 1
            n = str(n)

            try:
                action.wait_for(var_stx_app.driver_customer, var_stx_app.login_phone, time_wait=1.5)
                break
            except:
                g7.logout_g7(self)


            try:
                var_stx_app.open_app(var_stx_app.driver_customer)
                # var_stx_app.reset_app(var_stx_app.driver_customer)
                time.sleep(5)
                g7.logout_g7(self)
                break
            except:
                var_stx_app.open_app(var_stx_app.driver_customer)
                # var_stx_app.reset_app(var_stx_app.driver_customer)


            try:
                action.click(var_stx_app.driver_customer, var_stx_app.confirm1, time_wait=1)
                time.sleep(3)
            except:
                pass

            try:
                action.click(var_stx_app.driver_customer, var_stx_app.allow, time_wait=1)
                time.sleep(1)
            except:
                pass
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.ALLOW, time_wait=1)
                time.sleep(1)
            except:
                pass
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.allow, time_wait=1)
                time.sleep(1)
            except:
                pass
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.SKIP, time_wait=1)
                time.sleep(1)
            except:
                pass

            n = int(n)



    def logout_g7(self):
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.account, time_wait=3)
            time.sleep(1.5)
            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.5, 0.8, 0.5, 0.3, 1000)
            time.sleep(1)
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.g7_icon_logout, time_wait=5)
            except:
                action.click(var_stx_app.driver_customer, var_stx_app.logout, time_wait=5)
            action.click(var_stx_app.driver_customer, var_stx_app.igree, time_wait=5)
            action.wait_for(var_stx_app.driver_customer, var_stx_app.login_phone, time_wait=15)
            print("logout g7 thành công")
        except:
            print("logout g7 thất bại")



    def change_language(self, code, eventname, result, path_button, desire, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)
        if name_image == "_G7_DoiNgonNgu_TiengAnh.png":
            var_stx_app.reset_app(var_stx_app.driver_customer)
            # var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.login_phone)
        except:
            # var_stx_app.reset_app(var_stx_app.driver_customer)
            g7.display_login_g7(self)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.icon_language)
        except:
            var_stx_app.reset_app(var_stx_app.driver_customer)
            g7.logout_g7(self)

        action.click(var_stx_app.driver_customer, var_stx_app.icon_language)
        action.click(var_stx_app.driver_customer, path_button)
        action.click(var_stx_app.driver_customer, var_stx_app.igree_language)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_change_language, time_wait=5)
        except:
            # var_stx_app.reset_app(var_stx_app.driver_customer)
            var_stx_app.open_app(var_stx_app.driver_customer)
        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Màn hình đăng nhập(g7) - Đổi ngôn ngữ",
                                                  var_stx_app.check_change_language, desire, name_image)



    def register(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.login_phone)
        except:
            g7.display_login_g7(self)

        action.click(var_stx_app.driver_customer, var_stx_app.register)

        action.clear(var_stx_app.driver_customer, var_stx_app.register_phone)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.register_phone, var_stx_app.data['login']['register_phone'])

        action.clear(var_stx_app.driver_customer, var_stx_app.register_name)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.register_name, var_stx_app.data['login']['register_name'])

        action.wait_for(var_stx_app.driver_customer, var_stx_app.register_sex)

        action.click(var_stx_app.driver_customer, var_stx_app.register_brith_day)
        action.click(var_stx_app.driver_customer, var_stx_app.confirm1)

        action.clear(var_stx_app.driver_customer, var_stx_app.register_email)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.register_email, var_stx_app.data['login']['register_email'])

        action.clear(var_stx_app.driver_customer, var_stx_app.register_address)

        action.send_keys(var_stx_app.driver_customer, var_stx_app.register_address, var_stx_app.data['login']['register_address'])

        time.sleep(1)
        var_stx_app.driver_customer.swipe(330, 1130, 85, 330, 600)
        time.sleep(1.5)
        action.wait_for(var_stx_app.driver_customer, var_stx_app.register_referral_code)

        action.click(var_stx_app.driver_customer, var_stx_app.register_checkbox)
        action.click(var_stx_app.driver_customer, var_stx_app.register)

        action.wait_for(var_stx_app.driver_customer, var_stx_app.check_register, time_wait=7)
        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Màn hình đăng nhập(g7) - Đăng ký",
                                                  var_stx_app.check_register, "Tài khoản của bạn đã tồn tại trên hệ thống, bạn hãy đăng nhập để tiếp tục sử dụng.", "_G7_DangKy.png")


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.login, time_wait=1)
            time.sleep(2.5)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.register_phone, time_wait=2)
            action.click(var_stx_app.driver_customer, var_stx_app.register_back)
            time.sleep(2)
        except:
            pass

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.otp_back, time_wait=2)
            time.sleep(2)
        except:
            pass


    def login_sdt(self, code, eventname, result, phone_number, path_check, desire, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.login_phone, time_wait=1)
        except:
            g7.display_login_g7(self)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.login_phone, time_wait=1)
            time.sleep(1)
            action.clear(var_stx_app.driver_customer, var_stx_app.login_phone)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.login_phone, time_wait=1)
        except:
            g7.display_login_g7(self)


        action.click(var_stx_app.driver_customer, var_stx_app.login_phone)
        action.clear_only(var_stx_app.driver_customer, var_stx_app.login_phone)
        var_stx_app.driver_customer.execute_script("mobile: type", {"text": phone_number})

        action.click(var_stx_app.driver_customer, var_stx_app.continue1)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.register_back, time_wait=5)
            var_stx_app.driver_customer.swipe(300, 1100, 300, 600, 1000)
            time.sleep(1)
        except:
            pass

        action.wait_for(var_stx_app.driver_customer, path_check, time_wait=10)
        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Màn hình đăng nhập(g7)",
                                                  path_check, desire, name_image)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.register_phone, time_wait=1)
            action.click(var_stx_app.driver_customer, var_stx_app.register_back, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.otp1, time_wait=1)
            action.click(var_stx_app.driver_customer, var_stx_app.otp_back, time_wait=1)
            time.sleep(2)
        except:
            pass





class driver_g7:


    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def login_driver_g7(self, user, password, vehicle):
        # var_stx_app.reset_app(var_stx_app.driver_driver)
        var_stx_app.open_app(var_stx_app.driver_driver)
        homepage_driver.homepage_g7_drive_back()

        n = 0
        while (n < 5):
            n = n + 1
            n = str(n)
            try:
                action.wait_for(var_stx_app.driver_driver, var_stx_app.notification, time_wait=10)
                break
            except:
                pass

            try:
                action.click(var_stx_app.driver_driver, var_stx_app.check_end_of_shift, time_wait=1)
                action.wait_for(var_stx_app.driver_driver, var_stx_app.notification, time_wait=7)
                break
            except:
                pass

            try:
                action.clear(var_stx_app.driver_driver, var_stx_app.login_driver_user, time_wait=1)
            except:
                homepage_driver.homepage_g7_drive_back()
                try:
                    action.wait_for(var_stx_app.driver_driver, var_stx_app.notification, time_wait=1)
                    break
                except:
                    pass

            action.clear(var_stx_app.driver_driver, var_stx_app.login_driver_user)
            action.send_keys(var_stx_app.driver_driver, var_stx_app.login_driver_user, user)

            action.clear(var_stx_app.driver_driver, var_stx_app.login_driver_password)
            action.send_keys(var_stx_app.driver_driver, var_stx_app.login_driver_password, password)

            action.clear(var_stx_app.driver_driver, var_stx_app.login_driver_vehicle)
            action.send_keys(var_stx_app.driver_driver, var_stx_app.login_driver_vehicle, vehicle)

            try:
                action.click(var_stx_app.driver_driver, var_stx_app.login_buttonlogin1, time_wait=5)
            except:
                action.click(var_stx_app.driver_driver, var_stx_app.check_end_of_shift, time_wait=5)
            time.sleep(2)
            var_stx_app.driver_driver.tap([(450, 500)])
            time.sleep(0.5)
            var_stx_app.driver_driver.tap([(450, 500)])
            time.sleep(0.5)

            try:
                action.click(var_stx_app.driver_driver, var_stx_app.ALLOW, time_wait=1)
                time.sleep(1.5)
            except:
                pass
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.allow, time_wait=1)
                time.sleep(1)
            except:
                pass
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.ALLOW, time_wait=1)
                time.sleep(1)
            except:
                pass
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.skip, time_wait=1)
                time.sleep(2)
            except:
                pass

            try:
                action.wait_for(var_stx_app.driver_driver, var_stx_app.notification, time_wait=7)
                break
            except:
                pass
            n = int(n)



    def logout_driver_g7(self):
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=1)
        except:
            pass
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=3)
            action.click(var_stx_app.driver_driver, var_stx_app.leave)
            action.click(var_stx_app.driver_driver, var_stx_app.leave1)
        except Exception as e:
            print(f"Không rời ca được: {e}")

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_end_of_shift, time_wait=10)
            print("logout g7 driver thành công")
        except:
            print("logout g7 driver thất bại")



    def check_login_driver_g7(self, code, eventname, result, user, password, vehicle, path_check, desire, name_image):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.login_driver_user, time_wait=1)
        except:
            login_driverg7(self, "Xe sân bay")
            driver_g7.logout_driver_g7(self)

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.skip, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.clear(var_stx_app.driver_driver, var_stx_app.login_driver_user, time_wait=2)
        except:
            driver_g7.logout_driver_g7(self)



        if name_image == "_LaiXeG7_DangNhapSai.png":
            action.clear(var_stx_app.driver_driver, var_stx_app.login_driver_user)
            action.send_keys(var_stx_app.driver_driver, var_stx_app.login_driver_user, user)

            action.clear(var_stx_app.driver_driver, var_stx_app.login_driver_password)
            action.send_keys(var_stx_app.driver_driver, var_stx_app.login_driver_password, password)

            action.clear(var_stx_app.driver_driver, var_stx_app.login_driver_vehicle)
            action.send_keys(var_stx_app.driver_driver, var_stx_app.login_driver_vehicle, vehicle)

            action.click(var_stx_app.driver_driver, var_stx_app.icon_hide_passwork)
            time.sleep(1)
            action.click(var_stx_app.driver_driver, var_stx_app.login_buttonlogin1)
            time.sleep(3)
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.ALLOW, time_wait=1)
                time.sleep(2)
            except:
                pass

            try:
                action.wait_for(var_stx_app.driver_driver, path_check, time_wait=5)
            except:
                pass

            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Màn hình đăng nhập(Lái xe G7)",
                                                          path_check, desire, name_image)

            try:
                action.click(var_stx_app.driver_driver, var_stx_app.dismis, time_wait=1)
            except:
                pass
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.skip, time_wait=1)
            except:
                pass
            time.sleep(1)


        else:
            login_driverg7(self, "Xe sân bay")
            module_other_stx_app.write_result_text_try_if_in(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc",
                                                                var_stx_app.g7_driver_check_drive, "", name_image)



    def code_active(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.login_driver_user, time_wait=1)
        except:
            login_driverg7(self, "Xe sân bay")
            driver_g7.logout_driver_g7(self)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.skip, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.clear(var_stx_app.driver_driver, var_stx_app.login_driver_user, time_wait=1)
        except:
            driver_g7.logout_driver_g7(self)

        element = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.login_change_area)

        # Nhấn giữ vào element trong 2 giây
        touch_action = TouchAction(var_stx_app.driver_driver)
        touch_action.long_press(el=element, duration=2500).release().perform()
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=1)
        except:
            touch_action.long_press(el=element, duration=2500).release().perform()

        action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=5)
        time.sleep(3)
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Xếp tài")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            g7_hn = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.g7_hn).text
            g7_hcm = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.g7_hcm).text
            g7_hcm_bank = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.g7_hcm_bank).text

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Chi nhánh 1: {}\nChi nhánh 2: {}\nChi nhánh 3: {}".format(g7_hn, g7_hcm, g7_hcm_bank))
            var_stx_app.logging.info("Chi nhánh 1: {}\nChi nhánh 2: {}\nChi nhánh 3: {}".format(g7_hn, g7_hcm, g7_hcm_bank))
            if g7_hn == "G7 Taxi Hà Nội" and g7_hcm == "G7 Taxi HCM" and g7_hcm_bank == "G7 Taxi HCM BAK":
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_Login_Driver_ChuyenChiNhanh.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_Login_Driver_ChuyenChiNhanh.png")
        except:
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_Login_Driver_ChuyenChiNhanh.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_Login_Driver_ChuyenChiNhanh.png")

        action.click(var_stx_app.driver_driver, var_stx_app.g7_hn, time_wait=5)
        time.sleep(3)

        # if username == "truongtq.BA":  # Máy Truongtq
        #     if type == "Xe sân bay":
        #         driver_g7.login_driver_g7(self, "auto383", "atgmj123","29A96320")  # 29A1240(test)    #29A96320(staging)   ĐINH MẠNH CƯỜNG
        # else:
        #     if type == "Xe sân bay":
        #         driver_g7.login_driver_g7(self, "auto376", "atgmj123", "30A76818")  # 30E48956(test)    #30A76818(staging)



    def fill_code_active_wrong(self, code, eventname, result, code_active, button, path_check, desire, name_image):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.RESTORE, time_wait=1)
        except:
            driver_g7.code_active(self, "", "", "")

        action.clear(var_stx_app.driver_driver, var_stx_app.fill_code_active)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.fill_code_active, code_active)

        action.click(var_stx_app.driver_driver, button)

        try:
            action.wait_for(var_stx_app.driver_driver,path_check, time_wait=5)
        except:
            pass
        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Đổi chi nhanh - Mã kích hoạt",
                                              path_check, desire, name_image)















