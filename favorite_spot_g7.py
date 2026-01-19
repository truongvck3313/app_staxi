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
import var_stx_app
wait = WebDriverWait(var_stx_app.driver_customer, 10)
import homepage_g7
import action




class favorite_spot:



    def check_location_home(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.homepage, time_wait=2)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.homepage)

        try:
            home_location_before = action.get_text(var_stx_app.driver_customer, var_stx_app.home_before)
        except:
            var_stx_app.restart_driver(var_stx_app.driver_customer)

        home_location_before = action.get_text(var_stx_app.driver_customer, var_stx_app.home_before)
        action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot)

        home_location_after = action.get_text(var_stx_app.driver_customer, var_stx_app.home_location_after)
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
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "_DiemYeuThich_CheckViTri.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_DiemYeuThich_CheckViTri.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "_DiemYeuThich_CheckViTri.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_DiemYeuThich_CheckViTri.png")


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot_back, time_wait=3)
            time.sleep(1)
        except:
            pass



    def search_spot_from(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot, time_wait=2)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot)

        action.click(var_stx_app.driver_customer, var_stx_app.add_favorite_spot)
        action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot_from)

        action.send_keys(var_stx_app.driver_customer, var_stx_app.favorite_spot_from_input, "250 Đường Phan Trọng Tuệ")
        action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot_to1)


        action.send_keys(var_stx_app.driver_customer, var_stx_app.favorite_spot_to_input1, "250 Đường Phan Trọng Tuệ")

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_search_spot_to1, time_wait=15)
        except:
            action.clear(var_stx_app.driver_customer, var_stx_app.favorite_spot_to_input1)
            action.send_keys(var_stx_app.driver_customer, var_stx_app.favorite_spot_to_input1, "250 Đường Phan Trọng Tuệ")


        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_search_spot_to1)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Điểm yêu thích(g7) - Tìm kiếm",
                                                      var_stx_app.check_search_spot_to1, "250 Đường Phan Trọng Tuệ, phường Thanh Liệt, thành phố Hà Nội",
                                                      "_DiemYeuThich_TimKiemDiemDen.png")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot_back1, time_wait=7)
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot_back2)
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot_back3)
            time.sleep(1)
        except:
            pass



    def add_favorite_spot(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot, time_wait=2)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot)


        try:
            favorite_spot.select_spot(self, var_stx_app.data['favorite_spot_g7']['add_new'])
            action.click(var_stx_app.driver_customer, var_stx_app.DELETE)
        except:
            pass


        action.click(var_stx_app.driver_customer, var_stx_app.add_favorite_spot)
        action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot_to_x)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.favorite_spot_to_input, var_stx_app.data['favorite_spot_g7']['add_new'])
        action.click(var_stx_app.driver_customer, var_stx_app.SAVE_SPOT)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_add_favorite_spot, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Điểm yêu thích(g7)",
                                                      var_stx_app.check_add_favorite_spot, var_stx_app.data['favorite_spot_g7']['add_new'],
                                                      "_DiemYeuThich_ThemDiaChiYeuThich.png")



    def choose_favorite_spot(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot, time_wait=2)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot)



        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_add_favorite_spot, time_wait=3)
        except:
            favorite_spot.add_favorite_spot(self, "", "", "")

        action.click(var_stx_app.driver_customer, var_stx_app.check_add_favorite_spot)
        action.click(var_stx_app.driver_customer, var_stx_app.icon_pick_up_point)
        try:
            action.send_keys(var_stx_app.driver_customer, var_stx_app.icon_pick_up_point_input, "15 Ngách 15 Ngõ Gốc Đề", time_wait=10)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_pick_up_point)
            action.send_keys(var_stx_app.driver_customer, var_stx_app.icon_pick_up_point_input, "15 Ngách 15 Ngõ Gốc Đề")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_pick_up_point_input2, time_wait=15)
        except:
            action.clear(var_stx_app.driver_customer, var_stx_app.icon_pick_up_point_input)
            action.send_keys(var_stx_app.driver_customer, var_stx_app.icon_pick_up_point_input, "15 Ngách 15 Ngõ Gốc Đề")
            action.click(var_stx_app.driver_customer, var_stx_app.icon_pick_up_point_input2)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.location_2)
        except:
            pass

        module_other_stx_app.write_result_text_try_if_cut(var_stx_app.driver_customer, code, eventname, result, "Điểm yêu thích(g7)",
                                                      var_stx_app.location_2, 0, 14, var_stx_app.data['favorite_spot_g7']['add_new'],
                                                      "_DiemYeuThich_ChonDiemYeuThich.png")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.order_car_back, time_wait=3)
            time.sleep(2)
        except:
            pass

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.order_car_back, time_wait=1)
            time.sleep(2)
        except:
            pass



    def select_spot(self, data):
        n = 0
        while (n < 10):
            n = n + 1
            path_name = f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[{str(n)}]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView[1]"

            path_icon = f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[{str(n)}]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.widget.TextView"
            print(f"n: {n}")
            print(f"path_icon: {path_icon}")

            try:
                name = action.get_text(var_stx_app.driver_customer, path_name, time_wait=1)
                print(f"name: {name}")
                if name == data:
                    action.click(var_stx_app.driver_customer, path_icon)
                    time.sleep(2)
                    break
            except:
                pass



    def select_name_spot(self, data):
        n = 0
        while (n < 10):
            n = n + 1
            n = str(n)
            path_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView[1]"
            path_address = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView[2]"

            try:
                name = action.get_text(var_stx_app.driver_customer, path_name, time_wait=1)
                if name == data:
                    address = action.get_text(var_stx_app.driver_customer, path_address)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 14, 2, address)
                    action.click(var_stx_app.driver_customer, path_name)
                    time.sleep(2)
                    break
            except:
                pass
            n = int(n)



    def favorite_edit(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot, time_wait=2)

        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_add_favorite_spot, time_wait=3)
        except:
            var_stx_app.restart_driver(var_stx_app.driver_customer)
            favorite_spot.add_favorite_spot(self, "", "", "")

        favorite_spot.select_spot(self, var_stx_app.data['favorite_spot_g7']['add_new'])
        action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot_to_x)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.favorite_spot_to_input, var_stx_app.data['favorite_spot_g7']['add_new_edit'])
        action.click(var_stx_app.driver_customer, var_stx_app.SAVE_SPOT)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_add_favorite_spot_edit, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Điểm yêu thích(g7)",
                                                      var_stx_app.check_add_favorite_spot_edit, var_stx_app.data['favorite_spot_g7']['add_new_edit'],
                                                      "_DiemYeuThich_SuaDiaYeuThich.png")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot_back3, time_wait=5)
            time.sleep(2)
        except:
            pass



    def favorite_delete(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot, time_wait=2)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot)


        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_add_favorite_spot_edit, time_wait=1)
        except:
            favorite_spot.favorite_edit(self, "", "", "")

        favorite_spot.select_spot(self, var_stx_app.data['favorite_spot_g7']['add_new_edit'])
        action.click(var_stx_app.driver_customer, var_stx_app.DELETE)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.check_add_favorite_spot_edit, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_not_displayed_try(var_stx_app.driver_customer, code, eventname, result, "Điểm yêu thích(g7)",
                                                      var_stx_app.check_add_favorite_spot_edit, "_DiemYeuThich_XoaDiemYeuThich.png")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot_back3, time_wait=5)
            time.sleep(2)
        except:
            pass



    def favorite_spot_edit(self, code, eventname, result, name, module, path_check, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot, time_wait=2)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot)

        favorite_spot.select_spot(self, name)
        # try:
        #     var_stx_app.driver_customer.swipe(750, 700, 140, 900, 1000)
        # except:
        #     var_stx_app.driver_customer.swipe(200, 500, 200, 900, 1000)

        module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.1, 0.3, 0.9, 0.3, 1000)
        time.sleep(2)

        edit_spot_to = action.get_text(var_stx_app.driver_customer, var_stx_app.edit_spot_to)
        action.click(var_stx_app.driver_customer, var_stx_app.SAVE_SPOT)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info(module)
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            check_text = action.get_text(var_stx_app.driver_customer, path_check, time_wait=15)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Điểm đến chỉnh sửa: {}\nĐiểm đến sau khi lưu: {}".format(edit_spot_to, check_text))
            var_stx_app.logging.info(check_text)
            if check_text == edit_spot_to:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + name_image)
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + name_image)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)



    def select_spot_to(self, code, eventname, result, name, module, path_check, number_from, number_to, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot, time_wait=2)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.favorite_spot)

        favorite_spot.select_name_spot(self, name)
        action.click(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info(module)
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            check_text = action.get_text(var_stx_app.driver_customer, path_check, time_wait=15)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, check_text)
            var_stx_app.logging.info(check_text)
            var_stx_app.logging.info(check_text[number_from: number_to])
            var_stx_app.logging.info(name)
            if check_text[number_from: number_to] == name:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + name_image)
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + name_image)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)



        try:
            action.click(var_stx_app.driver_customer, var_stx_app.order_car_back, time_wait=5)
            time.sleep(2)
        except:
            pass

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.order_car_back, time_wait=1)
            time.sleep(2.5)
        except:
            pass



