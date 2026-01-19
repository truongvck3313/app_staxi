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



def login_driverg7(self, type):
    if username == "truongtq.BA":  # Máy Truongtq
        # driver_g7.logout_driver_g7(self)
        if type == "Xe thường":
            driver_g7.login_driver_g7(self, "auto409", "atgmj123", "29E04479")
        if type == "Xe sân bay":
            driver_g7.login_driver_g7(self, "auto383", "atgmj123", "29A96320")   #29A1240(test)    #29A96320(staging)   ĐINH MẠNH CƯỜNG
    else:
        if type == "Xe thường":
            driver_g7.login_driver_g7(self, "auto82", "atgmj123", "30E05364")
        if type == "Xe sân bay":
            driver_g7.login_driver_g7(self, "auto376", "atgmj123", "30A76818")  #30E48956(test)    #30A76818(staging)








class g7:

    def login_g7(self, phone):
        var_stx_app.driver.implicitly_wait(0.3)
        homepage_g7.homepage_g7_back()

        n = 0
        while (n < 5):
            n = n + 1
            n = str(n)
            if n == "1":
                try:
                    print("n1")
                    keyboard.press(Key.f1)
                    time.sleep(3)
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.g7_taxi).click()
                    action.wail_until(var_stx_app.login_phone, 6)
                except:
                    print("n2")
                    try:
                        var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm1).click()
                        time.sleep(2)
                        print("n3")
                    except:
                        try:
                            print("n4")
                            action.wail_until(var_stx_app.home_page, 7)
                            break
                        except:
                            var_stx_app.driver.press_keycode(4)
                            time.sleep(3)
                            print("n5")
                            try:
                                var_stx_app.driver.find_element(By.XPATH, var_stx_app.g7_taxi).click()
                                time.sleep(4)
                                print("n6")
                            except:
                                pass
                            print("n7")
                            try:
                                var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm1).click()
                                time.sleep(3)
                                print("n8")
                            except:
                                pass
            try:
                action.wail_until(var_stx_app.home_page, 7)
                print("n9")
                break
            except:
                try:
                    action.wail_until(var_stx_app.login_phone, 1)
                    try:
                        var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_phone).click()
                    except:
                        var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_phone1).click()
                    time.sleep(1)
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_phone_input).clear()
                    time.sleep(0.5)
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_phone_input).send_keys(phone)
                    print("n10")
                except:
                    try:
                        var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_phone).click()
                    except:
                        var_stx_app.driver.press_keycode(4)
                        time.sleep(2)
                        var_stx_app.driver.press_keycode(4)
                        time.sleep(2)
                        var_stx_app.driver.find_element(By.XPATH, var_stx_app.g7_taxi).click()
                        time.sleep(3.5)
                        try:
                            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_phone).click()
                        except:
                            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_phone1).click()
                        time.sleep(1)
                        var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_phone_input).clear()
                        time.sleep(0.5)
                        var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_phone_input).send_keys(phone)
                        print("n11")
                time.sleep(1)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.continue1).click()
                time.sleep(5)
                var_stx_app.driver.tap([(500, 500)])
                time.sleep(0.5)
                var_stx_app.driver.tap([(500, 500)])
                time.sleep(1.5)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.otp1).send_keys("9")
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.otp2).send_keys("9")
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.otp3).send_keys("9")
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.otp4).send_keys("9")
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm).click()
                try:
                    print("n12")
                    action.wail_until(var_stx_app.home_page, 7)
                    time.sleep(1)
                    break
                except:
                    print("n13")
                try:
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.allow).click()
                    time.sleep(1)
                except:
                    pass
                try:
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.ALLOW).click()
                    time.sleep(1)
                except:
                    pass
                try:
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.allow).click()
                    time.sleep(1)
                except:
                    pass
                try:
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.SKIP).click()
                    time.sleep(1)
                except:
                    pass

            n = int(n)
        homepage_g7.homepage_g7_back()



    def login_g7_close_app(self, phone):
        n = 0
        while (n < 5):
            n = n + 1
            n = str(n)
            if n == "1":
                module_other_stx_app.close_app()
                action.click(var_stx_app.g7_taxi)
                try:
                    action.wail_until(var_stx_app.login_phone, 6)
                except:
                    var_stx_app.driver.press_keycode(4)
                    time.sleep(3)
                    action.click(var_stx_app.g7_taxi)
            try:
                action.wail_until(var_stx_app.home_page, 7)
                break
            except:
                try:
                    action.wail_until(var_stx_app.login_phone, 1)
                    action.click(var_stx_app.login_phone)
                    action.send_keys(var_stx_app.login_phone_input, phone)
                except:
                    action.send_keys(var_stx_app.login_phone_input, phone)
                action.click(var_stx_app.continue1)
                time.sleep(7)
                action.send_keys(var_stx_app.otp1, "9")
                action.send_keys(var_stx_app.otp2, "9")
                action.send_keys(var_stx_app.otp3, "9")
                action.send_keys(var_stx_app.otp4, "9")
                action.click(var_stx_app.confirm)
                try:
                    action.wail_until(var_stx_app.home_page, 7)
                except:
                    break
            n = int(n)




    def display_login_g7(self):
        var_stx_app.driver.implicitly_wait(0.3)
        n = 0
        while (n < 5):
            n = n + 1
            n = str(n)
            try:
                print("n1")
                
                g7.logout_g7(self)
                action.wail_until(var_stx_app.logo_g7, 6)
                break
            except:
                var_stx_app.driver.press_keycode(4)
                time.sleep(3)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.g7_taxi).click()
                time.sleep(3)
                g7.logout_g7(self)
                try:
                    action.wail_until(var_stx_app.logo_g7, 6)
                    break
                except:
                    pass

            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm1).click()
                time.sleep(3)
                print("n8")
            except:
                pass

            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.allow).click()
                time.sleep(1)
            except:
                pass
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.ALLOW).click()
                time.sleep(1)
            except:
                pass
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.allow).click()
                time.sleep(1)
            except:
                pass
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.SKIP).click()
                time.sleep(1)
            except:
                pass

            n = int(n)
        homepage_g7.homepage_g7_back()









    def logout_g7(self):
        var_stx_app.driver.implicitly_wait(2)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account).click()
            time.sleep(1.5)
            var_stx_app.driver.swipe(400, 1200, 465, 480, 500)
            time.sleep(1)
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.g7_icon_logout).click()
            except:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.logout).click()
            time.sleep(1.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(3)
            print("logout g7 thành công")
        except:
            print("logout g7 thất bại")



    def change_language(self, code, eventname, result, path_button, desire, name_image):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.logo_g7)
        except:
            g7.display_login_g7(self)


        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_language).click()
        time.sleep(1.5)
        var_stx_app.driver.find_element(By.XPATH, path_button).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree_language).click()
        time.sleep(2.5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_change_language)
        except:
            var_stx_app.driver.press_keycode(4)
            time.sleep(2)
            action.click(var_stx_app.g7_taxi)
            time.sleep(3.5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập(g7) - Đổi ngôn ngữ",
                                                  var_stx_app.check_change_language, desire, name_image)



    def register(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.logo_g7)
        except:
            g7.display_login_g7(self)



        var_stx_app.driver.find_element(By.XPATH, var_stx_app.register).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.register_phone).click()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.register_phone_input).send_keys(var_stx_app.data['login']['register_phone'])
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.register_name).click()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.register_name_input).send_keys(var_stx_app.data['login']['register_name'])
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.register_sex).click()
        time.sleep(1.5)
        var_stx_app.driver.tap([(177, 1077)])
        time.sleep(1)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.register_brith_day).click()
        time.sleep(1.5)
        var_stx_app.driver.tap([(560, 1050)])
        time.sleep(1)
        var_stx_app.driver.tap([(650, 1200)])
        time.sleep(1)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.register_email).click()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.register_email_input).send_keys(var_stx_app.data['login']['register_email'])
        time.sleep(0.5)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.register_address).click()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.register_address_input).send_keys(var_stx_app.data['login']['register_address'])
        time.sleep(0.5)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.register_referral_code1).click()
        time.sleep(0.5)
        # var_stx_app.driver.find_element(By.XPATH, var_stx_app.register_referral_code_input1).send_keys(var_stx_app.data['login']['register_referral_code'])
        # time.sleep(0.5)

        var_stx_app.driver.swipe(330, 1130, 85, 330, 600)
        time.sleep(1.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.register_checkbox).click()
        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.REGISTER).click()
        action.wail_until(var_stx_app.check_register, 5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập(g7) - Đăng ký",
                                                  var_stx_app.check_register, "Tài khoản của bạn đã tồn tại trên hệ thống, bạn hãy đăng nhập để tiếp tục sử dụng.", "_G7_DangKy.png")


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login).click()
            time.sleep(2.5)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.register_phone_input)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.register_back).click()
            time.sleep(2)
        except:
            pass



    def login_sdt(self, code, eventname, result, phone_number, path_check, desire, name_image):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.logo_g7)
        except:
            g7.display_login_g7(self)

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_phone1).click()
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_phone_input).clear()
            time.sleep(0.5)
            print("b2")
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.logo_g7)
            print("b3")
        except:
            g7.display_login_g7(self)



        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_phone).click()
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_phone1).click()
        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_phone_input).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_phone_input).send_keys(phone_number)
        time.sleep(0.5)
        print("b8")
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.continue1).click()
        time.sleep(2)
        print("b9")
        try:
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.register_back)))
            print("b10")
            var_stx_app.driver.swipe(300, 1100, 300, 600, 1000)
            time.sleep(1)
            print("b11")
        except:
            pass
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, path_check)))
        print("b12")
        time.sleep(0.5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập(g7)",
                                                  path_check, desire, name_image)

        print("b13")
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.register_phone_input)
            print("b14")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.register_back).click()
            time.sleep(2)
            print("b5")
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.otp1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.otp_back).click()
            print("b16")
            time.sleep(2)
        except:
            pass





class driver_g7:

    def login_driver_g7(self, user, password, vehicle):
        var_stx_app.driver.implicitly_wait(1)
        homepage_driver.homepage_g7_drive_back()

        n = 0
        while (n < 5):
            n = n + 1
            n = str(n)
            try:
                var_stx_app.driver.implicitly_wait(0.3)
                keyboard.press(Key.f1)
                print("n1")
                time.sleep(1.2)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
                time.sleep(3.5)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_buttonlogin1)
                time.sleep(2.5)
                var_stx_app.driver.tap([(450, 500)])
                time.sleep(0.5)
                var_stx_app.driver.tap([(450, 500)])
                try:
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.ALLOW).click()
                    time.sleep(1.5)
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.ALLOW).click()
                    time.sleep(1)
                except:
                    pass
                try:
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.allow).click()
                    time.sleep(1)
                except:
                    pass
                try:
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.ALLOW).click()
                    time.sleep(1)
                except:
                    pass
            except:
                pass
            try:
                var_stx_app.driver.tap([(500, 500)])
                time.sleep(0.5)
                var_stx_app.driver.tap([(500, 500)])
                time.sleep(1)
            except:
                pass
            time.sleep(2)
            try:
                var_stx_app.driver.implicitly_wait(0.3)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.skip).click()
                time.sleep(2)
            except:
                pass

            try:
                var_stx_app.driver.implicitly_wait(0.5)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_driver_user).send_keys(user)
                print("n2")
            except:
                print("n3")
                var_stx_app.driver.press_keycode(4)
                time.sleep(1.5)
                try:
                    var_stx_app.driver.implicitly_wait(1)
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
                    time.sleep(3.5)
                except:
                    pass

            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification)
                print("Đã login vào app g7 driver1")
                break
            except:
                pass


            try:
                var_stx_app.driver.implicitly_wait(0.3)
                print("n4")
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_driver_user).clear()
                time.sleep(0.5)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_driver_user).send_keys(user)
                time.sleep(0.5)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_driver_password).clear()
                time.sleep(0.5)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_driver_password).send_keys(password)
                time.sleep(0.5)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_driver_vehicle).clear()
                time.sleep(0.5)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_driver_vehicle).send_keys(vehicle)
                action.click(var_stx_app.login_buttonlogin1)
                time.sleep(2.5)
                var_stx_app.driver.tap([(450, 500)])
                time.sleep(0.5)
                var_stx_app.driver.tap([(450, 500)])
                time.sleep(1)
                try:
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.ALLOW).click()
                    time.sleep(1.5)
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.ALLOW).click()
                    time.sleep(1)
                except:
                    pass
                try:
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.allow).click()
                    time.sleep(1)
                except:
                    pass
                try:
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.ALLOW).click()
                    time.sleep(1)
                except:
                    pass
                action.wail_until(var_stx_app.notification, 5)
            except:
                pass

            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification)
                print("Đã login vào app g7 driver2")
                break
            except:
                pass

            n = int(n)



    def logout_driver_g7(self):
        var_stx_app.driver.implicitly_wait(2)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(5)
            print("n0")
        except:
            pass

        try:
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.icon_option)))
            print("n1")
        except:
            var_stx_app.driver.tap([(444, 777)])
            time.sleep(0.5)
            var_stx_app.driver.tap([(444, 777)])
            print("n2")


        try:
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.icon_option)))
            print("n3")
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_option).click()
            time.sleep(1.5)
            var_stx_app.driver.swipe(200, 1100, 200, 500, 1000)
            time.sleep(1)
            print("n4")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.leave).click()
            time.sleep(1.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.leave1).click()
            time.sleep(5)
            try:
                print("n5")
                var_stx_app.driver.implicitly_wait(0.3)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.leave1).click()
                time.sleep(3)
            except:
                pass

            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.leave1).click()
                time.sleep(3)
            except:
                pass
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.login_driver_user)))
            print("logout g7 driver thành công")
        except:
            print("logout g7 driver thất bại")



    def check_login_driver_g7(self, code, eventname, result, user, password, vehicle, path_check, desire, name_image):
        var_stx_app.driver.implicitly_wait(3)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_driver_user)
        except:
            login_driverg7(self, "Xe sân bay")
            driver_g7.logout_driver_g7(self)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.skip).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_driver_user).clear()
        except:
            driver_g7.logout_driver_g7(self)
            time.sleep(2)



        if name_image == "_LaiXeG7_DangNhapSai.png":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_driver_user).clear()
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_driver_user).send_keys(user)
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_driver_password).clear()
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_driver_password).send_keys(password)
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_driver_vehicle).clear()
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_driver_vehicle).send_keys(vehicle)
            action.click(var_stx_app.login_buttonlogin1)
            time.sleep(3)
            try:
                var_stx_app.driver.implicitly_wait(0.3)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.ALLOW).clear()
                time.sleep(2)
            except:
                pass
            var_stx_app.driver.tap([(400, 820)])
            time.sleep(0.5)
            var_stx_app.driver.tap([(400, 820)])
            time.sleep(1.5)
            module_other_stx_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập(Lái xe G7)",
                                                          path_check, desire, name_image)
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.g7_driver_skip).click()
                time.sleep(1.5)
            except:
                pass

        else:
            login_driverg7(self, "Xe sân bay")
            # module_other_stx_app.write_result_text_try_if_cut(code, eventname, result, "Màn hình đăng nhập(Lái xe G7)",
            #                                               path_check, 0, 18, desire, name_image)

            module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Màn hình đăng nhập(Lái xe G7)",
                                                          path_check, "", name_image)




    def code_active(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(3)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_driver_user)
        except:
            login_driverg7(self, "Xe sân bay")
            driver_g7.logout_driver_g7(self)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.skip).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_driver_user).clear()
        except:
            driver_g7.logout_driver_g7(self)
            time.sleep(2)

        element = var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_change_area)

        # Nhấn giữ vào element trong 2 giây
        touch_action = TouchAction(var_stx_app.driver)
        touch_action.long_press(el=element, duration=2500).release().perform()
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree)
        except:
            touch_action.long_press(el=element, duration=2500).release().perform()

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        time.sleep(3)
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Xếp tài")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            g7_hn = var_stx_app.driver.find_element(By.XPATH, var_stx_app.g7_hn).text
            g7_hcm = var_stx_app.driver.find_element(By.XPATH, var_stx_app.g7_hcm).text
            g7_hcm_bank = var_stx_app.driver.find_element(By.XPATH, var_stx_app.g7_hcm_bank).text

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Chi nhánh 1: {}\nChi nhánh 2: {}\nChi nhánh 3: {}".format(g7_hn, g7_hcm, g7_hcm_bank))
            var_stx_app.logging.info("Chi nhánh 1: {}\nChi nhánh 2: {}\nChi nhánh 3: {}".format(g7_hn, g7_hcm, g7_hcm_bank))
            if g7_hn == "G7 Taxi Hà Nội" and g7_hcm == "G7 Taxi HCM" and g7_hcm_bank == "G7 Taxi HCM BAK":
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_Login_Driver_ChuyenChiNhanh.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_Login_Driver_ChuyenChiNhanh.png")
        except:
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_Login_Driver_ChuyenChiNhanh.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_Login_Driver_ChuyenChiNhanh.png")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.g7_hn).click()
        time.sleep(3)

        # if username == "truongtq.BA":  # Máy Truongtq
        #     if type == "Xe sân bay":
        #         driver_g7.login_driver_g7(self, "auto383", "atgmj123","29A96320")  # 29A1240(test)    #29A96320(staging)   ĐINH MẠNH CƯỜNG
        # else:
        #     if type == "Xe sân bay":
        #         driver_g7.login_driver_g7(self, "auto376", "atgmj123", "30A76818")  # 30E48956(test)    #30A76818(staging)



    def fill_code_active_wrong(self, code, eventname, result, code_active, button, path_check, desire, name_image):
        var_stx_app.driver.implicitly_wait(3)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.RESTORE)
        except:
            driver_g7.code_active(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.fill_code_active).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.fill_code_active).send_keys(code_active)
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, button).click()
        time.sleep(2)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Đổi chi nhanh - Mã kích hoạt",
                                              path_check, desire, name_image)















