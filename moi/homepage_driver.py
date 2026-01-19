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
import homepage_g7
from pynput.keyboard import Key, Controller
keyboard = Controller()
from datetime import datetime
import cv2
import unicodedata
import action
import var_stx_app






def wait_toast_message(driver, time_wait=5):
    end_time = time.time() + time_wait
    while time.time() < end_time:
        try:
            toast = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.XPATH, "//android.widget.Toast")))
            message = toast.get_attribute("text")
            print(f"Toast message: {message}")
            return message
        except:
            time.sleep(0.2)
    print("❌ Không bắt được Toast message")


def wait_toast_message_click(driver, button, time_wait=5):
    end_time = time.time() + time_wait
    while time.time() < end_time:
        try:
            action.click(driver, button, time_wait=1)
            toast = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.XPATH, "//android.widget.Toast")))
            message = toast.get_attribute("text")
            print(f"Toast message: {message}")
            return message
        except:
            time.sleep(0.2)
    print("❌ Không bắt được Toast message")
# raise TimeoutError()


def wait_toast_message_click2(driver, button1, button2, time_wait=5):
    end_time = time.time() + time_wait
    while time.time() < end_time:
        try:
            action.click(driver, button1, time_wait=3)
            action.click(driver, button2, time_wait=3)
            toast = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.XPATH, "//android.widget.Toast")))
            message = toast.get_attribute("text")
            print(f"Toast message: {message}")
            return message
        except:
            time.sleep(0.2)
    print("❌ Không bắt được Toast message")


def select_detail(field, row):
    var_stx_app.driver_driver.implicitly_wait(0.05)  # nhiên liệu
    n = 0
    while (n < 10):
        n += 1
        n = str(n)
        path_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup[1]/android.widget.TextView[1]"
        path_data = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup[1]/android.widget.TextView[2]"
        print(n)
        try:
            name = var_stx_app.driver_driver.find_element(By.XPATH, path_name).text
            print(name)
            if name == field:
                data = var_stx_app.driver_driver.find_element(By.XPATH, path_data).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", row, 3, data)
                print(data)
                break
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", row, 3, 0)
        n = int(n)



def select_detail1(field, row):
    var_stx_app.driver_driver.implicitly_wait(0.05)  # nhiên liệu
    n = 0
    while (n < 10):
        n += 1
        n = str(n)
        path_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup[1]/android.widget.TextView[1]"
        path_data = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup[1]/android.widget.TextView[2]"
        print(n)
        try:
            name = var_stx_app.driver_driver.find_element(By.XPATH, path_name).text
            print(name)
            if name == field:
                data = var_stx_app.driver_driver.find_element(By.XPATH, path_data).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", row, 3, data)
                print(data)
                break
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", row, 3, 0)
        n = int(n)



def homepage_g7_drive_back():
    print("bắt đầu reset app driver")
    var_stx_app.reset_app(var_stx_app.driver_driver)
    print("đã reset app driver")
    try:
        action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=9)
        time.sleep(2)
        print("r0")
    except:
        pass
    print("đang tắt thông báo app driver")

    try:
        action.click(var_stx_app.driver_driver, var_stx_app.stt, time_wait=1)
        action.click(var_stx_app.driver_driver, var_stx_app.cancel_drive, time_wait=20)
        action.click(var_stx_app.driver_driver, var_stx_app.confirm1, time_wait=20)
        action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=20)
        action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=20)
        print("đã hủy tài thành công")
    except:
        pass

    try:
        action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=1)
        return
    except:
        pass

    try:
        action.click(var_stx_app.driver_driver, var_stx_app.GIVE_BACK_CUSTOMER, time_wait=1)
        time.sleep(2)
        print("r1")
    except:
        pass

    try:
        action.click(var_stx_app.driver_driver, var_stx_app.CASH, time_wait=1)
        time.sleep(2)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.CASH_100k, time_wait=3)
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=5)
            action.click(var_stx_app.driver_driver, var_stx_app.payment, time_wait=5)
        except:
            pass
        print("r2")
    except:
        pass

    try:
        action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=1)
        time.sleep(2)
        print("r3")
    except:
        pass



    try:
        action.click(var_stx_app.driver_driver, var_stx_app.CANCEL, time_wait=1)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.reasson_other, time_wait=3)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.reasson_other1, time_wait=10)
            action.send_keys(var_stx_app.driver_driver, var_stx_app.reasson_other1_input, "Trường test huy cuốc lái xe", time_wait=10)
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=10)
        print("r4")
    except:
        pass

    try:
        action.click(var_stx_app.driver_driver, var_stx_app.WRONG_CUSTOMER, time_wait=1)
        action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=15)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_wrong_customer, time_wait=1)
        except:
            pass
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=5)
            time.sleep(2)
        except:
            pass
        action.click(var_stx_app.driver_driver, var_stx_app.RETURN_GUESTS, time_wait=15)
        action.click(var_stx_app.driver_driver, var_stx_app.CASH, time_wait=15)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=5)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.money2, time_wait=5)
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=5)
            action.click(var_stx_app.driver_driver, var_stx_app.payment, time_wait=5)
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=5)
            except:
                pass
        print("r5")
    except:
        pass

    try:
        action.wait_for(var_stx_app.driver_driver, var_stx_app.PAY_CARD, time_wait=1)
    except:
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=1)
            action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=5)
            action.click(var_stx_app.driver_driver, var_stx_app.icon_3daugach, time_wait=5)
            action.click(var_stx_app.driver_driver, var_stx_app.thanhtoantienmat, time_wait=5)
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=5)
                time.sleep(2)
            except:
                pass
            print("r6")
        except:
            pass

    try:
        action.click(var_stx_app.driver_driver, var_stx_app.i_readed, time_wait=1)
        time.sleep(2)
        print("r6.5")
    except:
        pass
    try:
        action.click(var_stx_app.driver_driver, var_stx_app.close_tab, time_wait=1)
        time.sleep(2)
        print("r6.6")
    except:
        pass

    try:
        action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=1)
        time.sleep(2)
        print("r7")
    except:
        pass

    try:
        action.click(var_stx_app.driver_driver, var_stx_app.exit, time_wait=1)
        time.sleep(2)
        print("r8")
    except:
        pass
    try:
        action.click(var_stx_app.driver_driver, var_stx_app.BACK, time_wait=1)
        time.sleep(2)
        print("r9")
    except:
        pass
    try:
        action.click(var_stx_app.driver_driver, var_stx_app.COME_BACK, time_wait=1)
        time.sleep(2)
        print("r10")
    except:
        pass

    try:
        action.click(var_stx_app.driver_driver, var_stx_app.cancel, time_wait=1)
        time.sleep(2)
        print("r11")
    except:
        pass
    try:
        action.click(var_stx_app.driver_driver, var_stx_app.CANCEL, time_wait=1)
        time.sleep(2)
        print("r11")
    except:
        pass
    try:
        action.click(var_stx_app.driver_driver, var_stx_app.SKIP, time_wait=1)
        time.sleep(2)
        print("r12")
    except:
        pass
    try:
        action.click(var_stx_app.driver_driver, var_stx_app.skip, time_wait=1)
        time.sleep(2)
        print("r13")
    except:
        pass
    try:
        action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=1)
        time.sleep(2)
        print("r14")
    except:
        pass
    try:
        action.click(var_stx_app.driver_driver, var_stx_app.IGREE, time_wait=1)
        time.sleep(2)
        print("r15")
    except:
        pass
    try:
        action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=1)
        time.sleep(2)
        print("r16")
    except:
        pass

    try:
        print("Check session")
        # LỆNH BẮT BUỘC proxy qua UiAutomator2
        var_stx_app.driver_driver.get_window_size()
        print("vẫn còn session")
    except Exception as e:
        print(f"session chết thật rồi → recreate driver: {e}")
        var_stx_app.restart_driver(var_stx_app.driver_driver)
        print("đã reset lại session")

    print("đã tắt thông báo app driver")














def RECEIVE_APP(times):
    # action.click(var_stx_app.driver_driver, var_stx_app.RECEIVE_APP, time_wait=times)
    n = 0
    while (n < times):
        n += 1
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.RECEIVE_APP, time_wait=1)
            break
        except:
            pass
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.igree, time_wait=1)
            action.click(var_stx_app.driver_customer, var_stx_app.payment_app, time_wait=3)
        except:
            pass




def check_image(times, name_image, threshold_number, type_click):
    pass
    # var_stx_app.driver_driver.implicitly_wait(0.5)  # nhiên liệu
    # n = -1
    # while (n < times):
    #     n += 1
    #     if n >= times:
    #         raise Exception(f"Không tìm thấy ảnh '{name_image}' sau {times} lần thử.")
    #     try:
    #         module_other_stx_app.check_icon(var_stx_app.screen + name_image, region=None, threshold=threshold_number, click=type_click, show=True)
    #         break
    #     except:
    #         pass
    #     time.sleep(1)
    #     print(f"đang tìm path s thứ: {n}")


#homepage_driver.check_image(10, "NHAN_APP.png", 0.8, True)



def normalize_text(text):
    # Chuẩn hóa unicode, bỏ dấu
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    # Đưa về chữ thường, bỏ ký tự đặc biệt và khoảng trắng dư
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s]', '', text)  # giữ lại chữ, số và khoảng trắng
    return text




class home_page:

    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def status_driver(self, type, status):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=1)
        except:
            login_stx_app.login_driverg7(self, type)


        name_status = action.get_text(var_stx_app.driver_driver, var_stx_app.name_status_driver)

        if name_status != status:
            action.click(var_stx_app.driver_driver, var_stx_app.name_status_driver_radio)
            time.sleep(2)

        action.click(var_stx_app.driver_driver, var_stx_app.Accept_street_hails)
        time.sleep(1.5)
        check_text = var_stx_app.driver_driver.find_element(By.XPATH, "//android.widget.Toast").text
        print(check_text)
        if check_text == "Sẵn sàng nhận cuốc phố":
            pass
        else:
            time.sleep(2)
            action.click(var_stx_app.driver_driver, var_stx_app.Accept_street_hails)
            time.sleep(1.5)
            check_text = var_stx_app.driver_driver.find_element(By.XPATH, "//android.widget.Toast").text
            print(check_text)









class waiting_for_a_passenger:


    def waiting_for_a_passenger(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=1)
        except:
            home_page.status_driver(self, "Xe sân bay", "SẴN SÀNG")
            action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach)

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.waiting_for_a_passenger)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach)
            action.click(var_stx_app.driver_driver, var_stx_app.waiting_for_a_passenger)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_waiting_for_a_passenger, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc",
                                                      var_stx_app.check_waiting_for_a_passenger, "G7 Taxi Hà Nội", "_TrangChu_ChoCuoc.png")



    def check_display_icon(self, code, eventname, result, path_icon, name_image):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=1)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")

        # action.click(var_stx_app.driver_driver, path_icon, time_wait=7)
        wait_toast_message_click(var_stx_app.driver_driver, path_icon, 7)
        module_other_stx_app.write_result_text_try_if_toast_other(var_stx_app.driver_driver, code, eventname, result,
                                                                  "Quản trị - Danh sách xe", "", "", name_image)



    def check_display_icon_current_location(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=1)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")


        module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.5, 0.25, 0.5, 0.7, 500)
        time.sleep(1)
        module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.5, 0.25, 0.5, 0.7, 500)
        time.sleep(1)
        module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.5, 0.25, 0.5, 0.7, 500)
        time.sleep(2)
        action.click(var_stx_app.driver_driver, var_stx_app.icon_current_location_driver, time_wait=10)
        time.sleep(2)

        module_other_stx_app.write_result_displayed_try(var_stx_app.driver_driver, code, eventname, result, "Quản trị - Danh sách xe",
                                              var_stx_app.icon_car, "_TrangChu_IconViTriHienTai.png")



    def check_display_icon_traffic_light(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=1)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")


        action.click(var_stx_app.driver_driver, var_stx_app.icon_traffic_light, time_wait=15)
        time.sleep(2)
        action.click(var_stx_app.driver_driver, var_stx_app.icon_traffic_light, time_wait=15)
        time.sleep(1)
        module_other_stx_app.write_result_displayed_try(var_stx_app.driver_driver, code, eventname, result, "Quản trị - Danh sách xe",
                                              var_stx_app.icon_traffic_light, "_TrangChu_IconDenGiaoThong.png")



    def check_display_icon_xeplot(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=1)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")

        message = wait_toast_message_click(var_stx_app.driver_driver, var_stx_app.icon_config_lot, 7)
        if message == "Bạn đang theo dõi vị trí theo điện thoại.":
            module_other_stx_app.write_result_text_try_if_toast(var_stx_app.driver_driver, code, eventname, result, "Quản trị - Danh sách xe",
                                                  "", "Bạn đang theo dõi vị trí theo điện thoại.", "_TrangChu_IconCauHinhXepLot.png")
        else:
            wait_toast_message_click(var_stx_app.driver_driver, var_stx_app.icon_config_lot, 7)
            module_other_stx_app.write_result_text_try_if_toast(var_stx_app.driver_driver, code, eventname, result, "Quản trị - Danh sách xe",
                                                                "", "Bạn đang theo dõi vị trí theo điện thoại.", "_TrangChu_IconCauHinhXepLot.png")
            time.sleep(2)



    def check_display_icon_cuocpho(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=1)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")

        message = wait_toast_message_click(var_stx_app.driver_driver, var_stx_app.icon_accept_street, 7)
        if message == "Sẵn sàng nhận cuốc phố":
            module_other_stx_app.write_result_text_try_if_toast(var_stx_app.driver_driver, code, eventname, result, "Quản trị - Danh sách xe",
                                                  "", "Sẵn sàng nhận cuốc phố", "_TrangChu_IconCauHinhXepLot.png")
        else:
            wait_toast_message_click(var_stx_app.driver_driver, var_stx_app.icon_accept_street, 7)
            module_other_stx_app.write_result_text_try_if_toast(var_stx_app.driver_driver, code, eventname, result, "Quản trị - Danh sách xe",
                                                  "", "Sẵn sàng nhận cuốc phố", "_TrangChu_IconCauHinhXepLot.png")



    def check_icon_help(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=1)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")


        action.click(var_stx_app.driver_driver, var_stx_app.icon_help, time_wait=15)


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            check_icon_name1 = action.get_text(var_stx_app.driver_driver, var_stx_app.check_icon_name1, time_wait=15)
            check_icon_name2 = action.get_text(var_stx_app.driver_driver, var_stx_app.check_icon_name2)
            check_icon_name3 = action.get_text(var_stx_app.driver_driver, var_stx_app.check_icon_name3)
            check_icon_name4 = action.get_text(var_stx_app.driver_driver, var_stx_app.check_icon_name4)

            check_icon_data1 = action.get_text(var_stx_app.driver_driver, var_stx_app.check_icon_data1)
            check_icon_data2 = action.get_text(var_stx_app.driver_driver, var_stx_app.check_icon_data2)
            check_icon_data3 = action.get_text(var_stx_app.driver_driver, var_stx_app.check_icon_data3)
            check_icon_data4 = action.get_text(var_stx_app.driver_driver, var_stx_app.check_icon_data4)

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "1.{}\n{}\n2.{}\n{}\n3.{}\n{}\n4.{}\n{}"
                                           .format(check_icon_name1, check_icon_data1, check_icon_name2, check_icon_data2,
                                                   check_icon_name3, check_icon_data3, check_icon_name4, check_icon_data4))
            var_stx_app.logging.info("1.{}\n{}\n2.{}\n{}\n3.{}\n{}\n4.{}\n{}"
                                           .format(check_icon_name1, check_icon_data1, check_icon_name2, check_icon_data2,
                                                   check_icon_name3, check_icon_data3, check_icon_name4, check_icon_data4))
            if (check_icon_name1 == "Đường dây nóng" and check_icon_data1 != "") and (check_icon_name2 == "Trung tâm điều hành&CSKH" and check_icon_data2 != "") \
                    and (check_icon_name3 == "Văn Phòng" and check_icon_data3 != "") and (check_icon_name4 == "Hỗ trợ định vị, App" and check_icon_data4 != ""):

                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_IconHoTroKhanCap.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_IconHoTroKhanCap.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_IconHoTroKhanCap.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_IconHoTroKhanCap.png")

        var_stx_app.driver_driver.back()
        # action.click(var_stx_app.driver_driver, var_stx_app.icon_help, time_wait=15)
        time.sleep(1.5)



    def status(self, code, eventname, result, status, name_image):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=1)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")



        name_status = action.get_text(var_stx_app.driver_driver, var_stx_app.name_status_driver)

        if name_status != status:
            action.click(var_stx_app.driver_driver, var_stx_app.name_status_driver_radio)
            time.sleep(2)

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc",
                                                      var_stx_app.name_status_driver, status, name_image)



    def check_location_car(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=1)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")


        module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.5, 0.25, 0.5, 0.7, 500)
        time.sleep(1)
        module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.5, 0.25, 0.5, 0.7, 500)
        time.sleep(1)
        module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.5, 0.25, 0.5, 0.7, 500)

        action.wait_for(var_stx_app.driver_driver, var_stx_app.icon_car, time_wait=20)
        module_other_stx_app.write_result_displayed_try(var_stx_app.driver_driver, code, eventname, result, "Quản trị - Danh sách xe",
                                              var_stx_app.icon_car, "_TrangChu_IconXe.png")



    def check_over_map(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        waiting_for_a_passenger.create_order(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.create_order_search_to)
        action.clear(var_stx_app.driver_driver, var_stx_app.create_order_location2_input)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.create_order_location2_input, var_stx_app.data['home_page_g7']['check_open_map'])

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.select_searh)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=15)
            action.click(var_stx_app.driver_driver, var_stx_app.create_order_search_to)
            action.clear(var_stx_app.driver_driver, var_stx_app.create_order_location2_input)
            action.send_keys(var_stx_app.driver_driver, var_stx_app.create_order_location2_input, var_stx_app.data['home_page_g7']['check_open_map'])


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Chọn địa chỉ_OpenMap_Gợi ý điểm xung quanh vị trí app")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            search_location1 = action.get_text(var_stx_app.driver_driver, var_stx_app.search_location1)
            search_location2 = action.get_text(var_stx_app.driver_driver, var_stx_app.search_location2)
            search_location3 = action.get_text(var_stx_app.driver_driver, var_stx_app.search_location3)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f"Địa chỉ 1: {search_location1}\n"
                                                                                            f"Địa chỉ 2: {search_location2}\n"
                                                                                            f"Địa chỉ 3: {search_location3}\n")
            var_stx_app.logging.info(f"Địa chỉ 1: {search_location1}\n"
                                    f"Địa chỉ 2: {search_location2}\n"
                                    f"Địa chỉ 3: {search_location3}\n")

            if any(var_stx_app.data['home_page_g7']['check_open_map'] in ele for ele in [search_location1, search_location2, search_location3]):
                print("✅ Có chứa '40 Bằng Liệt'")
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_CheckOpenMap.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_CheckOpenMap.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_IconXe.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_CheckOpenMap.png")


        action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=15)
        action.click(var_stx_app.driver_driver, var_stx_app.COME_BACK, time_wait=15)
        time.sleep(2)



    def get_info_drive(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=1)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")



        overview_namediver_number = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_namediver_number, time_wait=20)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 45, 2, overview_namediver_number)

        overview_typevehicle_liscenseplate = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_typevehicle_liscenseplate, time_wait=20)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 46, 2, overview_typevehicle_liscenseplate)


        action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=15)


        icon_3gach_version = action.get_text(var_stx_app.driver_driver, var_stx_app.icon_3gach_version, time_wait=20)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 47, 3, icon_3gach_version)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 123, 2, icon_3gach_version)

        icon_3gach_name = action.get_text(var_stx_app.driver_driver, var_stx_app.icon_3gach_name, time_wait=20)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 45, 3, icon_3gach_name)



        action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach_image, time_wait=15)

        detail_drive_name3 = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_drive_name3, time_wait=20)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 45, 4, detail_drive_name3)

        detail_drive_review = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_drive_review, time_wait=20)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 48, 4, detail_drive_review)

        detail_drive_type_vehicle = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_drive_type_vehicle, time_wait=20)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 46, 4, detail_drive_type_vehicle)

        detail_drive_liscense_plate = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_drive_liscense_plate, time_wait=20)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 49, 4, detail_drive_liscense_plate)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Thông tin cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("True")
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")



    def check_info_drive_name(self, code, eventname, result):
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 45, 2))
        overview = overview.split("-")[0].strip()
        overview1 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 45, 3))

        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 45, 4))
        detail = detail.split("-")[0].strip()

        overview = normalize_text(overview)
        overview1 = normalize_text(overview1)
        detail = normalize_text(detail)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình Chờ cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Tên lái xe(Màn hình chờ cuốc): {}".format(overview))
        var_stx_app.logging.info("Tên lái xe(Dấu 3 gạch)       : {}".format(overview1))
        var_stx_app.logging.info("Tên lái xe(Thông tin cá nhân): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "1.Tên lái xe(Màn hình chờ cuốc): {}\n2.Tên lái xe(Dấu 3 gạch)       : {}\n3.Tên lái xe(Thông tin cá nhân): {}"
                                       .format(overview, overview1, detail))
        if overview == overview1 == detail:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_drive_type_vehicle(self, code, eventname, result):
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 46, 2))
        overview = overview.split("-")[0].strip()
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 46, 4))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình Chờ cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Loại xe(Màn hình chờ cuốc): {}".format(overview))
        var_stx_app.logging.info("Loại xe(Thông tin cá nhân): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "1.Loại xe(Màn hình chờ cuốc): {}\n2.Loại xe(Thông tin cá nhân): {}"
                                       .format(overview, detail))
        if overview == detail:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_drive_version(self, code, eventname, result):
        overview1 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 47, 3))
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 45, 4))
        detail = detail.split("-")[1].strip()

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình Chờ cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Phiên bản(Dấu 3 gạch)       : {}".format(overview1))
        var_stx_app.logging.info("Phiên bản(Thông tin cá nhân): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "1.Phiên bản(Dấu 3 gạch)       : {}\n2.Phiên bản(Thông tin cá nhân): {}"
                                       .format(overview1, detail))
        if overview1 == detail:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_drive_star(self, code, eventname, result):
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 48, 4))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình Chờ cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Số sao(Thông tin cá nhân): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "1.Số sao(Thông tin cá nhân): {}".format(detail))
        if detail != "None":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_drive_liscense_plate(self, code, eventname, result):
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 46, 2))
        overview = overview.split("-")[1].strip()
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 49, 4))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình Chờ cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Biển số xe(Màn hình chờ cuốc): {}".format(overview))
        var_stx_app.logging.info("Biển số xe(Thông tin cá nhân): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "1.Biển số xe(Màn hình chờ cuốc): {}\n2.Biển số xe(Thông tin cá nhân): {}"
                                       .format(overview, detail))
        if overview == detail:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def change_password(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.personal_information, time_wait=1)
        except:
            waiting_for_a_passenger.get_info_drive(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.change_password)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.change_password_old, "atgmj123")
        action.send_keys(var_stx_app.driver_driver, var_stx_app.change_password_new1, "atgmj123")
        action.send_keys(var_stx_app.driver_driver, var_stx_app.change_password_new2, "atgmj123")
        wait_toast_message_click(var_stx_app.driver_driver, var_stx_app.confirm1, 7)
        module_other_stx_app.write_result_text_try_if_toast(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Thông tin cá nhân - Đổi mật khẩu",
                                              "", "Mật khẩu mới trùng với mật khẩu cũ, vui lòng thử lại!", "_TrangChu_DoiMatKhau.png")


        try:
            action.click(var_stx_app.driver_driver, var_stx_app.change_password_back, time_wait=3)
            action.click(var_stx_app.driver_driver, var_stx_app.info_drive_back)
            time.sleep(2)
        except:
            pass







    def driver_dispatching(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=1)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")


        # rời sảnh
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.stt, time_wait=1)
            action.click(var_stx_app.driver_driver, var_stx_app.cancel_drive, time_wait=20)
            action.click(var_stx_app.driver_driver, var_stx_app.confirm1, time_wait=20)
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=20)
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=20)
            print("đã hủy tài thành công")
        except:
            pass

        action.click(var_stx_app.driver_driver, var_stx_app.driver_dispatching, time_wait=20)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_driver_dispatching, time_wait=20)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Xếp tài",
                                              var_stx_app.check_driver_dispatching, "Danh sách sảnh", "_TrangChu_XepTai.png")



    def binhanh_parking_lot(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_driver_dispatching, time_wait=1)
        except:
            waiting_for_a_passenger.driver_dispatching(self, "", "", "")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.binhanh_parking_lot, time_wait=15)
        except:
            module_other_stx_app.tap_percent(var_stx_app.driver_driver, 0.5, 0.2)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_binhanh_parking_lot, time_wait=20)
        except:
            pass

        module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Xếp tài",
                                                            var_stx_app.check_binhanh_parking_lot, "", "_TrangChu_XepTai_SanhBinhAnh.png")



    def check_info_binhanh_parking_lot(self, code, eventname, result, type, path_check, name_image):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.cancel_drive, time_wait=1)
        except:
            waiting_for_a_passenger.binhanh_parking_lot(self, "", "", "")


        if type == "0":
            module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_driver, code, eventname, result,
                                                                "Trang Chủ(Lái xe g7) - Chờ cuốc - Xếp tài",
                                                                path_check, "", name_image)
        else:
            var_stx_app.logging.info("--------------")
            var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Xếp tài")
            var_stx_app.logging.info("Mã - " + code)
            var_stx_app.logging.info("Tên sự kiện - " + eventname)
            var_stx_app.logging.info("Kết quả - " + result)
            try:
                check_text = var_stx_app.driver_driver.find_element(By.XPATH, path_check).text
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, check_text)
                var_stx_app.logging.info(check_text)
                if check_text != "":
                    var_stx_app.logging.info("True")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)
            except:
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)



    def cancel_drive(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            print("n1")
            action.click(var_stx_app.driver_driver, var_stx_app.stt, time_wait=1)
            action.click(var_stx_app.driver_driver, var_stx_app.cancel_drive, time_wait=20)
            action.click(var_stx_app.driver_driver, var_stx_app.confirm1, time_wait=20)
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=20)
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=20)
            print("đã hủy tài thành công")
        except:
            pass

        try:
            print("n2")
            action.wait_for(var_stx_app.driver_driver, var_stx_app.cancel_drive, time_wait=1)
            print("n3")
        except:
            waiting_for_a_passenger.binhanh_parking_lot(self, "", "", "")
            print("n4")

        action.click(var_stx_app.driver_driver, var_stx_app.cancel_drive, time_wait=20)
        action.click(var_stx_app.driver_driver, var_stx_app.confirm1, time_wait=20)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_cancel_drive, time_wait=20)
        except:
            pass

        print("n5")
        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Xếp tài",
                                              var_stx_app.check_cancel_drive, "Bạn đã hủy tài thành công", "_SanhBinhAnh_HuyTai.png")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=3)
            time.sleep(2)
        except:
            pass
        print("n6")
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=7)
        except:
            pass



    def driver_dispatching_create_order(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.stt, time_wait=1)
        except:
            waiting_for_a_passenger.binhanh_parking_lot(self, "", "", "")
            action.click(var_stx_app.driver_driver, var_stx_app.dispatching_back)

        waiting_for_a_passenger.cash(self, "", "", "")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=5)
            time.sleep(3)
        except:
            pass


        module_other_stx_app.write_result_not_displayed_try(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Xếp tài - Tạo cuốc",
                                                            var_stx_app.stt, "_SanhBinhAnh_XepTai_TaoCuoc.png")

        # hủy tài
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.stt, time_wait=3)
            action.click(var_stx_app.driver_driver, var_stx_app.cancel_drive, time_wait=20)
            action.click(var_stx_app.driver_driver, var_stx_app.confirm1, time_wait=20)
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=20)
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=20)
            print("đã hủy tài thành công")
        except:
            pass







    def create_order(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.notification, time_wait=1)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.create_order)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_create_order)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc",
                                                      var_stx_app.check_create_order, "TẠO CUỐC", "_ChoCuoc_TaoCuoc.png")



    def create_order_back(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.COME_BACK, time_wait=1)
        except:
            waiting_for_a_passenger.create_order(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.COME_BACK)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc",
                                                            var_stx_app.home_page, "Trang chủ", "_ChoCuoc_TaoCuoc.png")



    def create_order_search(self, code, eventname, result, type_search, path_search_input, data, path_check, desrire, name_image):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.create_order, time_wait=1)
            time.sleep(2.5)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.COME_BACK, time_wait=1)
        except:
            waiting_for_a_passenger.create_order(self, "", "", "")

        if type_search == "diachidon":
            action.click(var_stx_app.driver_driver, var_stx_app.create_order_search_from, time_wait=15)
        if type_search == "diachitra":
            action.click(var_stx_app.driver_driver, var_stx_app.create_order_search_to, time_wait=15)

        try:
            action.clear(var_stx_app.driver_driver, path_search_input, time_wait=10)
        except:
            if type_search == "diachidon":
                action.click(var_stx_app.driver_driver, var_stx_app.create_order_search_from, time_wait=15)
            if type_search == "diachitra":
                action.click(var_stx_app.driver_driver, var_stx_app.create_order_search_to, time_wait=15)

        action.clear(var_stx_app.driver_driver, path_search_input, time_wait=10)
        action.send_keys(var_stx_app.driver_driver, path_search_input, data)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.select_searh, time_wait=15)
        except:
            action.clear(var_stx_app.driver_driver, path_search_input)
            action.send_keys(var_stx_app.driver_driver, path_search_input, data)
            action.click(var_stx_app.driver_driver, var_stx_app.select_searh)

        try:
            action.wait_for(var_stx_app.driver_driver, path_check, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if_in(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc",
                                                      path_check, desrire, name_image)



    def create_order_note(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.COME_BACK, time_wait=1)
        except:
            waiting_for_a_passenger.create_order(self, "", "", "")


        action.click(var_stx_app.driver_driver, var_stx_app.note)
        action.clear(var_stx_app.driver_driver, var_stx_app.create_order_note_input)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.create_order_note_input, var_stx_app.data['home_drive']['note'])
        action.click(var_stx_app.driver_driver, var_stx_app.igree)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_create_order_note, time_wait=20)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc",
                                                      var_stx_app.check_create_order_note, var_stx_app.data['home_drive']['note'], "_TaoCuoc_GhiChu.png")



    def create_order_type(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.COME_BACK, time_wait=1)
        except:
            waiting_for_a_passenger.create_order(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.order_type, time_wait=20)
        name_type_order = action.get_text(var_stx_app.driver_driver, var_stx_app.type_order2, time_wait=20)
        action.click(var_stx_app.driver_driver, var_stx_app.type_order2, time_wait=20)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_create_order_type, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc",
                                                            var_stx_app.check_create_order_type, name_type_order, "_TaoCuoc_LoaiCuoc.png")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.type_order2_x, time_wait=1)
            time.sleep(2)
        except:
            pass



    def create_order_icon_wifi(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.COME_BACK, time_wait=1)
        except:
            waiting_for_a_passenger.create_order(self, "", "", "")

        wait_toast_message_click(var_stx_app.driver_driver, var_stx_app.icon_wifi1, 3)
        module_other_stx_app.write_result_text_try_if_toast_other(var_stx_app.driver_driver, code, eventname, result, "Tạo cuốc - check icon",
                                              "", "", "_TaoCuoc_iconWifi.png")



    def create_order_icon_location(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.COME_BACK, time_wait=1)
        except:
            waiting_for_a_passenger.create_order(self, "", "", "")

        module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.8, 0.8, 0.2, 0.8, 1000)
        time.sleep(1)
        module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.8, 0.8, 0.2, 0.8, 1000)
        time.sleep(1)
        module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.8, 0.8, 0.2, 0.8, 1000)
        time.sleep(1)
        action.click(var_stx_app.driver_driver, var_stx_app.icon_current_location1, time_wait=10)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.icon_vitrihientai1, time_wait=10)
        except:
            pass
        module_other_stx_app.write_result_displayed_try(var_stx_app.driver_driver, code, eventname, result, "Tạo cuốc - check icon",#chamxanh
                                              var_stx_app.icon_vitrihientai1, "_TaoCuoc_iconViTriHienTai.png")



    def create_order_icon_trafic(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.COME_BACK, time_wait=1)
        except:
            waiting_for_a_passenger.create_order(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.icon_traffic_light1, time_wait=10)


        module_other_stx_app.write_result_displayed_try(var_stx_app.driver_driver, code, eventname, result, "Tạo cuốc - check icon",
                                              var_stx_app.icon_traffic_light1, "_TaoCuoc_IconDenGiaoThong.png")

        action.click(var_stx_app.driver_driver, var_stx_app.COME_BACK, time_wait=5)
        time.sleep(2)












    def create_order_create_order(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        waiting_for_a_passenger.create_order_search(self, "", "", "", "diachidon", var_stx_app.create_order_location1_input,
                                                    "14 Nguyễn Cảnh Dị, hà nội", "", "", "")

        waiting_for_a_passenger.create_order_search(self, "", "", "", "diachitra", var_stx_app.create_order_location2_input,
                                                    "132 Ngõ 245 Định Công, hà nội", "", "", "")


        waiting_for_a_passenger.create_order_note(self, "", "", "")

        # check_image(5, "khongnhancuockhitaocuoc.png", 0.8, False)

        action.click(var_stx_app.driver_driver, var_stx_app.type_order, time_wait=20)
        action.click(var_stx_app.driver_driver, var_stx_app.type_order2, time_wait=20)
        action.click(var_stx_app.driver_driver, var_stx_app.CREATE_ORDER, time_wait=20)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.GIVE_BACK_CUSTOMER, time_wait=20)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc",
                                                            var_stx_app.GIVE_BACK_CUSTOMER, "TRẢ KHÁCH", "_TaoCuoc_TaoCuoc.png")



    def create_order_see_route(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.GIVE_BACK_CUSTOMER, time_wait=1)
        except:
            waiting_for_a_passenger.create_order_create_order(self, "", "", "")


        action.click(var_stx_app.driver_driver, var_stx_app.create_order_see_route, time_wait=15)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.see_route_back, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_displayed_try(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc",
                                              var_stx_app.see_route_back, "_TaoCuoc_XemLoTrinh.png")



    def create_order_see_route_icon(self, code, eventname, result, type, path_icon, name_image):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.see_route_back, time_wait=1)
        except:
            waiting_for_a_passenger.create_order_see_route(self, "", "", "")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.see_route_icon_location, time_wait=1)
            time.sleep(2)
        except:
            pass



        if type == "0":
            action.click(var_stx_app.driver_driver, path_icon, time_wait=10)

            module_other_stx_app.write_result_displayed_try(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Tạo cuốc - Xem lộ trình",
                                                            path_icon, name_image)


        if type == "1":
            # action.click(var_stx_app.driver_driver, path_icon, time_wait=10)
            # try:
            #     action.click(var_stx_app.driver_driver, var_stx_app.USE_APP, time_wait=2)
            # except:
            #     pass

            module_other_stx_app.write_result_displayed_try(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Tạo cuốc - Xem lộ trình",
                                                  path_icon, name_image)
            # time.sleep(2)
            # var_stx_app.open_app(var_stx_app.driver_driver)
            # time.sleep(2)
            #
            # try:
            #     action.click(var_stx_app.driver_driver, var_stx_app.ggmap_x, time_wait=2)
            # except:
            #     try:
            #         action.click(var_stx_app.driver_driver, var_stx_app.ggmap, time_wait=2)
            #         action.click(var_stx_app.driver_driver, var_stx_app.ggmap_x, time_wait=2)
            #     except:
            #         pass


        if type == "2":
            wait_toast_message_click(var_stx_app.driver_driver, path_icon, 7)
            module_other_stx_app.write_result_text_try_if_toast_other(var_stx_app.driver_driver, code, eventname, result,
                                                                      "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Tạo cuốc - Xem lộ trình", "", "", name_image)


        if name_image == "_TaoCuoc_XemLoTrinh_IconDieuHuong.png":
            action.click(var_stx_app.driver_driver, var_stx_app.see_route_back, time_wait=5)
            time.sleep(2.2)



    def see_route_search_location2(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        var_stx_app.driver_driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.driver_driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.see_route_search_location2)
            var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.see_route_back).click()
            time.sleep(2.2)
        except:
            pass
        try:
            var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.DROP_OFF_PASSENGERS)
        except:
            waiting_for_a_passenger.create_order_create_order(self, "", "", "")

        var_stx_app.driver_driver.implicitly_wait(5)

        var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.see_route_search_location2).click()
        time.sleep(2)
        var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.see_route_search_location2_input).clear()
        time.sleep(0.5)
        var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.see_route_search_location2_input).send_keys(var_stx_app.data['home_drive']['location2'])
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver_driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.select_searh)))
        name_location = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.select_searh1).text
        data_location = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.select_searh2).text
        element.click()
        time.sleep(2.5)
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            location2_name = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.location2_name).text
            location2_data = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.location2_data).text

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Tên điểm     :{}\nĐịa chỉ điểm:{}".format(location2_name, location2_data))
            var_stx_app.logging.info("Tên điểm     :{}\nĐịa chỉ điểm:{}".format(location2_name, location2_data))
            if (location2_name == var_stx_app.data['home_drive']['location2'] == name_location) and (location2_data == data_location):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_TaoCuoc_TaoCuoc_DiaChỉTra.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TaoCuoc_TaoCuoc_DiaChỉTra.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_TaoCuoc_TaoCuoc_DiaChỉTra.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TaoCuoc_TaoCuoc_DiaChỉTra.png")











    def see_route_drop_off_passengers(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.DROP_OFF_PASSENGERS, time_wait=1)
        except:
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.see_route_back, time_wait=1)
                time.sleep(2)
            except:
                pass

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.DROP_OFF_PASSENGERS, time_wait=1)
        except:
            waiting_for_a_passenger.create_order_create_order(self, "", "", "")


        action.click(var_stx_app.driver_driver, var_stx_app.DROP_OFF_PASSENGERS, time_wait=15)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.fee, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Trả khách",
                                                      var_stx_app.fee, "Cước phí", "_TaoCuoc_TraKhach.png")



    def add_money_fee(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.fee, time_wait=1)
        except:
            waiting_for_a_passenger.see_route_drop_off_passengers(self, "", "", "")


        action.click(var_stx_app.driver_driver, var_stx_app.icon_edit, time_wait=20)
        action.clear(var_stx_app.driver_driver, var_stx_app.money_fee_icon_input)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.money_fee_icon_input, "25,000")
        action.click(var_stx_app.driver_driver, var_stx_app.continue2)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_add_money_fee, time_wait=20)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Phụ phí",
                                                            var_stx_app.check_add_money_fee, "25.000 ₫", "_TaoCuoc_CuocPhi.png")



    def add_fee(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.fee, time_wait=1)
        except:
            waiting_for_a_passenger.see_route_drop_off_passengers(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.add_fee, time_wait=20)
        action.click(var_stx_app.driver_driver, var_stx_app.ADD_FEE)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.add_fee_input, "15000")
        action.click(var_stx_app.driver_driver, var_stx_app.igree)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_add_fee, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Phụ phí",
                                                            var_stx_app.check_add_fee, "15.000 ₫", "_TaoCuoc_ThemPhuPhi.png")



    def add_fee_edit(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.ADD_FEE, time_wait=1)
        except:
            waiting_for_a_passenger.add_fee(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.ADD_FEE_15k, time_wait=20)
        action.clear(var_stx_app.driver_driver, var_stx_app.add_fee_input)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.add_fee_input, "20000")
        action.click(var_stx_app.driver_driver, var_stx_app.igree)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_add_fee, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Phụ phí",
                                                            var_stx_app.check_add_fee, "20.000 ₫", "_TaoCuoc_SuaPhuPhi.png")



    def add_fee_delete(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.ADD_FEE, time_wait=1)
        except:
            waiting_for_a_passenger.add_fee_edit(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.add_fee_delete, time_wait=20)
        action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=20)
        action.click(var_stx_app.driver_driver, var_stx_app.SAVE_FEE, time_wait=20)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_add_fee_delete, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Phụ phí",
                                                      var_stx_app.check_add_fee_delete, "0 ₫", "_TaoCuoc_ThemPhuPhi_Xoa.png")

        action.click(var_stx_app.driver_driver, var_stx_app.add_fee, time_wait=20)
        action.click(var_stx_app.driver_driver, var_stx_app.ADD_FEE)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.add_fee_input, "15000")
        action.click(var_stx_app.driver_driver, var_stx_app.igree)
        action.click(var_stx_app.driver_driver, var_stx_app.SAVE_FEE)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_add_fee_delete, time_wait=15)
        except:
            pass



    def collected_from_customers1(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.add_fee, time_wait=1)
        except:
            waiting_for_a_passenger.add_fee_delete(self, "", "", "")

        collected_from_customers = action.get_text(var_stx_app.driver_driver, var_stx_app.collected_from_customers_money, time_wait=15)
        collected_from_customers = int(''.join(re.findall(r'\d+', collected_from_customers)))
        print(collected_from_customers)


        fee1 = action.get_text(var_stx_app.driver_driver, var_stx_app.check_add_money_fee, time_wait=15)#cước phí
        fee1 = int(''.join(re.findall(r'\d+', fee1)))
        print(fee1)

        fee2 = action.get_text(var_stx_app.driver_driver, var_stx_app.fee2, time_wait=15)#tổng(phụ phí)
        fee2 = int(''.join(re.findall(r'\d+', fee2)))
        print(fee2)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Thu của khách")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f"Cước phí: {fee1}\nPhụ phí: {fee2}\nThu của khách: {collected_from_customers}")
            var_stx_app.logging.info(f"Cước phí: {fee1}\nPhụ phí: {fee2}\nThu của khách: {collected_from_customers}")
            if collected_from_customers == fee1 + fee2:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_TaoCuoc_ThuCuaKhach.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TaoCuoc_ThuCuaKhach.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_TaoCuoc_ThuCuaKhach.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TaoCuoc_ThuCuaKhach.png")



    def cash(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.fee, time_wait=1)
        except:
            waiting_for_a_passenger.see_route_drop_off_passengers(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.CASH, time_wait=20)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.CASH_100k, time_wait=3)
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=5)
            action.click(var_stx_app.driver_driver, var_stx_app.payment, time_wait=5)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.scan_qr, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc",
                                                      var_stx_app.scan_qr, "Quét mã QRCode để xuất hóa đơn", "_TaoCuoc_TienMat.png")



    def check_info_end(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.scan_qr, time_wait=1)
        except:
            waiting_for_a_passenger.cash(self, "", "", "")


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Kết thúc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            order_id = action.get_text(var_stx_app.driver_driver, var_stx_app.order_id, time_wait=10)
            location_to = action.get_text(var_stx_app.driver_driver, var_stx_app.location_to, time_wait=10)
            payment_money = action.get_text(var_stx_app.driver_driver, var_stx_app.payment_money, time_wait=10)

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f"Mã cuốc: : {order_id}\nĐiểm trả: {location_to}\nSố tiền thanh toán:  {payment_money}")
            var_stx_app.logging.info(f"Mã cuốc: : {order_id}\nĐiểm trả: {location_to}\nSố tiền thanh toán:  {payment_money}")
            if (order_id != "") and (location_to != "") and (payment_money != ""):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_TaoCuoc_CheckThongTin_KetThuc.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TaoCuoc_CheckThongTin_KetThuc.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_TaoCuoc_CheckThongTin_KetThuc.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TaoCuoc_CheckThongTin_KetThuc.png")



    def scan_qr(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.scan_qr, time_wait=1)
        except:
            waiting_for_a_passenger.cash(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.icon_qr, time_wait=15)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.image_qr, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_displayed_try(var_stx_app.driver_driver, code, eventname, result,
                                                      "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Kết thúc",
                                                      var_stx_app.image_qr, "_TaoCuoc_ClickMaQR.png")

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.image_qr, time_wait=3)
            var_stx_app.driver_driver.back()
            time.sleep(1.5)
        except:
            pass



    def fill_sec(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.scan_qr, time_wait=1)
        except:
            waiting_for_a_passenger.cash(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.fill_sec, time_wait=15)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.info_payment_sec)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Kết thúc",
                                                      var_stx_app.info_payment_sec, "Thông tin thanh toán séc giấy", "_TaoCuoc_NhapSecGiay.png")



    def check_info_sec(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.info_payment_sec, time_wait=1)
        except:
            waiting_for_a_passenger.fill_sec(self, "", "", "")


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Kết thúc - Thông tin thanh toán sec giấy")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            sec_order_id = action.get_text(var_stx_app.driver_driver, var_stx_app.sec_order_id, time_wait=10)
            sec_location_to = action.get_text(var_stx_app.driver_driver, var_stx_app.sec_location_to, time_wait=10)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f"{sec_order_id}\n{sec_location_to}")
            var_stx_app.logging.info(f"Mã cuốc: : {sec_order_id}\nĐiểm trả: {sec_location_to}")
            if (sec_order_id != "") and (sec_location_to != ""):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_TaoCuoc_CheckThongTin_ThongTinThanhToanSecGiay.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TaoCuoc_CheckThongTin_ThongTinThanhToanSecGiay.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_TaoCuoc_CheckThongTin_ThongTinThanhToanSecGiay.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TaoCuoc_CheckThongTin_ThongTinThanhToanSecGiay.png")



    def info_sec_hd(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.info_payment_sec, time_wait=1)
        except:
            waiting_for_a_passenger.check_info_sec(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.receipt_invoice_codehd, time_wait=10)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_info_sec_hd, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Kết thúc",
                                                        var_stx_app.check_info_sec_hd, "​HD0001 - Công ty cổ phần quản lý G7 taxi", "_ThongTinThanhToanSecGiay_CheckHD.png")

        action.click(var_stx_app.driver_driver, var_stx_app.check_info_sec_hd, time_wait=5)
        time.sleep(1)



    def info_sec_send_info(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.info_payment_sec, time_wait=1)
        except:
            waiting_for_a_passenger.info_sec_hd(self, "", "", "")

        action.clear(var_stx_app.driver_driver, var_stx_app.info_trip_sec, time_wait=10)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.info_trip_sec, "99999929920")
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
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_ThongTinThanhToanSecGiay_GuiThongTin.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_ThongTinThanhToanSecGiay_GuiThongTin.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_ThongTinThanhToanSecGiay_GuiThongTin.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_ThongTinThanhToanSecGiay_GuiThongTin.png")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.close_tab)
            time.sleep(2)
        except:
            pass



    def end(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.scan_qr, time_wait=1)
        except:
            waiting_for_a_passenger.cash(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=15)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Chuyển khoản",
                                              var_stx_app.home_page, "Trang chủ", "_TaoCuoc_KetThuc.png")



    def card_pay_transfer(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=1)
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")


        waiting_for_a_passenger.create_order_search(self, "", "", "", "diachidon", var_stx_app.create_order_location1_input,
                                                    "14 Nguyễn Cảnh Dị, hà nội", "", "", "")

        waiting_for_a_passenger.create_order_search(self, "", "", "", "diachitra", var_stx_app.create_order_location2_input,
                                                    "40 Ngõ 40 Ta Quang Bửu, hà nội", "", "", "")


        waiting_for_a_passenger.create_order_note(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.CREATE_ORDER, time_wait=20)
        action.click(var_stx_app.driver_driver, var_stx_app.GIVE_BACK_CUSTOMER, time_wait=20)


        #cước phí
        action.click(var_stx_app.driver_driver, var_stx_app.icon_edit, time_wait=20)
        action.clear(var_stx_app.driver_driver, var_stx_app.money_fee_icon_input)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.money_fee_icon_input, "45000")
        action.click(var_stx_app.driver_driver, var_stx_app.continue2)

        #phụ phí
        action.click(var_stx_app.driver_driver, var_stx_app.add_fee, time_wait=20)
        action.click(var_stx_app.driver_driver, var_stx_app.ADD_FEE)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.add_fee_input, "15000")
        action.click(var_stx_app.driver_driver, var_stx_app.igree)
        action.click(var_stx_app.driver_driver, var_stx_app.SAVE_FEE)


        #THẺ THANH TOÁN
        action.click(var_stx_app.driver_driver, var_stx_app.pttt1)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.pttt_transfer, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Chuyển khoản",
                                              var_stx_app.pttt_transfer, "Chuyển khoản", "_TaoCuoc_ChuyenKhoan.png")

        action.click(var_stx_app.driver_driver, var_stx_app.pttt_transfer)
        action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=10)



    def card_pay_g7_check_info(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.pttt1, time_wait=1)
        except:
            waiting_for_a_passenger.card_pay_transfer(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.pttt1, time_wait=15)
        action.click(var_stx_app.driver_driver, var_stx_app.pttt1_g7, time_wait=15)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.ALLOW, time_wait=3.5)
        except:
            pass

        action.click(var_stx_app.driver_driver, var_stx_app.FILL_CODE_CARD, time_wait=15)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.FILL_CODE_CARD_INPUT, "8880999016579311")
        action.click(var_stx_app.driver_driver, var_stx_app.confirm1, time_wait=15)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.info_customer_card_code, time_wait=10)
        except:
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=5)
            except:
                action.clear(var_stx_app.driver_driver, var_stx_app.FILL_CODE_CARD_INPUT)
                action.send_keys(var_stx_app.driver_driver, var_stx_app.FILL_CODE_CARD_INPUT, "8880999016579311")
                action.click(var_stx_app.driver_driver, var_stx_app.confirm1)
                time.sleep(3)


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Quét thẻ thành viên G7 Taxi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            info_customer_card_code = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.info_customer_card_code).text
            info_customer_card_date = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.info_customer_card_date).text
            info_customer_card_type = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.info_customer_card_type).text
            info_customer_card_code_hd = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.info_customer_card_code_hd).text
            info_customer_card_customer = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.info_customer_card_customer).text
            info_customer_card_phone = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.info_customer_card_phone).text
            info_customer_card_fee1 = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.info_customer_card_fee1).text
            info_customer_card_fee2 = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.info_customer_card_fee2).text

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Mã thẻ: {}\nNgày hết hạn: {}\nLoại thẻ: {}\nMã hợp đồng: {}\nKhách hàng: {}\nĐiện thoại: {}\nCước, phí chuyến đi: {}\nThu của khách: {}"
                                           .format(info_customer_card_code, info_customer_card_date, info_customer_card_type, info_customer_card_code_hd,
                                                   info_customer_card_customer, info_customer_card_phone, info_customer_card_fee1, info_customer_card_fee2))
            var_stx_app.logging.info("Mã thẻ: {}\nNgày hết hạn: {}\nLoại thẻ: {}\nMã hợp đồng: {}\nKhách hàng: {}\nĐiện thoại: {}\nCước, phí chuyến đi: {}\nThu của khách: {}"
                                           .format(info_customer_card_code, info_customer_card_date, info_customer_card_type, info_customer_card_code_hd,
                                                   info_customer_card_customer, info_customer_card_phone, info_customer_card_fee1, info_customer_card_fee2))
            if (info_customer_card_code != "") and (info_customer_card_date != "") and (info_customer_card_type != "") and (info_customer_card_code_hd != "") \
                and (info_customer_card_customer != "") and (info_customer_card_phone != "") and (info_customer_card_fee1 != "") and (info_customer_card_fee2 != ""):

                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_TaoCuoc_TheG7_CheckThongTin.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TaoCuoc_TheG7_CheckThongTin.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_TaoCuoc_TheG7_CheckThongTin.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TaoCuoc_TheG7_CheckThongTin.png")



    def collected_from_customers(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.info_customer_card_code, time_wait=1)
        except:
            waiting_for_a_passenger.card_pay_g7_check_info(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.collected_from_customers, time_wait=10)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_collected_from_customers, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Quét thẻ thành viên G7 Taxi",
                                              var_stx_app.check_collected_from_customers, "Chi tiết thanh toán", "_TaoCuoc_ThuCuaKhach.png")
        var_stx_app.driver_driver.back()
        time.sleep(2)



    def pay_card(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.PAY_CARD, time_wait=1)
        except:
            waiting_for_a_passenger.card_pay_g7_check_info(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.PAY_CARD, time_wait=15)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=2)
        except:
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.end, time_wait=2)
            except:
                pass

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_pay_card, time_wait=10)
        except:
            pass


        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Quét thẻ thành viên G7 Taxi",
                                              var_stx_app.check_pay_card, "Bạn đã thanh toán thành công", "_TaoCuoc_ThanhToanThe.png")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=5)
        except:
            pass
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=2)
        except:
            pass
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=10)
        except:
            pass


        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.PAY_CARD, time_wait=1)
        except:
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=1)
                action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=5)
                action.click(var_stx_app.driver_driver, var_stx_app.icon_3daugach, time_wait=5)
                action.click(var_stx_app.driver_driver, var_stx_app.thanhtoantienmat, time_wait=5)
                try:
                    action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=5)
                    time.sleep(2)
                except:
                    pass
            except:
                pass
















    def order_fixed(self, type, address):
        var_stx_app.open_app(var_stx_app.driver_driver)
        if type == "1":
            pass

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=1)
        except:
            home_page.status_driver(self, "Xe sân bay", "SẴN SÀNG")


        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.home_page, time_wait=1)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
        homepage_g7.home_page.choose_location(self, address)



    def check_order_fixed(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        waiting_for_a_passenger.order_fixed(self, "1", "120 Phố Chùa Láng, phường Láng Thượng, quận Đống Đa, thành phố Hà Nội")

        homepage_g7.select_type_car("7 Chỗ")
        homepage_g7.select_type_car("7 CHỖ")

        action.click(var_stx_app.driver_customer, var_stx_app.pttt, time_wait=15)
        action.click(var_stx_app.driver_customer, var_stx_app.CASH, time_wait=15)
        action.click(var_stx_app.driver_customer, var_stx_app.payment_app, time_wait=15)

        # RECEIVE_APP(25)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            order_fixed_location_from = action.get_text(var_stx_app.driver_driver, var_stx_app.order_fixed_location_from, time_wait=25)
            order_fixed_location_to = action.get_text(var_stx_app.driver_driver, var_stx_app.order_fixed_location_to, time_wait=15)
            order_fixed_money = action.get_text(var_stx_app.driver_driver, var_stx_app.order_fixed_money, time_wait=15)
            order_fixed_note = action.get_text(var_stx_app.driver_driver, var_stx_app.order_fixed_note, time_wait=15)

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Địa chỉ đón: {}\nĐịa chỉ trả: {}\nCước chuyến đi: {}\nGhi chú: {}"
                                           .format(order_fixed_location_from, order_fixed_location_to, order_fixed_money, order_fixed_note))
            var_stx_app.logging.info("Địa chỉ đón: {}\nĐịa chỉ trả: {}\nCước chuyến đi: {}\nGhi chú: {}"
                                           .format(order_fixed_location_from, order_fixed_location_to, order_fixed_money, order_fixed_note))

            if (order_fixed_location_from != "") and (order_fixed_location_to != "") and (order_fixed_money != "") and (order_fixed_note != ""):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_Cuoc_Fixed_CheckThongTin.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_Cuoc_Fixed_CheckThongTin.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_Cuoc_Fixed_CheckThongTin.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_Cuoc_Fixed_CheckThongTin.png")



    def order_fixed_refuse(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.REFUSE, time_wait=1)
        except:
            waiting_for_a_passenger.order_fixed(self, "0", "120 Phố Chùa Láng, phường Láng Thượng, quận Đống Đa, thành phố Hà Nội")
            homepage_g7.select_type_car("7 Chỗ")
            homepage_g7.select_type_car("7 CHỖ")

            action.click(var_stx_app.driver_customer, var_stx_app.pttt, time_wait=15)
            action.click(var_stx_app.driver_customer, var_stx_app.CASH, time_wait=15)
            action.click(var_stx_app.driver_customer, var_stx_app.payment_app, time_wait=15)
            action.wait_for(var_stx_app.driver_driver, var_stx_app.REFUSE, time_wait=20)

        action.click(var_stx_app.driver_driver, var_stx_app.REFUSE, time_wait=20)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_order_fixed_refuse, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH",
                                                            var_stx_app.check_order_fixed_refuse, "Bạn đã từ chối thành công", "_Cuoc_Fixed_TuChoi.png")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=5)
            time.sleep(2)
        except:
            pass



    def order_fixed_receive_app(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.RESET_ORDER_CAR, time_wait=5)
        except:
            waiting_for_a_passenger.order_fixed(self, "0", "120 Phố Chùa Láng, phường Láng Thượng, quận Đống Đa, thành phố Hà Nội")
            homepage_g7.select_type_car("7 Chỗ")
            homepage_g7.select_type_car("7 CHỖ")
            action.click(var_stx_app.driver_customer, var_stx_app.pttt, time_wait=15)
            action.click(var_stx_app.driver_customer, var_stx_app.CASH, time_wait=15)
            action.click(var_stx_app.driver_customer, var_stx_app.payment_app, time_wait=15)

        RECEIVE_APP(25)
        time.sleep(4)
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)

        overview_order_fixed_location = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_order_fixed_location, time_wait=15)
        overview_order_fixed_type = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_order_fixed_type, time_wait=15)
        overview_order_fixed_fee = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_order_fixed_fee, time_wait=15)
        overview_order_fixed_detail = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_order_fixed_detail, time_wait=15)
        overview_order_fixed_location_vehicle = action.get_text(var_stx_app.driver_driver, var_stx_app.location_vehicle, time_wait=15)
        overview_order_fixed_phone = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_order_fixed_phone, time_wait=15)

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Địa chỉ đón: {}\nLoại cuốc: {}\nCước chuyến đi: {}\nbutton 1: {}\nbutton 2: {}\nSố điện thoại: {}"
                                       .format(overview_order_fixed_location, overview_order_fixed_type, overview_order_fixed_fee, overview_order_fixed_detail, overview_order_fixed_location_vehicle,
                                               overview_order_fixed_phone))

        var_stx_app.logging.info("Địa chỉ đón: {}\nLoại cuốc: {}\nCước chuyến đi: {}\nbutton 1: {}\nbutton 2: {}\nSố điện thoại: {}"
                                       .format(overview_order_fixed_location, overview_order_fixed_type, overview_order_fixed_fee, overview_order_fixed_detail, overview_order_fixed_location_vehicle,
                                               overview_order_fixed_phone))

        if (overview_order_fixed_location != "") and ("Cuốc fixed theo AppKH" in overview_order_fixed_type) and (overview_order_fixed_fee != "") and (overview_order_fixed_detail == "Xem chi tiết") \
                and (overview_order_fixed_location_vehicle == "Vị trí xe") and (overview_order_fixed_phone != ""):
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_Cuoc_Fixed_NhanApp.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_Cuoc_Fixed_NhanApp.png")



    def order_fixed_see_detail(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.see_detail, time_wait=1)
        except:
            waiting_for_a_passenger.order_fixed_receive_app(self, "", "", "")

        #OVERVIEW
        overview_order_fixed_location = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_order_fixed_location, time_wait=15)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 55, 2, overview_order_fixed_location)

        overview_order_fixed_type = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_order_fixed_type, time_wait=15)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 56, 2, overview_order_fixed_type)

        overview_order_fixed_phone = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_order_fixed_phone, time_wait=15)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 57, 2, overview_order_fixed_phone)

        #DETAIL
        action.click(var_stx_app.driver_driver, var_stx_app.see_detail, time_wait=10)

        detail1_location_from = action.get_text(var_stx_app.driver_driver, var_stx_app.detail1_location_from, time_wait=15)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 55, 3, detail1_location_from)


        detail1_location_to = action.get_text(var_stx_app.driver_driver, var_stx_app.detail1_location_to, time_wait=15)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 58, 3, detail1_location_to)


        detail1_money = action.get_text(var_stx_app.driver_driver, var_stx_app.detail1_money, time_wait=15)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 59, 3, detail1_money)


        detail1_note = action.get_text(var_stx_app.driver_driver, var_stx_app.detail1_note, time_wait=15)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 60, 3, detail1_note)


        detail1_pttt = action.get_text(var_stx_app.driver_driver, var_stx_app.detail1_pttt, time_wait=15)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 61, 3, detail1_pttt)


        detail1_origin = action.get_text(var_stx_app.driver_driver, var_stx_app.detail1_origin, time_wait=15)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 56, 3, detail1_origin)


        detail1_phone = action.get_text(var_stx_app.driver_driver, var_stx_app.detail1_phone, time_wait=15)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 57, 3, detail1_phone)

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Cuốc fixed theo AppKH - Xem chi tiết",
                                                            var_stx_app.note, "Ghi chú", "_Cuoc_Fixed_XemChiTiet.png")




    def detail_if(self, code, eventname, result, row, name):
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row, 2))
        overview = normalize_text(overview)

        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row, 3))
        detail = normalize_text(detail)


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Cuốc fixed theo AppKH - Xem chi tiết")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info(name+"(Thông tin cuốc): {}".format(overview))
        var_stx_app.logging.info(name+"(Xem chi tiết): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Thông tin cuốc: {}\nXem chi tiết: {}".format(overview, detail))
        if detail in overview:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def detail_if_cv(self, code, eventname, result, row, name):
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row, 2))
        overview = " ".join(overview.split()).lower()
        overview = ''.join(
            ch for ch in unicodedata.normalize('NFKD', overview)
            if not unicodedata.combining(ch))


        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row, 3))
        detail = normalize_text(detail)
        detail = " ".join(detail.split()).lower()
        detail = ''.join(
            ch for ch in unicodedata.normalize('NFKD', detail)
            if not unicodedata.combining(ch))


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Cuốc fixed theo AppKH - Xem chi tiết")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info(name+"(Thông tin cuốc): {}".format(overview))
        var_stx_app.logging.info(name+"(Xem chi tiết): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Thông tin cuốc: {}\nXem chi tiết: {}".format(overview, detail))
        if detail == overview:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def detail_other(self, code, eventname, result, row, name):
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row, 3))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Cuốc fixed theo AppKH - Xem chi tiết")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info(name+"(Xem chi tiết): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, name+"(Xem chi tiết): {}".format(detail))
        if detail != "None":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def detail_note(self, code, eventname, result):
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.PTTT, time_wait=1)
        except:
            waiting_for_a_passenger.order_fixed_see_detail(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.see_detail, time_wait=15)
        note = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_note, time_wait=15)
        action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=15)

        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 60, 3))
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Xem chi tiết: {}\nHộp thoại ghi chú: {}".format(note, detail))
            var_stx_app.logging.info("Xem chi tiết: {}\nHộp thoại ghi chú: {}".format(note, detail))
            if note == detail:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_Cuoc_Fixed_XemChiTiet_GhiChu.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_Cuoc_Fixed_XemChiTiet_GhiChu.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_Cuoc_Fixed_XemChiTiet_GhiChu.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_Cuoc_Fixed_XemChiTiet_GhiChu.png")



    def detail_cancel(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.PTTT, time_wait=1)
        except:
            waiting_for_a_passenger.order_fixed_see_detail(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.CANCEL, time_wait=15)

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.reasson_other, time_wait=3)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.reasson_other1, time_wait=10)
            action.send_keys(var_stx_app.driver_driver, var_stx_app.reasson_other1_input, "Trường test huy cuốc lái xe", time_wait=10)
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=10)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_detail_cancel, time_wait=15)
        except:
            pass


        module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH",
                                              var_stx_app.check_detail_cancel, "", "_Cuoc_Fixed_HuyBo.png")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=3)
        except:
            pass
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.igree, time_wait=3)
        except:
            pass

        # try:
        #     var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.order_car_back).click()
        #     time.sleep(2.5)
        # except:
        #     pass



    def order_fixed_location_vehicle(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.payment_app, time_wait=3)
            RECEIVE_APP(25)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.CANCEL, time_wait=2)
        except:
            waiting_for_a_passenger.order_fixed_receive_app(self, "", "", "")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.location_vehicle, time_wait=3)
            time.sleep(2)

        except:
            action.click(var_stx_app.driver_driver, var_stx_app.location_customer, time_wait=3)
            time.sleep(1)
            action.click(var_stx_app.driver_driver, var_stx_app.location_vehicle, time_wait=3)

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - Vị trí",
                                                      var_stx_app.location_customer, "Vị trí khách", "_Cuoc_Fixed_ViTriXe.png")



    def order_fixed_location_customer(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.CANCEL, time_wait=2)
        except:
            waiting_for_a_passenger.order_fixed_receive_app(self, "", "", "")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.location_customer, time_wait=3)
            time.sleep(2)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.location_vehicle, time_wait=3)
            time.sleep(1)
            action.click(var_stx_app.driver_driver, var_stx_app.location_customer, time_wait=3)

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result,
                                                      "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - Vị trí",
                                                      var_stx_app.location_vehicle, "Vị trí xe", "_Cuoc_Fixed_ViTriKhach.png")



    def order_fixed_see_customer(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.CANCEL, time_wait=1)
        except:
            waiting_for_a_passenger.order_fixed_receive_app(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.SEE_CUSTOMER, time_wait=15)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.call_customer, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - Xác nhận tiền thanh toán",
                                                            var_stx_app.call_customer, "Gọi khách hàng:", "_XacNhanTienThanhToan.png")










    def check_confirm_pay_money_confirm(self, code, eventname, result, path_check, name_image):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.call_customer, time_wait=1)
        except:
            waiting_for_a_passenger.order_fixed_see_customer(self, "", "", "")

        module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - G7 Taxi Hà Nội",
                                                            path_check, "", name_image)



    def electronic_contract(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.call_customer, time_wait=1)
        except:
            waiting_for_a_passenger.order_fixed_see_customer(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.electronic_contract1, time_wait=15)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_electronic_contract, time_wait=30)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - G7 Taxi Hà Nội",
                                              var_stx_app.check_electronic_contract, "HỢP ĐỒNG VẬN CHUYỂN HÀNH KHÁCH", "_Fixed_HopDongDienTu.png")

        try:
            var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.icon_back1).click()
            time.sleep(2)
        except:
            pass



    def wrong_customer(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.call_customer, time_wait=1)
        except:
            waiting_for_a_passenger.order_fixed_see_customer(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.WRONG_CUSTOMER, time_wait=15)
        action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=15)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_wrong_customer, time_wait=1)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - G7 Taxi Hà Nội",
                                              var_stx_app.check_wrong_customer, "Thông tin nhầm khách đã được gửi lên điều hành", "_Fixed_NhamKhach.png")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=5)
            time.sleep(2)
        except:
            pass



    def wrong_customer_return_guests(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.RETURN_GUESTS, time_wait=3)
        except:
            waiting_for_a_passenger.wrong_customer(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.RETURN_GUESTS, time_wait=15)
        action.click(var_stx_app.driver_driver, var_stx_app.CASH, time_wait=15)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=5)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.money2, time_wait=5)
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=5)
            action.click(var_stx_app.driver_driver, var_stx_app.payment, time_wait=5)
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=5)
            except:
                pass

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - G7 Taxi Hà Nội",
                                                            var_stx_app.home_page, "Trang chủ", "_Fixed_NhamKhach_TraKhach.png")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.igree, time_wait=5)
            time.sleep(2)
        except:
            pass

        # try:
        #     var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.order_car_back).click()
        #     time.sleep(2.5)
        # except:
        #     pass



    def return_guests(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.payment_app, time_wait=3)
            RECEIVE_APP(25)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.CANCEL, time_wait=2)
        except:
            waiting_for_a_passenger.order_fixed_receive_app(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.SEE_CUSTOMER, time_wait=15)
        action.click(var_stx_app.driver_driver, var_stx_app.RETURN_GUESTS, time_wait=15)
        action.click(var_stx_app.driver_driver, var_stx_app.CASH, time_wait=15)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.end1, time_wait=5)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - G7 Taxi Hà Nội",
                                                            var_stx_app.home_page, "Trang chủ", "_Fixed_TraKhach.png")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.CANCEL, time_wait=5)
            time.sleep(2)
        except:
            pass







class notification:


    def notification(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.notification, time_wait=1)
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        action.click(var_stx_app.driver_driver, var_stx_app.notification, time_wait=15)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.personal, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result,
                                                      "Thông báo(Lái xe)",
                                                      var_stx_app.personal, "Cá nhân", "_ThongBao.png")



    def notification_search(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.personal, time_wait=1)
        except:
            notification.notification(self, "", "", "")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.notification_search_icon, time_wait=15)
            notification_fromday = action.get_text(var_stx_app.driver_driver, var_stx_app.notification_fromday, time_wait=5)
        except:
            n = 0
            while (n < 60):
                n = n + 1
                try:
                    action.click(var_stx_app.driver_driver, var_stx_app.notification_search_icon, time_wait=1)
                    notification_fromday = action.get_text(var_stx_app.driver_driver, var_stx_app.notification_fromday, time_wait=2)
                    break
                except:
                    time.sleep(1)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Thông báo(Lái xe)")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            notification_fromday = action.get_text(var_stx_app.driver_driver, var_stx_app.notification_fromday, time_wait=15)
            notification_today = action.get_text(var_stx_app.driver_driver, var_stx_app.notification_today, time_wait=15)
            notification_input = action.get_text(var_stx_app.driver_driver, var_stx_app.notification_input, time_wait=15)

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Từ ngày: {}\nĐến ngày: {}\ninput: {}".
                                           format(notification_fromday, notification_today, notification_input))
            var_stx_app.logging.info("Từ ngày: {}\nĐến ngày: {}\ninput: {}".
                                           format(notification_fromday, notification_today, notification_input))

            if (notification_fromday != "") and (notification_today != "") and (notification_input == "Nhập tiêu đề tìm kiếm"):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_ThongBao_TimKiem.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_ThongBao_TimKiem.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_ThongBao_TimKiem.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_ThongBao_TimKiem.png")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.notification_search_icon, time_wait=3)
            time.sleep(2)
        except:
            pass



    def check_info_notification(self, code, eventname, result, path_button, type, name_image):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.personal, time_wait=1)
        except:
            notification.notification_search(self, "", "", "")

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.notification_name, time_wait=1)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.notification_back, time_wait=2)
            action.click(var_stx_app.driver_driver, var_stx_app.notification, time_wait=10)
            time.sleep(2)

        action.click(var_stx_app.driver_driver, path_button, time_wait=15)
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Thông báo(Lái xe)")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        if type == "0":
            try:
                notification_name = action.get_text(var_stx_app.driver_driver, var_stx_app.notification_name, time_wait=10)
                notification_date = action.get_text(var_stx_app.driver_driver, var_stx_app.notification_date, time_wait=10)
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Tên thông báo: {}\nNgày thông báo: {}". format(notification_name, notification_date))
                var_stx_app.logging.info("Tên thông báo: {}\nNgày thông báo: {}".format(notification_name, notification_date))

                if (notification_name != "") and (notification_date != ""):
                    var_stx_app.logging.info("True")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    var_stx_app.logging.info("False")
                    var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)
            except:
                var_stx_app.logging.info("False")
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)

        if type == "1":
            try:
                not_result = action.get_text(var_stx_app.driver_driver, var_stx_app.not_result, time_wait=10)
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, not_result)
                var_stx_app.logging.info(not_result)
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            except:
                notification_name = action.get_text(var_stx_app.driver_driver, var_stx_app.notification_name, time_wait=10)
                notification_date = action.get_text(var_stx_app.driver_driver, var_stx_app.notification_date, time_wait=10)
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Tên thông báo: {}\nNgày thông báo: {}". format(notification_name, notification_date))
                var_stx_app.logging.info("Tên thông báo: {}\nNgày thông báo: {}".format(notification_name, notification_date))

                if (notification_name != "") and (notification_date != ""):
                    var_stx_app.logging.info("True")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    var_stx_app.logging.info("False")
                    var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)



    def check_info_notification_detail(self, code, eventname, result, path_button, name_image):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.personal, time_wait=1)
        except:
            notification.notification_search(self, "", "", "")

        action.click(var_stx_app.driver_driver, path_button, time_wait=10)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.notification_detail, time_wait=10)
        except:
            module_other_stx_app.tap_percent(var_stx_app.driver_driver, 0.5, 0.25)


        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_info_notification_detail, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_driver, code, eventname, result, "Thông báo(Lái xe) - Chi tiết",
                                                            var_stx_app.check_info_notification_detail, "", name_image)

        try:
            not_result = action.get_text(var_stx_app.driver_driver, var_stx_app.not_result, time_wait=1)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, not_result)
        except:
            pass
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.i_readed_back, time_wait=1.5)
            time.sleep(2)
        except:
            pass
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.notification_detail_back, time_wait=1.5)
            time.sleep(2)
        except:
            pass

        if name_image == "_ThongBao_QuanTrong_ChiTiet.png":
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.notification_back1, time_wait=1.5)
                time.sleep(2)
            except:
                pass







class history:


    def history(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.history, time_wait=1)
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        action.click(var_stx_app.driver_driver, var_stx_app.history, time_wait=10)

        text1 = action.get_text(var_stx_app.driver_driver, var_stx_app.check_history1, time_wait=10)
        # text1 = "Lịch sử - 09-30A38981"
        text2 = "Lịch sử - xx-xxxxxxxx"

        pattern = text2

        pattern = pattern.replace("xx", ".+")
        pattern = pattern.replace("x", ".")
        pattern = f"^{pattern}$"

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe)")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, text1)
        if re.match(pattern, text1):
            print("✅ text1 khớp form text2")
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu.png")


        # module_other_stx_app.write_result_text_try_if_in(code, eventname, result, "Lịch sử(Lái xe)",
        #                                       var_stx_app.check_history1, "Lịch sử -", "_LichSu.png")



    def history_calendar(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_history1, time_wait=1)
        except:
            history.history(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.history_calendar, time_wait=15)
        action.click(var_stx_app.driver_driver, var_stx_app.in_30day, time_wait=15)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.history_detail_day, time_wait=5)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=10)
            action.click(var_stx_app.driver_driver, var_stx_app.history, time_wait=10)
            action.click(var_stx_app.driver_driver, var_stx_app.history_calendar, time_wait=15)
            action.click(var_stx_app.driver_driver, var_stx_app.in_30day, time_wait=15)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.history_detail_day, time_wait=10)
        except:
            pass


        module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_driver, code, eventname, result, "Lịch sử(Lái xe) - Tìm kiếm",
                                              var_stx_app.history_detail_day, "", "_LichSu.png")



    def history_detail_check_time_fill(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.history_detail_day, time_wait=1)
        except:
            history.history_calendar(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.history_detail_status_icon, time_wait=15)
        time.sleep(2)
        var_stx_app.driver_driver.press_keycode(20)  # 20 = KEYCODE_DPAD_DOWN
        time.sleep(1)
        var_stx_app.driver_driver.press_keycode(66)  # 66 = KEYCODE_ENTER
        time.sleep(3)

        # var_stx_app.driver_driver.tap([(100, 500)])
        # time.sleep(2.5)

        from datetime import datetime, timedelta

        fmt = "%H:%M"
        now = datetime.now()
        time_n = None

        n = 0
        while n < 25:
            n += 1
            path_time = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + str(n) + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[2]"
            try:
                time_history = var_stx_app.driver_driver.find_element(By.XPATH, path_time).text  # "HH:MM"
                t = datetime.strptime(time_history, fmt).replace(year=now.year, month=now.month, day=now.day)

                if t < now - timedelta(minutes=20):
                    time_n = t.strftime(fmt)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 38, 2, path_time)
                    break
            except:
                pass

        if time_n:
            print("time_n =", time_n)
        else:
            print("Không có thời gian nào < hiện tại 30 phút.")


        path_detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 38, 2))
        action.click(var_stx_app.driver_driver, path_detail, time_wait=10)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.detail, time_wait=10)
            module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.5, 0.8, 0.5, 0.2, 1000)
            time.sleep(1)
        except:
            pass

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.invoice_receipt, time_wait=3)
        except:
            module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.5, 0.8, 0.5, 0.2, 1000)
            time.sleep(1)
            action.click(var_stx_app.driver_driver, var_stx_app.invoice_receipt, time_wait=10)



        action.click(var_stx_app.driver_driver, var_stx_app.CODE_QRPAY_link, time_wait=10)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_receipt_invoice_link, time_wait=30)
        except:
            pass


        try:
            action.click(var_stx_app.driver_driver, var_stx_app.receipt_invoice_codehd, time_wait=10)
            time.sleep(2)
        except:
            pass

        module_other_stx_app.write_result_not_displayed_try(var_stx_app.driver_driver, code, eventname, result, "Lịch sử(Lái xe) - QR - Check thời gian hiệu lực",
                                              var_stx_app.path_codehd, "_LichSu_Qr_ThoiGianHieuLuc.png")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.close_tab, time_wait=2)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.CODE_QRPAY_link, time_wait=3)
            var_stx_app.driver_driver.back()
            time.sleep(2)
        except:
            pass

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=2)
            time.sleep(2)
        except:
            pass



    def history_detail_status(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.history_detail_day, time_wait=1)
        except:
            history.history_calendar(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.history_detail_status_icon, time_wait=15)
        time.sleep(2)
        var_stx_app.driver_driver.press_keycode(20)  # 20 = KEYCODE_DPAD_DOWN
        time.sleep(1)
        var_stx_app.driver_driver.press_keycode(66)  # 66 = KEYCODE_ENTER
        time.sleep(3)
        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Lịch sử(Lái xe) - Tìm kiếm",
                                              var_stx_app.history_detail_status, "Hoàn thành", "_LichSu_ChiTiet_TrangThai.png")



    def get_info_history_detail(self, code, eventname, result):
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 65, 2, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 66, 2, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 67, 2, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 68, 2, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 69, 2, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 70, 2, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 2, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 72, 2, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 73, 2, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 74, 2, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 75, 2, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 76, 2, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 77, 2, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 78, 2, "")

        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 65, 3, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 66, 3, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 67, 3, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 68, 3, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 69, 3, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 70, 3, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 3, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 72, 3, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 73, 3, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 74, 3, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 75, 3, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 76, 3, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 77, 3, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 78, 3, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 114, 3, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 115, 3, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 116, 3, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 117, 3, "")

        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.history_detail_day, time_wait=1)
        except:
            history.history_detail_status(self, "", "", "")


        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.overview_history_day, time_wait=2)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.history_calendar, time_wait=5)
            action.click(var_stx_app.driver_driver, var_stx_app.in_30day, time_wait=5)
            time.sleep(2.5)

        overview_history_day = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_history_day, time_wait=10)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 65, 2, overview_history_day)


        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.overview_history_location2a, time_wait=3) #check có dòng thứ 6 không

            try:
                overview_history_time = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_history_time, time_wait=5)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 66, 2, overview_history_time)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 66, 2, "")

            try:
                overview_history_money = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_history_money, time_wait=5)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 67, 2, overview_history_money)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 67, 2, 0)

            try:
                overview_history_origin = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_history_origin, time_wait=5)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 68, 2, overview_history_origin)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 68, 2, "")

            try:
                overview_history_pttt = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_history_pttt, time_wait=5)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 69, 2, overview_history_pttt)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 69, 2, "")

            try:
                overview_history_status = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_history_status, time_wait=5)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 70, 2, overview_history_status)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 70, 2, "")

            try:
                overview_history_note = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_history_note, time_wait=5)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 2, overview_history_note)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 2, "")

            try:
                overview_history_location1a = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_history_location1a, time_wait=5)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 72, 2, overview_history_location1a)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 72, 2, "")

            try:
                overview_history_location2a = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_history_location2a, time_wait=5)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 73, 2, overview_history_location2a)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 73, 2, "")


        except:
            overview_history_time = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_history_time, time_wait=5)
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 66, 2, overview_history_time)

            try:
                overview_history_money = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_history_money, time_wait=5)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 67, 2, overview_history_money)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 67, 2, 0)

            try:
                overview_history_origin1 = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_history_origin1, time_wait=5)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 68, 2, overview_history_origin1)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 68, 2, "")

            try:
                overview_history_pttt1 = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_history_pttt, time_wait=5)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 69, 2, overview_history_pttt1)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 69, 2, "")

            try:
                overview_history_status = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_history_status, time_wait=5)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 70, 2, overview_history_status)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 70, 2, "")

            try:
                overview_history_note1 = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_history_note1, time_wait=5)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 2, overview_history_note1)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 2, "")

            try:
                overview_history_location1b = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_history_location1b, time_wait=5)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 72, 2, overview_history_location1b)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 72, 2, "")

            try:
                overview_history_location2b = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_history_location2b, time_wait=5)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 73, 2, overview_history_location2b)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 73, 2, "")






        #Detail
        print("chuẩn bị xem chi tiết")
        action.click(var_stx_app.driver_driver, var_stx_app.overview_history_time, time_wait=10)
        time.sleep(3.5)
        try:
            print("n1")
            detail_history_drive = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_history_drive, time_wait=5)
        except:
            print("n2")
            action.click(var_stx_app.driver_driver, var_stx_app.overview_history_time, time_wait=10)
            time.sleep(3.5)
        print("đã xem chi tiết")


        try:
            detail_history_drive = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_history_drive, time_wait=2)
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 114, 3, detail_history_drive)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 114, 3, "")

        try:
            detail_history_phone = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_history_phone, time_wait=2)
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 115, 3, detail_history_phone)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 115, 3, "")

        try:
            detail_history_vehicle_number = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_history_vehicle_number, time_wait=2)
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 116, 3, detail_history_vehicle_number)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 116, 3, "")

        try:
            detail_history_star_number = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_history_star_number, time_wait=2)
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 117, 3, detail_history_star_number)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 117, 3, "")

        try:
            detail_history_number_order = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_history_number_order, time_wait=2)
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 118, 3, detail_history_number_order)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 118, 3, "")

        try:
            detail_history_location1 = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_history_location1, time_wait=2)
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 72, 3, detail_history_location1)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 72, 3, "")

        try:
            detail_history_location2 = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_history_location2, time_wait=2)
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 73, 3, detail_history_location2)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 73, 3, "")

        try:
            detail_history_time = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_history_time, time_wait=2)
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 77, 3, detail_history_time)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 77, 3, "")


        try:
            detail_history_pttt = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_history_pttt, time_wait=2)
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 69, 3, detail_history_pttt)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 69, 3, "")

        try:
            detail_history_status = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_history_status, time_wait=2)
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 70, 3, detail_history_status)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 70, 3, "")


        module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.5, 0.8, 0.5, 0.2, 1000)
        time.sleep(1)

        try:
            detail_history_note = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_history_note, time_wait=2)
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 3, detail_history_note)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 3, "")

        # try:
        #     action.wait_for(var_stx_app.driver_driver, var_stx_app.check_detail_history_note, time_wait=2)
        #     detail_history_note = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_history_note_a, time_wait=2)
        #     module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 3, detail_history_note)
        # except:
        #     try:
        #         detail_history_note = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_history_note, time_wait=2)
        #         module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 3, detail_history_note)
        #     except:
        #         try:
        #             detail_history_note1 = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_history_note1, time_wait=2)
        #             module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 3, detail_history_note1)
        #         except:
        #             detail_history_note2 = action.get_text(var_stx_app.driver_driver, var_stx_app.detail_history_note2, time_wait=2)
        #             module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 3, detail_history_note2)


        select_detail("Cước di chuyển", 74)
        select_detail("phụ phí 1", 75)
        select_detail("KH thanh toán", 76)
        select_detail("Khung giờ", 78)


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - Tìm kiếm")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("True")
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")



    def check_info_history_other(self, code, eventname, result, row, column):
        data = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row, column))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - Chi tiết - Thông tin cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("{}".format(data))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "{}".format(data))
        if data != "None":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu_ThongTinCuoc.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu_ThongTinCuoc.png")



    def check_info_history_if(self, code, eventname, result, row1, column1, row2, column2):
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row1, column1))
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row2, column2))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - Chi tiết - Thông tin cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Lịch sử cuốc  : {}".format(overview))
        var_stx_app.logging.info("Thông tin cuốc: {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Lịch sử cuốc  : {}\nThông tin cuốc: {}".format(overview, detail))
        if overview == detail:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu_ThongTinCuoc.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu_ThongTinCuoc.png")



    def check_info_history_hoe_source(self, code, eventname, result):
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 68, 2))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - Chi tiết - Thông tin cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Lịch sử cuốc  : {}".format(overview))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Lịch sử cuốc  : {}".format(overview))
        if overview != "None":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu_ThongTinCuoc_NguonCuoc.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu_ThongTinCuoc_NguonCuoc.png")



    def check_info_history_time(self, code, eventname, result):
        day = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 65, 2))
        time = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 66, 2))
        fulltime = time+"-"+day
        fulltime1 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 77, 3))

        print("time1: {}".format(fulltime))
        print("time2: {}".format(fulltime1))

        dt1 = datetime.strptime(fulltime, "%H:%M-%d-%m-%Y")  # Dùng dấu '-'
        dt2 = datetime.strptime(fulltime1, "%H:%M-%d/%m/%Y")  # Dùng dấu '/'

        # So sánh
        print(dt1 == dt2)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - Chi tiết - Thông tin cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Giờ:Phút          : {}".format(time))
        var_stx_app.logging.info("Ngày - Tháng - Năm: {}".format(day))
        var_stx_app.logging.info("Thời gian         : {}".format(fulltime1))
        var_stx_app.logging.info(fulltime)

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Giờ:Phút          : {}\nNgày - Tháng - Năm: {}\nThời gian         : {}"
                                       .format(time, day, fulltime1))
        if dt1 == dt2:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu_ThongTinCuoc.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu_ThongTinCuoc.png")



    def check_info_history_other1(self, code, eventname, result, row, column):
        data = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row, column))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - Chi tiết - Thông tin cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("{}".format(data))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "{}".format(data))
        if data != "None":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")



    def check_info_history_pay(self, code, eventname, result):
        fee_move = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 74, 3))
        fee_move = ''.join(re.findall(r'\d+', fee_move))
        fee_move = int(fee_move)

        fee = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 75, 3))
        fee = ''.join(re.findall(r'\d+', fee))
        fee = int(fee)


        kh_pay = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 76, 3))
        kh_pay = ''.join(re.findall(r'\d+', kh_pay))
        kh_pay = int(kh_pay)


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - Chi tiết - Thông tin cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Cước di chuyển: {}".format(fee_move))
        var_stx_app.logging.info("Phụ phí       : {}".format(fee))
        var_stx_app.logging.info("KH Thanh toán : {}".format(kh_pay))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Cước di chuyển: {}\nPhụ phí       : {}\nKH Thanh toán : {}"
                                       .format(fee_move, fee, kh_pay))
        print(kh_pay)
        print(type(kh_pay))
        print(fee_move)
        print(type(fee_move))
        print(fee)
        print(type(fee))
        if kh_pay == (fee_move + fee):
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu_ThongTinCuoc.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu_ThongTinCuoc.png")



    def history_detail_qr(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.status, time_wait=1)
        except:
            history.get_info_history_detail(self, "", "", "")


        try:
            action.click(var_stx_app.driver_driver, var_stx_app.invoice_receipt, time_wait=5)
        except:
            module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.5, 0.8, 0.5, 0.2, 1000)
            time.sleep(1)
            action.click(var_stx_app.driver_driver, var_stx_app.invoice_receipt, time_wait=5)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_history_detail_qr, time_wait=10)
        except:
            pass

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - Thông tin cuốc - Hóa đơn/Biên lai")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.check_history_detail_qr).is_displayed()
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        except NoSuchElementException:
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu_ThongTinCuoc_HoaDonBienLai.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu_ThongTinCuoc_HoaDonBienLai.png")

        var_stx_app.driver_driver.back()
        time.sleep(2)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_history_detail_qr, time_wait=2)
            var_stx_app.driver_driver.back()
            time.sleep(2)
        except:
            pass



    def history_detail_qr1(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.status, time_wait=1)
        except:
            history.get_info_history_detail(self, "", "", "")


        try:
            action.click(var_stx_app.driver_driver, var_stx_app.CODE_QRPAY, time_wait=5)
        except:
            module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.5, 0.8, 0.5, 0.2, 1000)
            time.sleep(1)
            action.click(var_stx_app.driver_driver, var_stx_app.CODE_QRPAY, time_wait=5)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_history_detail_qr, time_wait=10)
        except:
            pass

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - Thông tin cuốc, Mã QR")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.check_history_detail_qr).is_displayed()
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        except NoSuchElementException:
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu_ThongTinCuoc_MaQrPAY.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu_ThongTinCuoc_MaQrPAY.png")

        var_stx_app.driver_driver.back()
        time.sleep(2)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_history_detail_qr, time_wait=2)
            var_stx_app.driver_driver.back()
            time.sleep(2)
        except:
            pass

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=3)
            time.sleep(2)
        except:
            pass



    def check_fee(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 79, 2, "")
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 79, 3, "")
        history.history_calendar(self, "", "", "")


        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.overview_history_day, time_wait=1)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.history_calendar, time_wait=10)
            action.click(var_stx_app.driver_driver, var_stx_app.in_30day, time_wait=10)
            time.sleep(2.5)



        n = 0
        while (n < 25):
            n = n + 1
            try:
                overview_surcharge = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_surcharge1, time_wait=1)
                print(overview_surcharge)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 79, 2, overview_surcharge)
                action.click(var_stx_app.driver_driver, var_stx_app.overview_surcharge1, time_wait=2)
                time.sleep(2.5)
                break
            except:
                pass
            try:
                overview_surcharge = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_surcharge2, time_wait=1)
                print(overview_surcharge)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 79, 2, overview_surcharge)
                action.click(var_stx_app.driver_driver, var_stx_app.overview_surcharge2, time_wait=2)
                time.sleep(2.5)
                break
            except:
                pass
            try:
                overview_surcharge = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_surcharge3, time_wait=1)
                print(overview_surcharge)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 79, 2, overview_surcharge)
                action.click(var_stx_app.driver_driver, var_stx_app.overview_surcharge3, time_wait=2)
                time.sleep(2.5)
                break
            except:
                pass
            try:
                overview_surcharge = action.get_text(var_stx_app.driver_driver, var_stx_app.overview_surcharge4, time_wait=1)
                print(overview_surcharge)
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 79, 2, overview_surcharge)
                action.click(var_stx_app.driver_driver, var_stx_app.overview_surcharge4, time_wait=2)
                time.sleep(2.5)
                break
            except:
                pass

            module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.5, 0.8, 0.5, 0.2, 1000)
            time.sleep(1)


        module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.5, 0.8, 0.5, 0.2, 1000)
        # var_stx_app.driver_driver.swipe(450, 1250, 450, 450, 1000)
        time.sleep(1)
        select_detail("phụ phí 1", 79)

        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 79, 2))
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 79, 3))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - Chi tiết - Thông tin cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Lịch sử cuốc  : {}".format(overview))
        var_stx_app.logging.info("Thông tin cuốc: {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Lịch sử cuốc  : {}\nThông tin cuốc: {}".format(overview, detail))
        if overview == detail:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu_ThongTinCuoc.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu_ThongTinCuoc.png")


        try:
            action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=2)
            time.sleep(2)
        except:
            pass



    def statistical(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=1)
        except:
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.history1_back, time_wait=1)
                time.sleep(2.5)
            except:
                pass
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=1)
                time.sleep(2.5)
            except:
                pass
            history.history_calendar(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.statistical, time_wait=15)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_statistical, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Lịch sử(Lái xe) - THỐNG KÊ",
                                                      var_stx_app.check_statistical, "Tổng cuốc", "_LichSu_ThongKe.png")



    def statistical_sum_order(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.statistical1, time_wait=1)
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_statistical, time_wait=1)
        except:
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.history1_back, time_wait=1)
                time.sleep(2.5)
            except:
                pass
            try:
                action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=1)
                time.sleep(2.5)
            except:
                pass
            history.history_calendar(self, "", "", "")
            history.statistical(self, "", "", "")


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - THỐNG KÊ")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            statistical1 = action.get_text(var_stx_app.driver_driver, var_stx_app.statistical1, time_wait=5)
            statistical2 = action.get_text(var_stx_app.driver_driver, var_stx_app.statistical2, time_wait=5)
            statistical3 = action.get_text(var_stx_app.driver_driver, var_stx_app.statistical3, time_wait=5)
            statistical4 = action.get_text(var_stx_app.driver_driver, var_stx_app.statistical4, time_wait=5)
            statistical5 = action.get_text(var_stx_app.driver_driver, var_stx_app.statistical5, time_wait=5)
            statistical6 = action.get_text(var_stx_app.driver_driver, var_stx_app.statistical6, time_wait=5)
            statistical_sum = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.statistical_sum).text

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Hoàn thành: {}\nQuá giờ không nhận: {}\nTừ chối: {}\nHủy: {}"
                                                                                            "\nNhầm khách: {}\nKhông được chọn: {}\nTổng cuốc: {}"
                                           .format(statistical1, statistical2, statistical3, statistical4, statistical5, statistical6, statistical_sum))
            var_stx_app.logging.info("Hoàn thành: {}\nQuá giờ không nhận: {}\nTừ chối: {}\nHủy: {}"
                                            "\nNhầm khách: {}\nKhông được chọn: {}\nTổng cuốc: {}"
                                           .format(statistical1, statistical2, statistical3, statistical4, statistical5, statistical6, statistical_sum))

            if (int(statistical1) + int(statistical2) + int(statistical3) + int(statistical4) + int(statistical5) + int(statistical6)) == int(statistical_sum):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu_ThongKe_TongCuoc.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu_ThongKe_TongCuoc.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu_ThongKe_TongCuoc.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu_ThongKe_TongCuoc.png")



    def check_statistical_other(self, code, eventname, result, path_check, name_image):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_statistical, time_wait=1)
        except:
            history.statistical(self, "", "", "")


        module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_driver, code, eventname, result, "Lịch sử(Lái xe) - THỐNG KÊ",
                                              path_check, "", name_image)

        if name_image == "_LichSu_ThongKe_KhongDuocChon.png":
            action.click(var_stx_app.driver_driver, var_stx_app.history1_back, time_wait=2)
            time.sleep(2.5)







class account_wallet:


    def account_wallet(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        var_stx_app.driver_driver.implicitly_wait(5)



        try:
            var_stx_app.driver_driver.implicitly_wait(0.3)
            var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.homepage).click()
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.icon_dash_3).click()
        time.sleep(2)
        var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.account_wallet).click()
        time.sleep(2)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Ví tài khoản(Lái xe)",
                                              var_stx_app.check_account_wallet, "Ví tài khoản", "_ViTaiKhoan.png")



    def account_wallet_calendar(self, code, eventname, result):
        var_stx_app.driver_driver.implicitly_wait(5)
        try:
            var_stx_app.driver_driver.implicitly_wait(0.3)
            var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.driver_driver_g7).click()
            time.sleep(3)
        except:
            pass


        try:
            var_stx_app.driver_driver.implicitly_wait(0.3)
            var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.check_account_wallet)
        except:
            account_wallet.account_wallet(self, "", "", "")

        var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.account_wallet_calendar).click()
        time.sleep(2)
        var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.in_30day).click()
        time.sleep(1)
        wait = WebDriverWait(var_stx_app.driver_driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.account_wallet_balance2)))

        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Ví tài khoản(Lái xe)",
                                              var_stx_app.account_wallet_balance2, "", "_ViTaiKhoan_Loc.png")
        time.sleep(1)



    def check_info_account_wallet_other(self, code, eventname, result, path_check, name_image):
        var_stx_app.driver_driver.implicitly_wait(5)
        try:
            var_stx_app.driver_driver.implicitly_wait(0.3)
            var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.driver_driver_g7).click()
            time.sleep(3)
        except:
            pass


        try:
            var_stx_app.driver_driver.implicitly_wait(0.3)
            var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.account_wallet_balance2)
        except:
            account_wallet.account_wallet_calendar(self, "", "", "")

        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Ví tài khoản(Lái xe) - Check thông tin",
                                              path_check, "", name_image)


        if name_image == "_ViTaiKhoan_GhiChu.png":
            var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.account_wallet_back).click()
            time.sleep(2.5)





class cash_wallet:


    def cash_wallet(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=1)
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=10)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.cash_wallet1, time_wait=5)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=10)
            action.click(var_stx_app.driver_driver, var_stx_app.cash_wallet1, time_wait=5)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_cash_wallet, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Ví tiền mặt(Lái xe)",
                                              var_stx_app.check_cash_wallet, "Ví tiền mặt", "_ViTienMat.png")



    def cash_wallet_calendar(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_cash_wallet, time_wait=1)
        except:
            cash_wallet.cash_wallet(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.cash_wallet_calendar, time_wait=15)
        action.click(var_stx_app.driver_driver, var_stx_app.in_30day, time_wait=15)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.cash_wallet_balance1, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_driver, code, eventname, result, "Ví tiền mặt(Lái xe)",
                                              var_stx_app.cash_wallet_balance1, "", "_ViTienMat_Loc.png")



    def cash_wallet_transfer_money(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.cash_wallet_balance2, time_wait=1)
        except:
            cash_wallet.cash_wallet_calendar(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.TRANSFER_MONEY, time_wait=10)
        action.clear(var_stx_app.driver_driver, var_stx_app.TRANSFER_MONEY_input, time_wait=10)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.TRANSFER_MONEY_input, "10000", time_wait=10)
        action.click(var_stx_app.driver_driver, var_stx_app.CONFIRM_TRANSFER_MONEY, time_wait=10)
        action.click(var_stx_app.driver_driver, var_stx_app.cash_confirm, time_wait=10)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.cash_wallet_money, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Ví tiền mặt(Lái xe) - Chuyển tiền",
                                              var_stx_app.cash_wallet_money, ": 10.000 ₫", "_ViTienMat_ChuyenTien.png")

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.CONFIRM_TRANSFER_MONEY, time_wait=1)
            action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=10)
            time.sleep(2.5)
        except:
            pass



    def check_info_cash_wallet_other(self, code, eventname, result, path_check, name_image):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.cash_wallet_money, time_wait=1)
        except:
            cash_wallet.cash_wallet_calendar(self, "", "", "")


        module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_driver, code, eventname, result, "Ví tin mặt(Lái xe) - Check thông tin",
                                              path_check, "", name_image)

        if name_image == "_ViTienMat_GhiChu.png":
            var_stx_app.reset_app(var_stx_app.driver_driver)





class trip_payment:


    def trip_payment(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=1)
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=10)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.trip_payment1, time_wait=5)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=10)
            action.click(var_stx_app.driver_driver, var_stx_app.trip_payment1, time_wait=5)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_trip_payment, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Thanh toán chuyến đi(Lái xe)",
                                                            var_stx_app.check_trip_payment, "Thanh toán chuyến đi", "_ThanhToanChuyenDi.png")



    def trip_payment_address(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.qr_drive, time_wait=1)
        except:
            trip_payment.trip_payment(self, "", "", "")

        module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_driver, code, eventname, result, "Thanh toán chuyến đi(Lái xe)",
                                                            var_stx_app.trip_payment_address, "", "_ThanhToanChuyenDi_DiaChi.png")




    def trip_payment_qr_drive(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.qr_drive, time_wait=1)
        except:
            trip_payment.trip_payment(self, "", "", "")


        action.click(var_stx_app.driver_driver, var_stx_app.fill_pay_money_input, time_wait=10)
        action.clear(var_stx_app.driver_driver, var_stx_app.trip_payment_input1, time_wait=10)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.trip_payment_input1, "25000", time_wait=10)
        action.click(var_stx_app.driver_driver, var_stx_app.continue2, time_wait=10)
        action.click(var_stx_app.driver_driver, var_stx_app.qr_drive, time_wait=10)
        action.click(var_stx_app.driver_driver, var_stx_app.payment, time_wait=10)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_trip_payment_qr_drive, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Thanh toán chuyến đi(Lái xe)",
                                              var_stx_app.check_trip_payment_qr_drive, "25.000 ₫", "_ThanhToanChuyenDi_QRLaiXe.png")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=2)
            time.sleep(2)
        except:
            pass




    def trip_payment_qr_customer(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.qr_customer, time_wait=1)
        except:
            trip_payment.trip_payment(self, "", "", "")


        action.click(var_stx_app.driver_driver, var_stx_app.fill_pay_money_input, time_wait=10)
        action.clear(var_stx_app.driver_driver, var_stx_app.trip_payment_input1, time_wait=10)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.trip_payment_input1, "35000", time_wait=10)
        action.click(var_stx_app.driver_driver, var_stx_app.continue2, time_wait=10)
        action.click(var_stx_app.driver_driver, var_stx_app.qr_customer, time_wait=10)
        action.click(var_stx_app.driver_driver, var_stx_app.payment, time_wait=10)
        action.click(var_stx_app.driver_driver, var_stx_app.FILL_CODE_CARD, time_wait=10)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.FILL_CODE_CARD_INPUT, "8880999016579311")
        action.click(var_stx_app.driver_driver, var_stx_app.confirm1, time_wait=10)
        action.click(var_stx_app.driver_driver, var_stx_app.PAY_CARD, time_wait=10)

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.check_trip_payment_qr_customer, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result,
                                                      "Thanh toán chuyến đi(Lái xe)",
                                                      var_stx_app.check_trip_payment_qr_customer,
                                                      "Thanh toán qua thẻ thành công",
                                                      "_ThanhToanChuyenDi_QRKhachHang.png")
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=2)
            var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2)
        except:
            pass




class vnpay_wallet:


    def vnpay_wallet(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=1)
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=10)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.vnpay_wallet1, time_wait=5)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=10)
            action.click(var_stx_app.driver_driver, var_stx_app.vnpay_wallet1, time_wait=5)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_vnpay_wallet, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Ví VNPAY(Lái xe)",
                                              var_stx_app.check_vnpay_wallet, "Liên kết Ví", "_ViVNPay.png")



    def vnpay_wallet_link(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_vnpay_wallet, time_wait=1)
        except:
            vnpay_wallet.vnpay_wallet(self, "", "", "")

        name = action.get_text(var_stx_app.driver_driver, var_stx_app.vnpay_wallet_name_input, time_wait=15)
        password = action.get_text(var_stx_app.driver_driver, var_stx_app.vnpay_wallet_password_input, time_wait=15)

        action.clear(var_stx_app.driver_driver, var_stx_app.vnpay_wallet_name_input, time_wait=15)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.vnpay_wallet_name_input, name)

        action.clear(var_stx_app.driver_driver, var_stx_app.vnpay_wallet_password_input)
        action.send_keys(var_stx_app.driver_driver, var_stx_app.vnpay_wallet_password_input, password)

        action.click(var_stx_app.driver_driver, var_stx_app.confirm1)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_vnpay_wallet_link, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_driver, code, eventname, result, "Ví VNPAY(Lái xe)",
                                              var_stx_app.check_vnpay_wallet_link, "Có lỗi khi liên kết tài khoản VNPAY", "_ViVNPay_LienKet.png")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=5)
            action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=5)
            time.sleep(2.5)
        except:
            pass





class setting:



    def setting(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=1)
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.setting1, time_wait=5)
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_setting, time_wait=5)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.setting1, time_wait=5)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_setting, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Cài đặt(Lái xe)",
                                                            var_stx_app.check_setting, "Thiết lập khác", "_CaiDat.png")



    def setting_vesion(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_setting, time_wait=1)
        except:
            setting.setting(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.setting_vesion, time_wait=10)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_setting_vesion, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if_in(var_stx_app.driver_driver, code, eventname, result, "Cài đặt - (Lái xe)",
                                              var_stx_app.check_setting_vesion, "là phiên bản mới nhất", "_CaiDat_PhienBan.png")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=3)
            time.sleep(2)
        except:
            pass



    def setting_checkbox(self, code, eventname, result, button, name_image):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_setting, time_wait=1)
        except:
            setting.setting(self, "", "", "")

        try:
            action.click(var_stx_app.driver_driver, f"//*[@text='{button}']", time_wait=2)
        except:
            module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.5, 0.8, 0.5, 0.2, 1000)
            action.click(var_stx_app.driver_driver, f"//*[@text='{button}']", time_wait=3)
        time.sleep(1)

        module_other_stx_app.write_result_displayed_try(var_stx_app.driver_driver, code, eventname, result, "Cài đặt - (Lái xe)",
                                              f"//*[@text='{button}']", name_image)
        action.click(var_stx_app.driver_driver, f"//*[@text='{button}']", time_wait=2)
        time.sleep(1)


    def setting_blu(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_setting, time_wait=1)
        except:
            setting.setting(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.setting_blu, time_wait=5)

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.ALLOW, time_wait=3)
            time.sleep(2)
        except:
            pass


        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_setting_blu, time_wait=20)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Cài đặt - (Lái xe)",
                                              var_stx_app.check_setting_blu, "Đang tìm kiếm thiết bị bật bluetooth", "_CaiDat_Bluetooth.png")
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.skip, time_wait=20)
            time.sleep(2)
        except:
            pass
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.skip, time_wait=2)
            time.sleep(2)
        except:
            pass
        action.wait_for(var_stx_app.driver_driver, var_stx_app.NOT_ALLOW, time_wait=20)
        action.wait_for(var_stx_app.driver_driver, var_stx_app.ALLOW, time_wait=20)
        var_stx_app.driver_driver.back()
        time.sleep(2)



    def setting_sync(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_setting, time_wait=1)
            print("n1")
        except:
            setting.setting(self, "", "", "")
            print("n2")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.setting_sync, time_wait=5)
        except:
            setting.setting(self, "", "", "")
            module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.5, 0.2, 0.5, 0.8, 1000)
            action.click(var_stx_app.driver_driver, var_stx_app.setting_sync, time_wait=10)

        try:
            text = action.get_text(var_stx_app.driver_driver, var_stx_app.check_setting_sync, time_wait=20)
            print(f"Text: {text}")
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Cài đặt - (Lái xe)",
                                              var_stx_app.check_setting_sync, "Dữ liệu đã đồng bộ thành công, Khởi động lại ứng dụng để cập nhật", "_CaiDat_Dongbo.png")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.igree, time_wait=5)
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=20)
        except:
            pass

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.login_buttonlogin1, time_wait=1)
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=20)
        except:
            pass

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.setting1, time_wait=1)
            time.sleep(2)
        except:
            pass



    def setting_send_error(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_setting, time_wait=1)
        except:
            setting.setting(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.setting_send_error, time_wait=10)
        wait_toast_message(var_stx_app.driver_driver, 15)

        # message = wait_toast_message_click(var_stx_app.driver_driver, var_stx_app.setting_send_error, 7)
        # print(message)
        module_other_stx_app.write_result_text_try_if_toast(var_stx_app.driver_driver, code, eventname, result, "Cài đặt - (Lái xe)",
                                                            "", "Gửi báo cáo lỗi thành công.", "_CaiDat_GuiBaoCaoLoi.png")



    def setting_change_size_word(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            print("n0")
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_setting, time_wait=1)
            print("n1")
        except:
            print("n2")
            setting.setting(self, "", "", "")
            print("n3")
        module_other_stx_app.swipe_percent(var_stx_app.driver_driver, 0.5, 0.8, 0.5, 0.2, 1000)
        time.sleep(1)
        print("n4")
        message = wait_toast_message_click2(var_stx_app.driver_driver, var_stx_app.setting_change_size_word, var_stx_app.confirm1, 7)
        print(message)
        module_other_stx_app.write_result_text_try_if_toast(var_stx_app.driver_driver, code, eventname, result, "Cài đặt - (Lái xe)",
                                                            "", "Không có sự thay đổi nào về font chữ.", "_CaiDat_ThayDoiCoChu.png")
        print("n5")
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=5)
            time.sleep(2)
        except:
            pass
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.setting_change_size_word, time_wait=1)
            var_stx_app.driver_driver.back()
            time.sleep(2)
        except:
            pass








class report:


    def report(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=1)
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=10)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.report1, time_wait=5)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=10)
            action.click(var_stx_app.driver_driver, var_stx_app.report1, time_wait=5)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_report, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Cài đặt(Lái xe)",
                                              var_stx_app.check_report, "Báo cáo", "_BaoCao.png")



    def report_violate(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_report, time_wait=1)
        except:
            report.report(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.report_violate, time_wait=15)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_report_violate, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Báo cáo(Lái xe) - Vi phạm",
                                              var_stx_app.check_report_violate, "Lịch sử vi phạm", "_BaoCao_ViPham.png")



    def check_report_violate(self, code, eventname, result, button, path_check, desire, name_image):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_report_violate, time_wait=1)
        except:
            report.report_violate(self, "", "", "")

        action.click(var_stx_app.driver_driver, button, time_wait=10)

        try:
            action.wait_for(var_stx_app.driver_driver, path_check, time_wait=5)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Báo cáo(Lái xe) - Vi phạm",
                                              path_check, desire, name_image)


        if name_image == "_BaoCao_ViPham_ViPham.png":
            action.click(var_stx_app.driver_driver, var_stx_app.report_violate_back, time_wait=5)
            time.sleep(2)



    def check_report_violate_statistical(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_report_violate, time_wait=1)
        except:
            report.report_violate(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.violate_statistical, time_wait=10)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.not_violate, time_wait=4)
            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Báo cáo(Lái xe) - Vi phạm",
                                                  var_stx_app.not_violate, "Bạn không có thống kê vi phạm", "_BaoCao_ViPham_ThongKe.png")
        except:
            var_stx_app.logging.info("--------------")
            var_stx_app.logging.info("Báo cáo(Lái xe) - Vi phạm")
            var_stx_app.logging.info("Mã - " + code)
            var_stx_app.logging.info("Tên sự kiện - " + eventname)
            var_stx_app.logging.info("Kết quả - " + result)
            try:
                violate_type = action.get_text(var_stx_app.driver_driver, var_stx_app.violate_type, time_wait=7)
                violate_violate = action.get_text(var_stx_app.driver_driver, var_stx_app.violate_violate1, time_wait=7)
                violate_sum = action.get_text(var_stx_app.driver_driver, var_stx_app.violate_sum, time_wait=7)

                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f"Loại lỗi: {violate_type}\nVi phạm: {violate_violate}\n"
                                                                                                f"Tổng số lần đã vi phạm: {violate_sum}")
                var_stx_app.logging.info(f"Loại lỗi: {violate_type}\nVi phạm: {violate_violate}\nTổng số lần đã vi phạm: {violate_sum}")
                if (violate_type != "") and (violate_violate != "") and (violate_sum != ""):
                    var_stx_app.logging.info("True")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    var_stx_app.logging.info("False")
                    var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_BaoCao_ViPham_ThongKe.png")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_BaoCao_ViPham_ThongKe.png")
            except:
                var_stx_app.logging.info("False")
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_BaoCao_ViPham_ThongKe.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_BaoCao_ViPham_ThongKe.png")



    def check_report_violate_violate(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_report_violate, time_wait=1)
        except:
            report.report_violate(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.violate_violate, time_wait=10)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.not_result1, time_wait=10)
            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Báo cáo(Lái xe) - Vi phạm",
                                                  var_stx_app.not_result1, "Không có kết quả nào được tìm thấy!", "_BaoCao_ViPham_ViPham.png")#var_stx_app.not_history
        except:
            var_stx_app.logging.info("--------------")
            var_stx_app.logging.info("Báo cáo(Lái xe) - Vi phạm")
            var_stx_app.logging.info("Mã - " + code)
            var_stx_app.logging.info("Tên sự kiện - " + eventname)
            var_stx_app.logging.info("Kết quả - " + result)
            try:
                violate_time = action.get_text(var_stx_app.driver_driver, var_stx_app.violate_time, time_wait=10)
                violate_violate = action.get_text(var_stx_app.driver_driver, var_stx_app.violate_violate2, time_wait=10)
                violate_address = action.get_text(var_stx_app.driver_driver, var_stx_app.violate_address, time_wait=10)

                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f"Thời gian: {violate_time}\nVi phạm: {violate_violate}\n"
                                                                                                f"Địa điểm: {violate_address}")
                var_stx_app.logging.info(f"Thời gian: {violate_time}\nVi phạm: {violate_violate}\n"
                                                                                                f"Địa điểm: {violate_address}")
                if (violate_time != "") and (violate_violate != "") and (violate_address != ""):
                    var_stx_app.logging.info("True")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    var_stx_app.logging.info("False")
                    var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_BaoCao_ViPham_ViPham.png")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_BaoCao_ViPham_ViPham.png")
            except:
                var_stx_app.logging.info("False")
                var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + "_BaoCao_ViPham_ViPham.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_BaoCao_ViPham_ViPham.png")

        action.click(var_stx_app.driver_driver, var_stx_app.report_violate_back, time_wait=10)
        time.sleep(2)



    def report_fee_dam(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_report, time_wait=1)
        except:
            report.report(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.report_fee_dam, time_wait=10)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_report_fee_dam, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Báo cáo(Lái xe) - PhiDam",
                                              var_stx_app.check_report_fee_dam, "Phí đàm", "_BaoCao_PhiDam.png")

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.report_fee_dam_back, time_wait=5)
            action.click(var_stx_app.driver_driver, var_stx_app.report_back, time_wait=5)
            time.sleep(2)
        except:
            pass




    def customer_payment_report(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_report, time_wait=1)
        except:
            report.report(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.customer_payment_report, time_wait=10)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_customer_payment_report, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Báo cáo(Lái xe) - Báo cáo thanh toán cuốc khách",
                                              var_stx_app.check_customer_payment_report, "Báo cáo thanh toán cuốc khách", "_BaoCao_BaoCaoThanhToanCuocKhach.png")



    def customer_payment_report_carlender(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_customer_payment_report, time_wait=1)
        except:
            report.customer_payment_report(self, "", "", "")

        before_fromday = action.get_text(var_stx_app.driver_driver, var_stx_app.before_fromday, time_wait=10)
        action.click(var_stx_app.driver_driver, var_stx_app.carlender_icon, time_wait=10)
        action.click(var_stx_app.driver_driver, var_stx_app.in_30day, time_wait=10)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.before_fromday, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_driver, code, eventname, result, "Báo cáo(Lái xe) - Báo cáo thanh toán cuốc khách",
                                              var_stx_app.before_fromday, before_fromday, "_BaoCao_BaoCaoThanhToanCuocKhach_TuNgayDenNgay.png")


        report_day_mon_year = var_stx_app.driver_driver.find_element(By.XPATH, var_stx_app.report_day_mon_year).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 180, 2, report_day_mon_year)

        n = 0
        while (n < 25):
            n = int(n)
            n = n + 1
            n = str(n)

            report_time = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[2]"
            report_fromday = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView[2]"
            report_today = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.widget.TextView[2]"
            report_paycard = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.widget.TextView[2]"
            report_paycash = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.ViewGroup[2]/android.widget.TextView[2]"
            report_ca = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[5]/android.widget.TextView[2]"
            report_status = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView"

            n = int(n)
            try:
                report_time = action.get_text(var_stx_app.driver_driver, report_time, time_wait=1)
                report_fromday = action.get_text(var_stx_app.driver_driver, report_fromday, time_wait=1)
                report_today = action.get_text(var_stx_app.driver_driver, report_today, time_wait=1)
                report_paycard = action.get_text(var_stx_app.driver_driver, report_paycard, time_wait=1)
                report_paycash = action.get_text(var_stx_app.driver_driver, report_paycash, time_wait=1)
                report_ca = action.get_text(var_stx_app.driver_driver, report_ca, time_wait=1)
                report_status = action.get_text(var_stx_app.driver_driver, report_status, time_wait=1)

                if report_status == "Chưa thanh toán":
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 181, 2, report_time)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 182, 2, report_fromday)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 183, 2, report_today)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 184, 2, report_paycard)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 185, 2, report_paycash)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 186, 2, report_ca)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 187, 2, report_status)
                    break
            except:
                pass



    def check_info_customer_payment_report(self, code, eventname, result, row, name_image):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.report_day_mon_year, time_wait=1)
        except:
            report.customer_payment_report_carlender(self, "", "", "")

        data = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row, 2))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Thẻ thành viên - Lịch sử thẻ")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        if data != "None":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, data)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            var_stx_app.driver_driver.save_screenshot(var_stx_app.imagepath + code + name_image)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)

        if name_image == "BaoCaoThanhToanCuocKhach_TrangThai.png":
            action.click(var_stx_app.driver_driver, var_stx_app.customer_payment_report_back, time_wait=5)
            action.click(var_stx_app.driver_driver, var_stx_app.report_back1, time_wait=5)
            time.sleep(2)






class help:


    def help(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=1)
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=10)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.help1, time_wait=5)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=10)
            action.click(var_stx_app.driver_driver, var_stx_app.help1, time_wait=5)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_help, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result,
                                                      "Trợ giúp(Lái xe)",
                                                      var_stx_app.check_help, "Trợ giúp", "_TroGiup.png")



    def help_comments(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_help, time_wait=1)
        except:
            help.help(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.comment, time_wait=10)
        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_comment1, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Trợ giúp(Lái xe) - Góp ý",
                                              var_stx_app.check_comment1, "Chúng tôi mong muốn nhận góp ý của bạn để hoàn thiện dịch vụ tốt hơn", "_TroGiup_GopY.png")



    def help_comments_sdt(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_comment1, time_wait=1)
        except:
            help.help_comments(self, "", "", "")


        module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_driver, code, eventname, result, "Trợ giúp(Lái xe) - Góp ý",
                                              var_stx_app.help_comments_sdt, "", "_TroGiup_GopY_SDT.png")



    def help_comments_send(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_comment1, time_wait=1)
        except:
            help.help_comments(self, "", "", "")

        end_time = time.time() + 10
        while time.time() < end_time:
            try:
                try:
                    action.click(var_stx_app.driver_driver, var_stx_app.comment, time_wait=2)
                    time.sleep(2.5)
                except:
                    pass
                action.send_keys(var_stx_app.driver_driver, var_stx_app.comment_title_input, "Test chức năng góp ý")
                action.send_keys(var_stx_app.driver_driver, var_stx_app.comment_content_input, "Không")
                action.click(var_stx_app.driver_driver, var_stx_app.send_comment, time_wait=10)
                toast = WebDriverWait(var_stx_app.driver_driver, 0.5).until( EC.presence_of_element_located((By.XPATH, "//android.widget.Toast")))
                message = toast.get_attribute("text")
                print(f"Toast message: {message}")
                module_other_stx_app.write_result_text_try_if_toast(var_stx_app.driver_driver, code, eventname, result,  "Trợ giúp(Lái xe) - Góp ý",
                                                                    "", "Cảm ơn bạn đã gửi góp ý cho chúng tôi","_TroGiup_GopY_GuiGopY.png")
                break
            except:
                time.sleep(0.2)
        print("❌ Không bắt được Toast message")




    def help_comments_help(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_help, time_wait=1)
        except:
            help.help(self, "", "", "")

        action.click(var_stx_app.driver_driver, var_stx_app.help_comments_help, time_wait=10)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_help_comments_help, time_wait=10)
            module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_driver, code, eventname, result, "Trợ giúp(Lái xe) - Góp ý",
                                                  var_stx_app.check_help_comments_help, "", "_TroGiup_GopY_HuongDan.png")
        except:
            module_other_stx_app.write_result_not_displayed_try(var_stx_app.driver_driver, code, eventname, result, "Trợ giúp(Lái xe) - Góp ý",
                                                  var_stx_app.comment, "_TroGiup_GopY_HuongDan1.png")#không còn ở trang trợ giúp

        try:
            action.click(var_stx_app.driver_driver, var_stx_app.close_tab, time_wait=3)
            time.sleep(2.5)
        except:
            pass
        var_stx_app.driver_driver.back()
        time.sleep(2)
        #
        # try:
        #     action.click(var_stx_app.driver_driver, var_stx_app.icon_back1, time_wait=3)
        #     time.sleep(2.5)
        # except:
        #     pass




class end_of_shift:


    def end_of_shift(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_driver)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.home_page, time_wait=1)
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=10)
        try:
            action.click(var_stx_app.driver_driver, var_stx_app.end_of_shift1, time_wait=5)
        except:
            action.click(var_stx_app.driver_driver, var_stx_app.icon_3_gach, time_wait=10)
            action.click(var_stx_app.driver_driver, var_stx_app.end_of_shift1, time_wait=5)

        action.click(var_stx_app.driver_driver, var_stx_app.END_OF_SHIFT, time_wait=10)

        try:
            action.wait_for(var_stx_app.driver_driver, var_stx_app.check_end_of_shift, time_wait=10)
        except:
            pass


        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_driver, code, eventname, result, "Rời ca(Lái xe)",
                                              var_stx_app.check_end_of_shift, "VÀO CA", "_RoiCa.png")

        action.click(var_stx_app.driver_driver, var_stx_app.check_end_of_shift, time_wait=10)
        time.sleep(3)














