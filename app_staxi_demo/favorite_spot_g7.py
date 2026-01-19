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
wait = WebDriverWait(var_stx_app.driver, 10)
import homepage_g7





class favorite_spot:



    def check_location_home(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(2)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage).click()
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage).click()
        time.sleep(2)
        try:
            home_location_before = var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_location_before1).text
        except:
            home_location_before = var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_location_before).text
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot).click()
        time.sleep(2.5)
        home_location_after = var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_location_after).text
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Điểm yêu thích(g7)")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)

        try:
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Trang chủ: {}\nĐiểm yêu thích: {}".format(home_location_before, home_location_after))
            var_stx_app.logging.info("Trang chủ: {}\nĐiểm yêu thích: {}".format(home_location_before, home_location_after))
            if home_location_before == home_location_after:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_DiemYeuThich_CheckViTri.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_DiemYeuThich_CheckViTri.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_DiemYeuThich_CheckViTri.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_DiemYeuThich_CheckViTri.png")


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot_back).click()
            time.sleep(2)
        except:
            pass



    def search_spot_from(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(2)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot).click()
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot).click()
        time.sleep(2)

        # module_other_stx_app.close_app()
        # login_stx_app.g7.login_g7(self, "0359667694")
        # var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot).click()
        # time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.add_favorite_spot).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot_from).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot_from_input).send_keys("231 Quan Nhân")
        time.sleep(2.5)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_search_spot_from1)
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot_from_input).clear()
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot_from_input).send_keys("231 Quan Nhân")
            time.sleep(2.5)

        # var_stx_app.driver.tap([(450, 500)])
        # time.sleep(0.5)
        # var_stx_app.driver.tap([(450, 500)])
        # var_stx_app.driver.tap([(450, 500)])
        # time.sleep(0.5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Điểm yêu thích(g7) - Tìm kiếm",
                                                      var_stx_app.check_search_spot_from1, "231 Quan Nhân",
                                                      "_DiemYeuThich_TimKiemDiemDen.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot_back1).click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot_back2).click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot_back3).click()
            time.sleep(2)
        except:
            pass



    def add_favorite_spot(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(2)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot).click()
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot).click()
        time.sleep(2)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.add_favorite_spot).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot_to_x).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot_to_input).send_keys(var_stx_app.data['favorite_spot_g7']['add_new'])
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.SAVE_SPOT).click()
        time.sleep(3.5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Điểm yêu thích(g7)",
                                                      var_stx_app.check_add_favorite_spot, var_stx_app.data['favorite_spot_g7']['add_new'],
                                                      "_DiemYeuThich_ThemDiaChiYeuThich.png")



    def choose_favorite_spot(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(2)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot).click()
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot).click()
        time.sleep(2)


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_add_favorite_spot)
        except:
            favorite_spot.add_favorite_spot(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_add_favorite_spot).click()
        time.sleep(3)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_pick_up_point).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_pick_up_point_input).send_keys("15 Ngách 15 Ngõ Gốc Đề")
        time.sleep(2.5)
        # location_before = var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_pick_up_point_input1).text
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_pick_up_point_input2).click()
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_pick_up_point_input).clear()
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_pick_up_point_input).send_keys()
            time.sleep(2.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_pick_up_point_input2).click()
        time.sleep(3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_pick_up_point).click()
            time.sleep(3)
        except:
            pass
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.location_2)))

        module_other_stx_app.write_result_text_try_if_cut(code, eventname, result, "Điểm yêu thích(g7)",
                                                      var_stx_app.location_2, 0, 14, var_stx_app.data['favorite_spot_g7']['add_new'],
                                                      "_DiemYeuThich_ChonDiemYeuThich.png")

        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.order_car_back)))
            element.click()
            time.sleep(2.5)
        except:
            pass
        try:
            var_stx_app.driver.implicitly_wait(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_car_back).click()
            time.sleep(2.5)
        except:
            pass



    def select_spot(self, data):
        var_stx_app.driver.implicitly_wait(0.1)
        n = 0
        while (n < 25):
            n = n + 1
            n = str(n)
            path_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView[1]"
            path_icon = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.widget.TextView"
            try:
                name = var_stx_app.driver.find_element(By.XPATH, path_name).text
                if name == data:
                    var_stx_app.driver.find_element(By.XPATH, path_icon).click()
                    time.sleep(3)
                    break
            except:
                pass
            n = int(n)



    def select_name_spot(self, data):
        var_stx_app.driver.implicitly_wait(0.1)
        n = 0
        while (n < 25):
            n = n + 1
            n = str(n)
            path_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView[1]"
            path_address = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView[2]"
            try:
                name = var_stx_app.driver.find_element(By.XPATH, path_name).text
                if name == data:
                    address = var_stx_app.driver.find_element(By.XPATH, path_address).text
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 14, 2, address)
                    var_stx_app.driver.find_element(By.XPATH, path_name).click()
                    time.sleep(3)
                    break
            except:
                pass
            n = int(n)



    def favorite_edit(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(2)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot).click()
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot).click()
        time.sleep(2)

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_add_favorite_spot)
        except:
            favorite_spot.add_favorite_spot(self, "", "", "")


        favorite_spot.select_spot(self, var_stx_app.data['favorite_spot_g7']['add_new'])

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot_to_x).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot_to_input).send_keys(var_stx_app.data['favorite_spot_g7']['add_new_edit'])
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.SAVE_SPOT).click()
        time.sleep(3.5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Điểm yêu thích(g7)",
                                                      var_stx_app.check_add_favorite_spot_edit, var_stx_app.data['favorite_spot_g7']['add_new_edit'],
                                                      "_DiemYeuThich_SuaDiaYeuThich.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot_back3).click()
            time.sleep(2)
        except:
            pass



    def favorite_delete(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(2)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot).click()
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot).click()
        time.sleep(2)

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_add_favorite_spot_edit)
        except:
            favorite_spot.favorite_edit(self, "", "", "")

        favorite_spot.select_spot(self, var_stx_app.data['favorite_spot_g7']['add_new_edit'])

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.DELETE).click()
        time.sleep(3.5)
        module_other_stx_app.write_result_not_displayed_try(code, eventname, result, "Điểm yêu thích(g7)",
                                                      var_stx_app.check_add_favorite_spot_edit, "_DiemYeuThich_XoaDiemYeuThich.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot_back3).click()
            time.sleep(2)
        except:
            pass




    def favorite_spot_edit(self, code, eventname, result, name, module, path_check, name_image):
        var_stx_app.driver.implicitly_wait(2)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot).click()
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot).click()
        time.sleep(2)

        favorite_spot.select_spot(self, name)
        try:
            var_stx_app.driver.swipe(750, 700, 140, 900, 1000)
        except:
            var_stx_app.driver.swipe(200, 500, 200, 900, 1000)
        time.sleep(1.5)
        # var_stx_app.driver.swipe(750, 700, 140, 900, 1000)
        edit_spot_to = var_stx_app.driver.find_element(By.XPATH, var_stx_app.edit_spot_to).text

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.SAVE_SPOT).click()
        time.sleep(3.5)
        # module_other_stx_app.write_result_text_try_if(code, eventname, result, module,
        #                                               path_check, edit_spot_to, name_image)
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info(module)
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            check_text = var_stx_app.driver.find_element(By.XPATH, path_check).text
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Điểm đến chỉnh sửa: {}\nĐiểm đến sau khi lưu: {}".format(edit_spot_to, check_text))
            var_stx_app.logging.info(check_text)
            if check_text == edit_spot_to:
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




    def select_spot_to(self, code, eventname, result, name, module, path_check, number_from, number_to, name_image):
        var_stx_app.driver.implicitly_wait(2)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot).click()
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.favorite_spot).click()
        time.sleep(2)

        favorite_spot.select_name_spot(self, name)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_pick_up_point).click()
        # address = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 14, 2))
        time.sleep(3.5)
        #
        # a = var_stx_app.driver.find_element(By.XPATH, path_check).text
        # print(a[number_from: number_to])
        # print(address)
        # module_other_stx_app.write_result_text_try_if_cut(code, eventname, result, module, path_check,
        #                                                   number_from, number_to, address, name_image)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info(module)
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            check_text = var_stx_app.driver.find_element(By.XPATH, path_check).text
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, check_text)
            var_stx_app.logging.info(check_text)
            var_stx_app.logging.info(check_text[number_from: number_to])
            var_stx_app.logging.info(name)
            if check_text[number_from: number_to] == name:
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



