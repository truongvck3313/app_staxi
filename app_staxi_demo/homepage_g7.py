import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import re
import module_other_stx_app
import login_stx_app
import var_stx_app
import requests
import json
from retry import retry
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import homepage_driver
from pynput.keyboard import Key, Controller
keyboard = Controller()
import math
import pyautogui



def select_type_car(type_car):
    n = 0
    while (n < 7):
        n = n + 1
        n = str(n)
        try:
            var_stx_app.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup//*[@text='"+type_car+"']")
        except:
            var_stx_app.driver.swipe(805, 1055, 110, 1055, 1000)
            time.sleep(1)

        path_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView"
        path_button = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup"
        try:
            name = var_stx_app.driver.find_element(By.XPATH, path_name).text
            print(name)
            if name == type_car:
                var_stx_app.driver.find_element(By.XPATH, path_button).click()
                time.sleep(2)
                break
        except:
            pass
        n = int(n)





def normalize(self, text):
    return re.sub(r"[^\w\s]", "", text.lower()).strip()


# result = normalize(self, location_before) in normalize(self, location_after)


def homepage_g7_back():
    var_stx_app.driver.implicitly_wait(0.1)
    #Khach huy dat xe 1
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CANCEL_BOOKING).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.customer_cancels_order)))
        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        time.sleep(2)
        print("n_1")
    except:
        pass

    #Khach huy dat xe 2
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CANCEL_BOOKING).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.customer_cancels_order)))
        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        time.sleep(2)
        print("n_2")
    except:
        pass

    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back1).click()
        time.sleep(0.5)
        print("n_3")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back2).click()
        time.sleep(0.5)
        print("n_4")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back3).click()
        time.sleep(0.5)
        print("n_5")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back4).click()
        time.sleep(0.5)
        print("n_6")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back5).click()
        time.sleep(0.5)
        print("n_7")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back6).click()
        time.sleep(0.5)
        print("n_8")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back7).click()
        time.sleep(0.5)
        print("n_9")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back8).click()
        time.sleep(0.5)
        print("n_10")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back9).click()
        time.sleep(0.5)
        print("n_11")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back10).click()
        time.sleep(0.5)
        print("n_12")
    except:
        pass
    # try:
    #     var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back11).click()
    #     time.sleep(1)
    #     print("n_13")
    # except:
    #     pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back12).click()
        time.sleep(0.5)
        print("n_14")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back13).click()
        time.sleep(0.5)
        print("n_15")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back14).click()
        time.sleep(0.5)
        print("n_16")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back15).click()
        time.sleep(0.5)
        print("n_17")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back16).click()
        time.sleep(0.5)
        print("n_18")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back17).click()
        time.sleep(0.5)
        print("n_19")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back18).click()
        time.sleep(0.5)
        print("n_20")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back19).click()
        time.sleep(0.5)
        print("n_21")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back20).click()
        time.sleep(0.5)
        print("n_22")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back21).click()
        time.sleep(0.5)
        print("n_23")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back22).click()
        time.sleep(0.5)
        print("n_24")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back23).click()
        time.sleep(0.5)
        print("n_25")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back24).click()
        time.sleep(0.5)
        print("n_26")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back25).click()
        time.sleep(0.5)
        print("n_27")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back26).click()
        time.sleep(0.5)
        print("n_28")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_g7_back27).click()
        time.sleep(0.5)
        print("n_29")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage).click()
        time.sleep(0.5)
        print("n_30")
    except:
        pass

    try:
        var_stx_app.driver.implicitly_wait(0.3)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage_iconx1).click()
        time.sleep(0.5)
        print("n_31")
    except:
        pass

    try:
        var_stx_app.driver.implicitly_wait(5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.close_app).click()
        time.sleep(3)
        print("n_32")
    except:
        pass












class home_page:

    def icon_map(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(2)
        

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_map)
        except:
            module_other_stx_app.click_app("G7 Taxi")

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_map).click()
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_map).click()

        time.sleep(2)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(g7) - Map",
                                              var_stx_app.check_icon_map, "Điểm đến", "_TrangChu_IconMap.png")
        if code == "HomePage01":
            try:
                var_stx_app.driver.implicitly_wait(0.3)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_map_back).click()
                time.sleep(1.5)
            except:
                pass
            try:
                var_stx_app.driver.implicitly_wait(0.3)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_map_back1).click()
                time.sleep(1.5)
            except:
                pass



    def icon_destination(self, code, eventname, result, path_icon, name_before, name_before1,  number_from, number_to, name_image):
        var_stx_app.driver.implicitly_wait(2)
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, "//*[@text='"+path_icon+"']")
        except:
            login_stx_app.g7.login_g7(self, "0359667694")


        try:
            name_before = var_stx_app.driver.find_element(By.XPATH, name_before).text
            var_stx_app.driver.find_element(By.XPATH, "//*[@text='"+path_icon+"']").click()
        except:
            name_before = var_stx_app.driver.find_element(By.XPATH, name_before1).text
            var_stx_app.driver.find_element(By.XPATH, "//*[@text='"+path_icon+"']").click()
        time.sleep(2)


        if path_icon == "Trường học":
            try:
                var_stx_app.driver.implicitly_wait(0.3)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.skip).click()
                time.sleep(1)
            except:
                pass
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_destination_note).click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_destination_note_input).send_keys(var_stx_app.data['home_page_g7']['note'])
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.IGREE).click()
            time.sleep(1.5)

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.skip).click()
            time.sleep(1)
        except:
            pass

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_pick_up_point).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_icon)))
        time.sleep(0.5)


        if path_icon == "Trường học":
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.path_note)))
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.path_note).click()
            time.sleep(2)
            name_note = var_stx_app.driver.find_element(By.XPATH, var_stx_app.name_note).text
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm1).click()
            time.sleep(2.5)
            name_school = var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_2).text
            var_stx_app.logging.info("--------------")
            var_stx_app.logging.info("Trang Chủ(g7) - Map")
            var_stx_app.logging.info("Mã - " + code)
            var_stx_app.logging.info("Tên sự kiện - " + eventname)
            var_stx_app.logging.info("Kết quả - " + result)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Trường học: {}\nGhi chú: {}".format(name_school, name_note))
            var_stx_app.logging.info(name_note)
            var_stx_app.logging.info(name_school)
            if (name_note == var_stx_app.data['home_page_g7']['note']) and (name_school[12:-1] == name_before):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)


        else:
            module_other_stx_app.write_result_text_try_if_cut(code, eventname, result, "Trang Chủ(g7) - Map",
                                                  var_stx_app.location_2, number_from, number_to, name_before, name_image)

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_back).click()
            time.sleep(1.5)
        except:
            pass



    def icon_add_adress(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(2)
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_map)
            time.sleep(2)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")

        try:
            var_stx_app.driver.swipe(815, 434, 85, 434, 1000)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.add_adress).click()
        except:
            var_stx_app.driver.swipe(610, 500, 100, 500, 1000)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.add_adress).click()
        time.sleep(1.5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(g7) - Map",
                                              var_stx_app.check_add_adress, "Điểm yêu thích", "_TrangChu_ThemDiaChi.png")

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.add_adress_back).click()
            time.sleep(1.5)
        except:
            pass



    def check_info_accout(self, code, eventname, result, path_name, path_data, check_name, check_data, name_image):
        var_stx_app.driver.implicitly_wait(2)
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_change_account)
        except:
            try:
                var_stx_app.driver.implicitly_wait(0.3)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account1).click()
                time.sleep(2)
            except:
                login_stx_app.g7.login_g7(self, "0359667694")
                try:
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account).click()
                except:
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account1).click()
                time.sleep(2)


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(g7) - Thay đổi tài khoản")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            name = var_stx_app.driver.find_element(By.XPATH, path_name).text
            data = var_stx_app.driver.find_element(By.XPATH, path_data).text
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "{} {}".format(name, data))
            var_stx_app.logging.info(name)
            var_stx_app.logging.info(data)

            if (name == check_name) and (data == check_data):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + name_image)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)



    def change_accout_skip(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(2)
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_change_account)
        except:
            try:
                var_stx_app.driver.implicitly_wait(0.3)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account).click()
                time.sleep(2)
            except:
                login_stx_app.g7.login_g7(self, "0359667694")
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account).click()
                time.sleep(2)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.skip).click()
        time.sleep(2)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(g7) - Thay đổi tài khoản",
                                              var_stx_app.home_page, "Trang chủ", "_TrangChu_ThayDoiTaiKhoan_BoQua.png")



    def change_accout_update(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(2)
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_change_account)
        except:
            try:
                var_stx_app.driver.implicitly_wait(0.3)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account).click()
            except:
                login_stx_app.g7.login_g7(self, "0359667694")
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account1).click()
            time.sleep(3)


        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_icon_image).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_icon_image1).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.save).click()
        time.sleep(2.5)


        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_name).click()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_name_input).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_name_input).send_keys("Trần Quang Truờng1")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_sex).click()
        time.sleep(1.5)
        var_stx_app.driver.tap([(156, 841)])
        # var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_sex_male).click()
        time.sleep(1.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_brith_day)
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_email).click()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_email_input).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_email_input).send_keys("truongvck1@gmail.com")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_referrer_code)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.update).click()
        time.sleep(1)
        # wait = WebDriverWait(var_stx_app.driver, 10)
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_update_change_acount)))
        time.sleep(0.5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(g7) - Thay đổi tài khoản",
                                              var_stx_app.check_update_change_acount, "Cập nhật thông tin thành công", "_TrangChu_ThayDoiTaiKhoan_BoQua.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account).click()
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account1).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_name).click()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_name_input).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_name_input).send_keys("Trần Quang Truờng")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_email).click()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_email_input).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_account_email_input).send_keys("truongvck33@gmail.com")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.update).click()
        time.sleep(3)










    def icon_current_location(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(2)
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.book_a_car_quickly).click()
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.book_a_car_quickly).click()

        time.sleep(3)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.skip).click()
            time.sleep(1)
        except:
            pass

        var_stx_app.driver.swipe(450, 450, 550, 450, 1000)
        time.sleep(0.5)
        location_before = var_stx_app.driver.find_element(By.XPATH, var_stx_app.current_location).text
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_current_location).click()
        time.sleep(2)
        location_after = var_stx_app.driver.find_element(By.XPATH, var_stx_app.current_location).text

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(g7) - Thay đổi tài khoản")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Vị trí trước khi click icon: {}\nVị trí sau khi click icon: {}".format(location_before, location_after))
        var_stx_app.logging.info("Vị trí trước khi click icon: {}\nVị trí sau khi click icon: {}".format(location_before, location_after))
        if location_before != location_after:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_DatNhanh_ViTriHienTai.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_DatNhanh_ViTriHienTai.png")



    def book_a_car_quickly(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(2)
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.current_location)
        except:
                home_page.icon_current_location(self, "", "", "")

        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.icon_pick_up_point)))
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_pick_up_point).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_pick_up_point_input).send_keys("Sơn Tây")
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_pick_up_point_input3).click()
        time.sleep(3)
        # var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_pick_up_point).click()
        # time.sleep(2)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(g7) - Đặt xe nhanh",
                                              var_stx_app.check_book_a_car_quickly, "G7 Taxi đang tìm kiếm lái xe. Bạn vui lòng đợi trong giây lát…", "_TrangChu_DatXeNhanh.png")

        var_stx_app.driver.tap([(422, 376)])
        time.sleep(2)
        var_stx_app.driver.press_keycode(4)
        time.sleep(3)







    def icon_record(self, code, eventname, result):
        

        var_stx_app.driver.implicitly_wait(2)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_icon_map)
        except:
            home_page.icon_map(self, "", "", "")

        module_other_stx_app.write_result_displayed_try(code, eventname, result, "Trang Chủ(g7) - Đặt xe - Icon Ghi âm",
                                              var_stx_app.icon_record, "_TrangChu_IconGhiAm.png")
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_record).click()
        time.sleep(1.5)
        var_stx_app.driver.press_keycode(4)
        time.sleep(3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_record)
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_map).click()
            time.sleep(2.5)








    def icon_location_to(self, code, eventname, result):
        


        var_stx_app.driver.implicitly_wait(2)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_icon_map)
        except:
            home_page.icon_map(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_to_input).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_to_input).send_keys("Ngõ 31 Thi Sách")
        time.sleep(2.5)

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_icon_location_to)
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_to_input).clear()
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_to_input).send_keys("Ngõ 31 Thi Sách")
            time.sleep(2.5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(g7) - Bản đồ - Chọn điểm đến",
                                              var_stx_app.check_icon_location_to, "Ngõ 31 Thi Sách", "_TrangChu_ChonDiemDen.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_icon_location_to).click()
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_to_input1).click()
        time.sleep(3)



    def check_location_from(self, code, eventname, result):
        

        var_stx_app.driver.implicitly_wait(2)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_pick_up_point)
        except:
            home_page.icon_location_to(self, "", "", "")

        try:
            var_stx_app.driver.swipe(71, 253, 550, 550, 500)
            var_stx_app.driver.swipe(71, 253, 550, 550, 500)
        except:
            var_stx_app.driver.swipe(450, 450, 410, 450, 500)
            var_stx_app.driver.swipe(450, 450, 410, 450, 500)

        time.sleep(2.5)
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(g7) - Check vị trí điểm đến")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            location_to_1_name = var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_to_1_name).text
            location_to_1_data = var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_to_1_data).text

            location_to_2_name = var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_to_2_name).text
            location_to_2_data = var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_to_2_data).text

            location_to_3_name = var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_to_3_name).text
            location_to_3_data = var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_to_3_data).text

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Vị trí 1: {}({})\nVị trí 2: {}({})\nVị trí 3: {}({})"
                                           .format(location_to_1_name, location_to_1_data, location_to_2_name, location_to_2_data, location_to_3_name, location_to_3_data))

            var_stx_app.logging.info("Vị trí 1: {}({})\nVị trí 2: {}({})\nVị trí 3: {}({})"
                                           .format(location_to_1_name, location_to_1_data, location_to_2_name, location_to_2_data, location_to_3_name, location_to_3_data))

            if (location_to_1_name != "") and (location_to_1_data != "") and (location_to_2_name != "") and (location_to_2_data != "") and (location_to_3_name != "") and (location_to_3_data != ""):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_CheckViTriDiemDon.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_CheckViTriDiemDon.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_CheckViTriDiemDon.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_CheckViTriDiemDon.png")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_location_from_back).click()
        time.sleep(3)





    def icon_destination1(self, code, eventname, result):
        


        var_stx_app.driver.implicitly_wait(2)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_destination).click()
        except:
            home_page.icon_map(self, "", "", "")
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.icon_destination)))
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_destination).click()

        time.sleep(2.5)
        location_before = var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_record_location_before1).text
        print(location_before)
        try:
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.CONFIRM_DESTINATION)))
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.CONFIRM_DESTINATION).click()
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_destination).click()
        time.sleep(2.5)
        var_stx_app.driver.swipe(71, 253, 550, 550, 1000)
        time.sleep(2)
        var_stx_app.driver.swipe(71, 253, 550, 550, 1000)
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_pick_up_point).click()
        time.sleep(3)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.skip).click()
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_location_here).click()
            time.sleep(2)
            var_stx_app.driver.swipe(450, 450, 410, 450, 1000)
            time.sleep(2)
        except:
            pass

        try:
            location_after = var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_record_location_after).text
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_location_here1).click()
            time.sleep(2)
            var_stx_app.driver.swipe(450, 450, 410, 450, 1000)
            time.sleep(2)
            var_stx_app.driver.swipe(450, 450, 410, 450, 1000)
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_pick_up_point).click()
            time.sleep(3)
            location_after = var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_record_location_after1).text
        print(location_after)



        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(g7) - Đặt xe - Icon Điểm đến")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Vị trí trước khi xác nhận điểm đến: {}\nVị trí sau khi xác nhận điểm đến: {}"
                                       .format(location_before, location_after))
        var_stx_app.logging.info("Vị trí trước khi xác nhận điểm đến: {}\nVị trí sau khi xác nhận điểm đến: {}".format(location_before, location_after))
        result = normalize(self, location_before) in normalize(self, location_after)
        if result == True:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_IconDiemDen.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_IconDiemDen.png")

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_back).click()
            time.sleep(1.5)
        except:
            pass



    def icon_pick_up_point(self, code, eventname, result):
        


        var_stx_app.driver.implicitly_wait(2)
        home_page.icon_map(self, "", "", "")
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_destination).click()
        time.sleep(2.5)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.CONFIRM_DESTINATION).click()
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_destination).click()
        time.sleep(2.5)


        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_pick_up_point).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_pick_up_point_input).send_keys("46 Bạch Mai")
        time.sleep(3)
        try:
            location_before = var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_pick_up_point_input1).text
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_pick_up_point_input).clear()
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_pick_up_point_input).send_keys("46 Bạch Mai")
            time.sleep(3)
            location_before = var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_pick_up_point_input1).text


        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_pick_up_point_input2).click()
        time.sleep(3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_pick_up_point).click()
            time.sleep(2)
        except:
            pass
        location_after = var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_1).text
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(g7) - Đặt xe - Icon Điểm đón")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Vị trí trước khi xác nhận điểm đón: {}\nVị trí sau khi xác nhận điểm đón: {}"
                                       .format(location_before, location_after))
        var_stx_app.logging.info("Vị trí trước khi xác nhận điểm đón: {}\nVị trí sau khi xác nhận điểm đón: {}".format(location_before, location_after))
        if location_before == "46 Bạch Mai" and location_after == "46, Bạch Mai, TP. Hà Nội (46, Bạch Mai, P. Cầu Dền, Q. Hai Bà Trưng, TP. Hà Nội)":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_IconDiemDon.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_IconDiemDon.png")

        # try:
        #     var_stx_app.driver.implicitly_wait(0.3)
        #     var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_back).click()
        #     time.sleep(1.5)
        # except:
        #     pass



    def edit_location(self, code, eventname, result, path_icon, path_input, data, path_check, desire, name_image):
        


        var_stx_app.driver.implicitly_wait(2)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.PTTT)
        except:
            home_page.icon_pick_up_point(self, "", "", "")

        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, path_icon)))
        var_stx_app.driver.find_element(By.XPATH, path_icon).click()
        time.sleep(2)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, path_input)))
        var_stx_app.driver.find_element(By.XPATH, path_input).send_keys(data)
        time.sleep(3)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.search_data1).click()
        time.sleep(3)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(g7) - Đặt xe",
                                              path_check, desire, name_image)



    def icon_change_position_2_location(self, code, eventname, result):
        

        var_stx_app.driver.implicitly_wait(2)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_3)
        except:
            home_page.edit_location(self, "", "", "", var_stx_app.location_2_icon,
                                    var_stx_app.search_location_input, "40 Đặng Văn Ngữ", "","","")


        location2_before = var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_2).text
        location3_before = var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_3).text

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_2_icon).click()
        time.sleep(1.5)
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(g7) - Đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            location2_after = var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_2).text
            location3_after = var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_3).text
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Điểm 1 trước khi đổi: {}\nĐiểm 2 trước khi đổi: {}\nĐiểm 1 sau khi đổi: {}\nĐiểm 2 sau khi đổi: {}"
                                           .format(location2_before, location3_before, location2_after, location3_after))
            var_stx_app.logging.info("Điểm đến 1(a): {}\nĐiểm đến 2(a): {}\nĐiểm đến 1(b): {}\nĐiểm đến 2(b): {}"
                                           .format(location2_before, location3_before, location2_after, location3_after))
            if location2_before == location3_after and location3_before == location2_after:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_DatXe_IconDoiViTri2Diem.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_DatXe_IconDoiViTri2Diem.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_DatXe_IconDoiViTri2Diem.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_DatXe_IconDoiViTri2Diem.png")



    def icon_delete_location2(self, code, eventname, result):
        


        var_stx_app.driver.implicitly_wait(2)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_3)
        except:
            home_page.icon_change_position_2_location(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_3_icon).click()
        time.sleep(2)
        module_other_stx_app.write_result_not_displayed_try(code, eventname, result, "Trang Chủ(g7) - Đặt xe",
                                              var_stx_app.location_3, "_TrangChu_DatXe_IconXoaViTriDiem2.png")



    def icon_info_vehicle(self, code, eventname, result):
        


        var_stx_app.driver.implicitly_wait(2)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_2)
        except:
            home_page.edit_location(self, "", "", "", var_stx_app.location_1,
                                    var_stx_app.search_location_input, "120 Đường Cầu Giấy", "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_info_vehicle).click()
        time.sleep(2.5)
        module_other_stx_app.write_result_not_displayed_try(code, eventname, result, "Trang Chủ(g7) - Đặt xe - Thông tin xe",
                                              var_stx_app.location_3, "_TrangChu_DatXe_IconXoaViTriDiem2.png")

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(g7) - Đặt xe - Thông tin xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            type_vehicle = var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_vehicle_type_vehicle).text
            transportation_fee = var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_vehicle_transportation_fee).text
            distance = var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_vehicle_distance).text
            time1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_vehicle_time).text
            total_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_vehicle_total_amount).text


            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "{}\nCước di chuyển: {}\nKhoảng cách: {}\nKhung giờ: {}\nTổng tiền thanh toán: {}"
                                           .format(type_vehicle, transportation_fee, distance, time1, total_amount))
            var_stx_app.logging.info("Loại xe: {}\nCước di chuyển: {}\nKhoảng cách: {}\nKhung giờ: {}\nTổng tiền thanh toán: {}"
                                           .format(type_vehicle, transportation_fee, distance, time, total_amount))
            if type_vehicle != "" and transportation_fee != "" and distance != "" and time1 != "" and total_amount != "":
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_DatXe_ThongTinxe.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_DatXe_ThongTinxe.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_DatXe_ThongTinxe.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_DatXe_ThongTinxe.png")


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_vehicle_x).click()
            time.sleep(2)
        except:
            pass


    def book_for_you(self, code, eventname, result):
        

        var_stx_app.driver.implicitly_wait(2)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_2)
        except:
            home_page.edit_location(self, "", "", "", var_stx_app.location_1,
                                    var_stx_app.search_location_input, "120 Đường Cầu Giấy", "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.book_for_you).click()
        time.sleep(2.5)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.book_for_you_checkbox)
        # var_stx_app.driver.find_element(By.XPATH, var_stx_app.book_for_you_sdt).click()
        # time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.book_for_you_sdt_input).send_keys("0369443728")
        time.sleep(0.5)
        # var_stx_app.driver.find_element(By.XPATH, var_stx_app.book_for_you_name).click()
        # time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.book_for_you_name_input).send_keys("Thu Thủy")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.SEND).click()
        time.sleep(1.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        time.sleep(3)

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.book_for_you)
            module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(g7) - Đặt hộ",
                                                  var_stx_app.book_for_you, "Thu Thủy", "_TrangChu_DatHo.png")
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(1.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.SEND).click()
            time.sleep(1.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(3)
            module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(g7) - Đặt hộ",
                                                  var_stx_app.book_for_you, "Thu Thủy", "_TrangChu_DatHo.png")
        except:
            pass


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.book_for_you_x).click()
            time.sleep(1.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(1.5)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_back).click()
            time.sleep(1.5)
        except:
            pass
        module_other_stx_app.close_app()





    def choose_location(self, location_to):
        

        home_page.icon_map(self, "", "", "")
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_to_input).send_keys(location_to)
        except:
            homepage_g7_back()
            home_page.icon_map(self, "", "", "")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_to_input).send_keys(location_to)
        time.sleep(3.5)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_to1).click()
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_to_input).clear()
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_to_input).send_keys(location_to)
            time.sleep(3.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_to1).click()
        time.sleep(3)

        try:
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.confirm_pick_up_point)))
            element.click()
        except:
            var_stx_app.driver.tap([(375, 255)])
            time.sleep(1)
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.confirm_pick_up_point)))
            element.click()
        # var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_pick_up_point).click()
        time.sleep(3.5)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_map_location_to)
            var_stx_app.driver.tap([(375, 255)])
            time.sleep(2)
        except:
            pass




    def book_car_cancel(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(2)
        homepage_driver.home_page.status_driver(self, "Xe sân bay", "SẴN SÀNG")
        login_stx_app.g7.login_g7(self, "0359667694")
        home_page.choose_location(self, "110 Cầu Giấy")

        select_type_car("7 Chỗ")
        # var_stx_app.driver.find_element(By.XPATH, var_stx_app.car_7_sit).click()
        # time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt).click()
        time.sleep(3)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt_card_g7).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.clock_taxi).click()
        time.sleep(3)
        wait = WebDriverWait(var_stx_app.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.RECEIVE_APP)))
        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.RECEIVE_APP).click()
        time.sleep(2)
        module_other_stx_app.click_app("G7 Taxi")

        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.SKIP).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CANCEL_BOOKING).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.customer_cancels_order)))
        time.sleep(1)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(g7) - Đặt cuốc",
                                              var_stx_app.customer_cancels_order, "Khách hàng hủy cuốc.", "_TrangChu_DatCuoc_HuyDatXe.png")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        time.sleep(2)
        module_other_stx_app.click_app("G7 Taxi")
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_car_back).click()
        time.sleep(2)



    def book_car_see_car(self, code, eventname, result, type):
        var_stx_app.driver.implicitly_wait(5)
        

        if type == "1":
            pass
            # module_other_stx_app.close_app()
        homepage_driver.home_page.status_driver(self, "Xe sân bay", "SẴN SÀNG")
        login_stx_app.g7.login_g7(self, "0359667694")
        home_page.choose_location(self, "89 Chùa Láng")
        #

        select_type_car("7 Chỗ")

        wait = WebDriverWait(var_stx_app.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.pttt)))
        # element.click()
        # time.sleep(1)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.pttt)))
        element.click()
        time.sleep(3)

        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.pttt_card_g7)))
            element.click()
            time.sleep(2)
        except:
            wait = WebDriverWait(var_stx_app.driver, 30)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.pttt_tienmat)))
            element.click()
            time.sleep(2)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.payment_app)))
        element.click()
        time.sleep(3)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.RECEIVE_APP)))
        element.click()
        time.sleep(3)

        if type == "1":
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.SEE_CUSTOMER)))
            element.click()
            time.sleep(3)

            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.CONFIRM)))
                element.click()
                time.sleep(3)
            except:
                pass

            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.GIVE_BACK_CUSTOMER)))
            element.click()
            time.sleep(3)

            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.card_g7)))
            element.click()
            time.sleep(3)

            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.CONFIRM)))
            element.click()
            time.sleep(3)

            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.igree)))
            element.click()
            time.sleep(3)

            try:
                var_stx_app.driver.implicitly_wait(0.5)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.card_g7_3cham).click()
                time.sleep(2)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.thanhtoantienmat).click()
                time.sleep(3)
            except:
                pass

            try:
                wait = WebDriverWait(var_stx_app.driver, 20)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.notification_icon_down)))
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification_icon_down).click()
                time.sleep(2)
            except:
                pass
            module_other_stx_app.click_app("G7 Taxi")
            time.sleep(2)


            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.SEND)
            except:
                module_other_stx_app.click_app("G7 Taxi")
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification_icon_down).click()
                time.sleep(1)
            except:
                pass



            #đánh giá lái xe
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.SEND)
            except:
                module_other_stx_app.click_app("G7 Taxi")
                time.sleep(2)


            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.friendly_attitude_checkbox)))
                element.click()
            except:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.friendly_attitude_checkbox1).click()
            time.sleep(1)
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.on_cared).click()# đã lên xe
                time.sleep(1)
            except:
                pass
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.review_4_star).click()
            except:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.review_4_star1).click()
            time.sleep(1)
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.review_checkbox1).click()
                time.sleep(1)
            except:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.review_checkbox2).click()
                time.sleep(1)
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.more_5000).click()
            except:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.more_5000_1).click()
            time.sleep(1)
            var_stx_app.driver.swipe(350, 950, 350, 400, 1000)
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.SEND).click()
            time.sleep(2)

            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.CONFIRM)))
            element.click()
            time.sleep(1)

            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_see_car)))
            time.sleep(1)
            module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(g7) - Đặt cuốc",
                                                  var_stx_app.check_see_car, "Cảm ơn quý khách đã tin dùng dịch vụ G7 Taxi, Chúc quý khách có một chuyến đi an toàn.", "_TrangChu_DatCuoc_GapXe.png")


        if type == "2":
            module_other_stx_app.click_app("G7 Taxi")



    def get_info_order(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)

        


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.space1)
        except:
            home_page.book_car_see_car(self, "", "", "", "2")

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_space_name)
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_icon_show).click()
            time.sleep(2)


        try:
            overview_time = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_time).text   #thời gian dự kiến
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 13, 2, overview_time)
        except:
            pass

        try:
            overview_space = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_space).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 2, 2, overview_space)
        except:
            overview_space = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_space_b).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 2, 2, overview_space)

        try:
            overview_fee = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_fee).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 3, 2, overview_fee)
        except:
            overview_fee = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_fee_b).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 3, 2, overview_fee)

        try:
            overview_promotion = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_promotion).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 4, 2, overview_promotion)
        except:
            overview_promotion = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_promotion_b).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 4, 2, overview_promotion)

        try:
            overview_price = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_price).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 5, 2, overview_price)
        except:
            overview_price = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_price_b).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 5, 2, overview_price)

        try:
            overview_location_from = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_location_from).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 6, 2, overview_location_from)
        except:
            overview_location_from = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_location_from_b).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 6, 2, overview_location_from)

        try:
            overview_location_to = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_location_to).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 7, 2, overview_location_to)
        except:
            overview_location_to = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_location_to_b).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 7, 2, overview_location_to)

        try:
            overview_liscenseplate_typecar = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_liscenseplate_typecar).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 8, 2, overview_liscenseplate_typecar)
        except:
            overview_liscenseplate_typecar = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_liscenseplate_typecar_b).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 8, 2, overview_liscenseplate_typecar)

        try:
            overview_typecar = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_typecar).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 9, 2, overview_typecar)
        except:
            overview_typecar = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_typecar_b).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 9, 2, overview_typecar)

        try:
            overview_star = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_star).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 10, 2, overview_star)
        except:
            overview_star = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_star_b).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 10, 2, overview_star)

        #icon phí 1
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_order_icon_fee_b).click()
        time.sleep(2)
        detail_typecar1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_typecar1).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 9, 3, detail_typecar1)

        detail_feemove1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_feemove1).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 3, 3, detail_feemove1)

        detail_space1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_space1).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 2, 3, detail_space1)

        detail_price1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_price1).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 5, 3, detail_price1)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_order_icon_fee_x).click()
        time.sleep(2)

        #chi tiết chuyến đi 2
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_order_see_detail_b).click()
        time.sleep(2)
        detail_namedriver2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_namedriver2).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 11, 4, detail_namedriver2)

        detail_typecar2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_typecar2).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 9, 4, detail_typecar2)

        detail_number2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_number2).text     #số hiệu
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 12, 4, detail_number2)

        detail_star2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_star2).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 10, 4, detail_star2)

        detail_space2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_space2).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 2, 4, detail_space2)

        detail_fee2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_fee2).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 3, 4, detail_fee2)

        detail_promotion2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_promotion2).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 4, 4, detail_promotion2)

        detail_price2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_price2).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 5, 4, detail_price2)

        detail_location_from2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_location_from2).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 6, 4, detail_location_from2)

        detail_location_to2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_location_to2).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 7, 4, detail_location_to2)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_order_see_detail_x).click()
        time.sleep(2)
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(g7) - Màn hình Thông tin cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("True")
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")


    def order_car_icon(self, code, eventname, result, type, path_icon, path_icon1, path_icon_x, path_check, desire, name_image):
        var_stx_app.driver.implicitly_wait(5)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.space1)
        except:
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_icon_show).click()
                time.sleep(2)
            except:
                pass


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.space1)
        except:
            home_page.book_car_see_car(self, "", "", "", "2")



        if type == "0":
            try:
                var_stx_app.driver.implicitly_wait(0.3)
                var_stx_app.driver.find_element(By.XPATH, path_icon).click()
            except:
                try:
                    var_stx_app.driver.find_element(By.XPATH, path_icon1).click()
                except:
                    pass
            time.sleep(1)
            module_other_stx_app.write_result_displayed_try(code, eventname, result, "Trang Chủ(g7) - Màn hình đã nhận cuốc",
                                                  path_check, name_image)

        if type == "1":
            try:
                var_stx_app.driver.implicitly_wait(0.3)
                var_stx_app.driver.find_element(By.XPATH, path_icon).click()
            except:
                try:
                    var_stx_app.driver.find_element(By.XPATH, path_icon1).click()
                except:
                    pass
            time.sleep(2.5)
            module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(g7) - Màn hình đã nhận cuốc",
                                                  path_check, desire, name_image)

            var_stx_app.driver.find_element(By.XPATH, path_icon_x).click()
            time.sleep(2)

        if type == "2":
            try:
                var_stx_app.driver.implicitly_wait(0.3)
                var_stx_app.driver.find_element(By.XPATH, path_icon).click()
            except:
                try:
                    var_stx_app.driver.find_element(By.XPATH, path_icon1).click()
                except:
                    pass
            time.sleep(2)
            module_other_stx_app.write_result_not_displayed_try(code, eventname, result, "Trang Chủ(g7) - Màn hình đã nhận cuốc",
                                                            path_check, name_image)
            try:
                var_stx_app.driver.implicitly_wait(0.3)
                var_stx_app.driver.find_element(By.XPATH, path_icon_x).click()
            except:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_car_icon_hide_b2).click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking).click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.CANCEL_BOOKING).click()
            time.sleep(2)
            wait = WebDriverWait(var_stx_app.driver, 20)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.customer_cancels_order)))
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2)
            module_other_stx_app.click_app("G7 Taxi")
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_car_back).click()
            time.sleep(2)

        if type == "3":
            try:
                var_stx_app.driver.implicitly_wait(0.3)
                var_stx_app.driver.find_element(By.XPATH, path_icon).click()
            except:
                try:
                    var_stx_app.driver.find_element(By.XPATH, path_icon1).click()
                except:
                    pass
            time.sleep(1)
            var_stx_app.logging.info("--------------")
            var_stx_app.logging.info("Trang Chủ(g7) - Màn hình đã nhận cuốc")
            var_stx_app.logging.info("Mã - " + code)
            var_stx_app.logging.info("Tên sự kiện - " + eventname)
            var_stx_app.logging.info("Kết quả - " + result)
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")

        if type == "4":
            try:
                var_stx_app.driver.implicitly_wait(0.3)
                var_stx_app.driver.find_element(By.XPATH, path_icon).click()
            except:
                try:
                    var_stx_app.driver.find_element(By.XPATH, path_icon1).click()
                except:
                    pass
            time.sleep(2.5)


            module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(g7) - Màn hình đã nhận cuốc",
                                                  path_check, desire, name_image)


    def cancel_order_car(self):
        var_stx_app.driver.implicitly_wait(7)
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CANCEL_BOOKING).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.customer_cancels_order)))
        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        time.sleep(2)
        module_other_stx_app.click_app("G7 Taxi")
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_car_back).click()
        time.sleep(2)


    def check_info_order_other(self, code, eventname, result, row, column, name):
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row, column))
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info(name+": {}".format(overview))
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, name+": {}".format(overview))
        if overview != "None":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            if name == "Thời gian dự kiến":
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "")
        module_other_stx_app.close_app()




    def check_info_order_distance(self, code, eventname, result):
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass


        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 2, 2))
        overview = re.findall(r'\d+', overview)
        detail1 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 2, 3))
        detail1 = re.findall(r'\d+', detail1)
        detail2 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 2, 4))
        detail2 = re.findall(r'\d+', detail2)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Khoảng cách(Tổng quan)    : {}".format(overview))
        var_stx_app.logging.info("Khoảng cách(icon cước phí): {}".format(detail1))
        var_stx_app.logging.info("Khoảng cách(Xem chi tiết) : {}".format(detail2))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Khoảng cách(Tổng quan): {}\nKhoảng cách(icon cước phí): {}\nKhoảng cách(Xem chi tiết): {}"
                                       .format(overview, detail1, detail2))
        if overview == detail1 == detail2:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")


    def convert_to_number(self, price):
        # Loại bỏ ký tự không phải số
        price = re.sub(r'[^\d]', '', price)
        return int(price)


    def check_info_order_fee(self, code, eventname, result):
        


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 3, 2))
        detail1 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 3, 3))
        detail2 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 3, 4))

        overview = home_page.convert_to_number(self, overview)
        detail1 = home_page.convert_to_number(self, detail1)
        detail1 = detail1 * 1000
        detail2 = home_page.convert_to_number(self, detail2)


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Cước phí(Tổng quan)          : {}".format(overview))
        var_stx_app.logging.info("Cước di chuyển(icon cước phí): {}".format(detail1))
        var_stx_app.logging.info("Cước phí(Xem chi tiết)       : {}".format(detail2))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Cước phí(Tổng quan): {}\nCước phí(icon cước phí): {}\nCước phí(Xem chi tiết): {}"
                                       .format(overview, detail1, detail2))
        if overview == detail1 == detail2:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")


    def check_info_order_promotion(self, code, eventname, result):
        


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 4, 2))
        detail2 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 4, 4))

        overview = home_page.convert_to_number(self, overview)
        detail2 = home_page.convert_to_number(self, detail2)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Khuyến mãi(Tổng quan)   : {}".format(overview))
        var_stx_app.logging.info("Khuyến mãi(Xem chi tiết): {}".format(detail2))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Khuyến mãi(Tổng quan): {}\nKhuyến mãi(Xem chi tiết): {}"
                                       .format(overview, detail2))
        if overview == detail2:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")


    def check_info_order_price(self, code, eventname, result):
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 5, 2))
        detail1 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 5, 3))
        detail2 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 5, 4))

        overview = home_page.convert_to_number(self, overview)
        detail1 = home_page.convert_to_number(self, detail1)
        detail1 = detail1 * 1000
        detail2 = home_page.convert_to_number(self, detail2)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Giá cước(Tổng quan)                : {}".format(overview))
        var_stx_app.logging.info("Tổng tiền thanh toán(icon cước phí): {}".format(detail1))
        var_stx_app.logging.info("Tiền mặt/Thẻ G7(Xem chi tiết)      : {}".format(detail2))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Giá cước(Tổng quan): {}\nTổng tiền thanh toán(icon cước phí): {}\nTiền mặt/Thẻ G7(Xem chi tiết): {}"
                                       .format(overview, detail1, detail2))
        if overview == detail1 == detail2:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")


    def check_info_order_location_from(self, code, eventname, result):
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 6, 2))
        detail2 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 6, 4))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Điểm đón(Tổng quan)   : {}".format(overview))
        var_stx_app.logging.info("Điểm đón(Xem chi tiết): {}".format(detail2))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Điểm đón(Tổng quan): {}\nĐiểm đón(Xem chi tiết): {}"
                                       .format(overview, detail2))

        result = normalize(self, detail2) in normalize(self, overview)
        if result == True:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")


    def check_info_order_location_to(self, code, eventname, result):
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 7, 2))
        detail2 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 7, 4))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Điểm đến(Tổng quan)   : {}".format(overview))
        var_stx_app.logging.info("Điểm đến(Xem chi tiết): {}".format(detail2))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Điểm đến(Tổng quan): {}\nĐiểm đến(Xem chi tiết): {}"
                                       .format(overview, detail2))

        result = normalize(self, detail2) in normalize(self, overview)
        if result == True:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")


    def check_info_order_star(self, code, eventname, result):
        


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 10, 2))
        detail2 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 10, 4))


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Số sao(Tổng quan)   : {}".format(overview))
        var_stx_app.logging.info("Số sao(Xem chi tiết): {}".format(detail2))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Số sao(Tổng quan): {}\nSố sao(Xem chi tiết): {}"
                                       .format(overview, detail2))
        if overview == detail2:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")


    def check_info_order_liscense_plate(self, code, eventname, result):
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 8, 2))
        bien_so = overview.split(" - ")  # Tách theo dấu " - "
        bien_so = bien_so[0]  # "30E03908"

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Biển số(Tổng quan)   : {}".format(overview))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Biển số(Tổng quan): {}"
                                       .format(bien_so))
        if bien_so != "None":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")


    def check_info_order_type_vehicle(self, code, eventname, result):
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 9, 2))
        detail1 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 9, 3))
        detail2 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 9, 4))
        overview = ''.join(re.findall(r'\d+', overview))
        detail1 = ''.join(re.findall(r'\d+', detail1))
        detail2 = ''.join(re.findall(r'\d+', detail2))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Loại xe(Tổng quan)    : {}".format(overview))
        var_stx_app.logging.info("Loại xe(icon cước phí): {}".format(detail1))
        var_stx_app.logging.info("Loại xe(Xem chi tiết) : {}".format(detail2))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Loại xe(Tổng quan): {}\nLoại xe(icon cước phí): {}\nLoại xe(Xem chi tiết): {}"
                                       .format(overview, detail1, detail2))
        if overview == detail1 == detail2:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")

















    def check_km(self, location_from, location_to, code_promotion, code_promotion1):
        wait = WebDriverWait(var_stx_app.driver, 10)

        


        var_stx_app.driver.implicitly_wait(2)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt)
        except:
            home_page.choose_location(self, "110 Cầu Giấy")

        #Điểm đón
        if location_from == "":
            pass
        else:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.location_1)))
            element.click()
            time.sleep(2)
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.search_location_input).send_keys(location_from)
            except:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_1).click()
                time.sleep(2)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.search_location_input).send_keys(location_from)
            time.sleep(3)
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.search_data1)))
                element.click()
            except:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.search_location_input).clear()
                time.sleep(0.5)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.search_location_input).send_keys(location_from)
                time.sleep(3)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.search_data1)))
                element.click()
            time.sleep(3)
            var_stx_app.driver.tap([(450, 550)])
            time.sleep(0.5)
            var_stx_app.driver.tap([(450, 550)])
            time.sleep(1.5)

        #Điểm đến
        if location_to == "":
            pass
        else:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.location_2)))
            element.click()
            time.sleep(2)
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.search_location_input).send_keys(location_to)
                time.sleep(3)
            except:
                var_stx_app.driver.tap([(450, 550)])
                time.sleep(0.5)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.location_2)))
                element.click()
                time.sleep(2)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.search_location_input).send_keys(location_to)
                time.sleep(3)
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.search_data1)))
                element.click()
            except:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.search_location_input).clear()
                time.sleep(1)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.search_location_input).send_keys(location_to)
                time.sleep(3)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.search_data1)))
                element.click()
            time.sleep(3)
            var_stx_app.driver.tap([(450, 550)])
            time.sleep(0.5)
            var_stx_app.driver.tap([(450, 550)])
            time.sleep(1.5)

        if code_promotion == "":
            pass
        else:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.PROMOTION)))
            element.click()
            time.sleep(2)
            try:
                wait = WebDriverWait(var_stx_app.driver, 20)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_PROMOTION)))
            except:
                var_stx_app.driver.tap([(450, 550)])
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.PROMOTION_input).clear()
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.PROMOTION_input).send_keys(code_promotion)
            time.sleep(1)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.PROMOTION_v)))
            element.click()
            time.sleep(1)
            try:
                wait = WebDriverWait(var_stx_app.driver, 10)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//*[@text='"+code_promotion+"']")))
            except:
                try:
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
                    time.sleep(2)
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.PROMOTION_input).clear()
                    time.sleep(0.5)
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.PROMOTION_input).send_keys(code_promotion1)
                    time.sleep(1)
                    var_stx_app.driver.find_element(By.XPATH, var_stx_app.PROMOTION_v).click()
                    time.sleep(1)
                    wait = WebDriverWait(var_stx_app.driver, 10)
                    element = wait.until(EC.element_to_be_clickable((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//*[@text='" + code_promotion + "']")))
                except:
                    pass
            time.sleep(1)



    def discount_15(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        home_page.check_km(self, "14 Nguyễn Cảnh Dị", "110 Cầu Giấy", "AUTOAQ", "AUTOER")
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        principal_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.principal_amount).text
        print(principal_amount)
        app_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.app_amount).text
        print(app_amount)

        try:
            #Số tiền gốc
            principal_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.principal_amount).text
            principal_amount = ''.join(re.findall(r'\d+', principal_amount))
            principal_amount = int(principal_amount)
            print(principal_amount)

            #Ưu đãi 15%
            money_promotion = (principal_amount/100)*15
            money_promotion = math.ceil(money_promotion)
            print(money_promotion)

            #Số tiền sau khi đã áp mã
            app_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.app_amount).text
            app_amount = ''.join(re.findall(r'\d+', app_amount))
            app_amount = int(app_amount)
            print(app_amount)

            #Số tiền tool tính
            money = principal_amount - money_promotion

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Số tiền gốc: {}\n- Ưu đãi 15%: {}\n- Số tiền sau áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, money_promotion, app_amount, money))
            var_stx_app.logging.info("Số tiền gốc: {}\n- Ưu đãi: 15%\n- Số tiền đã áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, app_amount, money_promotion))

            if abs(app_amount - money) <= 2:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam15%.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam15.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam15.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam15.png")



    def discount_20_order_100(self, code, eventname, result, location_from, location_to):
        var_stx_app.driver.implicitly_wait(5)
        home_page.check_km(self, location_from, location_to, "AUTOCH", "AUTO36")
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        principal_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.principal_amount).text
        print(principal_amount)
        app_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.app_amount).text
        print(app_amount)

        try:
            #Số tiền gốc
            principal_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.principal_amount).text
            principal_amount = ''.join(re.findall(r'\d+', principal_amount))
            principal_amount = int(principal_amount)
            print(principal_amount)

            #Ưu đãi 20%
            if principal_amount > 100:
                money_promotion = (principal_amount/100)*20
                money_promotion = math.ceil(money_promotion)
                print(money_promotion)
            else:
                money_promotion = 0

            #Số tiền sau khi đã áp mã
            app_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.app_amount).text
            app_amount = ''.join(re.findall(r'\d+', app_amount))
            app_amount = int(app_amount)
            print(app_amount)

            #Số tiền tool tính
            money = principal_amount - money_promotion

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Số tiền gốc: {}\n- Ưu đãi 20% đơn từ 100k: {}\n- Số tiền sau áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, money_promotion, app_amount, money))
            var_stx_app.logging.info("Số tiền gốc: {}\n- Ưu đãi 20% đơn từ 100k\n- Số tiền đã áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, app_amount, money_promotion))

            if abs(app_amount - money) <= 2:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam20%_Don100k.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam20%_Don100k.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam20%_Don100k.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam20%_Don100k.png")



    def discount_20_max_50k(self, code, eventname, result, location_from, location_to):
        var_stx_app.driver.implicitly_wait(5)
        home_page.check_km(self, location_from, location_to, "AUTOJ5", "AUTO1W")
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        principal_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.principal_amount).text
        app_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.app_amount).text

        try:
            #Số tiền gốc
            principal_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.principal_amount).text
            principal_amount = ''.join(re.findall(r'\d+', principal_amount))
            principal_amount = int(principal_amount)
            print("số tiền gốc: {}".format(principal_amount))

            #Ưu đãi 20%
            if principal_amount > 250:
                money_promotion = 50
                print("ưu đãi: {}".format(money_promotion))
            else:
                money_promotion = (principal_amount/100) * 20
                money_promotion = math.ceil(money_promotion)
                print("ưu đãi: {}".format(money_promotion))



            #Số tiền sau khi đã áp mã
            app_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.app_amount).text
            app_amount = ''.join(re.findall(r'\d+', app_amount))
            app_amount = int(app_amount)
            print("tiền sau khi áp mã: {}".format(app_amount))

            #Số tiền tool tính
            money = principal_amount - money_promotion
            print("tiền tool tính: {}".format(money))



            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Số tiền gốc: {}\n- Ưu đãi Giảm 20% Tối đa 50k: {}\n- Số tiền sau áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, money_promotion, app_amount, money))
            var_stx_app.logging.info("Số tiền gốc: {}\n- Ưu đãi Giảm 20% Tối đa 50k\n- Số tiền đã áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, app_amount, money_promotion))

            if abs(app_amount - money) <= 2:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam20%_Don100k.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam20%_Don100k.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam20%_Don100k.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam20%_Don100k.png")



    def discount_30_apply_for_customer(self, code, eventname, result, tratien, path_check, desire):
        var_stx_app.driver.implicitly_wait(5)
        home_page.check_km(self, "14 Nguyễn Cảnh Dị", "898 Chùa Láng", "AUTO7J", "AUTO1Q")
        # home_page.check_km(self, "", "", "AUTO1Q")
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)


        if tratien == "Trả tiền theo APP":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.payment_app).click()

        if tratien == "Đồng hồ Taxi":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.payment_clock_taxi).click()

        time.sleep(3)
        try:
            print("n1")
            # check_text = var_stx_app.driver.find_element(By.XPATH, path_check).text
            wait = WebDriverWait(var_stx_app.driver, 30)
            check_text = wait.until(EC.element_to_be_clickable((By.XPATH, path_check))).text

            print("n2")
            print(check_text)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, check_text)
            var_stx_app.logging.info(check_text)

            if check_text == desire:
                print("n3")
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam30%_AppKhachHang.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam30%_AppKhachHang.png")
        except:
            print("n4")
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam20%_Don100k.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam30%_AppKhachHang.png")



        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.goitongdai).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2)
        except:
            pass



    def discount_35_by_card(self, code, eventname, result, pttt):
        var_stx_app.driver.implicitly_wait(5)
        home_page.check_km(self, "14 Nguyễn Cảnh Dị", "231 Quan Nhân", "AUTOYG", "AUTO8S")
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt).click()
        time.sleep(2)

        if pttt == "TIỀN MẶT":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.tienmat).click()

        if pttt == "THẺ THÀNH VIÊN G7 TAXI":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt_card_g7).click()

        time.sleep(2)

        try:
            #Số tiền gốc
            principal_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.principal_amount).text
            principal_amount = ''.join(re.findall(r'\d+', principal_amount))
            principal_amount = int(principal_amount)
            print("số tiền gốc: {}".format(principal_amount))

            #Ưu đãi 35%
            if pttt == "THẺ THÀNH VIÊN G7 TAXI":
                money_promotion = (principal_amount/100) * 35
                money_promotion = math.ceil(money_promotion)
                print("ưu đãi: {}".format(money_promotion))
            else:
                money_promotion = 0
                print("ưu đãi: {}".format(money_promotion))

            #Số tiền sau khi đã áp mã
            app_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.app_amount).text
            app_amount = ''.join(re.findall(r'\d+', app_amount))
            app_amount = int(app_amount)
            print("tiền sau khi áp mã: {}".format(app_amount))

            #Số tiền tool tính
            money = principal_amount - money_promotion
            print("tiền tool tính: {}".format(money))

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "- Số tiền gốc: {}\n- Ưu đãi Giảm 35% khi thanh toán bằng ví điện tử: {}\n- Số tiền sau áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, money_promotion, app_amount, money))
            var_stx_app.logging.info("- Số tiền gốc: {}\n- Ưu đãi Giảm 35% khi thanh toán bằng ví điện tử\n- Số tiền đã áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, app_amount, money_promotion))

            if abs(app_amount - money) <= 2:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam35%_ThanhToanBangViDienTu.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam35%_ThanhToanBangViDienTu.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam35%_ThanhToanBangViDienTu.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam35%_ThanhToanBangViDienTu.png")



    def discount_25_for_10km(self, code, eventname, result, type):
        var_stx_app.driver.implicitly_wait(5)
        if type == "duoi10km":
            home_page.check_km(self, "14 Nguyễn Cảnh Dị", "230 Đại Từ", "AUTOSK", "AUTOXM")

        if type == "tren10km":
            home_page.check_km(self, "120 Thanh Nhàn", "Bờ Kè", "AUTOSK", "AUTOXM")

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)

        try:
            #Số tiền gốc
            principal_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.principal_amount).text
            principal_amount = ''.join(re.findall(r'\d+', principal_amount))
            principal_amount = int(principal_amount)
            print("số tiền gốc: {}".format(principal_amount))

            #Ưu đãi 25%
            if type == "duoi10km":
                money_promotion = 0
                print("ưu đãi: {}".format(money_promotion))
            else:
                money_promotion = (principal_amount/100) * 25
                money_promotion = math.ceil(money_promotion)
                print("ưu đãi: {}".format(money_promotion))


            #Số tiền sau khi đã áp mã
            app_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.app_amount).text
            app_amount = ''.join(re.findall(r'\d+', app_amount))
            app_amount = int(app_amount)
            print("tiền sau khi áp mã: {}".format(app_amount))

            #Số tiền tool tính
            money = principal_amount - money_promotion
            print("tiền tool tính: {}".format(money))


            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Số tiền gốc: {}\n- Ưu đãi Giảm 25% cho chuyến xe có quãng đường trên 10km: {}\n- Số tiền sau áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, money_promotion, app_amount, money))
            var_stx_app.logging.info("Số tiền gốc: {}\n- Ưu đãi Giảm 25% cho chuyến xe có quãng đường trên 10km\n- Số tiền đã áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, app_amount, money_promotion))

            if abs(app_amount - money) <= 2:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam25%_Don10km.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam25%_Don10km.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam25%_Don10km.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam25%_Don10km.png")



    def discount_30_inner_city(self, code, eventname, result, type):
        var_stx_app.driver.implicitly_wait(5)
        if type == "noithanh":
            home_page.check_km(self, "14 Nguyễn Cảnh Dị", "136 Giải Phóng", "AUTO3R", "AUTOPO")

        if type == "ngoaithanh":
            home_page.check_km(self, "Công ty TNHH Công Nghiệp Diamond", "Nội Bài", "AUTO3R", "AUTOPO")

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)

        try:
            #Số tiền gốc
            principal_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.principal_amount).text
            principal_amount = ''.join(re.findall(r'\d+', principal_amount))
            principal_amount = int(principal_amount)
            print("số tiền gốc: {}".format(principal_amount))

            #Ưu đãi 25%
            if type == "ngoaithanh":
                money_promotion = 0
                print("ưu đãi: {}".format(money_promotion))
            else:
                money_promotion = (principal_amount/100) * 30
                money_promotion = math.ceil(money_promotion)
                print("ưu đãi: {}".format(money_promotion))


            #Số tiền sau khi đã áp mã
            app_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.app_amount).text
            app_amount = ''.join(re.findall(r'\d+', app_amount))
            app_amount = int(app_amount)
            print("tiền sau khi áp mã: {}".format(app_amount))

            #Số tiền tool tính
            money = principal_amount - money_promotion
            print("tiền tool tính: {}".format(money))


            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Số tiền gốc: {}\n- Ưu đãi Giảm 30% cho cuốc tuyến nội thành: {}\n- Số tiền sau áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, money_promotion, app_amount, money))
            var_stx_app.logging.info("Số tiền gốc: {}\n- Ưu đãi Giảm 30% cho cuốc tuyến nội thành: {}\n- Số tiền đã áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, money_promotion, app_amount, money_promotion))

            if abs(app_amount - money) <= 2:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam30%_NoiThanh.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam30%_NoiThanh.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam30%_NoiThanh.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam30%_NoiThanh.png")



    def discount_15k(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        home_page.check_km(self, "14 Nguyễn Cảnh Dị", "231 Quan Nhân", "AUTOE2", "AUTOZG")
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)

        try:
            #Số tiền gốc
            principal_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.principal_amount).text
            principal_amount = ''.join(re.findall(r'\d+', principal_amount))
            principal_amount = int(principal_amount)
            print("số tiền gốc: {}".format(principal_amount))

            #Ưu đãi 15k
            money_promotion = 15
            if principal_amount <= 15:
                money_promotion = 0
            else:
                pass
            print("ưu đãi: {}".format(money_promotion))

            #Số tiền sau khi đã áp mã
            app_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.app_amount).text
            app_amount = ''.join(re.findall(r'\d+', app_amount))
            app_amount = int(app_amount)
            print("tiền sau khi áp mã: {}".format(app_amount))

            #Số tiền tool tính
            money = principal_amount - money_promotion
            print("tiền tool tính: {}".format(money))



            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Số tiền gốc: {}\n- Ưu đãi Giảm 15k: {}\n- Số tiền sau áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, money_promotion, app_amount, money))
            var_stx_app.logging.info("Số tiền gốc: {}\n- Ưu đãi Giảm 15k\n- Số tiền đã áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, app_amount, money_promotion))

            if app_amount == money:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam15k.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam15k.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam15k.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam15k.png")



    def discount_20k_order_100k(self, code, eventname, result, location_from, location_to):
        var_stx_app.driver.implicitly_wait(5)
        home_page.check_km(self, location_from, location_to, "AUTO1N", "AUTOK6")
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)

        try:
            #Số tiền gốc
            principal_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.principal_amount).text
            principal_amount = ''.join(re.findall(r'\d+', principal_amount))
            principal_amount = int(principal_amount)
            print("số tiền gốc: {}".format(principal_amount))

            #Ưu đãi 15k
            money_promotion = 20
            if principal_amount < 100:
                money_promotion = 0
            else:
                pass
            print("ưu đãi: {}".format(money_promotion))

            #Số tiền sau khi đã áp mã
            app_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.app_amount).text
            app_amount = ''.join(re.findall(r'\d+', app_amount))
            app_amount = int(app_amount)
            print("tiền sau khi áp mã: {}".format(app_amount))

            #Số tiền tool tính
            money = principal_amount - money_promotion
            print("tiền tool tính: {}".format(money))



            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Số tiền gốc: {}\n- Ưu đãi Giảm 20k đơn từ 100k: {}\n- Số tiền sau áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, money_promotion, app_amount, money))
            var_stx_app.logging.info("Số tiền gốc: {}\n- Ưu đãi Giảm 20k đơn từ 100k\n- Số tiền đã áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, app_amount, money_promotion))

            if abs(app_amount - money) <= 2:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam20k_DonTu100k.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam20k_DonTu100k.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam20k_DonTu100k.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam20k_DonTu100k.png")



    def discount_30k_apply_for_clock(self, code, eventname, result, tratien, path_check, desire):
        var_stx_app.driver.implicitly_wait(5)
        home_page.check_km(self, "14 Nguyễn Cảnh Dị", "110 Cầu Giấy", "AUTOCG", "AUTOPP")
        # home_page.check_km(self, "", "", "AUTO1Q")
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)


        if tratien == "Trả tiền theo APP":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.payment_app).click()

        if tratien == "Đồng hồ Taxi":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.payment_clock_taxi).click()

        time.sleep(3)
        try:
            print("n1")
            # check_text = var_stx_app.driver.find_element(By.XPATH, path_check).text
            wait = WebDriverWait(var_stx_app.driver, 30)
            check_text = wait.until(EC.element_to_be_clickable((By.XPATH, path_check))).text

            print("n2")
            print(check_text)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, check_text)
            var_stx_app.logging.info(check_text)

            if check_text == desire:
                print("n3")
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam30k_DongHoTaxi.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam30k_DongHoTaxi.png")
        except:
            print("n4")
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam30k_DongHoTaxi.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam30k_DongHoTaxi.png")



        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.goitongdai).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2)
        except:
            pass



    def discount_35k_by_card(self, code, eventname, result, pttt):
        var_stx_app.driver.implicitly_wait(5)
        home_page.check_km(self, "14 Nguyễn Cảnh Dị", "62 Hoàng Mai, Q. Hoàng Mai", "AUTO1H", "AUTOIY")
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt).click()
        time.sleep(2)

        if pttt == "TIỀN MẶT":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.tienmat).click()

        if pttt == "THẺ THÀNH VIÊN G7 TAXI":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt_card_g7).click()

        time.sleep(2)

        try:
            #Số tiền gốc
            principal_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.principal_amount).text
            principal_amount = ''.join(re.findall(r'\d+', principal_amount))
            principal_amount = int(principal_amount)
            print("số tiền gốc: {}".format(principal_amount))

            #Ưu đãi 355
            if pttt == "THẺ THÀNH VIÊN G7 TAXI":
                money_promotion = 35
            else:
                money_promotion = 0
                print("ưu đãi: {}".format(money_promotion))

            #Số tiền sau khi đã áp mã
            app_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.app_amount).text
            app_amount = ''.join(re.findall(r'\d+', app_amount))
            app_amount = int(app_amount)
            print("tiền sau khi áp mã: {}".format(app_amount))

            #Số tiền tool tính
            money = principal_amount - money_promotion
            if money < 0:
                money = 0

            print("tiền tool tính: {}".format(money))

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "- Số tiền gốc: {}\n- Ưu đãi Giảm 35k khi thanh toán bằng thẻ: {}\n- Số tiền sau áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, money_promotion, app_amount, money))
            var_stx_app.logging.info("- Số tiền gốc: {}\n- Ưu đãi Giảm 35k khi thanh toán bằng thẻ\n- Số tiền đã áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, app_amount, money_promotion))

            if abs(app_amount - money) <= 2:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam35K_ThanhToanBangThe.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam35K_ThanhToanBangThe.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam35K_ThanhToanBangThe.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam35K_ThanhToanBangThe.png")



    def discount_50k_inner_city(self, code, eventname, result, type):
        var_stx_app.driver.implicitly_wait(5)
        if type == "noithanh":
            home_page.check_km(self, "Nội Bài", " 62 Hoàng Mai, Q. Hoàng Mai", "AUTORN", "AUTOM8")

        if type == "ngoaithanh":
            home_page.check_km(self, "Nội Bài", "Đại Thành, H. Quốc Oai", "AUTORN", "AUTOM8")

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)

        try:
            #Số tiền gốc
            principal_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.principal_amount).text
            principal_amount = ''.join(re.findall(r'\d+', principal_amount))
            principal_amount = int(principal_amount)
            print("số tiền gốc: {}".format(principal_amount))

            #Ưu đãi 25%
            if type == "ngoaithanh":
                money_promotion = 0
                print("ưu đãi: {}".format(money_promotion))
            else:
                money_promotion = 50
                print("ưu đãi: {}".format(money_promotion))


            #Số tiền sau khi đã áp mã
            app_amount = var_stx_app.driver.find_element(By.XPATH, var_stx_app.app_amount).text
            app_amount = ''.join(re.findall(r'\d+', app_amount))
            app_amount = int(app_amount)
            print("tiền sau khi áp mã: {}".format(app_amount))

            #Số tiền tool tính
            money = principal_amount - money_promotion
            if money < 0:
                money = 0
            print("tiền tool tính: {}".format(money))


            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Số tiền gốc: {}\n- Ưu đãi Giảm 50k cho chuyến xe đi từ sân bay về trung tâm thành phố: {}\n- Số tiền sau áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, money_promotion, app_amount, money))
            var_stx_app.logging.info("Số tiền gốc: {}\n- Ưu đãi Giảm 50k cho chuyến xe đi từ sân bay về trung tâm thành phố: {}\n- Số tiền đã áp mã: {}\n- Số tiền tool tính: {}"
                                           .format(principal_amount, money_promotion, app_amount, money_promotion))

            if abs(app_amount - money) <= 2:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam30k_TuSanBay.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam30k_TuSanBay.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam30k_TuSanBay.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam30k_TuSanBay.png")

        if type == "ngoaithanh":
            module_other_stx_app.close_app()








    def book_car_inner_city(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(2)
        module_other_stx_app.close_app()

        wait = WebDriverWait(var_stx_app.driver, 10)
        homepage_driver.home_page.status_driver(self, "Xe sân bay", "SẴN SÀNG")
        login_stx_app.g7.login_g7(self, "0359667694")
        # 
        # try:
        #     module_other_stx_app.click_app("Lái xe G7")
        #     time.sleep(1)
        #     var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification)
        # except:
        #     homepage_driver.home_page.status_driver(self, "Xe sân bay", "SẴN SÀNG")
        # 
        # try:
        #     module_other_stx_app.click_app("G7 Taxi")
        #     time.sleep(1)
        #     var_stx_app.driver.find_element(By.XPATH, var_stx_app.promotion)
        # except:
        #     login_stx_app.g7.login_g7(self, "0359667694")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.book_car_inner_city).click()
        time.sleep(3)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_destination_note).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_destination_note_input).send_keys(var_stx_app.data['home_page_g7']['note'])
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.IGREE).click()
        time.sleep(1.5)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.confirm_pick_up_point)))
        element.click()
        time.sleep(3.5)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.location_2_icon)))
        element.click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.search_location_input).send_keys("102 Mai Dịch")
        time.sleep(3)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.search_data1)))
        element.click()
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.search_data1)
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.search_location_input).clear()
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.search_location_input).send_keys("102 Mai Dịch")
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.search_data1)))
            element.click()

        time.sleep(3)
        select_type_car("7 Chỗ")

        # var_stx_app.driver.find_element(By.XPATH, var_stx_app.car_7_sit).click()
        # time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt).click()
        time.sleep(3)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt_card_g7).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.clock_taxi).click()
        time.sleep(3)
        wait = WebDriverWait(var_stx_app.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.RECEIVE_APP)))
        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.RECEIVE_APP).click()
        time.sleep(2.5)
        module_other_stx_app.click_app("G7 Taxi")
        time.sleep(1)
        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Trang Chủ(g7) - Đặt cuốc nội thành",
                                              var_stx_app.order_car_drive, "", "_TrangChu_DatCuocNọiThanh.png")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.SKIP).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CANCEL_BOOKING).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.customer_cancels_order)))
        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        time.sleep(2)
        module_other_stx_app.click_app("G7 Taxi")
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_car_back).click()
        time.sleep(2)



    def book_car_inner_airport(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(2)
        wait = WebDriverWait(var_stx_app.driver, 10)
        homepage_driver.home_page.status_driver(self, "Xe sân bay", "SẴN SÀNG")
        login_stx_app.g7.login_g7(self, "0359667694")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.book_car_inner_airport).click()
        time.sleep(3)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_destination_note).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_destination_note_input).send_keys(var_stx_app.data['home_page_g7']['note'])
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.IGREE).click()
        time.sleep(1.5)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.confirm_pick_up_point)))
        element.click()
        time.sleep(3.5)

        try:
            select_type_car("Sân Bay 7 Chỗ")
            # var_stx_app.driver.find_element(By.XPATH, var_stx_app.car_airport_7_sit).click()
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt).click()
            time.sleep(3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt_card_g7).click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.clock_taxi).click()
            time.sleep(3)
            print("da chon the")
        except:
            pass
        try:
            wait = WebDriverWait(var_stx_app.driver, 20)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.RECEIVE_APP)))
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.RESET_CAR).click()
            time.sleep(3)
            wait = WebDriverWait(var_stx_app.driver, 20)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.RECEIVE_APP)))
        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.RECEIVE_APP).click()
        time.sleep(2.5)
        module_other_stx_app.click_app("G7 Taxi")
        time.sleep(1)
        try:
            wait = WebDriverWait(var_stx_app.driver, 5)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.order_car_location_to)))
        except:
            pass
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(g7) - Đặt cuốc sân bay",
                                              var_stx_app.order_car_location_to, "Sân Bay Quốc Tế Nội Bài", "_TrangChu_DatCuocSanBay.png")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.SKIP).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_booking).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CANCEL_BOOKING).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.customer_cancels_order)))
        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        time.sleep(2)
        module_other_stx_app.click_app("G7 Taxi")
        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_car_back).click()
        time.sleep(2)
        module_other_stx_app.close_app()







