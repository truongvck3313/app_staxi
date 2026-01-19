import time
from selenium.webdriver.common.by import By
import re
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
import action
import module_other_stx_app
import login_stx_app
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import homepage_driver
from pynput.keyboard import Key, Controller
keyboard = Controller()
import math
import var_stx_app
import threading



wait = WebDriverWait(var_stx_app.driver_customer, 10)



def select_type_car(type_car):
    n = 0
    while (n < 5):
        n = n + 1
        n = str(n)
        path_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[" + n + "]/android.view.ViewGroup[2]/android.widget.TextView"
        path_button = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[" + n + "]/android.view.ViewGroup[1]/android.widget.ImageView"

        try:
            name = action.get_text(var_stx_app.driver_customer, path_name, time_wait=1)
            print(name)
            if name == type_car:
                action.click(var_stx_app.driver_customer, path_button)
                time.sleep(2)
                break
        except:
            pass
        n = int(n)









def normalize(self, text):
    return re.sub(r"[^\w\s]", "", text.lower()).strip()
# result = normalize(self, location_before) in normalize(self, location_after)


def homepage_g7_back():
    var_stx_app.reset_app(var_stx_app.driver_customer)
    # var_stx_app.open_app(var_stx_app.driver_customer)
    try:
        action.click(var_stx_app.driver_customer, var_stx_app.icon_fee_x, time_wait=8)
        time.sleep(2)
        print("l1")
    except:
        pass
    print("đang tắt thông báo app customer")

    try:
        action.wait_for(var_stx_app.driver_customer, var_stx_app.home_page, time_wait=1)
        return
    except:
        pass

    try:
        action.click(var_stx_app.driver_customer, var_stx_app.icon_back1, time_wait=1)
        time.sleep(2)
        print("l2")
    except:
        pass

    try:
        action.click(var_stx_app.driver_customer, var_stx_app.cancel_booking, time_wait=1)
        time.sleep(2)
        print("l3")
    except:
        pass

    try:
        action.click(var_stx_app.driver_customer, var_stx_app.call_and_cancel, time_wait=1)
        time.sleep(2)
        print("l4")
    except:
        pass

    try:
        action.click(var_stx_app.driver_customer, var_stx_app.igree, time_wait=1)
        time.sleep(2)
        print("l5")
    except:
        pass

    try:
        action.click(var_stx_app.driver_customer, var_stx_app.complete, time_wait=1)
        time.sleep(2.5)
        print("l6")
    except:
        pass
    try:
        action.click(var_stx_app.driver_customer, var_stx_app.review_x, time_wait=1)
        time.sleep(2)
        print("l7")
    except:
        pass

    try:
        action.click(var_stx_app.driver_customer, var_stx_app.ALLOW, time_wait=1)
        time.sleep(2)
        print("l8")
    except:
        pass
    try:
        action.click(var_stx_app.driver_customer, var_stx_app.USE_APP, time_wait=1)
        time.sleep(2)
        print("l9")
    except:
        pass
    try:
        action.click(var_stx_app.driver_customer, var_stx_app.complete, time_wait=1)
        time.sleep(2)
        print("l10")
    except:
        pass
    try:
        action.click(var_stx_app.driver_customer, var_stx_app.CANCEL, time_wait=1)
        time.sleep(2)
        print("l11")
    except:
        pass
    try:
        action.wait_for(var_stx_app.driver_customer, var_stx_app.location_1, time_wait=1)
        action.click(var_stx_app.driver_customer, var_stx_app.order_car_back, time_wait=3)
        time.sleep(2)
        print("l12")
    except:
        pass

    try:
        print("Check session customer")
        # LỆNH BẮT BUỘC proxy qua UiAutomator2
        var_stx_app.driver_customer.get_window_size()
        print("vẫn còn session")
    except Exception as e:
        print(f"session chết thật rồi → recreate driver: {e}")
        var_stx_app.restart_driver(var_stx_app.driver_customer)
        print("đã reset lại session")

    print("đã tắt thông báo app customer")



def zoom(driver, type_zoom, number):
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    i = 0
    if type_zoom == "Phóng to":
        for i in range(number):
            i = i + 1
            # Ngón tay thứ nhất kéo từ xa về gần trung tâm
            action1.press(x=450, y=200).move_to(x=450, y=500).release()

            # Ngón tay thứ hai kéo từ xa về gần trung tâm
            action2.press(x=450, y=950).move_to(x=450, y=550).release()

            # Kết hợp hai hành động thành MultiAction
            pinch_action = MultiAction(driver)
            pinch_action.add(action1, action2)
            pinch_action.perform()
            time.sleep(1)
            print("Đã phóng to lần: ", i)

    if type_zoom == "Thu nhỏ":
        for i in range(number):
            i = i + 1
            # Ngón tay thứ nhất kéo từ xa về gần trung tâm
            action1.press(x=830, y=230).move_to(x=450, y=500).release()

            # Ngón tay thứ hai kéo từ xa về gần trung tâm
            action2.press(x=60, y=900).move_to(x=400, y=600).release()

            # Kết hợp hai hành động thành MultiAction
            pinch_action = MultiAction(driver)
            pinch_action.add(action1, action2)
            pinch_action.perform()
            time.sleep(2)
            print("Đã thu nhỏ lần: ", i)



def wait_complete(times):
    n = 0
    while (n < times):
        n = n + 1
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.complete, time_wait=1)
            time.sleep(2)
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.CANCEL, time_wait=1)
            except:
                pass
            break
        except:
            pass








class home_page:

    def icon_map(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_map, time_wait=1)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.icon_map)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_icon_map, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Map",
                                              var_stx_app.check_icon_map, "Chọn điểm đến", "_TrangChu_IconMap.png")
        if code == "HomePage01":
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.icon_map_back, time_wait=3)
                time.sleep(1.5)
            except:
                pass



    def icon_destination(self, code, eventname, result, path_icon, name_before, name_before1,  number_from, number_to, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            print("n0")
            action.wait_for(var_stx_app.driver_customer, "//*[@text='"+path_icon+"']", time_wait=1)
            print("n1")
        except:
            print("n2")
            login_stx_app.g7.login_g7(self, "0359667694")

        try:
            action.wait_for(var_stx_app.driver_customer, "//*[@text='"+path_icon+"']", time_wait=3)
            print("n3")
            print("//*[@text='"+path_icon+"']")
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            print("n4")



        try:
            name_before = action.get_text(var_stx_app.driver_customer, name_before)
            action.click(var_stx_app.driver_customer, "//*[@text='"+path_icon+"']")
            print(name_before)
            print("n5")
        except:
            print("n5.1")
            var_stx_app.driver_customer.tap([(480, 400)])
            action.click(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point)
            action.click(var_stx_app.driver_customer, var_stx_app.order_car_back)

            name_before = action.get_text(var_stx_app.driver_customer, name_before)
            action.click(var_stx_app.driver_customer, "//*[@text='"+path_icon+"']")
            print(name_before)
            print("n6")
        time.sleep(2)


        if path_icon == "Trường học":
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.skip, time_wait=1)
                time.sleep(1)
            except:
                pass
            action.click(var_stx_app.driver_customer, var_stx_app.icon_destination_note)
            action.send_keys(var_stx_app.driver_customer, var_stx_app.icon_destination_note_input, var_stx_app.data['home_page_g7']['note'])
            action.click(var_stx_app.driver_customer, var_stx_app.igree)
            time.sleep(1.5)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.skip, time_wait=1)
            time.sleep(1)
        except:
            pass

        action.click(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point)
        # action.click(var_stx_app.driver_customer, var_stx_app.order_car_back)

        if path_icon == "Trường học":
            action.click(var_stx_app.driver_customer, var_stx_app.path_note, time_wait=10)
            time.sleep(1)
            try:
                name_note = action.get_text(var_stx_app.driver_customer, var_stx_app.name_note)
            except:
                var_stx_app.driver_customer.tap([(450, 550)])
                time.sleep(0.5)
                var_stx_app.driver_customer.tap([(450, 550)])
                time.sleep(1)
                action.click(var_stx_app.driver_customer, var_stx_app.path_note)
                name_note = action.get_text(var_stx_app.driver_customer, var_stx_app.name_note)

            #Xuất hóa đơn
            action.click(var_stx_app.driver_customer, var_stx_app.issue_invoice)
            time.sleep(2)
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.save1, time_wait=3)
                time.sleep(2)
            except:
                pass

            action.click(var_stx_app.driver_customer, var_stx_app.update)
            time.sleep(1.5)
            name_school = action.get_text(var_stx_app.driver_customer, var_stx_app.location_2)
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
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + name_image)
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)


        else:
            module_other_stx_app.write_result_text_try_if_cut(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Map",
                                                  var_stx_app.location_2, number_from, number_to, name_before, name_image)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.order_car_back, time_wait=1)
            time.sleep(1.5)
        except:
            pass



    def icon_add_adress(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.icon_map, time_wait=1)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")

        try:
            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.8, 0.2, 0.2, 0.2)
            action.click(var_stx_app.driver_customer, var_stx_app.add_adress, time_wait=5)
        except:
            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.8, 0.3, 0.2, 0.3)
            action.click(var_stx_app.driver_customer, var_stx_app.add_adress, time_wait=5)



        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_add_adress, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Map",
                                              var_stx_app.check_add_adress, "Điểm yêu thích", "_TrangChu_ThemDiaChi.png")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.add_adress_back, time_wait=1)
            time.sleep(1.5)
        except:
            pass



    def check_info_accout(self, code, eventname, result, path_name, path_data, check_name, check_data, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_change_account, time_wait=1)
        except:
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.change_account, time_wait=1)
            except:
                login_stx_app.g7.login_g7(self, "0359667694")
                action.click(var_stx_app.driver_customer, var_stx_app.change_account)

        try:
            action.wait_for(var_stx_app.driver_customer, path_name, time_wait=10)
        except:
            pass

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(g7) - Thay đổi tài khoản")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            name = var_stx_app.driver_customer.find_element(By.XPATH, path_name).text
            data = var_stx_app.driver_customer.find_element(By.XPATH, path_data).text
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "{} {}".format(name, data))
            var_stx_app.logging.info(name)
            var_stx_app.logging.info(data)

            if (name == check_name) and (data == check_data):
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



    def change_accout_skip(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_change_account, time_wait=1)
        except:
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.change_account, time_wait=1)
            except:
                login_stx_app.g7.login_g7(self, "0359667694")
                action.click(var_stx_app.driver_customer, var_stx_app.change_account)


        action.click(var_stx_app.driver_customer, var_stx_app.skip)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.home_page, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Thay đổi tài khoản",
                                              var_stx_app.home_page, "Trang chủ", "_TrangChu_ThayDoiTaiKhoan_BoQua.png")



    def change_accout_update(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_change_account, time_wait=1)
        except:
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.change_account, time_wait=1)
            except:
                login_stx_app.g7.login_g7(self, "0359667694")
                action.click(var_stx_app.driver_customer, var_stx_app.change_account)

        action.click(var_stx_app.driver_customer, var_stx_app.change_account_icon_image)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.ALLOW, time_wait=3)
            time.sleep(2)
        except:
            pass

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.change_account_icon_image1, time_wait=5)
        except:
            module_other_stx_app.tap_percent(var_stx_app.driver_customer, 0.5, 0.7)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.save, time_wait=3)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_save)

        action.clear(var_stx_app.driver_customer, var_stx_app.change_account_name)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.change_account_name, "Trần Quang Truờng1")


        action.click(var_stx_app.driver_customer, var_stx_app.change_account_sex)
        time.sleep(1.5)
        var_stx_app.driver_customer.tap([(156, 841)])
        # var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.change_account_sex_male).click()
        time.sleep(1.5)


        action.wait_for(var_stx_app.driver_customer, var_stx_app.change_account_brith_day)

        module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.5, 0.8, 0.5, 0.4)

        action.clear(var_stx_app.driver_customer, var_stx_app.change_account_email)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.change_account_email, "truongvck1@gmail.com")


        action.wait_for(var_stx_app.driver_customer, var_stx_app.change_account_referrer_code)
        action.click(var_stx_app.driver_customer, var_stx_app.update)
        message = homepage_driver.wait_toast_message(var_stx_app.driver_driver, 5)
        print(message)
        if message == "Cập nhật thông tin thành công":
            module_other_stx_app.write_result_text_try_if_toast(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Thay đổi tài khoản",
                                                                "", "Cập nhật thông tin thành công", "_TrangChu_ThayDoiTaiKhoan_CapNhat.png")
        else:
            message = homepage_driver.wait_toast_message_click2(var_stx_app.driver_customer, var_stx_app.change_account, var_stx_app.update, 7)
            print(message)
            module_other_stx_app.write_result_text_try_if_toast(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Thay đổi tài khoản",
                                                                "", "Cập nhật thông tin thành công", "_TrangChu_ThayDoiTaiKhoan_CapNhat.png")



        action.click(var_stx_app.driver_customer, var_stx_app.change_account)
        action.clear(var_stx_app.driver_customer, var_stx_app.change_account_name)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.change_account_name, "Trần Quang Truờng")

        action.clear(var_stx_app.driver_customer, var_stx_app.change_account_email)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.change_account_email, "truongvck33@gmail.com")

        action.click(var_stx_app.driver_customer, var_stx_app.update)
        # time.sleep(2)










    def icon_current_location(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)


        try:
            var_stx_app.driver_customer.implicitly_wait(0.3)
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.home_page)
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.book_a_car_quickly).click()
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            time.sleep(2)
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.book_a_car_quickly).click()

        time.sleep(3)
        try:
            var_stx_app.driver_customer.implicitly_wait(0.3)
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.skip).click()
            time.sleep(1)
        except:
            pass

        var_stx_app.driver_customer.swipe(700, 400, 200, 400, 1000)
        time.sleep(1)
        var_stx_app.driver_customer.swipe(700, 400, 200, 400, 1000)
        time.sleep(1)
        try:
            wait = WebDriverWait(var_stx_app.driver_customer, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.current_location)))
        except:
            var_stx_app.driver_customer.swipe(700, 400, 200, 400, 1000)
            time.sleep(1)
            var_stx_app.driver_customer.swipe(700, 400, 200, 400, 1000)
            time.sleep(2)
            wait = WebDriverWait(var_stx_app.driver_customer, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.current_location)))

        location_before = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.current_location).text
        var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.icon_current_location).click()
        time.sleep(2)
        location_after = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.current_location).text

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(g7) - Vị trí hiện tại")
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
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_DatNhanh_ViTriHienTai.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_DatNhanh_ViTriHienTai.png")



    def book_a_car_quickly(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        

        try:
            var_stx_app.driver_customer.implicitly_wait(0.3)
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.current_location)
        except:
                home_page.icon_current_location(self, "", "", "")

        wait = WebDriverWait(var_stx_app.driver_customer, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.icon_pick_up_point)))
        var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.icon_pick_up_point).click()
        time.sleep(2)
        var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.icon_pick_up_point_input).send_keys("Sơn Tây")
        time.sleep(2.5)
        var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.icon_pick_up_point_input3).click()
        time.sleep(3)
        # var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.confirm_pick_up_point).click()
        # time.sleep(2)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(g7) - Đặt xe nhanh",
                                              var_stx_app.check_book_a_car_quickly, "G7 Taxi đang tìm kiếm lái xe. Bạn vui lòng đợi trong giây lát…", "_TrangChu_DatXeNhanh.png")

        var_stx_app.driver_customer.tap([(422, 376)])
        time.sleep(2)
        var_stx_app.driver_customer.press_keycode(4)
        time.sleep(3)







    def icon_record(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_icon_map, time_wait=1)
        except:
            home_page.icon_map(self, "", "", "")

        module_other_stx_app.write_result_displayed_try(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Đặt xe - Icon Ghi âm",
                                              var_stx_app.icon_record, "_TrangChu_IconGhiAm.png")

        action.click(var_stx_app.driver_customer, var_stx_app.icon_record)
        time.sleep(1.5)
        var_stx_app.driver_customer.press_keycode(4)
        time.sleep(2)
        # try:
        #     action.wait_for(var_stx_app.driver_customer, var_stx_app.icon_record, time_wait=1)
        # except:
        #     var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.icon_map).click()
        #     time.sleep(2.5)



    def icon_location_to(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_icon_map, time_wait=1)
        except:
            home_page.icon_map(self, "", "", "")

        action.clear(var_stx_app.driver_customer, var_stx_app.location_to_input)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.location_to_input, "31 Ngõ Thi Sách")

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_icon_location_to, time_wait=10)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_location_to_back)
            action.click(var_stx_app.driver_customer, var_stx_app.icon_map)

            action.clear(var_stx_app.driver_customer, var_stx_app.location_to_input)
            action.send_keys(var_stx_app.driver_customer, var_stx_app.location_to_input, "31 Ngõ Thi Sách")

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_icon_location_to, time_wait=10)
        except:
            action.clear(var_stx_app.driver_customer, var_stx_app.location_to_input)
            action.send_keys(var_stx_app.driver_customer, var_stx_app.location_to_input, "31 Ngõ Thi Sách")
            time.sleep(2.5)

        module_other_stx_app.write_result_text_try_if_in(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Bản đồ - Chọn điểm đến",
                                              var_stx_app.check_icon_location_to, "31 Ngõ Thi Sách", "_TrangChu_ChonDiemDen.png")

        try:
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.check_icon_location_to).click()
        except:
            var_stx_app.driver_customer.tap([(200, 332)])
        time.sleep(2.5)



    def check_location_from(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point, time_wait=1)

        except:
            home_page.icon_location_to(self, "", "", "")

        try:
            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.8, 0.2, 0.2, 0.2)
            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.8, 0.2, 0.2, 0.2)
        except:
            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.8, 0.3, 0.2, 0.3)
            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.8, 0.3, 0.2, 0.3)

        time.sleep(2.5)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.location_to_1_name, time_wait=5)
        except:
            pass

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(g7) - Check vị trí điểm đến")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            location_to_1_name = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.location_to_1_name).text
            location_to_1_data = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.location_to_1_data).text

            location_to_2_name = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.location_to_2_name).text
            location_to_2_data = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.location_to_2_data).text

            location_to_3_name = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.location_to_3_name).text
            location_to_3_data = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.location_to_3_data).text

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Vị trí 1: {}({})\nVị trí 2: {}({})\nVị trí 3: {}({})"
                                           .format(location_to_1_name, location_to_1_data, location_to_2_name, location_to_2_data, location_to_3_name, location_to_3_data))

            var_stx_app.logging.info("Vị trí 1: {}({})\nVị trí 2: {}({})\nVị trí 3: {}({})"
                                           .format(location_to_1_name, location_to_1_data, location_to_2_name, location_to_2_data, location_to_3_name, location_to_3_data))

            if (location_to_1_name != "") and (location_to_1_data != "") and (location_to_2_name != "") and (location_to_2_data != "") and (location_to_3_name != "") and (location_to_3_data != ""):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_CheckViTriDiemDon.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_CheckViTriDiemDon.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_CheckViTriDiemDon.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_CheckViTriDiemDon.png")

        action.click(var_stx_app.driver_customer, var_stx_app.check_location_from_back, time_wait=10)
        time.sleep(3)



    def icon_destination1(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_destination, time_wait=1)
        except:
            home_page.icon_map(self, "", "", "")
            action.click(var_stx_app.driver_customer, var_stx_app.icon_destination)

        location_before = action.get_text(var_stx_app.driver_customer, var_stx_app.icon_record_location_before1)
        print(location_before)



        try:
            action.click(var_stx_app.driver_customer, var_stx_app.confirm_destination, time_wait=15)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.CONFIRM_DESTINATION, time_wait=15)



        time.sleep(1)
        action.wait_for(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point)
        module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.8, 0.3, 0.2, 0.3, 1000)
        time.sleep(2)
        module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.8, 0.3, 0.2, 0.3, 1000)
        time.sleep(2)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point)
            time.sleep(2.5)
            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.8, 0.3, 0.2, 0.3, 1000)
            time.sleep(2)
            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.8, 0.3, 0.2, 0.3, 1000)
            time.sleep(2)
            action.click(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point)
        time.sleep(2.5)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.skip, time_wait=1)
            time.sleep(1)
            action.click(var_stx_app.driver_customer, var_stx_app.icon_location_here)
            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.8, 0.3, 0.2, 0.3, 1000)
            time.sleep(2)
        except:
            pass


        try:
            location_after = action.get_text(var_stx_app.driver_customer, var_stx_app.location_2, time_wait=15)
        except:
            module_other_stx_app.tap_percent(var_stx_app.driver_customer, 0.5, 0.5)
            time.sleep(2)
            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.8, 0.3, 0.2, 0.3, 1000)
            time.sleep(2)
            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.8, 0.3, 0.2, 0.3, 1000)
            time.sleep(2)
            action.click(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point)
            time.sleep(2)
            location_after = action.get_text(var_stx_app.driver_customer, var_stx_app.location_2, time_wait=15)
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
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_IconDiemDen.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_IconDiemDen.png")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_back, time_wait=1)
            time.sleep(1.5)
        except:
            pass



    def icon_pick_up_point(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        home_page.icon_map(self, "", "", "")
        action.click(var_stx_app.driver_customer, var_stx_app.icon_destination)
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.confirm_destination, time_wait=10)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.CONFIRM_DESTINATION, time_wait=10)

        #đến đây
        action.click(var_stx_app.driver_customer, var_stx_app.icon_pick_up_point)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.icon_pick_up_point_input, "92 Phố Lê Thanh Nghị, Hà Nội")

        try:
            location_before = action.get_text(var_stx_app.driver_customer, var_stx_app.icon_pick_up_point_input1, time_wait=15)
        except:
            action.clear(var_stx_app.driver_customer, var_stx_app.icon_pick_up_point_input)
            action.send_keys(var_stx_app.driver_customer, var_stx_app.icon_pick_up_point_input, "92 Phố Lê Thanh Nghị, Hà Nội")
            location_before = action.get_text(var_stx_app.driver_customer, var_stx_app.icon_pick_up_point_input1, time_wait=15)


        action.click(var_stx_app.driver_customer, var_stx_app.icon_pick_up_point_input1)
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point, time_wait=2.5)
            time.sleep(2)
        except:
            pass

        location_after = action.get_text(var_stx_app.driver_customer, var_stx_app.location_1)
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(g7) - Đặt xe - Icon Điểm đón")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Vị trí trước khi xác nhận điểm đón: {}\nVị trí sau khi xác nhận điểm đón: {}"
                                       .format(location_before, location_after))
        var_stx_app.logging.info("Vị trí trước khi xác nhận điểm đón: {}\nVị trí sau khi xác nhận điểm đón: {}".format(location_before, location_after))
        if location_before == location_after:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_IconDiemDon.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_IconDiemDon.png")

        # try:
        #     var_stx_app.driver_customer.implicitly_wait(0.3)
        #     var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.icon_back).click()
        #     time.sleep(1.5)
        # except:
        #     pass



    def edit_location(self, code, eventname, result, path_icon, path_input, data, path_check, desire, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.PTTT, time_wait=1)
        except:
            home_page.icon_pick_up_point(self, "", "", "")

        action.click(var_stx_app.driver_customer, path_icon, time_wait=15)

        action.send_keys(var_stx_app.driver_customer, path_input, data)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.search_data1, time_wait=10)
        except:
            action.clear(var_stx_app.driver_customer, path_input)
            action.send_keys(var_stx_app.driver_customer, path_input, data)
            action.click(var_stx_app.driver_customer, var_stx_app.search_data1)

        try:
            action.wait_for(var_stx_app.driver_customer, path_check, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if_in(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Đặt xe",
                                              path_check, desire, name_image)



    def icon_change_position_2_location(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.location_3, time_wait=1)
        except:
            home_page.edit_location(self, "", "", "", var_stx_app.location_2_icon,
                                    var_stx_app.search_location_input, "40 Đặng Văn Ngữ, hà nội", "","","")

        location2_before = action.get_text(var_stx_app.driver_customer, var_stx_app.location_2)
        location3_before = action.get_text(var_stx_app.driver_customer, var_stx_app.location_3)

        action.click(var_stx_app.driver_customer, var_stx_app.location_2_icon)
        time.sleep(1.5)
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(g7) - Đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:

            location2_after = action.get_text(var_stx_app.driver_customer, var_stx_app.location_2, time_wait=7)
            location3_after = action.get_text(var_stx_app.driver_customer, var_stx_app.location_3)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Điểm 1 trước khi đổi: {}\nĐiểm 2 trước khi đổi: {}\nĐiểm 1 sau khi đổi: {}\nĐiểm 2 sau khi đổi: {}"
                                           .format(location2_before, location3_before, location2_after, location3_after))
            var_stx_app.logging.info("Điểm đến 1(a): {}\nĐiểm đến 2(a): {}\nĐiểm đến 1(b): {}\nĐiểm đến 2(b): {}"
                                           .format(location2_before, location3_before, location2_after, location3_after))
            if location2_before == location3_after and location3_before == location2_after:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_DatXe_IconDoiViTri2Diem.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_DatXe_IconDoiViTri2Diem.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_DatXe_IconDoiViTri2Diem.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_DatXe_IconDoiViTri2Diem.png")



    def icon_delete_location2(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.location_3, time_wait=1)

        except:
            home_page.icon_change_position_2_location(self, "", "", "")

        action.click(var_stx_app.driver_customer, var_stx_app.location_3_icon)
        time.sleep(2)
        module_other_stx_app.write_result_not_displayed_try(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Đặt xe",
                                              var_stx_app.location_3, "_TrangChu_DatXe_IconXoaViTriDiem2.png")



    def icon_info_vehicle(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.location_2, time_wait=1)
        except:
            home_page.edit_location(self, "", "", "", var_stx_app.location_1,
                                    var_stx_app.search_location_input, "120 Đường Cầu Giấy, hà nội", "", "", "")

        action.click(var_stx_app.driver_customer, var_stx_app.icon_info_vehicle)
        time.sleep(2.5)
        module_other_stx_app.write_result_not_displayed_try(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Đặt xe - Thông tin xe",
                                              var_stx_app.location_3, "_TrangChu_DatXe_IconXoaViTriDiem2.png")

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(g7) - Đặt xe - Thông tin xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:

            type_vehicle = action.get_text(var_stx_app.driver_customer, var_stx_app.info_vehicle_type_vehicle, time_wait=10)
            transportation_fee = action.get_text(var_stx_app.driver_customer, var_stx_app.info_vehicle_transportation_fee)
            distance = action.get_text(var_stx_app.driver_customer, var_stx_app.info_vehicle_distance)
            total_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.info_vehicle_total_amount)
            # time1 = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.info_vehicle_time).text#khung giờ
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "{}\nCước di chuyển: {}\nKhoảng cách: {}\nTổng tiền thanh toán: {}"
                                           .format(type_vehicle, transportation_fee, distance, total_amount))
            var_stx_app.logging.info("Loại xe: {}\nCước di chuyển: {}\nKhoảng cách: {}\nKhung giờ: {}\nTổng tiền thanh toán: {}"
                                           .format(type_vehicle, transportation_fee, distance, time, total_amount))

            if type_vehicle != "" and transportation_fee != "" and distance != "" and total_amount != "":
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_DatXe_ThongTinxe.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_DatXe_ThongTinxe.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_DatXe_ThongTinxe.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_DatXe_ThongTinxe.png")


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.info_vehicle_x, time_wait=10)
            time.sleep(2)
        except:
            pass



    def book_for_you(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.location_2, time_wait=1)
        except:
            home_page.edit_location(self, "", "", "", var_stx_app.location_1,
                                    var_stx_app.search_location_input, "120 Đường Cầu Giấy, hà nội", "", "", "")

        action.click(var_stx_app.driver_customer, var_stx_app.book_for_you)
        action.wait_for(var_stx_app.driver_customer, var_stx_app.book_for_you_checkbox, time_wait=15)


        action.send_keys(var_stx_app.driver_customer, var_stx_app.book_for_you_sdt, "0369443728")
        action.send_keys(var_stx_app.driver_customer, var_stx_app.book_for_you_name, "Thu Thủy")
        action.click(var_stx_app.driver_customer, var_stx_app.SEND)
        action.click(var_stx_app.driver_customer, var_stx_app.igree)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.book_for_you, time_wait=15)
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.book_for_you)
            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Đặt hộ",
                                                  var_stx_app.book_for_you, "Thu Thủy", "_TrangChu_DatHo.png")
        except:
            pass

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.igree, time_wait=1)
            action.click(var_stx_app.driver_customer, var_stx_app.SEND)
            action.click(var_stx_app.driver_customer, var_stx_app.igree)
            time.sleep(3)
            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Đặt hộ",
                                                  var_stx_app.book_for_you, "Thu Thủy", "_TrangChu_DatHo.png")
        except:
            pass






    def Prioritize_highways(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.location_2, time_wait=1)
        except:
            home_page.edit_location(self, "", "", "", var_stx_app.location_1,
                                    var_stx_app.search_location_input, "120 Đường Cầu Giấy, hà nội", "", "", "")

        action.click(var_stx_app.driver_customer, var_stx_app.Prioritize_highways)
        time.sleep(3)
        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Đặt xe",
                                                            var_stx_app.Prioritize_highways,  "Ưu tiên cao tốc", "_TrangChu_DatXe_UuTienCaoToc.png")


    def Book(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.location_2, time_wait=1)
        except:
            home_page.edit_location(self, "", "", "", var_stx_app.location_1,
                                    var_stx_app.search_location_input, "120 Đường Cầu Giấy, hà nội", "", "", "")

        action.click(var_stx_app.driver_customer, var_stx_app.Book)
        action.click(var_stx_app.driver_customer, var_stx_app.Book1)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_Book, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if_in(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Đặt xe",
                                                            var_stx_app.check_Book,  "Đặt trước -", "_TrangChu_DatXe_DatLich.png")












    def choose_location(self, location_to):
        home_page.icon_map(self, "", "", "")
        try:
            action.send_keys(var_stx_app.driver_customer, var_stx_app.location_to_input, location_to)
        except:
            homepage_g7_back()
            home_page.icon_map(self, "", "", "")
            action.send_keys(var_stx_app.driver_customer, var_stx_app.location_to_input, location_to)


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.location_to1)
        except:
            action.clear(var_stx_app.driver_customer, var_stx_app.location_to_input)
            action.send_keys(var_stx_app.driver_customer, var_stx_app.location_to_input, location_to)
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.location_to1)
            except:
                var_stx_app.driver_customer.tap([(240, 320)])


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point, time_wait=15)
        except:
            var_stx_app.driver_customer.tap([(375, 255)])
            time.sleep(0.5)
            var_stx_app.driver_customer.tap([(375, 255)])
            time.sleep(3)
            action.click(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point, time_wait=15)


        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.location_1, time_wait=3)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point, time_wait=5)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.icon_map_location_to, time_wait=3)
            var_stx_app.driver_customer.tap([(375, 255)])
            time.sleep(2)
        except:
            pass




    def book_car_cancel(self, code, eventname, result):
        def run_driver_app():
            var_stx_app.open_app(var_stx_app.driver_driver)

            homepage_driver.home_page.status_driver(self, "Xe sân bay", "SẴN SÀNG")

        def run_customer_app():
            var_stx_app.open_app(var_stx_app.driver_customer)
            login_stx_app.g7.login_g7(self, "0359667694")
            home_page.choose_location(self, "110 Cầu Giấy, hà nội")

            select_type_car("7 Chỗ")
            select_type_car("7 CHỖ")

            action.click(var_stx_app.driver_customer, var_stx_app.pttt)
            action.click(var_stx_app.driver_customer, var_stx_app.pttt_card_g7)
            action.click(var_stx_app.driver_customer, var_stx_app.clock_taxi)

        #chạy song song
        t_driver = threading.Thread(target=run_driver_app)
        t_customer = threading.Thread(target=run_customer_app)
        t_driver.start()
        t_customer.start()
        t_driver.join()
        t_customer.join()

        homepage_driver.RECEIVE_APP(25)

        action.click(var_stx_app.driver_customer, var_stx_app.cancel_booking)
        action.click(var_stx_app.driver_customer, var_stx_app.skip)
        action.click(var_stx_app.driver_customer, var_stx_app.cancel_booking)
        action.click(var_stx_app.driver_customer, var_stx_app.call_and_cancel)

        try:
            action.click(var_stx_app.driver_driver, 1, time_wait=3)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.customer_cancels_order1, time_wait=15)
        except:
            pass
        module_other_stx_app.write_result_text_try_if_in(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(g7) - Đặt xe",
                                                         var_stx_app.customer_cancels_order1, "Khách hàng hủy cuốc.", "_TrangChu_DatCuoc_HuyDatXe.png")

        action.click(var_stx_app.driver_driver, var_stx_app.igree)
        time.sleep(2)

        var_stx_app.reset_app(var_stx_app.driver_customer)




    def book_car_see_car(self, code, eventname, result, type):
        if type == "1":
            pass

        def run_driver_app():
            var_stx_app.open_app(var_stx_app.driver_driver)
            homepage_driver.home_page.status_driver(var_stx_app.driver_driver, "Xe sân bay", "SẴN SÀNG")

        def run_customer_app():
            var_stx_app.open_app(var_stx_app.driver_customer)
            login_stx_app.g7.login_g7(var_stx_app.driver_customer, "0359667694")
            home_page.choose_location(var_stx_app.driver_customer, "89 Chùa Láng, Hà Nội")
            try:
                action.wait_for(var_stx_app.driver_customer, var_stx_app.pttt, time_wait=15)
            except:
                action.click(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point, time_wait=10)

            action.click(var_stx_app.driver_customer, var_stx_app.pttt)
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.pttt_card_g7)
            except:
                action.click(var_stx_app.driver_customer, var_stx_app.CASH)
            select_type_car("7 Chỗ")
            select_type_car("7 CHỖ")
            action.click(var_stx_app.driver_customer, var_stx_app.payment_app)


        t_driver = threading.Thread(target=run_driver_app)
        t_customer = threading.Thread(target=run_customer_app)
        t_driver.start()
        t_customer.start()
        t_driver.join()
        t_customer.join()


        homepage_driver.RECEIVE_APP(25)
        #
        if type == "1":
            action.click(var_stx_app.driver_driver, var_stx_app.SEE_CUSTOMER)
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.CONFIRM, time_wait=4)
            except:
                pass

            action.click(var_stx_app.driver_driver, var_stx_app.DROP_OFF_PASSENGERS)
            action.click(var_stx_app.driver_driver, var_stx_app.card_g7)
            action.click(var_stx_app.driver_driver, var_stx_app.CONFIRM)
            action.click(var_stx_app.driver_driver, var_stx_app.igree)


            try:
                action.click(var_stx_app.driver_driver, var_stx_app.THEG7_3CHAM, time_wait=3)
                action.click(var_stx_app.driver_driver, var_stx_app.thanhtoantienmat)
            except:
                pass

            try:
                action.click(var_stx_app.driver_driver, var_stx_app.end, time_wait=3)
                time.sleep(2)
            except:
                pass

            try:
                action.click(var_stx_app.driver_driver, var_stx_app.notification_new_x, time_wait=15)
                time.sleep(1)
            except:
                pass


            #Khách
            action.click(var_stx_app.driver_customer, var_stx_app.review_checkbox1)
            time.sleep(1)
            note_review = action.get_text(var_stx_app.driver_customer, var_stx_app.note_review)
            print(note_review)
            time.sleep(1)
            #chọn đánh giá 5 sao
            action.wait_for(var_stx_app.driver_customer, var_stx_app.review_5_star)
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.more_5000)
            except:
                action.clear(var_stx_app.driver_customer, var_stx_app.review_tip)
                action.send_keys(var_stx_app.driver_customer, var_stx_app.review_tip, 5000)

            action.click(var_stx_app.driver_customer, var_stx_app.SEND)
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.CONFIRM, time_wait=15)
            except:
                pass


            try:
                action.wait_for(var_stx_app.driver_customer, var_stx_app.check_see_car)
            except:
                pass
            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Đặt cuốc",
                                                  var_stx_app.check_see_car, "Cảm ơn quý khách đã tin dùng dịch vụ G7 Taxi, Chúc quý khách có một chuyến đi an toàn.", "_TrangChu_DatCuoc_GapXe.png")


            try:
                action.click(var_stx_app.driver_customer, var_stx_app.i_readed, time_wait=2)
                time.sleep(2)
            except:
                pass

            try:
                action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=5)
            except:
                try:
                    var_stx_app.reset_app(var_stx_app.driver_driver)
                    action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=10)
                except:
                    pass



        if type == "2":
            pass
            # module_other_stx_app.click_app("G7 Taxi")



    def get_info_order(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.overview_location_from, time_wait=1)
        except:
            home_page.book_car_see_car(self, "", "", "", "2")

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.overview_space_name, time_wait=1)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.overview_icon_show)
            time.sleep(1.5)


        try:
            overview_time = action.get_text(var_stx_app.driver_customer, var_stx_app.overview_time, time_wait=1) #thời gian dự kiến,nếu có
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 13, 2, overview_time)
        except:
            pass

        overview_space = action.get_text(var_stx_app.driver_customer, var_stx_app.overview_space, time_wait=3)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 2, 2, overview_space)


        overview_fee = action.get_text(var_stx_app.driver_customer, var_stx_app.overview_fee, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 3, 2, overview_fee)


        overview_promotion = action.get_text(var_stx_app.driver_customer, var_stx_app.overview_promotion, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 4, 2, overview_promotion)


        overview_price = action.get_text(var_stx_app.driver_customer, var_stx_app.overview_price, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 5, 2, overview_price)


        overview_location_from = action.get_text(var_stx_app.driver_customer, var_stx_app.overview_location_from, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 6, 2, overview_location_from)


        overview_location_to = action.get_text(var_stx_app.driver_customer, var_stx_app.overview_location_to, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 7, 2, overview_location_to)


        overview_liscenseplate_typecar = action.get_text(var_stx_app.driver_customer, var_stx_app.overview_liscenseplate_typecar, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 8, 2, overview_liscenseplate_typecar)


        overview_typecar = action.get_text(var_stx_app.driver_customer, var_stx_app.overview_typecar, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 9, 2, overview_typecar)

        overview_star = action.get_text(var_stx_app.driver_customer, var_stx_app.overview_star, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 10, 2, overview_star)

        try:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 36, 2, "")
            overview_call = action.get_text(var_stx_app.driver_customer, var_stx_app.call_driver, time_wait=1) #gọi lái xe
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 36, 2, overview_call)
        except:
            pass



        #icon phí 1
        action.click(var_stx_app.driver_customer, var_stx_app.info_order_icon_fee_b)

        detail_typecar1 = action.get_text(var_stx_app.driver_customer, var_stx_app.detail_typecar1, time_wait=5)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 9, 3, detail_typecar1)


        detail_feemove1 = action.get_text(var_stx_app.driver_customer, var_stx_app.detail_feemove1, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 3, 3, detail_feemove1)

        detail_space1 = action.get_text(var_stx_app.driver_customer, var_stx_app.detail_space1, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 2, 3, detail_space1)

        detail_price1 = action.get_text(var_stx_app.driver_customer, var_stx_app.detail_price1, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 5, 3, detail_price1)

        action.click(var_stx_app.driver_customer, var_stx_app.info_order_icon_fee_x)
        time.sleep(2)


        #chi tiết chuyến đi 2----------------------------------------------------
        action.click(var_stx_app.driver_customer, var_stx_app.info_order_see_detail_b)


        detail_namedriver2 = action.get_text(var_stx_app.driver_customer, var_stx_app.detail_namedriver2, time_wait=5)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 11, 4, detail_namedriver2)


        detail_typecar2 = action.get_text(var_stx_app.driver_customer, var_stx_app.detail_typecar2, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 9, 4, detail_typecar2)


        detail_number2 = action.get_text(var_stx_app.driver_customer, var_stx_app.detail_number2, time_wait=1)   #số hiệu
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 12, 4, detail_number2)


        detail_star2 = action.get_text(var_stx_app.driver_customer, var_stx_app.detail_star2, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 10, 4, detail_star2)


        detail_space2 = action.get_text(var_stx_app.driver_customer, var_stx_app.detail_space2, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 2, 4, detail_space2)


        detail_fee2 = action.get_text(var_stx_app.driver_customer, var_stx_app.detail_fee2, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 3, 4, detail_fee2)


        detail_promotion2 = action.get_text(var_stx_app.driver_customer, var_stx_app.detail_promotion2, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 4, 4, detail_promotion2)


        detail_price2 = action.get_text(var_stx_app.driver_customer, var_stx_app.detail_price2, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 5, 4, detail_price2)


        detail_location_from2 = action.get_text(var_stx_app.driver_customer, var_stx_app.detail_location_from2, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 6, 4, detail_location_from2)


        detail_location_to2 = action.get_text(var_stx_app.driver_customer, var_stx_app.detail_location_to2, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 7, 4, detail_location_to2)


        detail_phone = action.get_text(var_stx_app.driver_customer, var_stx_app.detail_phone, time_wait=1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 90, 4, detail_phone)

        action.click(var_stx_app.driver_customer, var_stx_app.info_order_see_detail_x, time_wait=10)
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(g7) - Màn hình Thông tin cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("True")
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")



    def order_car_icon(self, code, eventname, result, type, path_icon, path_icon_x, path_check, desire, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.space1, time_wait=1)
            print("n0")
        except:
            var_stx_app.open_app(var_stx_app.driver_customer)
            var_stx_app.open_app(var_stx_app.driver_driver)

            try:
                action.click(var_stx_app.driver_customer, var_stx_app.overview_icon_show)
                time.sleep(2)
                print("n1")
            except:
                pass


        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.space1, time_wait=1)
            print("n2")
        except:
            print("n3")
            home_page.book_car_see_car(self, "", "", "", "2")
            print("n4")



        if type == "0":
            try:
                action.click(var_stx_app.driver_customer, path_icon, time_wait=1)
            except:
                pass
            time.sleep(1)
            module_other_stx_app.write_result_displayed_try(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Màn hình đã nhận cuốc",
                                                  path_check, name_image)

        if type == "1":
            action.click(var_stx_app.driver_customer, path_icon, time_wait=3)
            try:
                action.wait_for(var_stx_app.driver_customer, path_check, time_wait=5)
            except:
                pass

            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Màn hình đã nhận cuốc",
                                                  path_check, desire, name_image)

            action.click(var_stx_app.driver_customer, path_icon_x, time_wait=10)
            time.sleep(2)

        if type == "2":
            try:
                action.click(var_stx_app.driver_customer, path_icon, time_wait=1)
            except:
                pass

            try:
                action.wait_for(var_stx_app.driver_customer, path_check, time_wait=4)
                action.click(var_stx_app.driver_customer, path_icon)
                time.sleep(2)
            except:
                pass
            module_other_stx_app.write_result_not_displayed_try(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Màn hình đã nhận cuốc",
                                                            path_check, name_image)

            action.click(var_stx_app.driver_customer, var_stx_app.cancel_booking)
            action.click(var_stx_app.driver_customer, var_stx_app.call_and_cancel)

            
            try:
                action.wait_for(var_stx_app.driver_driver, var_stx_app.igree, time_wait=10)
            except:
                var_stx_app.reset_app(var_stx_app.driver_customer)
                var_stx_app.reset_app(var_stx_app.driver_driver)

        if type == "3":
            try:
                action.click(var_stx_app.driver_customer, path_icon, time_wait=1)
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
                action.click(var_stx_app.driver_customer, path_icon, time_wait=1)
            except:
                pass

            try:
                action.wait_for(var_stx_app.driver_customer, path_check, time_wait=5)
            except:
                pass

            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Màn hình đã nhận cuốc",
                                                  path_check, desire, name_image)

        if type == "5":
            time.sleep(2.5)
            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Màn hình đã nhận cuốc",
                                                  path_check, desire, name_image)

            try:
                action.click(var_stx_app.driver_customer, path_icon_x, time_wait=2)
                time.sleep(2.5)
            except:
                pass

        if type == "6":
            action.click(var_stx_app.driver_customer, var_stx_app.info_order_see_detail_b, time_wait=1)
            time.sleep(3)
            try:
                var_stx_app.driver_customer.swipe(400, 1300, 400, 400, 1000)
            except:
                module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.2, 0.8, 0.2, 0.2, 1000)#chưa test
            time.sleep(1)

            action.click(var_stx_app.driver_customer, path_icon)
            try:
                action.wait_for(var_stx_app.driver_customer, path_check, time_wait=7)
            except:
                pass

            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Màn hình đã nhận cuốc",
                                                  path_check, desire, name_image)

            action.click(var_stx_app.driver_customer, path_icon_x)
            time.sleep(2)

        if type == "7":
            action.click(var_stx_app.driver_customer, var_stx_app.info_order_see_detail_b, time_wait=1)
            action.wait_for(var_stx_app.driver_customer, path_check)

            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result,
                                                          "Trang Chủ(g7) - Màn hình đã nhận cuốc",
                                                          path_check, desire, name_image)

            action.click(var_stx_app.driver_customer, path_icon)
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.order_car_issue_invoice_x, time_wait=1)
                time.sleep(2)
            except:
                pass
            action.click(var_stx_app.driver_customer, path_icon_x)
            time.sleep(2)

        if type == "8":
            action.click(var_stx_app.driver_customer, var_stx_app.info_order_see_detail_b, time_wait=1)
            time.sleep(3)
            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.2, 0.8, 0.2, 0.2, 1000)  # chưa test
            time.sleep(1)
            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Màn hình đã nhận cuốc",
                                                  path_check, desire, name_image)

            action.click(var_stx_app.driver_customer, path_icon_x)
            time.sleep(2)



    def cancel_order_car(self):
        action.click(var_stx_app.driver_customer, var_stx_app.cancel_booking, time_wait=7)
        action.click(var_stx_app.driver_customer, var_stx_app.call_and_cancel)
        action.wait_for(var_stx_app.driver_customer, var_stx_app.customer_cancels_order)
        action.click(var_stx_app.driver_customer, var_stx_app.igree)
        action.click(var_stx_app.driver_customer, var_stx_app.order_car_back)
        time.sleep(2)






    def check_info_order_other(self, code, eventname, result, row, column, name):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver_customer.implicitly_wait(5)
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





    def check_info_order_number(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver_customer.implicitly_wait(5)
        detail2 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 9, 4))
        print(detail2)
        detail2 = detail2[0:6]
        detail2 = ''.join(re.findall(r'\d+', detail2))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Số hiệu: {}".format(detail2))
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Số hiệu: {}".format(detail2))
        if detail2 != "None":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")




    def check_info_order_distance(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass


        var_stx_app.driver_customer.implicitly_wait(5)
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
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver_customer.implicitly_wait(5)
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
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver_customer.implicitly_wait(5)
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
        var_stx_app.open_app(var_stx_app.driver_customer)


        try:
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver_customer.implicitly_wait(5)
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
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver_customer.implicitly_wait(5)
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
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver_customer.implicitly_wait(5)
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
        var_stx_app.open_app(var_stx_app.driver_customer)


        try:
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver_customer.implicitly_wait(5)
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
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver_customer.implicitly_wait(5)
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
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver_customer.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 9, 2))
        detail1 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 9, 3))
        detail2 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 9, 4))
        overview = ''.join(re.findall(r'\d+', overview))
        detail1 = ''.join(re.findall(r'\d+', detail1))

        detail2 = detail2.split("-")[1].split("|")[0]
        detail2 = re.search(r"\d+", detail2).group()

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


    def check_info_order_color_vehicle(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.cancel_booking)
            home_page.cancel_order_car(self)
        except:
            pass

        var_stx_app.driver_customer.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 9, 2))
        detail1 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 9, 4))

        overview = re.search(r"\w+", overview.split("-")[0]).group()
        detail1 = re.search(r"\w+", detail1.split("|")[-1]).group()

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Màu xe(Tổng quan)    : {}".format(overview))
        var_stx_app.logging.info("Màu xe(Xem chi tiết): {}".format(detail1))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Màu xe(Tổng quan): {}\nMàu xe(Xem chi tiết): {}"
                                       .format(overview, detail1))
        if overview == detail1:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
        

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.SEE_CUSTOMER)
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.CONFIRM, time_wait=4)
            except:
                pass

            action.click(var_stx_app.driver_driver, var_stx_app.DROP_OFF_PASSENGERS)
            action.click(var_stx_app.driver_driver, var_stx_app.card_g7)
            action.click(var_stx_app.driver_driver, var_stx_app.CONFIRM)
            action.click(var_stx_app.driver_driver, var_stx_app.igree)


            try:
                action.click(var_stx_app.driver_driver, var_stx_app.THEG7_3CHAM, time_wait=3)
                action.click(var_stx_app.driver_driver, var_stx_app.thanhtoantienmat)
            except:
                pass
        except:
            pass
        
        var_stx_app.reset_app(var_stx_app.driver_customer)
        var_stx_app.reset_app(var_stx_app.driver_driver)
        

    def check_info_order_call(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.cancel_booking, time_wait=1)
            home_page.cancel_order_car(self)
        except:
            pass
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 36, 2))
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Gọi lái xe(Tổng quan)   : {}".format(overview))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Gọi lái xe(Tổng quan): {}".format(overview))
        if overview == "Gọi lái xe":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def fill_location_from(self, location):
        n = 0
        while (n < 10):
            n = n + 1
            try:
                try:
                    action.clear(var_stx_app.driver_customer, var_stx_app.search_location_input, time_wait=3)
                    action.send_keys(var_stx_app.driver_customer, var_stx_app.search_location_input, location, time_wait=15)
                except:
                    action.click(var_stx_app.driver_customer, var_stx_app.location_1, time_wait=15)
                    action.clear(var_stx_app.driver_customer, var_stx_app.search_location_input, time_wait=15)
                    action.send_keys(var_stx_app.driver_customer, var_stx_app.search_location_input, location, time_wait=15)
                try:
                    action.click(var_stx_app.driver_customer, var_stx_app.search_data1, time_wait=15)
                    break
                except:
                    action.clear(var_stx_app.driver_customer, var_stx_app.search_location_input, time_wait=15)
                    action.send_keys(var_stx_app.driver_customer, var_stx_app.search_location_input, "abcasd", time_wait=15)
                    action.clear(var_stx_app.driver_customer, var_stx_app.search_location_input, time_wait=15)
                    action.send_keys(var_stx_app.driver_customer, var_stx_app.search_location_input, location, time_wait=15)
                    action.click(var_stx_app.driver_customer, var_stx_app.search_data1, time_wait=15)
                    break

            except:
                pass
            time.sleep(3)
            module_other_stx_app.tap_percent(var_stx_app.driver_customer, 0.5, 0.5)
            time.sleep(0.5)
            module_other_stx_app.tap_percent(var_stx_app.driver_customer, 0.5, 0.5)
            time.sleep(1.5)


    def fill_location_to(self, location):
        n = 0
        while (n < 10):
            n = n + 1
            try:
                try:
                    action.clear(var_stx_app.driver_customer, var_stx_app.search_location_input, time_wait=5)
                    action.send_keys(var_stx_app.driver_customer, var_stx_app.search_location_input, location, time_wait=15)
                except:
                    module_other_stx_app.tap_percent(var_stx_app.driver_customer, 0.5, 0.5)
                    time.sleep(0.5)
                    action.click(var_stx_app.driver_customer, var_stx_app.location_2, time_wait=15)
                    action.clear(var_stx_app.driver_customer, var_stx_app.search_location_input, time_wait=5)
                    action.send_keys(var_stx_app.driver_customer, var_stx_app.search_location_input, location, time_wait=15)
                try:
                    action.click(var_stx_app.driver_customer, var_stx_app.search_data1, time_wait=15)
                    break
                except:
                    action.clear(var_stx_app.driver_customer, var_stx_app.search_location_input, time_wait=3)
                    action.send_keys(var_stx_app.driver_customer, var_stx_app.search_location_input, "abc", time_wait=15)
                    action.clear(var_stx_app.driver_customer, var_stx_app.search_location_input, time_wait=15)
                    action.send_keys(var_stx_app.driver_customer, var_stx_app.search_location_input, location, time_wait=15)
                    try:
                        action.click(var_stx_app.driver_customer, var_stx_app.search_data1, time_wait=15)
                        break
                    except:
                        action.clear(var_stx_app.driver_customer, var_stx_app.search_location_input, time_wait=15)
                        action.send_keys(var_stx_app.driver_customer, var_stx_app.search_location_input, location, time_wait=15)
                        action.click(var_stx_app.driver_customer, var_stx_app.search_data1, time_wait=15)
                        break
            except:
                pass
            time.sleep(3)
            module_other_stx_app.tap_percent(var_stx_app.driver_customer, 0.5, 0.5)
            time.sleep(0.5)
            module_other_stx_app.tap_percent(var_stx_app.driver_customer, 0.5, 0.5)
            time.sleep(1.5)


    def check_km(self, location_from, location_to, code_promotion, code_promotion1):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.pttt, time_wait=1)
        except:
            home_page.choose_location(self, "110 Cầu Giấy, hà nội")


        #Điểm đón
        if location_from == "":
            pass
        else:
            action.click(var_stx_app.driver_customer, var_stx_app.location_1)
            time.sleep(2)
            home_page.fill_location_from(self, location_from)

        #Điểm đến
        if location_to == "":
            pass
        else:
            action.click(var_stx_app.driver_customer, var_stx_app.location_2)
            time.sleep(2)
            home_page.fill_location_to(self, location_to)


        if code_promotion == "":
            pass
        else:
            action.click(var_stx_app.driver_customer, var_stx_app.PROMOTION)
            time.sleep(2)
            try:
                action.clear(var_stx_app.driver_customer, var_stx_app.PROMOTION_input, time_wait=15)
            except:
                action.click(var_stx_app.driver_customer, var_stx_app.PROMOTION)
                action.clear(var_stx_app.driver_customer, var_stx_app.PROMOTION_input)

            action.send_keys(var_stx_app.driver_customer, var_stx_app.PROMOTION_input, code_promotion)
            time.sleep(1)
            action.click(var_stx_app.driver_customer, var_stx_app.PROMOTION_v)
            try:
                action.wait_for(var_stx_app.driver_customer, var_stx_app.location_1)
            except:
                try:
                    action.click(var_stx_app.driver_customer, var_stx_app.igree)
                    action.clear(var_stx_app.driver_customer, var_stx_app.PROMOTION_input)
                    action.send_keys(var_stx_app.driver_customer, var_stx_app.PROMOTION_input, code_promotion1)
                    action.click(var_stx_app.driver_customer, var_stx_app.PROMOTION_v)
                    action.wait_for(var_stx_app.driver_customer, var_stx_app.location_1)
                except:
                    pass
            time.sleep(1)





    def discount_15(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        home_page.check_km(self, "14, Nguyễn Cảnh Dị, hà nội", "110 Cầu Giấy", "AUTOXY", "AUTOXY")
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Kết quả - " + result)

        principal_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.principal_amount)
        print(principal_amount)

        app_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.app_amount)
        print(app_amount)

        try:
            #Số tiền gốc
            principal_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.principal_amount)
            principal_amount = ''.join(re.findall(r'\d+', principal_amount))
            principal_amount = int(principal_amount)
            print(principal_amount)

            #Ưu đãi 15%
            money_promotion = (principal_amount/100)*15
            money_promotion = math.ceil(money_promotion)
            print(money_promotion)

            #Số tiền sau khi đã áp mã
            app_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.app_amount)
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
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam15%.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam15.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam15.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam15.png")



    def discount_20_order_100(self, code, eventname, result, location_from, location_to, type):
        home_page.check_km(self, location_from, location_to, "AUTOMB", "AUTOMB")

        if type == "0":
            try:
                action.wait_for(var_stx_app.driver_customer, var_stx_app.discount_wrong, time_wait=10)
            except:
                pass

            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang chủ - Check khuyến mãi",
                                                  var_stx_app.discount_wrong, "Chương trình khuyến mại không hợp lệ, quý khách vui lòng xem thêm điều kiện áp dụng",
                                                          "CheckKhuyenMai_Giam20%_Don100k.png")
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.igree, time_wait=2)
                action.click(var_stx_app.driver_customer, var_stx_app.discount_back)
                time.sleep(2)
            except:
                pass

        else:
            var_stx_app.logging.info("--------------")
            var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
            var_stx_app.logging.info("Mã - " + code)
            var_stx_app.logging.info("Tên sự kiện - " + eventname)
            var_stx_app.logging.info("Kết quả - " + result)

            principal_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.principal_amount)
            app_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.app_amount)
            print(principal_amount)
            print(app_amount)

            try:
                #Số tiền gốc
                principal_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.principal_amount)
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
                app_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.app_amount)
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
                    var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam20%_Don100k.png")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam20%_Don100k.png")
            except:
                var_stx_app.logging.info("False")
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam20%_Don100k.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam20%_Don100k.png")

            action.click(var_stx_app.driver_customer, var_stx_app.order_car_back)
            time.sleep(2)


    def discount_20_max_50k(self, code, eventname, result, location_from, location_to):
        home_page.check_km(self, location_from, location_to, "AUTOX8", "AUTOX8")
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)

        try:
            #Số tiền gốc
            principal_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.principal_amount, time_wait=5)
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
            app_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.app_amount, time_wait=5)
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
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam20%_Don100k.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam20%_Don100k.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam20%_Don100k.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam20%_Don100k.png")



    def discount_30_apply_for_customer(self, code, eventname, result, tratien, path_check, desire):
        home_page.check_km(self, "14, Nguyễn Cảnh Dị hà nội", "898 Chùa Láng, hà nội ", "AUTO0W", "AUTO0W")
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)


        if tratien == "Trả tiền theo APP":
            action.click(var_stx_app.driver_customer, var_stx_app.payment_app)


        if tratien == "Đồng hồ Taxi":
            action.click(var_stx_app.driver_customer, var_stx_app.payment_clock_taxi)

        time.sleep(1.5)
        try:
            print("n1")
            check_text = action.get_text(var_stx_app.driver_customer, path_check)
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
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam30%_AppKhachHang.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam30%_AppKhachHang.png")
        except:
            print("n4")
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam20%_Don100k.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam30%_AppKhachHang.png")


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.GOITONGDAI, time_wait=2)
            var_stx_app.open_app(var_stx_app.driver_customer)
        except:
            pass

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.igree, time_wait=1)
            time.sleep(2)
        except:
            pass



    def discount_35_by_card(self, code, eventname, result, pttt):
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.pttt, time_wait=2)
        except:
            home_page.choose_location(var_stx_app.driver_customer, "89 Chùa Láng, Hà Nội")
            action.click(var_stx_app.driver_customer, var_stx_app.pttt)
        time.sleep(2)

        if pttt == "TIỀN MẶT":
            action.click(var_stx_app.driver_customer, var_stx_app.CASH, time_wait=15)
            home_page.check_km(self, "14, Nguyễn Cảnh Dị, hà nội", "231 Quan Nhân, hà nội", "AUTOO6", "AUTOO6")
            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang chủ - Check khuyến mãi",
                                                  var_stx_app.discount_wrong, "Chương trình khuyến mại không hợp lệ, quý khách vui lòng xem thêm điều kiện áp dụng",
                                                          "CheckKhuyenMai_Giam35%_ThanhToanBangViDienTu.png")
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.igree, time_wait=2)
                action.click(var_stx_app.driver_customer, var_stx_app.discount_back, time_wait=15)
                time.sleep(2)
            except:
                pass



        if pttt == "THẺ THÀNH VIÊN G7 TAXI":
            action.click(var_stx_app.driver_customer, var_stx_app.CARD_7G)
            time.sleep(2)
            home_page.check_km(self, "14, Nguyễn Cảnh Dị, hà nội", "231 Quan Nhân, hà nội", "AUTOO6", "AUTOO6")

            try:
                principal_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.principal_amount, time_wait=5)
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
                app_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.app_amount)
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
                    var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam35%_ThanhToanBangViDienTu.png")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam35%_ThanhToanBangViDienTu.png")
            except:
                var_stx_app.logging.info("False")
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam35%_ThanhToanBangViDienTu.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam35%_ThanhToanBangViDienTu.png")



    def discount_25_for_10km(self, code, eventname, result, type):
        if type == "duoi10km":
            home_page.check_km(self, "14, Nguyễn Cảnh Dị, hà nội", "230 Đại Từ, hà nội", "AUTOS5", "AUTOS5")
            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang chủ - Check khuyến mãi",
                                                          var_stx_app.discount_wrong, "Chương trình khuyến mại không hợp lệ, quý khách vui lòng xem thêm điều kiện áp dụng",
                                                          "CheckKhuyenMai_Giam25%_Don10km.png")
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.igree, time_wait=2)
                action.click(var_stx_app.driver_customer, var_stx_app.discount_back)
                time.sleep(2)
            except:
                pass


        if type == "tren10km":
            home_page.check_km(self, "120 Thanh Nhàn, hà nội", "huyện Đông Anh, thành phố Hà Nội", "AUTOS5", "AUTOS5")
            var_stx_app.logging.info("--------------")
            var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
            var_stx_app.logging.info("Mã - " + code)
            var_stx_app.logging.info("Tên sự kiện - " + eventname)
            var_stx_app.logging.info("Kết quả - " + result)

            try:
                #Số tiền gốc
                principal_amount = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.principal_amount).text
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
                app_amount = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.app_amount).text
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
                    var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam25%_Don10km.png")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam25%_Don10km.png")
            except:
                var_stx_app.logging.info("False")
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam25%_Don10km.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam25%_Don10km.png")



    def discount_30_inner_city(self, code, eventname, result, type):
        if type == "noithanh":
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.PROMOTION)
                action.click(var_stx_app.driver_customer, var_stx_app.PROMOTION_x)

                try:
                    action.wait_for(var_stx_app.driver_customer, var_stx_app.location_2, time_wait=15)
                except:
                    module_other_stx_app.tap_percent(var_stx_app.driver_customer, 0.5, 0.5)
                    time.sleep(0.5)
                    module_other_stx_app.tap_percent(var_stx_app.driver_customer, 0.5, 0.5)
                    time.sleep(0.5)
            except:
                pass


            home_page.check_km(self, "14, Nguyễn Cảnh Dị, hà nội", "136 Giải Phóng, hà nội", "AUTOKJ", "AUTOKJ")

        if type == "ngoaithanh":
            home_page.check_km(self, "Công ty TNHH Công Nghiệp Diamond", "Nội Bài", "AUTOKJ", "AUTOKJ")

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)

        try:
            #Số tiền gốc
            principal_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.principal_amount)
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
            app_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.app_amount)
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
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam30%_NoiThanh.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam30%_NoiThanh.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam30%_NoiThanh.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam30%_NoiThanh.png")



    def discount_30_inner_city_outner(self, code, eventname, result, location_from, location_to, code_promotion, code_promotion1):
        # home_page.check_km(self, "14, Nguyễn Cảnh Dị", "231 Quan Nhân", "AUTOE2", "AUTOZG")

        wait = WebDriverWait(var_stx_app.driver_customer, 10)
        
        var_stx_app.driver_customer.implicitly_wait(2)
        try:
            var_stx_app.driver_customer.implicitly_wait(0.3)
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.pttt)
        except:
            home_page.choose_location(self, "110 Cầu Giấy, hà nội")


        #Điểm đón
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.location_1)))
        # element.click()
        # time.sleep(2)
        # try:
        #     var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.search_location_input).send_keys(location_from)
        # except:
        #     var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.location_1).click()
        #     time.sleep(2)
        #     var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.search_location_input).send_keys(location_from)
        # time.sleep(3)
        # try:
        #     element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.search_data1)))
        #     element.click()
        # except:
        #     var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.search_location_input).clear()
        #     time.sleep(0.5)
        #     var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.search_location_input).send_keys(location_from)
        #     time.sleep(3)
        #     element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.search_data1)))
        #     element.click()
        # time.sleep(3)
        # var_stx_app.driver_customer.tap([(450, 550)])
        # time.sleep(0.5)
        # var_stx_app.driver_customer.tap([(450, 550)])
        # time.sleep(1.5)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.location_1)))
        element.click()
        time.sleep(2)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.order_car_icon_location_current_from)))
        element.click()
        time.sleep(2.5)
        # zoom("Phóng to", 5)
        zoom(var_stx_app.driver_customer, "Thu nhỏ", 10)
        var_stx_app.driver_customer.swipe(850, 500, 60, 500, 1000)
        var_stx_app.driver_customer.swipe(850, 500, 60, 500, 1000)
        var_stx_app.driver_customer.swipe(850, 500, 60, 500, 1000)
        time.sleep(2)
        var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.confirm_pick_up_point).click()
        time.sleep(3)
        var_stx_app.driver_customer.tap([(450, 550)])
        time.sleep(0.5)
        var_stx_app.driver_customer.tap([(450, 550)])
        time.sleep(1.5)


        #Check xem đã bỏ khuyến mãi chưa
        check_promotion = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.check_promotion_order).text
        print(f"Khuyến mãi: {check_promotion}")
        if check_promotion != "ƯU ĐÃI":
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.PROMOTION)))
            element.click()
            time.sleep(2)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.PROMOTION_x)))
            element.click()
            time.sleep(3)
            try:
                var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.location_2)
            except:
                var_stx_app.driver_customer.tap([(450, 550)])
                time.sleep(0.5)
                var_stx_app.driver_customer.tap([(450, 550)])
                time.sleep(0.5)


        #Điểm đến
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.location_2)))
        element.click()
        time.sleep(2)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.order_car_icon_location_current_from)))
        element.click()
        time.sleep(2.5)
        # zoom("Thu nhỏ", 10)


        var_stx_app.driver_customer.swipe(60, 500, 850, 500, 1000)
        var_stx_app.driver_customer.swipe(60, 500, 850, 500, 1000)
        var_stx_app.driver_customer.swipe(60, 500, 850, 500, 1000)
        time.sleep(2)
        var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.confirm_pick_up_point).click()
        time.sleep(3)
        var_stx_app.driver_customer.tap([(450, 550)])
        time.sleep(0.5)
        var_stx_app.driver_customer.tap([(450, 550)])
        time.sleep(1.5)


        # try:
        #     var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.search_location_input).send_keys(location_to)
        #     time.sleep(3)
        # except:
        #     var_stx_app.driver_customer.tap([(450, 550)])
        #     time.sleep(0.5)
        #     element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.location_2)))
        #     element.click()
        #     time.sleep(2)
        #     var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.search_location_input).send_keys(location_to)
        #     time.sleep(3)
        # try:
        #     element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.search_data1)))
        #     element.click()
        # except:
        #     var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.search_location_input).clear()
        #     time.sleep(1)
        #     var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.search_location_input).send_keys(location_to)
        #     time.sleep(3)
        #     try:
        #         element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.search_data1)))
        #         element.click()
        #     except:
        #         var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.search_location_input).clear()
        #         time.sleep(1)
        #         var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.search_location_input).send_keys(location_to)
        #         time.sleep(3)
        #         element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.search_data1)))
        #         element.click()
        # time.sleep(3)
        # var_stx_app.driver_customer.tap([(450, 550)])
        # time.sleep(0.5)
        # var_stx_app.driver_customer.tap([(450, 550)])
        # time.sleep(1.5)



        #khuyến mại
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.PROMOTION)))
        element.click()
        time.sleep(2)
        try:
            wait = WebDriverWait(var_stx_app.driver_customer, 20)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_PROMOTION)))
        except:
            var_stx_app.driver_customer.tap([(450, 550)])
        time.sleep(1)
        var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.PROMOTION_input).clear()
        time.sleep(0.5)
        var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.PROMOTION_input).send_keys(code_promotion)
        time.sleep(1)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.PROMOTION_v)))
        element.click()
        time.sleep(1)
        try:
            wait = WebDriverWait(var_stx_app.driver_customer, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//*[@text='"+code_promotion+"']")))
        except:
            try:
                var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.igree).click()
                time.sleep(2)
                var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.PROMOTION_input).clear()
                time.sleep(0.5)
                var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.PROMOTION_input).send_keys(code_promotion1)
                time.sleep(1)
                var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.PROMOTION_v).click()
                time.sleep(1)
                wait = WebDriverWait(var_stx_app.driver_customer, 10)
                element = wait.until(EC.element_to_be_clickable((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//*[@text='" + code_promotion + "']")))
            except:
                pass
        time.sleep(1)





        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)


















    def discount_15k(self, code, eventname, result):
        home_page.check_km(self, "14, Nguyễn Cảnh Dị, hà nội", "231 Quan Nhân, hà nội", "AUTOAJ", "AUTOAJ")
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)

        try:
            #Số tiền gốc
            principal_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.principal_amount)
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
            app_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.app_amount)
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
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam15k.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam15k.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam15k.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam15k.png")



    def discount_20k_order_100k(self, code, eventname, result, location_from, location_to, type):
        home_page.check_km(self, location_from, location_to, "AUTOXD", "AUTOXD")

        if type == "0":
            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang chủ - Check khuyến mãi",
                                                          var_stx_app.discount_wrong, "Chương trình khuyến mại không hợp lệ, quý khách vui lòng xem thêm điều kiện áp dụng",
                                                          "CheckKhuyenMai_Giam20k_DonTu100k.png")
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.igree, time_wait=2)
                action.click(var_stx_app.driver_customer, var_stx_app.discount_back)
                time.sleep(2)
            except:
                pass
        else:
            var_stx_app.logging.info("--------------")
            var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
            var_stx_app.logging.info("Mã - " + code)
            var_stx_app.logging.info("Tên sự kiện - " + eventname)
            var_stx_app.logging.info("Kết quả - " + result)

            try:
                #Số tiền gốc
                principal_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.principal_amount)
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
                app_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.app_amount)
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
                    var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam20k_DonTu100k.png")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam20k_DonTu100k.png")
            except:
                var_stx_app.logging.info("False")
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam20k_DonTu100k.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam20k_DonTu100k.png")


            #Xóa km
            action.click(var_stx_app.driver_customer, var_stx_app.PROMOTION)
            action.click(var_stx_app.driver_customer, var_stx_app.PROMOTION_x)
            time.sleep(2)



    def discount_30k_apply_for_clock(self, code, eventname, result, tratien, path_check, desire):
        home_page.check_km(self, "14, Nguyễn Cảnh Dị, hà nội", "110 Cầu Giấy, hà nội", "AUTO4R", "AUTO4R")
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)


        if tratien == "Trả tiền theo APP":
            action.click(var_stx_app.driver_customer, var_stx_app.payment_app)

        if tratien == "Đồng hồ Taxi":
            action.click(var_stx_app.driver_customer, var_stx_app.payment_clock_taxi)

        time.sleep(3)
        try:
            print("n1")
            check_text = action.get_text(var_stx_app.driver_customer,  path_check, time_wait=20)
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
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam30k_DongHoTaxi.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam30k_DongHoTaxi.png")
        except:
            print("n4")
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam30k_DongHoTaxi.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam30k_DongHoTaxi.png")



        try:
            # action.wait_for(var_stx_app.driver_customer, var_stx_app.GOITONGDAI, time_wait=1)
            action.click(var_stx_app.driver_customer, var_stx_app.GOITONGDAI, time_wait=2)
            var_stx_app.open_app(var_stx_app.driver_customer)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.igree, time_wait=1)
            time.sleep(2)
        except:
            pass



    def discount_35k_by_card(self, code, eventname, result, pttt):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.igree, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.pttt, time_wait=1)
        except:
            home_page.check_km(self, "14, Nguyễn Cảnh Dị, hà nội", "62 Hoàng Mai, Q. Hoàng Mai, hà nội", "AUTOFI", "AUTOFI")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.pttt, time_wait=15)
        except:
            pass

        if pttt == "TIỀN MẶT":
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.CASH, time_wait=15)
            except:
                pass
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.igree, time_wait=15)
                time.sleep(2)
            except:
                pass
            home_page.check_km(self, "14, Nguyễn Cảnh Dị, hà nội", "62 Hoàng Mai, Q. Hoàng Mai, hà nội", "AUTOFI", "AUTOFI")
            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang chủ - Check khuyến mãi",
                                                          var_stx_app.discount_wrong, "Chương trình khuyến mại không hợp lệ, quý khách vui lòng xem thêm điều kiện áp dụng",
                                                          "CheckKhuyenMai_Giam35K_ThanhToanBangThe.png")
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.igree, time_wait=2)
                action.click(var_stx_app.driver_customer, var_stx_app.discount_back)
                time.sleep(2.2)
            except:
                pass



        if pttt == "THẺ THÀNH VIÊN G7 TAXI":
            action.click(var_stx_app.driver_customer, var_stx_app.CARD_7G)
            time.sleep(2)
            home_page.check_km(self, "14, Nguyễn Cảnh Dị, hà nội", "62 Hoàng Mai, Q. Hoàng Mai, hà nội", "AUTOFI", "AUTOFI")
            var_stx_app.logging.info("--------------")
            var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
            var_stx_app.logging.info("Mã - " + code)
            var_stx_app.logging.info("Tên sự kiện - " + eventname)
            var_stx_app.logging.info("Kết quả - " + result)


            try:
                #Số tiền gốc
                principal_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.principal_amount)
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
                app_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.app_amount)
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
                    var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam35K_ThanhToanBangThe.png")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam35K_ThanhToanBangThe.png")
            except:
                var_stx_app.logging.info("False")
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam35K_ThanhToanBangThe.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam35K_ThanhToanBangThe.png")



    def discount_50k_inner_city(self, code, eventname, result, type):

        if type == "noithanh":
            home_page.check_km(self, "Phú Cường, H. Sóc Sơn, TP. Hà Nội", " 62 Hoàng Mai, Q. Hoàng Mai, hà nội", "AUTORN", "AUTOM8")

        if type == "ngoaithanh":
            home_page.check_km(self, "Phú Cường, H. Sóc Sơn, TP. Hà Nội", "Đại Thành, H. Quốc Oai", "AUTORN", "AUTOM8")


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ - Check khuyến mãi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)

        try:
            #Số tiền gốc
            principal_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.principal_amount)
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
            app_amount = action.get_text(var_stx_app.driver_customer, var_stx_app.app_amount)
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
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam30k_TuSanBay.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam30k_TuSanBay.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "CheckKhuyenMai_Giam30k_TuSanBay.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "CheckKhuyenMai_Giam30k_TuSanBay.png")





    def book_car_inner_city(self, code, eventname, result):
        def run_driver_app():
            var_stx_app.open_app(var_stx_app.driver_driver)
            homepage_driver.home_page.status_driver(self, "Xe sân bay", "SẴN SÀNG")

        def run_customer_app():
            var_stx_app.open_app(var_stx_app.driver_customer)
            login_stx_app.g7.login_g7(self, "0359667694")

        #chạy song song
        t_driver = threading.Thread(target=run_driver_app)
        t_customer = threading.Thread(target=run_customer_app)
        t_driver.start()
        t_customer.start()
        t_driver.join()
        t_customer.join()


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.book_car_inner_city, time_wait=15)
        except:
            var_stx_app.driver_customer.tap([(400, 700)])
            time.sleep(2)

        action.click(var_stx_app.driver_customer, var_stx_app.icon_destination_note)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.icon_destination_note_input, "Đặt cuốc nội thành")
        action.click(var_stx_app.driver_customer, var_stx_app.igree)
        action.click(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point)

        action.click(var_stx_app.driver_customer, var_stx_app.location_2_icon)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.search_location_input, "40 bach mai, hà nội")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.search_data1, time_wait=15)
        except:
            action.clear(var_stx_app.driver_customer, var_stx_app.search_location_input)
            action.send_keys(var_stx_app.driver_customer, var_stx_app.search_location_input, "40 bach mai, hà nội")
            action.click(var_stx_app.driver_customer, var_stx_app.search_data1, time_wait=15)
        time.sleep(2)


        select_type_car("7 Chỗ")
        select_type_car("7 CHỖ")

        # var_stx_app.driver_customer.tap([(450, 550)])
        # time.sleep(0.5)
        # var_stx_app.driver_customer.tap([(450, 550)])
        # time.sleep(2)

        action.click(var_stx_app.driver_customer, var_stx_app.pttt)
        action.click(var_stx_app.driver_customer, var_stx_app.pttt_card_g7)
        action.click(var_stx_app.driver_customer, var_stx_app.clock_taxi)

        homepage_driver.RECEIVE_APP(25)

        module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Đặt cuốc nội thành",
                                              var_stx_app.overview_liscenseplate_typecar, "", "_TrangChu_DatCuocNọiThanh.png")


        action.click(var_stx_app.driver_customer, var_stx_app.cancel_booking)
        action.click(var_stx_app.driver_customer, var_stx_app.call_and_cancel)
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.order_car_back, time_wait=5)
        except:
            pass
        action.click(var_stx_app.driver_driver, var_stx_app.agree)



    def book_car_inner_airport(self, code, eventname, result):
        def run_driver_app():
            var_stx_app.open_app(var_stx_app.driver_driver)
            homepage_driver.home_page.status_driver(self, "Xe sân bay", "SẴN SÀNG")

        def run_customer_app():
            var_stx_app.open_app(var_stx_app.driver_customer)
            login_stx_app.g7.login_g7(self, "0359667694")

        #chạy song song
        t_driver = threading.Thread(target=run_driver_app)
        t_customer = threading.Thread(target=run_customer_app)
        t_driver.start()
        t_customer.start()
        t_driver.join()
        t_customer.join()


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.book_car_inner_airport)
        except:
            var_stx_app.driver_customer.tap([(500, 1100)])
            time.sleep(2.5)


        action.click(var_stx_app.driver_customer, var_stx_app.icon_destination_note)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.icon_destination_note_input, "Đặt cuốc sân bay")
        action.click(var_stx_app.driver_customer, var_stx_app.igree)
        action.click(var_stx_app.driver_customer, var_stx_app.confirm_pick_up_point)
        action.wait_for(var_stx_app.driver_customer, var_stx_app.location_1)

        select_type_car("Sân Bay 7 Chỗ")
        select_type_car("SÂN BAY 7 CHỖ")

        action.click(var_stx_app.driver_customer, var_stx_app.pttt)
        action.click(var_stx_app.driver_customer, var_stx_app.pttt_card_g7)
        action.click(var_stx_app.driver_customer, var_stx_app.clock_taxi)


        homepage_driver.RECEIVE_APP(30)


        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.overview_location_to)
        except Exception as e:
            print(e)


        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Trang Chủ(g7) - Đặt cuốc sân bay",
                                              var_stx_app.overview_location_to, "Sân Bay Quốc Tế Nội Bài", "_TrangChu_DatCuocSanBay.png")



        action.click(var_stx_app.driver_customer, var_stx_app.cancel_booking)
        action.click(var_stx_app.driver_customer, var_stx_app.call_and_cancel)
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.order_car_back, time_wait=5)
        except:
            pass
        action.click(var_stx_app.driver_driver, var_stx_app.agree)










    def electronic_invoice_save(self, code, eventname, result):
        def run_driver_app():
            var_stx_app.open_app(var_stx_app.driver_driver)
            homepage_driver.home_page.status_driver(self, "Xe sân bay", "SẴN SÀNG")

        def run_customer_app():
            var_stx_app.open_app(var_stx_app.driver_customer)
            login_stx_app.g7.login_g7(self, "0359667694")
            home_page.choose_location(self, "89 Chùa Láng, hà nội")
            select_type_car("7 Chỗ")
            select_type_car("7 CHỖ")

            action.click(var_stx_app.driver_customer, var_stx_app.pttt)
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.pttt_card_g7, time_wait=10)
            except:
                action.click(var_stx_app.driver_customer, var_stx_app.pttt_tienmat)

            action.click(var_stx_app.driver_customer, var_stx_app.path_note)
            action.clear(var_stx_app.driver_customer, var_stx_app.setting_note)
            action.send_keys(var_stx_app.driver_customer, var_stx_app.setting_note, "Trường test xuất hóa đơn điện tử")


            try:
                action.wait_for(var_stx_app.driver_customer, var_stx_app.info_electronic_invoice, time_wait=3)
            except:
                action.click(var_stx_app.driver_customer, var_stx_app.i_want_electronic_invoice)
                time.sleep(2)
                try:
                    action.click(var_stx_app.driver_customer, var_stx_app.save1, time_wait=3)
                    time.sleep(2)
                except:
                    pass

            try:
                action.click(var_stx_app.driver_customer, var_stx_app.electronic_invoice_edit, time_wait=3)
            except:
                pass

            action.wait_for(var_stx_app.driver_customer, var_stx_app.electronic_invoice_tax_code)


            action.clear(var_stx_app.driver_customer, var_stx_app.electronic_invoice_tax_code)
            action.send_keys(var_stx_app.driver_customer, var_stx_app.electronic_invoice_tax_code, var_stx_app.data['home_page_g7']['electronic_invoice_tax_code'])

            action.clear(var_stx_app.driver_customer, var_stx_app.electronic_invoice_name)
            action.send_keys(var_stx_app.driver_customer, var_stx_app.electronic_invoice_name, var_stx_app.data['home_page_g7']['electronic_invoice_name'])

            action.clear(var_stx_app.driver_customer, var_stx_app.electronic_invoice_address)
            action.send_keys(var_stx_app.driver_customer, var_stx_app.electronic_invoice_address, var_stx_app.data['home_page_g7']['electronic_invoice_address'])

            action.clear(var_stx_app.driver_customer, var_stx_app.electronic_invoice_email)
            action.send_keys(var_stx_app.driver_customer, var_stx_app.electronic_invoice_email, var_stx_app.data['home_page_g7']['electronic_invoice_email'])

            action.clear(var_stx_app.driver_customer, var_stx_app.electronic_invoice_full_name)
            action.send_keys(var_stx_app.driver_customer, var_stx_app.electronic_invoice_full_name, var_stx_app.data['home_page_g7']['electronic_invoice_full_name'])

            try:
                action.clear(var_stx_app.driver_customer, var_stx_app.electronic_invoice_card, time_wait=3)
                action.send_keys(var_stx_app.driver_customer, var_stx_app.electronic_invoice_card, var_stx_app.data['home_page_g7']['electronic_invoice_card'])
            except:
                module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.5, 0.8, 0.5, 0.3, 1000)
                time.sleep(1)
                action.clear(var_stx_app.driver_customer, var_stx_app.electronic_invoice_card1, time_wait=10)
                action.send_keys(var_stx_app.driver_customer, var_stx_app.electronic_invoice_card1, var_stx_app.data['home_page_g7']['electronic_invoice_card'])



            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.5, 0.8, 0.5, 0.3, 1000)
            time.sleep(1)
            action.wait_for(var_stx_app.driver_customer, var_stx_app.electronic_invoice_dieukien, time_wait=15)

            action.click(var_stx_app.driver_customer, var_stx_app.save1)
            action.wait_for(var_stx_app.driver_customer, var_stx_app.info_electronic_invoice)
            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.5, 0.8, 0.5, 0.3, 1000)

            try:
                action.wait_for(var_stx_app.driver_customer, var_stx_app.check_electronic_invoice_address, time_wait=5)
            except:
                module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.5, 0.75, 0.5, 0.3, 1000)

            var_stx_app.logging.info("--------------")
            var_stx_app.logging.info("Trang chủ g7 - Hóa đơn điện tử")
            var_stx_app.logging.info("Mã - " + code)
            var_stx_app.logging.info("Tên sự kiện - " + eventname)
            var_stx_app.logging.info("Kết quả - " + result)
            try:
                check_electronic_invoice_email = action.get_text(var_stx_app.driver_customer, var_stx_app.check_electronic_invoice_email)
                check_electronic_invoice_tax_code = action.get_text(var_stx_app.driver_customer, var_stx_app.check_electronic_invoice_tax_code)
                check_electronic_invoice_name = action.get_text(var_stx_app.driver_customer, var_stx_app.check_electronic_invoice_name)
                check_electronic_invoice_address = action.get_text(var_stx_app.driver_customer, var_stx_app.check_electronic_invoice_address)

                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f"Email: {check_electronic_invoice_email}\nMã số thuế: {check_electronic_invoice_tax_code}\n"
                                                                                                f"Tên doanh nghiệp: {check_electronic_invoice_name}\nĐịa chỉ: {check_electronic_invoice_address}")
                var_stx_app.logging.info(f"Email: {check_electronic_invoice_email}\nMã số thuế: {check_electronic_invoice_tax_code}\n"
                                                                                                f"Tên doanh nghiệp: {check_electronic_invoice_name}\nĐịa chỉ: {check_electronic_invoice_address}")

                if (check_electronic_invoice_email == var_stx_app.data['home_page_g7']['electronic_invoice_email']) and \
                        (check_electronic_invoice_tax_code == var_stx_app.data['home_page_g7']['electronic_invoice_tax_code']) and \
                        (check_electronic_invoice_name == var_stx_app.data['home_page_g7']['electronic_invoice_name']) and \
                        (check_electronic_invoice_address == var_stx_app.data['home_page_g7']['electronic_invoice_address']):

                    var_stx_app.logging.info("True")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    var_stx_app.logging.info("False")
                    var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_XuatHoaDonDienTu_CapNhat.png")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_XuatHoaDonDienTu_CapNhat.png")
            except:
                var_stx_app.logging.info("False")
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_XuatHoaDonDienTu_CapNhat.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_XuatHoaDonDienTu_CapNhat.png")


        #chạy song song
        t_driver = threading.Thread(target=run_driver_app)
        t_customer = threading.Thread(target=run_customer_app)
        t_driver.start()
        t_customer.start()
        t_driver.join()
        t_customer.join()


    def check_electronic_invoice_customer(self,  code, eventname, result):
        def run_driver_app():
            var_stx_app.open_app(var_stx_app.driver_driver)
            try:
                action.wait_for(var_stx_app.driver_customer, var_stx_app.notification, time_wait=1)
            except:
                homepage_driver.home_page.status_driver(self, "Xe sân bay", "SẴN SÀNG")

        def run_customer_app():
            var_stx_app.open_app(var_stx_app.driver_customer)
            try:
                action.wait_for(var_stx_app.driver_customer, var_stx_app.info_electronic_invoice, time_wait=1)
            except:
                home_page.electronic_invoice_save(self, "", "", "")

        # chạy song song
        t_driver = threading.Thread(target=run_driver_app)
        t_customer = threading.Thread(target=run_customer_app)
        t_driver.start()
        t_customer.start()
        t_driver.join()
        t_customer.join()


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.order_car_setting_back, time_wait=10)
            time.sleep(2)
        except:
            pass

        action.click(var_stx_app.driver_customer, var_stx_app.payment_app)

        homepage_driver.RECEIVE_APP(25)

        action.click(var_stx_app.driver_customer, var_stx_app.see_detail1)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.info_electronic_invoice, time_wait=7)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.i_want_electronic_invoice)
            time.sleep(2)


        module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.5, 0.8, 0.5, 0.2, 1000)
        module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.5, 0.8, 0.5, 0.2, 1000)

        electronic_invoice_over_view_email = action.get_text(var_stx_app.driver_customer, var_stx_app.electronic_invoice_over_view_email)
        electronic_invoice_over_view_tax_code = action.get_text(var_stx_app.driver_customer, var_stx_app.electronic_invoice_over_view_tax_code)
        electronic_invoice_over_view_name = action.get_text(var_stx_app.driver_customer, var_stx_app.electronic_invoice_over_view_name)
        electronic_invoice_over_view_address = action.get_text(var_stx_app.driver_customer, var_stx_app.electronic_invoice_over_view_address)

        action.click(var_stx_app.driver_customer, var_stx_app.edit)
        action.wait_for(var_stx_app.driver_customer, var_stx_app.electronic_invoice_tax_code)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ g7 - Hóa đơn điện tử")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            electronic_invoice_detail_tax_code = action.get_text(var_stx_app.driver_customer, var_stx_app.electronic_invoice_tax_code)
            electronic_invoice_detail_name = action.get_text(var_stx_app.driver_customer, var_stx_app.electronic_invoice_name)
            electronic_invoice_detail_address = action.get_text(var_stx_app.driver_customer, var_stx_app.electronic_invoice_address)
            electronic_invoice_detail_email = action.get_text(var_stx_app.driver_customer, var_stx_app.electronic_invoice_email)
            electronic_invoice_detail_full_name = action.get_text(var_stx_app.driver_customer, var_stx_app.electronic_invoice_full_name)
            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.5, 0.8, 0.5, 0.3, 1000)
            time.sleep(1)
            try:
                electronic_invoice_detail_card = action.get_text(var_stx_app.driver_customer, var_stx_app.electronic_invoice_card, time_wait=3)
            except:
                electronic_invoice_detail_card = action.get_text(var_stx_app.driver_customer, var_stx_app.electronic_invoice_card1)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f"Mã số thuế: {electronic_invoice_detail_tax_code}\nTên doanh nghiệp: {electronic_invoice_detail_name}\n"
                                                                                            f"Địa chỉ: {electronic_invoice_detail_address}\nEmail: {electronic_invoice_detail_email}\n"
                                                                                            f"Họ và tên quý khách: {electronic_invoice_detail_full_name}\nThẻ thành viên: {electronic_invoice_detail_card}")


            var_stx_app.logging.info(f"Mã số thuế: {electronic_invoice_detail_tax_code}\nTên doanh nghiệp: {electronic_invoice_detail_name}\n"
                                                                                            f"Địa chỉ: {electronic_invoice_detail_address}\nEmail: {electronic_invoice_detail_email}\n"
                                                                                            f"Họ và tên quý khách: {electronic_invoice_detail_full_name}\nThẻ thành viên: {electronic_invoice_detail_card}")


            if (electronic_invoice_over_view_tax_code == electronic_invoice_detail_tax_code == var_stx_app.data['home_page_g7']['electronic_invoice_tax_code']) and \
                    (electronic_invoice_over_view_name == electronic_invoice_detail_name == var_stx_app.data['home_page_g7']['electronic_invoice_name']) and \
                    (electronic_invoice_over_view_address == electronic_invoice_detail_address == var_stx_app.data['home_page_g7']['electronic_invoice_address']) and \
                    (electronic_invoice_over_view_email == electronic_invoice_detail_email == var_stx_app.data['home_page_g7']['electronic_invoice_email']) and \
                    (electronic_invoice_over_view_address == electronic_invoice_detail_address == var_stx_app.data['home_page_g7']['electronic_invoice_address']) and \
                    (electronic_invoice_detail_full_name == var_stx_app.data['home_page_g7']['electronic_invoice_full_name']) and \
                    (electronic_invoice_detail_card == var_stx_app.data['home_page_g7']['electronic_invoice_card']):

                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "_XuatHoaDonDienTu_CheckThongTinKhachHang.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_XuatHoaDonDienTu_CheckThongTinKhachHang.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "_XuatHoaDonDienTu_CheckThongTinKhachHang.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_XuatHoaDonDienTu_CheckThongTinKhachHang.png")


        action.click(var_stx_app.driver_customer, var_stx_app.electronic_invoice_back)
        action.click(var_stx_app.driver_customer, var_stx_app.info_trip_back)
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.cancel_booking, time_wait=10)
            time.sleep(2)
        except:
            pass

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.call_and_cancel, time_wait=10)
            time.sleep(2)
        except:
            pass
        var_stx_app.reset_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=3)
            time.sleep(2)
            print("l5")
        except:
            pass


    def check_electronic_invoice_drive(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.SEE_CUSTOMER, time_wait=1)
        except:
            home_page.check_electronic_invoice_customer(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.SEE_CUSTOMER)

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.CONFIRM, time_wait=4)
        except:
            pass

        action.click(var_stx_app.driver_driver, var_stx_app.GIVE_BACK_CUSTOMER)

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.CASH, time_wait=3)
        except:
            pass
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.qr, time_wait=3)
        except:
            pass
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.fill_money, time_wait=3)
            action.send_keys(var_stx_app.driver_driver, var_stx_app.fee_input, 86000)
            action.click(var_stx_app.driver_driver, var_stx_app.continue1)
            time.sleep(2)
        except:
            pass

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.fill_sec, time_wait=3)
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_receipt_invoice_link, time_wait=20)
        except:
            pass

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.check_receipt_invoice, time_wait=2)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.check_receipt_invoice1, time_wait=5)


        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.serial_sec, time_wait=20)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.pay_sec_checkbox)
            time.sleep(2.5)

        #Mã hợp đồng - serial sec
        action.click(var_stx_app.driver_driver, var_stx_app.info_trip_mhd)
        action.click(var_stx_app.driver_driver, var_stx_app.info_trip_mhd1)
        time.sleep(2)

        action.clear(var_stx_app.driver_driver, var_stx_app.info_trip_sec)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.info_trip_sec, "020200007272")
        time.sleep(0.5)
        action.click(var_stx_app.driver_driver, var_stx_app.send_info)
        action.click(var_stx_app.driver_driver, var_stx_app.confirm1)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang chủ g7 - Hóa đơn điện tử")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            check_text = action.get_text(var_stx_app.driver_driver, var_stx_app.send_access)
            print(f"text1: {check_text}")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, check_text)
            var_stx_app.logging.info(check_text)
            if check_text == "Quý khách đã gửi thành công!":
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_XuatHoaDonDienTu_GuiThongTin.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_XuatHoaDonDienTu_GuiThongTin.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_XuatHoaDonDienTu_GuiThongTin.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_XuatHoaDonDienTu_GuiThongTin.png")





        try:
            action.click(var_stx_app.driver_driver, var_stx_app.close_tab)
            time.sleep(2)
        except:
            pass


        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_receipt_invoice, time_wait=5)
            time.sleep(1)
            module_other_stx_app.tap_percent(var_stx_app.driver_driver, 0.5, 0.12)
            time.sleep(2)
        except:
            pass

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.THEG7_3CHAM, time_wait=5)
            action.click(var_stx_app.driver_driver, var_stx_app.thanhtoantienmat1)
        except:
            var_stx_app.reset_app(var_stx_app.driver_driver)
            action.click(var_stx_app.driver_driver, var_stx_app.GIVE_BACK_CUSTOMER)
            action.click(var_stx_app.driver_driver, var_stx_app.THEG7_3CHAM, time_wait=5)
            action.click(var_stx_app.driver_driver, var_stx_app.thanhtoantienmat1)


        try:
            action.click(var_stx_app.driver_driver, var_stx_app.agree, time_wait=5)
        except:
            pass


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.complete, time_wait=5)
            action.click(var_stx_app.driver_customer, var_stx_app.review_x)
        except:
            var_stx_app.reset_app(var_stx_app.driver_customer)












class web_app:
    def __init__(self):
        self.driver2 = None


    def create_order(self, address, pttt):
        def run_driver_app():
            print("n1")
            homepage_driver.home_page.status_driver(self, "Xe sân bay", "SẴN SÀNG")
            print("n2")

        def run_customer_app():
            print("n3")
            login_stx_app.g7.login_g7(self, "0359667694")
            print("n4")
            home_page.choose_location(self, address)
            print("n5")
            select_type_car("7 Chỗ")
            select_type_car("7 CHỖ")

            action.click(var_stx_app.driver_customer, var_stx_app.pttt)

        #chạy song song
        t_driver = threading.Thread(target=run_driver_app)
        t_customer = threading.Thread(target=run_customer_app)
        t_driver.start()
        t_customer.start()
        t_driver.join()
        t_customer.join()

        print("n6")
        if pttt == "tiền mặt":
            action.click(var_stx_app.driver_customer, var_stx_app.CASH, time_wait=15)
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.CASH_1, time_wait=2)
                time.sleep(2)
            except:
                pass

        if pttt == "thẻ g7":
            action.click(var_stx_app.driver_customer, var_stx_app.card_g7, time_wait=15)
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.card_g7_1, time_wait=2)
            except:
                pass


    def search_tax_code(self, code, eventname, result):
        web_app.create_order(self, var_stx_app.data['web_app']['address1'], "tiền mặt")

        action.click(var_stx_app.driver_customer, var_stx_app.path_note)
        action.clear(var_stx_app.driver_customer, var_stx_app.setting_note)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.setting_note, "Khách hàng nhập xuất hóa đơn")

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.info_electronic_invoice, time_wait=1)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.i_want_electronic_invoice)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.electronic_invoice_edit, time_wait=3)
        except:
            pass
        action.clear(var_stx_app.driver_customer, var_stx_app.electronic_invoice_tax_code)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.electronic_invoice_tax_code, "0102306702")
        action.click(var_stx_app.driver_customer, var_stx_app.look_up)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.electronic_invoice_tax_code_input, time_wait=20)
        except:
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.look_up)
                action.wait_for(var_stx_app.driver_customer, var_stx_app.electronic_invoice_tax_code_input, time_wait=10)
            except:
                pass


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("CASE CHECK TRẠNG THÁI XUẤT HÓA ĐƠN WEB, APP - Tạo dữ liệu")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            tax_code = action.get_text(var_stx_app.driver_customer, var_stx_app.electronic_invoice_tax_code_input, time_wait=1)
            name_company = action.get_text(var_stx_app.driver_customer, var_stx_app.electronic_invoice_name_company_input)
            address = action.get_text(var_stx_app.driver_customer, var_stx_app.electronic_invoice_address_input)


            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f"Mã số thuế: {tax_code}\nTên doanh nghiệp: {name_company}\n- Địa chỉ: {address}")
            var_stx_app.logging.info(f"{tax_code}, {name_company}, {address}")
            if (tax_code == "0102306702") and (name_company == "CÔNG TY TNHH PHÁT TRIỂN CÔNG NGHỆ ĐIỆN TỬ BÌNH ANH") \
                    and (address == "Tầng 13, Tòa nhà Licogi 13 Tower, Số 164 đường Khuất Duy Tiến, Phường Thanh Xuân, TP Hà Nội"):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "_XuatHoaDonDienTu_case1.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_XuatHoaDonDienTu_case1.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "_XuatHoaDonDienTu_case1.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_XuatHoaDonDienTu_case1.png")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.confirm1, time_wait=2)
            time.sleep(2)
        except:
            pass

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.save1, time_wait=2)
            time.sleep(2)
        except:
            pass

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.electronic_invoice_x, time_wait=1)
            time.sleep(2)
        except:
            pass


    def fill_electronic_invoice(self,  code, eventname, result):
        def run_driver_app():
            try:
                action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=1)
            except:
                var_stx_app.reset_app(var_stx_app.driver_driver)
                homepage_driver.home_page.status_driver(self, "Xe sân bay", "SẴN SÀNG")

        def run_customer_app():
            try:
                print("n1")
                action.wait_for(var_stx_app.driver_customer, var_stx_app.info_electronic_invoice, time_wait=3)
            except:
                print("n2")
                web_app.search_tax_code(self, "", "", "")
                print("n3")


        #chạy song song
        t_driver = threading.Thread(target=run_driver_app)
        t_customer = threading.Thread(target=run_customer_app)
        t_driver.start()
        t_customer.start()
        t_driver.join()
        t_customer.join()


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.save1, time_wait=3)
            time.sleep(2)
        except:
            pass
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.path_note, time_wait=1)
            time.sleep(2)
        except:
            pass
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.info_electronic_invoice, time_wait=5)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.i_want_electronic_invoice)
            time.sleep(2)
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.update, time_wait=10)
            time.sleep(2)
        except:
            pass


        action.click(var_stx_app.driver_customer, var_stx_app.payment_app)

        homepage_driver.RECEIVE_APP(20)
        action.click(var_stx_app.driver_driver, var_stx_app.SEE_CUSTOMER)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.CONFIRM, time_wait=4)
        except:
            pass

        action.click(var_stx_app.driver_driver, var_stx_app.GIVE_BACK_CUSTOMER)
        action.click(var_stx_app.driver_driver, var_stx_app.CASH)
        time.sleep(3)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=2)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=10)
        except:
            var_stx_app.reset_app(var_stx_app.driver_driver)
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=4)
                time.sleep(2)
            except:
                pass
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=10)

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "CASE CHECK TRẠNG THÁI XUẤT HÓA ĐƠN WEB, APP - Tạo dữ liệu",
                                                            var_stx_app.home_page, "Trang chủ", "_XuatHoaDonDienTu_case1.png")

        wait_complete(60)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.review_x, time_wait=2)
            time.sleep(2)
        except:
            pass
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.notification_new_x, time_wait=1)
            time.sleep(1)
        except:
            pass





    def not_fill_electronic_invoice(self, code, eventname, result):
        web_app.create_order(self, var_stx_app.data['web_app']['address2'], "thẻ g7")

        action.click(var_stx_app.driver_customer, var_stx_app.path_note)
        action.clear(var_stx_app.driver_customer, var_stx_app.setting_note)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.setting_note, "1.Khách hàng không nhập xuất hóa đơn(Tạo dữ liệu)\n2.Đổi phương thức thanh toán(Tạo dữ liệu)")

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.info_electronic_invoice, time_wait=2)
            action.click(var_stx_app.driver_customer, var_stx_app.i_want_electronic_invoice)
        except:
            pass

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.update, time_wait=2.5)
            time.sleep(2)
        except:
            pass

        action.click(var_stx_app.driver_customer, var_stx_app.payment_app)


        homepage_driver.RECEIVE_APP(20)
        action.click(var_stx_app.driver_driver, var_stx_app.SEE_CUSTOMER)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.CONFIRM, time_wait=4)
        except:
            pass
        action.click(var_stx_app.driver_driver, var_stx_app.GIVE_BACK_CUSTOMER)

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.THEG7_3CHAM, time_wait=3.5)
            action.click(var_stx_app.driver_driver, var_stx_app.thanhtoantienmat)
            time.sleep(2.5)
        except:
            pass

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=3)
            time.sleep(2)
        except:
            pass

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.I_READED, time_wait=2)
            time.sleep(2)
        except:
            pass


        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=10)
        except:
            var_stx_app.reset_app(var_stx_app.driver_driver)
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=10)

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result,
                                                      "CASE CHECK TRẠNG THÁI XUẤT HÓA ĐƠN WEB, APP - Tạo dữ liệu",
                                                      var_stx_app.home_page, "Trang chủ", "_XuatHoaDonDienTu_case1.png")


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.review_x, time_wait=2)
            time.sleep(2)
        except:
            wait_complete(60)

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.notification_new_x, time_wait=1)
            time.sleep(1)
        except:
            pass


    def card_company_auto_export(self, code, eventname, result, address, serial, name_image):
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.homepage, time_wait=1)
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        homepage_driver.waiting_for_a_passenger.create_order_search(self, "", "", "", "diachidon",
                                                    var_stx_app.create_order_location1_input, "14 Nguyễn Cảnh Dị, hà nội", "", "", "")

        homepage_driver.waiting_for_a_passenger.create_order_search(self, "", "", "", "diachitra",
                                                    var_stx_app.create_order_location2_input, address, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.CREATE_ORDER)
        action.click(var_stx_app.driver_driver, var_stx_app.DROP_OFF_PASSENGERS)
        action.click(var_stx_app.driver_driver, var_stx_app.icon_edit)

        # Thêm phụ phí
        action.clear(var_stx_app.driver_driver, var_stx_app.freight_input)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.freight_input, "65000")
        action.click(var_stx_app.driver_driver, var_stx_app.continue2)
        action.click(var_stx_app.driver_driver, var_stx_app.pttt1)
        action.click(var_stx_app.driver_driver, var_stx_app.pttt1_g7)

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.ALLOW, time_wait=2)
        except:
            pass
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.USE_APP, time_wait=2)
        except:
            pass

        action.click(var_stx_app.driver_driver, var_stx_app.FILL_CODE_CARD)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.FILL_CODE_CARD_INPUT, serial)
        action.click(var_stx_app.driver_driver, var_stx_app.confirm1)
        action.click(var_stx_app.driver_driver, var_stx_app.PAY_CARD)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_pay_card, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result,  "CASE CHECK TRẠNG THÁI XUẤT HÓA ĐƠN WEB, APP - Tạo dữ liệu",
                                                      var_stx_app.check_pay_card, "Bạn đã thanh toán thành công", name_image)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.agree, time_wait=3)
            time.sleep(2)
        except:
            pass

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=3)
            time.sleep(2)
        except:
            var_stx_app.reset_app(var_stx_app.driver_driver)

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.i_readed, time_wait=20)
            time.sleep(2)
        except:
            pass




    def create_driver(self):
        from DrissionPage import ChromiumPage, ChromiumOptions
        do1 = ChromiumOptions().set_paths(local_port=9201, user_data_path=r"" + var_stx_app.uploadpath + "Profile 30""")
        self.driver2 = ChromiumPage(addr_or_opts=do1)


    def login_stx(self, user, password):
        web = web_app()
        web.create_driver()

        try:
            web.driver2.ele(var_stx_app.profile, timeout=3).click()
            time.sleep(1)
            web.driver2.ele(var_stx_app.icon_logout).click()
            time.sleep(2)
        except:
            pass

        web.driver2.get("https://g7staging.staxi.vn/")
        time.sleep(3)
        try:
            web.driver2.ele(var_stx_app.login_user, timeout=10)
        except:
            web.driver2.refresh()
            time.sleep(7)
        web.driver2.ele(var_stx_app.login_user1).clear()
        time.sleep(0.5)
        web.driver2.ele(var_stx_app.login_user1).input(user)
        time.sleep(0.5)

        web.driver2.ele(var_stx_app.login_password1).clear()
        time.sleep(0.5)
        web.driver2.ele(var_stx_app.login_password1).input(password)
        time.sleep(0.5)
        web.driver2.ele(var_stx_app.dangnhap1).click()
        time.sleep(5)


    def accounting_14_1(self):
        web = web_app()
        try:
            web.driver2.ele(var_stx_app.accounting).click()
        except:
            web.create_driver()
            web.login_stx(var_stx_app.data['login']['autoba_tk'], var_stx_app.data['login']['autoba_mk'])
            web.driver2.ele(var_stx_app.accounting).click()
        time.sleep(2)
        try:
            web.driver2.ele(var_stx_app.accounting_14_1).click()
        except:
            web.driver2.ele(var_stx_app.accounting).click()
            time.sleep(2)
            web.driver2.ele(var_stx_app.accounting_14_1).click()
        time.sleep(5)


    def admin_10_6_4(self):
        web = web_app()
        web.create_driver()
        web.login_stx(var_stx_app.data['login']['autoba_tk'], var_stx_app.data['login']['autoba_mk'])

        try:
            web.driver2.ele(var_stx_app.admin).click()
        except:
            web.create_driver()
            web.driver2.ele(var_stx_app.admin).click()
        time.sleep(2)
        try:
            web.driver2.ele(var_stx_app.admin_6).click()
        except:
            web.driver2.ele(var_stx_app.admin).click()
            time.sleep(2)
            web.driver2.ele(var_stx_app.admin_6).click()
        time.sleep(2)
        web.driver2.ele(var_stx_app.admin_6_4).click()
        time.sleep(5)


    def search_accounting(self, address):
        web = web_app()
        web.create_driver()
        try:
            web.driver2.ele(var_stx_app.reportrange).click()
        except:
            web.accounting_14_1()
            web.driver2.ele(var_stx_app.reportrange).click()
        time.sleep(2)
        web.driver2.ele(var_stx_app.today).click()
        time.sleep(2)

        web.driver2.ele(var_stx_app.MobileOrAddress).clear()
        time.sleep(0.5)
        web.driver2.ele(var_stx_app.MobileOrAddress).input(address)
        time.sleep(0.5)
        web.driver2.ele(var_stx_app.search).click()
        time.sleep(3.5)







    def check_not_fill_electronic_invoice(self, code, eventname, result):
        web = web_app()
        web.create_driver()

        #admin
        web.admin_10_6_4()
        try:
            web.driver2.ele(var_stx_app.name_config).clear()
        except:
            web.admin_10_6_4()
            web.driver2.ele(var_stx_app.name_config).clear()
        time.sleep(0.5)
        web.driver2.ele(var_stx_app.name_config).input("INVOICE_AUTO_CUSTAPP")
        time.sleep(0.5)
        web.driver2.ele(var_stx_app.search).click()
        time.sleep(3.5)
        name = web.driver2.ele(var_stx_app.config_name).text
        value = web.driver2.ele(var_stx_app.config_value).text


        #accounting
        web.accounting_14_1()
        web.search_accounting(var_stx_app.data['web_app']['search_address2'])
        id = web.driver2.ele(var_stx_app.id_electronic_invoice).text
        status = web.driver2.ele(var_stx_app.status_electronic_invoice).text


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("CASE CHECK TRẠNG THÁI XUẤT HÓA ĐƠN WEB, APP - Check dữ liệu")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f"Mã cuốc khách: {id}\nTrạng thái: {status}\nTên cấu hình: {name}\nValue: {value}")
        var_stx_app.logging.info(f"Mã cuốc khách: {id}\nTrạng thái: {status}\nTên cấu hình: {name}\nValue: {value}")

        if (value == "0") and (name == "INVOICE_AUTO_CUSTAPP"):
            if status == "Chưa xử lý":
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")


        if (value == "1") and (name == "INVOICE_AUTO_CUSTAPP"):
            if status != "Chưa xử lý":
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
        try:
            web.driver2.quit()
            time.sleep(2)
        except:
            pass



    def check_fill_electronic_invoice(self, code, eventname, result):
        web = web_app()
        web.create_driver()

        web.search_accounting(var_stx_app.data['web_app']['search_address1'])

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("CASE CHECK TRẠNG THÁI XUẤT HÓA ĐƠN WEB, APP - Check dữ liệu")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            id = web.driver2.ele(var_stx_app.id_electronic_invoice).text
            status = web.driver2.ele(var_stx_app.status_electronic_invoice).text
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f"Mã cuốc khách: {id}\nTrạng thái: {status}")
            var_stx_app.logging.info(f"Mã cuốc khách: {id}\nTrạng thái: {status}")
            if status != "Chưa xử lý":
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
        except:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
        try:
            web.driver2.quit()
            time.sleep(2)
        except:
            pass


    def check_card_company_auto_export(self, code, eventname, result):
        web = web_app()
        web.create_driver()

        web.search_accounting(var_stx_app.data['web_app']['search_address3'])

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("CASE CHECK TRẠNG THÁI XUẤT HÓA ĐƠN WEB, APP - Check dữ liệu")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            id = web.driver2.ele(var_stx_app.id_electronic_invoice).text
            status = web.driver2.ele(var_stx_app.status_electronic_invoice).text
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f"Mã cuốc khách: {id}\nTrạng thái: {status}")
            var_stx_app.logging.info(f"Mã cuốc khách: {id}\nTrạng thái: {status}")
            if status != "Chưa xử lý":
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
        except:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
        try:
            web.driver2.quit()
            time.sleep(2)
        except:
            pass


    def check_card_company_not_auto_export(self, code, eventname, result):
        web = web_app()
        web.create_driver()

        web.search_accounting(var_stx_app.data['web_app']['search_address4'])

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("CASE CHECK TRẠNG THÁI XUẤT HÓA ĐƠN WEB, APP - Check dữ liệu")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            id = web.driver2.ele(var_stx_app.id_electronic_invoice).text
            status = web.driver2.ele(var_stx_app.status_electronic_invoice).text
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f"Mã cuốc khách: {id}\nTrạng thái: {status}")
            var_stx_app.logging.info(f"Mã cuốc khách: {id}\nTrạng thái: {status}")
            if status == "Chưa xử lý":
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
        except:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
        try:
            web.driver2.quit()
            time.sleep(2)
        except:
            pass


    def check_pttt(self, code, eventname, result):
        web = web_app()
        web.create_driver()
        #accounting
        web.search_accounting(var_stx_app.data['web_app']['search_address2'])

        web.driver2.ele(var_stx_app.id_electronic_invoice).click()
        time.sleep(3)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("CASE CHECK TRẠNG THÁI XUẤT HÓA ĐƠN WEB, APP - Check dữ liệu")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            pttt_before = web.driver2.ele(var_stx_app.pttt_before).attr("value")
            pttt_after = web.driver2.ele(var_stx_app.pttt_after).attr("value")

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f" Phương thức thanh toán(Thông tin cuốc): {pttt_before}\nPhương thức thanh toán(Thông tin thanh toán): {pttt_after}")
            var_stx_app.logging.info(f" Phương thức thanh toán(Thông tin cuốc): {pttt_before}\nPhương thức thanh toán(Thông tin thanh toán): {pttt_after}")
            if (pttt_before == "Thanh toán qua AppKH") and (pttt_after == "Tiền mặt"):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
        except:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")


        try:
            web.driver2.quit()
            time.sleep(2)
        except:
            pass




