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
import random




class info_account:

    def icon_edit(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_account)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7_icon_edit).click()
        time.sleep(2.5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Thông tin tài khoản",
                                                      var_stx_app.check_icon_edit, "Thay đổi tài khoản", "TaiKhoan_IconSua.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.skip).click()
            time.sleep(2)
        except:
            pass


    def check_info_account(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_account)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Thông tin tài khoản")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            info_account_name = var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_account_name).text
            info_account_version = var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_account_version).text
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Tên: {}\n{}".format(info_account_name, info_account_version))
            var_stx_app.logging.info("Tên: {}\n{}".format(info_account_name, info_account_version))
            if (info_account_name != "") and (info_account_version != ""):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "TaiKhoan_ThongTinTaiKhoan.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "TaiKhoan_ThongTinTaiKhoan.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "TaiKhoan_ThongTinTaiKhoan.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "TaiKhoan_ThongTinTaiKhoan.png")


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_account_back).click()
            time.sleep(2)
        except:
            pass




class history_order_car:



    def history_order_car(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_order_car).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.history)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_order_car).click()
            time.sleep(2)

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Lịch sử đặt xe",
                                                      var_stx_app.check_history_order_car, "Lịch sử", "TaiKhoan_LichSuDatXe.png")



    def get_info_history_order_car(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_history_order_car)
        except:
            history_order_car.history_order_car(self, "", "", "")

        #Tổng quan
        try:
            history_overview_date = var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_overview_date).text  #Ngày/tháng/Năm
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 15, 2, history_overview_date)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 15, 2, "")

        try:
            history_overview_type_car = var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_overview_type_car).text  #Loại xe
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 16, 2, history_overview_type_car)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 16, 2, "")

        try:
            history_overview_status = var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_overview_status).text  #Trạng thái
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 17, 2, history_overview_status)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 17, 2, "")

        try:
            history_overview_time = var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_overview_time).text  #Giờ phút
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 18, 2, history_overview_time)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 18, 2, "")

        try:
            history_overview_location_from = var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_overview_location_from).text  #Điểm đón
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 19, 2, history_overview_location_from)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 19, 2, "")

        try:
            history_overview_location_to = var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_overview_location_to).text  #Điểm đến
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 20, 2, history_overview_location_to)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 20, 2, "")

        try:
            history_overview_pttt = var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_overview_pttt).text  #Phương thức thanh toán
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 21, 2, history_overview_pttt)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 21, 2, "")


        #Chi tiết
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.get_info_history_order_car1).click()
        time.sleep(2.5)
        try:
            history_detail_date = var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_detail_date).text  #Ngày/tháng/Năm - Giờ
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 15, 3, history_detail_date)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 15, 3, "")

        try:
            history_detail_type_car = var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_detail_type_car).text  #Loại xe
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 16, 3, history_detail_type_car)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 16, 3, "")

        try:
            history_detail_location_from = var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_detail_location_from).text  #Điểm đón
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 19, 3, history_detail_location_from)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 19, 3, "")

        try:
            history_detail_location_to = var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_detail_location_to).text  #Điểm đến
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 20, 3, history_detail_location_to)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 20, 3, "")

        try:
            history_detail_pttt = var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_detail_pttt).text  #Phương thức thanh toán
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 21, 3, history_detail_pttt)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 21, 3, "")

        try:
            history_detail_km_money = var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_detail_km_money).text  #Km - Số tiền
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 22, 3, history_detail_km_money)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 22, 3, "")

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Lịch sử đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("True")
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")



    def check_info_order_date(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 15, 2))
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 15, 3))
        match = re.search(r"\d{2}/\d{2}/\d{4}", detail)
        date_part = match.group()
        print(date_part)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Lịch sử đặt xe - Thông tin xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Ngày/tháng/Năm(Tổng quan)   : {}".format(overview))
        var_stx_app.logging.info("Ngày/tháng/Năm(Xem chi tiết): {}".format(date_part))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Ngày/tháng/Năm(Tổng quan)   : {}\nNgày/tháng/Năm(Xem chi tiết): {}"
                                       .format(overview, date_part))
        if overview == date_part:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_order_type_vehicle(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 16, 2))
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 16, 3))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Lịch sử đặt xe - Thông tin xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Loại xe(Tổng quan)   : {}".format(overview))
        var_stx_app.logging.info("Loại xe(Xem chi tiết): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Loại xe(Tổng quan)   : {}\nLoại xe(Xem chi tiết): {}"
                                       .format(overview, detail))
        if overview == detail:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_order_status(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 17, 2))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Lịch sử đặt xe - Thông tin xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Trạng thái(Tổng quan)   : {}".format(overview))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Trạng thái(Tổng quan)   : {}"
                                       .format(overview))
        if overview != "None":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_order_time(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 18, 2))
        overview1 = overview[0:5]
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 15, 3))
        detail1 = detail[-5::]


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Lịch sử đặt xe - Thông tin xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Giờ:Phút(Tổng quan)   : {}".format(overview1))
        var_stx_app.logging.info("Giờ:Phút(Xem chi tiết): {}".format(detail1))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Giờ:Phút(Tổng quan)  : {}\nGiờ:Phút(Xem chi tiết): {}"
                                       .format(overview1, detail1))
        print(type(overview1))
        print(overview1)
        print(type(detail1))
        print(detail1)
        if overview1 == detail1:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_order_locationfrom(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 19, 2))
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 19, 3))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Lịch sử đặt xe - Thông tin xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Điểm đón(Tổng quan)   : {}".format(overview))
        var_stx_app.logging.info("Điểm đón(Xem chi tiết): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Điểm đón(Tổng quan)   : {}\nĐiểm đón(Xem chi tiết): {}"
                                       .format(overview, detail))
        if overview == detail:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_order_locationto(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 20, 2))
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 20, 3))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Lịch sử đặt xe - Thông tin xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Điểm đến(Tổng quan)   : {}".format(overview))
        var_stx_app.logging.info("Điểm đến(Xem chi tiết): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Điểm đến(Tổng quan)   : {}\nĐiểm đến(Xem chi tiết): {}"
                                       .format(overview, detail))
        if overview == detail:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_order_pttt(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 21, 2))
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 21, 3))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Lịch sử đặt xe - Thông tin xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Phương thức thanh toán(Tổng quan)   : {}".format(overview))
        var_stx_app.logging.info("Phương thức thanh toán(Xem chi tiết): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Phương thức thanh toán(Tổng quan)   : {}\nPhương thức thanh toán(Xem chi tiết): {}"
                                       .format(overview, detail))
        if overview == detail:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_order_km_money(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 22, 3))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Lịch sử đặt xe - Thông tin xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Km - Số tiền(Chi tiết)   : {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Km - Số tiền(Chi tiết)   : {}"
                                       .format(detail))
        if detail != "None":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def re_order(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        



        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.RE_ORDER)
        except:
            history_order_car.get_info_history_order_car(self, "", "", "")

        var_stx_app.driver.implicitly_wait(3)
        #chi tiết cuốc
        location_from1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_detail_location_from).text
        location_to1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_detail_location_to).text
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CALL_COMPANY)  #GỌI HÃNG
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.RE_ORDER).click()
        time.sleep(1.75)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.ORDER_A_TO_B).click()
        time.sleep(3.5)
        check_location_from2 = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.location_1)))
        location_from2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_1).text
        location_to2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.location_2).text

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Lịch sử đặt xe - Thông tin xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Điểm đón(Chi tiết cuốc): {}\nĐiểm đến(Chi tiết cuốc): {}\nĐiểm đón(Màn đặt xe): {}\nĐiểm đến(Màn đặt xe): {}"
                                           .format(location_from1, location_to1, location_from2, location_to2))
            var_stx_app.logging.info("Điểm đón(Chi tiết cuốc): {}\nĐiểm đến(Chi tiết cuốc): {}\nĐiểm đón(Màn đặt xe): {}\nĐiểm đến(Màn đặt xe): {}"
                                           .format(location_from1, location_to1, location_from2, location_to2))
            if (location_from1 == location_from2) and (location_to1 == location_to2):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "TaiKhoan_LichSuDatXe_Datlai.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "TaiKhoan_LichSuDatXe_Datlai.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "TaiKhoan_LichSuDatXe_Datlai.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "TaiKhoan_LichSuDatXe_Datlai.png")


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_car_back).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_load1)
            var_stx_app.driver.press_keycode(4)
            time.sleep(4)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_load2)
            var_stx_app.driver.press_keycode(4)
            time.sleep(4)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_car_back).click()
            time.sleep(2)
        except:
            pass






class notification:


    def notification(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_account)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification).click()
        time.sleep(2.5)

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Thông báo",
                                                      var_stx_app.check_notification, "Thông báo", "TaiKhoan_ThongBao.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification_back).click()
            time.sleep(2)
        except:
            pass




class membership_card:


    def membership_card(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_account)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.membership_card).click()
        time.sleep(2.5)

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Thẻ thành viên",
                                                      var_stx_app.check_membership_card, "Chạm để phóng to", "TaiKhoan_TheThanhVien.png")


    def check_info_membership_card(self, code, eventname, result, path_check, name_image):
        var_stx_app.driver.implicitly_wait(5)
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.scan_qrcode)
        except:
            membership_card.membership_card(self, "", "", "")

        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Thông tin thẻ",
                                                      path_check, "", name_image)

        if name_image == "TaiKhoan_TheThanhVien_TkChinh.png":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_info_membership_card_iconhide).click()
            time.sleep(3)


    def scan_qrcode(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.scan_qrcode)
        except:
            membership_card.membership_card(self, "", "", "")

        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.scan_qrcode)))
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.scan_qrcode).click()
        time.sleep(2.5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.ALLOW).click()
            time.sleep(2.5)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Quét mã QrCode",
                                                      var_stx_app.check_scan_qrcode, "Quét mã Qr để thanh toán", "TaiKhoan_TheThanhVien_QuetMaQrCode.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.BACK).click()
            time.sleep(2.5)
        except:
            pass


    def reload_the_card(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.scan_qrcode)
        except:
            membership_card.membership_card(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.reload_the_card).click()
        time.sleep(2.5)

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Nạp tiền vào thẻ",
                                                      var_stx_app.check_reload_the_card, "Quý khách nạp tiền vào thẻ thông qua tài khoản:",
                                                      "TaiKhoan_TheThanhVien_NạpTienVaoThe.png")


    def check_info_reload_the_card(self, code, eventname, result, path_name, path_data, desire, name_image):
        var_stx_app.driver.implicitly_wait(5)
        


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_reload_the_card)
        except:
            membership_card.reload_the_card(self, "", "", "")

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Thẻ thành viên - Nạp tiền vào thẻ")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            name = var_stx_app.driver.find_element(By.XPATH, path_name).text
            data = var_stx_app.driver.find_element(By.XPATH, path_data).text
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f"{name} {data}")
            var_stx_app.logging.info(f"{name} {data}")
            if (name == desire) and (data != ""):
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


        # module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Nạp tiền vào thẻ",
        #                                               path_check, "", name_image)


    def check_icon_membership_card(self, code, eventname, result, path_icon, name_image):
        var_stx_app.driver.implicitly_wait(5)
        



        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_reload_the_card)
        except:
            membership_card.reload_the_card(self, "", "", "")


        var_stx_app.driver.find_element(By.XPATH, path_icon).click()
        time.sleep(1.5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.ALLOW).click()
            time.sleep(1.5)
        except:
            pass

        module_other_stx_app.write_result_displayed_try(code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Nạp tiền vào thẻ",
                                                      path_icon, name_image)


    def check_icon_help_membership_card(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        



        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_reload_the_card)
        except:
            membership_card.reload_the_card(self, "", "", "")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_help_membership_card).click()
        except:
            var_stx_app.driver.swipe(350, 800, 350, 500, 1000)
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_help_membership_card).click()
        time.sleep(2.5)
        try:
            wait = WebDriverWait(var_stx_app.driver, 40)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_icon_help_membership_card)))
            time.sleep(1)
        except:
            pass

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Thẻ thành viên - Nạp tiền vào thẻ")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            check_bank = var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_icon_help_membership_card).text
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, check_bank)
            var_stx_app.logging.info(check_bank)
            if check_bank == "Chủ tài khoản  : {{AName}}\n\nSố tài khoản   : {{ANumber}}\n\nNgân hàng    : {{Bank}}\n\n":
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "TheThanhVien_NapTienVaoThe_QuyKhachCanHoTro.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "TheThanhVien_NapTienVaoThe_QuyKhachCanHoTro.png")
            else:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "TheThanhVien_NapTienVaoThe_QuyKhachCanHoTro.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "TheThanhVien_NapTienVaoThe_QuyKhachCanHoTro.png")


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.desc_back).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.scan_qrcode_1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.desc_back).click()
            time.sleep(2)
        except:
            pass


    def donate_money(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        



        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.scan_qrcode)
        except:
            membership_card.membership_card(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.donate_money).click()
        time.sleep(2.5)

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Tặng tiền",
                                                      var_stx_app.check_donate_money, "Chọn số tiền muốn chuyển (VNĐ)",
                                                      "TaiKhoan_TheThanhVien_TangTien.png")


    def give_money_to_others(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        



        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_donate_money)
        except:
            membership_card.donate_money(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.donate_money_500k).click()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.donate_money_vnd_input).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.donate_money_vnd_input).send_keys("10000")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.donate_money_note).send_keys("Trường test tặng tiền")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.donate_money_sdt).send_keys("0977679816")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.check).click()
        time.sleep(2.5)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.donate_money_donate_money).click()
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.donate_money_sdt).clear()
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.donate_money_sdt).send_keys("0911223344")
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check).click()
            time.sleep(2.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.donate_money_donate_money).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        time.sleep(2.5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Tặng tiền",
                                                      var_stx_app.check_give_money_to_others, "Tặng tiền thành công",
                                                      "TheThanhVien_TangTien_TangTienChoNguoiKhac.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2.5)
        except:
            pass


    def history_car(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.scan_qrcode)
        except:
            membership_card.membership_card(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_car).click()
        time.sleep(2.5)

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Lịch sử thẻ",
                                                      var_stx_app.check_history_car, "Lịch sử thẻ",
                                                      "TaiKhoan_TheThanhVien_LichSuThe.png")
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.history_car_status)))
        except:
            pass
        history_car_tkchinh1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_car_tkchinh1).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 23, 2, history_car_tkchinh1)

        n = 0
        while (n < 25):
            n = int(n)
            n = n + 1
            n = str(n)

            history_car_time = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[2]"
            history_car_tkchinh2 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.widget.TextView[2]"
            history_car_tkkm = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.widget.TextView[4]"
            history_car_note = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.widget.TextView[5]"
            history_car_status = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView"
            history_car_tkchinh2_money = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[2]"
            history_car_tkkm_money = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView[2]"
            n = int(n)
            try:
                time1 = var_stx_app.driver.find_element(By.XPATH, history_car_time).text
                tkchinh2 = var_stx_app.driver.find_element(By.XPATH, history_car_tkchinh2).text
                tkkm = var_stx_app.driver.find_element(By.XPATH, history_car_tkkm).text
                note = var_stx_app.driver.find_element(By.XPATH, history_car_note).text
                status = var_stx_app.driver.find_element(By.XPATH, history_car_status).text
                tkchinh2_money = var_stx_app.driver.find_element(By.XPATH, history_car_tkchinh2_money).text
                tkkm_money = var_stx_app.driver.find_element(By.XPATH, history_car_tkkm_money).text

                if status == "Tặng tiền" or status == "Thêm tiền khuyến mại":
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 24, 2, time1)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 25, 2, tkchinh2)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 26, 2, tkkm)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 27, 2, note)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 28, 2, status)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 29, 2, tkchinh2_money)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 30, 2, tkkm_money)
                    break
            except:
                pass


    def check_info_history_car(self, code, eventname, result, row, name_image):
        var_stx_app.driver.implicitly_wait(5)
        


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_car_tkchinh1)
        except:
            membership_card.history_car(self, "", "", "")

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
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + name_image)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)

        if name_image == "TheThanhVien_LichSuThe_TrangThaiTkKm.png":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.desc_back).click()
            time.sleep(2.5)


    def info_pin(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.scan_qrcode)
        except:
            membership_card.membership_card(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_pin).click()
        time.sleep(2.5)

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Thông tin mã PIN thanh toán",
                                                      var_stx_app.check_info_pin, "Mã PIN thanh toán", "TheThanhVien_ThongTinMaPinThanhToan.png")


    def change_pin_code(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_info_pin)
        except:
            membership_card.info_pin(self, "", "", "")

        number = random.randint(1000, 9999)
        number = str(number)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_pin_code).click()
        time.sleep(2.5)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_pin_code1_click).click()
        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_pin_code1_input).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_pin_code1_input).send_keys("9999"+number)
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_pin_code2_click).click()
        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_pin_code2_input).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_pin_code2_input).send_keys("9999"+number)
        time.sleep(0.5)
        code_pin = var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_pin_code1_input).text

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CONFIRM).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_change_pin_code)))
        time.sleep(0.5)

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Thông tin mã PIN thanh toán",
                                                      var_stx_app.check_change_pin_code, "Bạn đã đổi mã PIN thành công. Vui lòng dùng mã PIN mới để thanh toán cuốc khách!",
                                                      "TheThanhVien_ThongTinMaPinThanhToan_DoiMaPhin.png")
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 14, code_pin)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 31, 2, code_pin)


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2.5)
        except:
            pass


    def check_change_pin_code(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_info_pin)
        except:
            membership_card.change_pin_code(self, "", "", "")

        code_pin = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 31, 2))
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_hide_code_pin).click()
        time.sleep(2)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Thông tin mã PIN thanh toán",
                                                      var_stx_app.check_change_pin_code1, code_pin, "TheThanhVien_ThongTinMaPinThanhToan_CheckMaPin.png")

        module_other_stx_app.close_app()
        # try:
        #     var_stx_app.driver.find_element(By.XPATH, var_stx_app.desc_back).click()
        #     time.sleep(2.5)
        #     var_stx_app.driver.find_element(By.XPATH, var_stx_app.desc_back).click()
        #     time.sleep(2.5)
        #     var_stx_app.driver.find_element(By.XPATH, var_stx_app.desc_back).click()
        #     time.sleep(2.5)
        #     var_stx_app.driver.find_element(By.XPATH, var_stx_app.desc_back).click()
        #     time.sleep(2.5)
        # except:
        #     pass







class verify_account:


    def verify_account(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_account)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.verify_account).click()
        time.sleep(2.5)

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Xác minh tài khoản đã giới thiệu",
                                                      var_stx_app.check_verify_account, "Xác minh mã giới thiệu", "TaiKhoan_XacMinhtaiKhoanDaGioiThieu.png")



    def check_info_verify_account(self, code, eventname, result, type, path_check, desire, name_image):
        var_stx_app.driver.implicitly_wait(5)
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_verify_account)
        except:
            verify_account.verify_account(self, "", "", "")

        if type == "0":
            var_stx_app.logging.info("--------------")
            var_stx_app.logging.info("Tài khoản(g7) - Xác minh tài khoản đã giới thiệu")
            var_stx_app.logging.info("Mã - " + code)
            var_stx_app.logging.info("Tên sự kiện - " + eventname)
            var_stx_app.logging.info("Kết quả - " + result)
            try:
                check_text = var_stx_app.driver.find_element(By.XPATH, path_check).text
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, check_text)
                var_stx_app.logging.info(check_text)
                if check_text != desire:
                    var_stx_app.logging.info("True")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    pass
                    # var_stx_app.logging.info("False")
                    # var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                    # module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                    # module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)
            except:
                pass
                # var_stx_app.logging.info("False")
                # var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                # module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                # module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)


        if type == "1":
            var_stx_app.logging.info("--------------")
            var_stx_app.logging.info("Tài khoản(g7) - Xác minh tài khoản đã giới thiệu")
            var_stx_app.logging.info("Mã - " + code)
            var_stx_app.logging.info("Tên sự kiện - " + eventname)
            var_stx_app.logging.info("Kết quả - " + result)
            try:
                check_text = var_stx_app.driver.find_element(By.XPATH, path_check).text
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, check_text)
                var_stx_app.logging.info(check_text)
                if check_text == desire:
                    var_stx_app.logging.info("True")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    pass
                    # var_stx_app.logging.info("False")
                    # var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                    # module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                    # module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)
            except:
                pass
                # var_stx_app.logging.info("False")
                # var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                # module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                # module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)

        if name_image == "_XacMinhtaiKhoanDaGioiThieu_XacNhan.png":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.desc_back).click()
            time.sleep(3)



    def check_info_verify_account1(self, code, eventname, result, name, name_image):
        var_stx_app.driver.implicitly_wait(5)
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_verify_account)
        except:
            verify_account.verify_account(self, "", "", "")


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Xác minh tài khoản đã giới thiệu")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            check_text = var_stx_app.driver.find_element(By.XPATH, var_stx_app.verify_account_name).text
            name_customer, phone = map(str.strip, check_text.split("-"))
            print(name_customer, phone)

            if name == "Tên khách hàng":
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, name_customer)
                var_stx_app.logging.info(check_text)
                if name_customer != "":
                    var_stx_app.logging.info("True")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    pass
                    # var_stx_app.logging.info("False")
                    # var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                    # module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                    # module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)

            if name == "Số điện thoại":
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, phone)
                var_stx_app.logging.info(check_text)
                if phone != "":
                    var_stx_app.logging.info("True")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    pass
                    # var_stx_app.logging.info("False")
                    # var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                    # module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                    # module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)

        except:
            pass
            # var_stx_app.logging.info("False")
            # var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + name_image)
            # module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            # module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)





class comment:


    def comment(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_account)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.comment).click()
        time.sleep(2.5)

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Góp ý",
                                                      var_stx_app.check_comment, "G7 Taxi mong muốn nhận được góp ý của bạn để ngày càng tốt hơn", "TaiKhoan_GopY.png")



    def send_comment(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_comment)
        except:
            comment.comment(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.comment_title).send_keys("Trường test góp ý")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.comment_content).send_keys("Không")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.SEND_COMMENT).click()
        time.sleep(2.5)
        module_other_stx_app.write_result_not_displayed_try(code, eventname, result, "Tài khoản(g7) - Góp ý",
                                                      var_stx_app.SEND_COMMENT, "TaiKhoan_GuiGopY.png")


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.SEND_COMMENT)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.desc_back).click()
            time.sleep(2.5)
        except:
            pass




class language:


    def language(self, code, eventname, result, path_language, desire, name_image):
        var_stx_app.driver.implicitly_wait(0.3)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_account)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)

        var_stx_app.driver.implicitly_wait(3)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.language).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, path_language).click()
        time.sleep(2.5)
        if name_image == "TaiKhoan_NgonNgu_TiengViet.png":
            module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Ngôn ngữ",
                                                          path_language, desire, name_image)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.language_x).click()
            time.sleep(2)

        else:
            module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Ngôn ngữ",
                                                          var_stx_app.check_language, desire, name_image)

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.skip).click()
            time.sleep(2)
        except:
            pass




class introduce_share:


    def introduce_share(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_account)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.g7_taxi).click()
                time.sleep(3)
            except:
                pass
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.introduce_share).click()
        except:
            var_stx_app.driver.swipe(350, 900, 350, 500, 1000)
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.introduce_share).click()
        time.sleep(2.5)

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Giới thiệu / Chia sẻ",
                                                      var_stx_app.check_introduce_share, "Taxi chính hãng", "TaiKhoan_GioiThieuChiaSe.png")



    def introduce_share_button(self, code, eventname, result, button, type, path_check, desire, name_image):
        var_stx_app.driver.implicitly_wait(5)
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_introduce_share)
        except:
            introduce_share.introduce_share(self, "", "", "")


        var_stx_app.driver.find_element(By.XPATH, button).click()
        time.sleep(4)
        if type == "0":
            module_other_stx_app.write_result_not_displayed_try(code, eventname, result, "Tài khoản(g7) - Giới thiệu / Chia sẻ",
                                                          path_check, name_image)
        else:
            module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Giới thiệu / Chia sẻ",
                                                          path_check, desire, name_image)


        var_stx_app.driver.press_keycode(4)
        time.sleep(2)
        if name_image == "_GioiThieuChiaSe_ChiaSe.png":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.desc_back).click()
            time.sleep(2)




class support:


    def support(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2.5)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_account)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.support).click()
        except:
            var_stx_app.driver.swipe(350, 900, 350, 500, 1000)
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.support).click()
        time.sleep(2.5)

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Hỗ trợ",
                                                      var_stx_app.check_support, "Chọn loại xe", "TaiKhoan_HoTro.png")



    def support_link(self, code, eventname, result, button, path_check, desire, name_image):
        var_stx_app.driver.implicitly_wait(5)
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_support)
        except:
            support.support(self, "", "", "")


        var_stx_app.driver.find_element(By.XPATH, button).click()
        time.sleep(2)
        try:
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, path_check)))
        except:
            pass
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Hỗ trợ",
                                                      path_check, desire, name_image)


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.desc_back).click()
            time.sleep(2)
        except:
            var_stx_app.driver.press_keycode(4)
            time.sleep(2)


    def support_link_app(self, code, eventname, result, button1, button2, path_check, name_image):
        var_stx_app.driver.implicitly_wait(5)
        wait = WebDriverWait(var_stx_app.driver, 10)
        

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_support)
        except:
            support.support(self, "", "", "")


        try:
            var_stx_app.driver.find_element(By.XPATH, button1).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, button2).click()
            time.sleep(3)
        except:
            pass


        module_other_stx_app.write_result_not_displayed_try(code, eventname, result, "Tài khoản(g7) - Hỗ trợ",
                                                      path_check, name_image)

        var_stx_app.driver.press_keycode(4)
        time.sleep(3.5)
        var_stx_app.driver.press_keycode(4)
        time.sleep(3.5)
        if name_image == "HoTro_CapNhatPhanMemTrenIOS.png":
            try:
                var_stx_app.driver.implicitly_wait(0.3)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.desc_back).click()
                time.sleep(2)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.desc_back).click()
                time.sleep(2)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.desc_back).click()
                time.sleep(2)
            except:
                pass




class logout:

    def logout(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.desc_back).click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.desc_back).click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.desc_back).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2.5)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_account)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_g7).click()
            time.sleep(2)

        var_stx_app.driver.swipe(400, 1200, 465, 480, 500)
        time.sleep(1)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.logout).click()
        except:
            var_stx_app.driver.swipe(350, 900, 350, 500, 500)
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.logout).click()
        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        time.sleep(1.5)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_logout)))

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Tài khoản(g7) - Đăng xuất",
                                                      var_stx_app.check_logout, "Nhập số điện thoại để trải nghiệm ngay bây giờ !", "TaiKhoan_DangXuat.png")
        module_other_stx_app.close_app()







