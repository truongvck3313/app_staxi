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
import random
import action
import homepage_driver


class info_account:

    def icon_edit(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.info_account, time_wait=1)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)

        action.click(var_stx_app.driver_customer, var_stx_app.account_g7_icon_edit)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_icon_edit, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Thông tin tài khoản",
                                                      var_stx_app.check_icon_edit, "Thay đổi tài khoản", "TaiKhoan_IconSua.png")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.skip, time_wait=1)
            time.sleep(1.5)
        except:
            pass


    def check_info_account(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.info_account, time_wait=1)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Thông tin tài khoản")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            info_account_name = action.get_text(var_stx_app.driver_customer, var_stx_app.info_account_name, time_wait=15)
            info_account_version = action.get_text(var_stx_app.driver_customer, var_stx_app.info_account_version)
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 122, 2, info_account_version)

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Tên: {}\n{}".format(info_account_name, info_account_version))
            var_stx_app.logging.info("Tên: {}\n{}".format(info_account_name, info_account_version))
            if (info_account_name != "") and (info_account_version != ""):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "TaiKhoan_ThongTinTaiKhoan.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "TaiKhoan_ThongTinTaiKhoan.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "TaiKhoan_ThongTinTaiKhoan.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "TaiKhoan_ThongTinTaiKhoan.png")


        try:
            action.get_text(var_stx_app.driver_customer, var_stx_app.info_account_back, time_wait=5)
            time.sleep(2)
        except:
            pass




class history_order_car:



    def history_order_car(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.history_order_car, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.history, time_wait=2)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)
            action.click(var_stx_app.driver_customer, var_stx_app.history_order_car)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_history_order_car, time_wait=15)
        except:
            pass


        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Lịch sử đặt xe",
                                                      var_stx_app.check_history_order_car, "Lịch sử", "TaiKhoan_LichSuDatXe.png")



    def get_info_history_order_car(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_history_order_car, time_wait=1)
        except:
            history_order_car.history_order_car(self, "", "", "")

        #check xem hiện path không
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.history_overview_type_car, time_wait=1)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_back1)
            action.click(var_stx_app.driver_customer, var_stx_app.history_order_car)




        #Tổng quan
        try:
            history_overview_date = action.get_text(var_stx_app.driver_customer, var_stx_app.history_overview_date, time_wait=10)#Ngày/tháng/Năm
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 15, 2, history_overview_date)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 15, 2, "")

        try:
            history_overview_type_car = action.get_text(var_stx_app.driver_customer, var_stx_app.history_overview_type_car, time_wait=1)#Loại xe
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 16, 2, history_overview_type_car)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 16, 2, "")

        try:
            history_overview_status = action.get_text(var_stx_app.driver_customer, var_stx_app.history_overview_status, time_wait=1)#Trạng thái
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 17, 2, history_overview_status)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 17, 2, "")

        try:
            history_overview_time = action.get_text(var_stx_app.driver_customer, var_stx_app.history_overview_time, time_wait=1)#Giờ phút
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 18, 2, history_overview_time)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 18, 2, "")

        try:
            history_overview_location_from = action.get_text(var_stx_app.driver_customer, var_stx_app.history_overview_location_from, time_wait=1)#Điểm đón
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 19, 2, history_overview_location_from)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 19, 2, "")

        try:
            history_overview_location_to = action.get_text(var_stx_app.driver_customer, var_stx_app.history_overview_location_to, time_wait=1)#Điểm đến
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 20, 2, history_overview_location_to)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 20, 2, "")

        try:
            history_overview_pttt = action.get_text(var_stx_app.driver_customer, var_stx_app.history_overview_pttt, time_wait=1)#Phương thức thanh toán
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 21, 2, history_overview_pttt)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 21, 2, "")


        #Chi tiết
        action.click(var_stx_app.driver_customer, var_stx_app.get_info_history_order_car1, time_wait=10)

        try:
            history_detail_date = action.get_text(var_stx_app.driver_customer, var_stx_app.history_detail_date, time_wait=10)#Ngày/tháng/Năm - Giờ
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 15, 3, history_detail_date)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 15, 3, "")

        try:
            history_detail_type_car = action.get_text(var_stx_app.driver_customer, var_stx_app.history_detail_type_car, time_wait=1)#Loại xe
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 16, 3, history_detail_type_car)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 16, 3, "")

        try:
            history_detail_location_from = action.get_text(var_stx_app.driver_customer, var_stx_app.history_detail_location_from, time_wait=1)#Điểm đón
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 19, 3, history_detail_location_from)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 19, 3, "")

        try:
            history_detail_location_to = action.get_text(var_stx_app.driver_customer, var_stx_app.history_detail_location_to, time_wait=1)#Điểm đến
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 20, 3, history_detail_location_to)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 20, 3, "")

        try:
            history_detail_pttt = action.get_text(var_stx_app.driver_customer, var_stx_app.history_detail_pttt, time_wait=1)#Phương thức thanh toán
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 21, 3, history_detail_pttt)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 21, 3, "")

        try:
            history_detail_km_money = action.get_text(var_stx_app.driver_customer, var_stx_app.history_detail_km_money, time_wait=1)#Km - Số tiền
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 22, 3, history_detail_km_money)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 22, 3, "")


        try:
            history_detail_number_vehicle = action.get_text(var_stx_app.driver_customer, var_stx_app.history_detail_number_vehicle, time_wait=1)#Số hiệu - Biển số xe
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 32, 3, history_detail_number_vehicle)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 32, 3, "")

        try:
            history_detail_namedrive_company = action.get_text(var_stx_app.driver_customer, var_stx_app.history_detail_namedrive_company, time_wait=1) #Tên lái xe - công ty
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 33, 3, history_detail_namedrive_company)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 33, 3, "")

        try:
            history_detail_phone = action.get_text(var_stx_app.driver_customer, var_stx_app.history_detail_phone, time_wait=1) #Số điện thoại
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 34, 3, history_detail_phone)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 34, 3, "")

        try:
            history_detail_execution_time = action.get_text(var_stx_app.driver_customer, var_stx_app.history_detail_execution_time, time_wait=1) #Thời gian thực hiện
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 35, 3, history_detail_execution_time)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 35, 3, "")


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Lịch sử đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("True")
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")



    def check_info_order_date(self, code, eventname, result):
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



    def check_info_order_other(self, code, eventname, result, name, row):
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row, 3))
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Lịch sử đặt xe - Thông tin xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info(f"{name}: {detail}")

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f"{name}: {detail}")
        if detail != "None":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")



    def info_order_icon_payment(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.RE_ORDER, time_wait=1)
        except:
            history_order_car.get_info_history_order_car(self, "", "", "")

        action.click(var_stx_app.driver_customer, var_stx_app.info_order_icon_payment)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Lịch sử đặt xe - Thông tin xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            type_vehicle = action.get_text(var_stx_app.driver_customer, var_stx_app.info_order_type_vehicle, time_wait=15)
            fee_move = action.get_text(var_stx_app.driver_customer, var_stx_app.info_order_fee_move)
            space = action.get_text(var_stx_app.driver_customer, var_stx_app.info_order_space)
            sum_money = action.get_text(var_stx_app.driver_customer, var_stx_app.info_order_sum_money)

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f"{type_vehicle}\nCước di chuyển: {fee_move}\n"
                                                                                            f"Khoảng cách: {space}\nTổng tiền thanh toán: {sum_money}")
            var_stx_app.logging.info(f"{type_vehicle}\nCước di chuyển: {fee_move}\nKhoảng cách: {space}\nTổng tiền thanh toán: {sum_money}")

            if (type_vehicle != "None") and (fee_move != "None") and (space != "None") and (sum_money != "None"):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "TaiKhoan_LichSuDatXe_IconThanhToan.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "TaiKhoan_LichSuDatXe_IconThanhToan.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "TaiKhoan_LichSuDatXe_IconThanhToan.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "TaiKhoan_LichSuDatXe_IconThanhToan.png")

        action.click(var_stx_app.driver_customer, var_stx_app.info_order_icon_payment_back, time_wait=5)
        time.sleep(2.2)



    def info_order_icon_hd(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.RE_ORDER, time_wait=1)
        except:
            history_order_car.get_info_history_order_car(self, "", "", "")


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.info_order_icon_hd)
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_info_order_icon_hd)
            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Lịch sử đặt xe - Hợp đồng điện tử",
                                                          var_stx_app.check_info_order_icon_hd, "HỢP ĐỒNG VẬN CHUYỂN HÀNH KHÁCH",
                                                          "TaiKhoan_LichSuDatXe_HopDongDienTu.png")
        except:
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "TaiKhoan_LichSuDatXe_HopDongDienTu.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "TaiKhoan_LichSuDatXe_HopDongDienTu.png")



        try:
            action.click(var_stx_app.driver_customer, var_stx_app.info_order_icon_hd_back, time_wait=5)
            time.sleep(2)
        except:
            var_stx_app.restart_driver(var_stx_app.driver_customer)



    def call_company(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.call_company, time_wait=3)
        except:
            history_order_car.get_info_history_order_car(self, "", "", "")


        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Lịch sử đặt xe - Gọi hãng",
                                                      var_stx_app.call_company, "GỌI HÃNG", "TaiKhoan_LichSuDatXe_GoiHang.png")



    def re_order(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.RE_ORDER, time_wait=1)
        except:
            history_order_car.get_info_history_order_car(self, "", "", "")


        #chi tiết cuốc

        location_from1 = action.get_text(var_stx_app.driver_customer, var_stx_app.history_detail_location_from, time_wait=10)
        location_to1 = action.get_text(var_stx_app.driver_customer, var_stx_app.history_detail_location_to)

        action.click(var_stx_app.driver_customer, var_stx_app.RE_ORDER)
        action.click(var_stx_app.driver_customer, var_stx_app.ORDER_A_TO_B)

        location_from2 = action.get_text(var_stx_app.driver_customer, var_stx_app.location_1)
        location_to2 = action.get_text(var_stx_app.driver_customer, var_stx_app.location_2)

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
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "TaiKhoan_LichSuDatXe_Datlai.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "TaiKhoan_LichSuDatXe_Datlai.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "TaiKhoan_LichSuDatXe_Datlai.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "TaiKhoan_LichSuDatXe_Datlai.png")


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.order_car_back, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.icon_load1, time_wait=1)
            var_stx_app.restart_driver(var_stx_app.driver_customer)
        except:
            pass












class notification:


    def notification(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.account_g7, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.info_account, time_wait=1)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)
            time.sleep(2)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.notification, time_wait=10)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_back1)
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)
            action.click(var_stx_app.driver_customer, var_stx_app.notification)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_notification, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Thông báo",
                                                      var_stx_app.check_notification, "Thông báo", "TaiKhoan_ThongBao.png")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.notification_back, time_wait=2)
            time.sleep(2)
        except:
            pass




class membership_card:


    def membership_card(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.info_account, time_wait=1)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.membership_card, time_wait=10)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_back1)
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)
            action.click(var_stx_app.driver_customer, var_stx_app.membership_card)


        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_membership_card, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Thẻ thành viên",
                                                      var_stx_app.check_membership_card, "Chạm để phóng to", "TaiKhoan_TheThanhVien.png")



    def check_info_membership_card(self, code, eventname, result, path_check, path_check1, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.scan_qrcode, time_wait=1)
        except:
            membership_card.membership_card(self, "", "", "")

        if name_image == "TaiKhoan_TheThanhVien_TkChinh.png":
            action.click(var_stx_app.driver_customer, var_stx_app.check_info_membership_card_iconhide, time_wait=1)
            time.sleep(2)


        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.card_bk, time_wait=1)
            module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Thông tin thẻ",
                                                          path_check, "", name_image)
            if name_image == "TaiKhoan_TheThanhVien_HetHan.png":
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "")


        except:
            module_other_stx_app.write_result_text_try_if_other(var_stx_app.card_bk, code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Thông tin thẻ",
                                                          path_check1, "", name_image)



    def scan_qrcode(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.scan_qrcode, time_wait=1)
        except:
            membership_card.membership_card(self, "", "", "")

        action.click(var_stx_app.driver_customer, var_stx_app.scan_qrcode)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.ALLOW, time_wait=3)
            time.sleep(2)
        except:
            pass

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.USE_APP, time_wait=3)
            time.sleep(2)
        except:
            pass

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.THIS_TIME_ONLY, time_wait=3)
            time.sleep(2)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Quét mã QrCode",
                                                      var_stx_app.check_scan_qrcode, "Quét mã Qr để thanh toán", "TaiKhoan_TheThanhVien_QuetMaQrCode.png")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.BACK, time_wait=5)
            time.sleep(2)
        except:
            pass



    def reload_the_card(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.scan_qrcode, time_wait=1)
        except:
            membership_card.membership_card(self, "", "", "")

        action.click(var_stx_app.driver_customer, var_stx_app.reload_the_card)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_reload_the_card, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Nạp tiền vào thẻ",
                                                      var_stx_app.check_reload_the_card, "Quý khách nạp tiền vào thẻ thông qua tài khoản:",
                                                      "TaiKhoan_TheThanhVien_NạpTienVaoThe.png")



    def check_info_reload_the_card(self, code, eventname, result, path_name, path_data, desire, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_reload_the_card, time_wait=1)

        except:
            membership_card.reload_the_card(self, "", "", "")

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Thẻ thành viên - Nạp tiền vào thẻ")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            name = action.get_text(var_stx_app.driver_customer, path_name, time_wait=2)
            data = action.get_text(var_stx_app.driver_customer, path_data, time_wait=2)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, f"{name} {data}")
            var_stx_app.logging.info(f"{name} {data}")
            if (name == desire) and (data != ""):
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



    def check_info_reload_the_card_bank(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_reload_the_card, time_wait=1)
        except:
            membership_card.reload_the_card(self, "", "", "")

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_reload_the_card, time_wait=1)
        except:
            pass

        module_other_stx_app.write_result_text_try_if_in(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Nạp tiền vào thẻ",
                                                      var_stx_app.bank_mb, "MBBank", "TheThanhVien_NapTienVaoThe_NganHang.png")





    def check_icon_membership_card(self, code, eventname, result, path_icon, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_reload_the_card, time_wait=1)
        except:
            membership_card.reload_the_card(self, "", "", "")

        action.click(var_stx_app.driver_customer, path_icon, time_wait=10)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.ALLOW, time_wait=2)
        except:
            pass


        module_other_stx_app.write_result_displayed_try(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Nạp tiền vào thẻ",
                                                      path_icon, name_image)



    def check_icon_membership_card_new(self, code, eventname, result, button, desire1, desire2, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_reload_the_card, time_wait=1)
        except:
            membership_card.reload_the_card(self, "", "", "")

        action.click(var_stx_app.driver_customer, button, time_wait=5)

        if name_image == "TheThanhVien_NapTienVaoThe_LưuMaQrCode.png":
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.ALLOW, time_wait=3.5)
                time.sleep(2)
            except:
                pass

        # action.click(var_stx_app.driver_customer, button, time_wait=5)
        # homepage_driver.wait_toast_message(var_stx_app.driver_customer, 5)
        #
        # module_other_stx_app.write_result_text_try_if_toast_in(var_stx_app.driver_customer, code, eventname, result,
        #                                                        "Tài khoản(g7) - Thẻ thành viên - Nạp tiền vào thẻ", "", desire1, name_image)

        message = homepage_driver.wait_toast_message_click(var_stx_app.driver_customer, button, 5)
        if message == desire1:
            module_other_stx_app.write_result_text_try_if_toast_in(var_stx_app.driver_customer, code, eventname, result,
                                                                   "Tài khoản(g7) - Thẻ thành viên - Nạp tiền vào thẻ",
                                                                   "", desire1, name_image)
        else:
            homepage_driver.wait_toast_message_click(var_stx_app.driver_customer, button, 5)
            module_other_stx_app.write_result_text_try_if_toast_in(var_stx_app.driver_customer, code, eventname, result,
                                                                   "Tài khoản(g7) - Thẻ thành viên - Nạp tiền vào thẻ",
                                                                   "", desire2, name_image)




    def check_icon_help_membership_card(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_reload_the_card, time_wait=1)
        except:
            membership_card.reload_the_card(self, "", "", "")


        module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.5, 0.8, 0.6, 0.3, 1000)
        action.click(var_stx_app.driver_customer, var_stx_app.icon_help_membership_card)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.support1, time_wait=10)
        except:
            pass


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Thẻ thành viên - Nạp tiền vào thẻ")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            check_bank = action.get_text(var_stx_app.driver_customer, var_stx_app.check_icon_help_membership_card, time_wait=15)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, check_bank)
            var_stx_app.logging.info(check_bank)
            if check_bank == "Chủ tài khoản  : {{AName}}\n\nSố tài khoản   : {{ANumber}}\n\nNgân hàng    : {{Bank}}\n\n":
                var_stx_app.logging.info("False")
                var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "TheThanhVien_NapTienVaoThe_QuyKhachCanHoTro.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "TheThanhVien_NapTienVaoThe_QuyKhachCanHoTro.png")
            else:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + "TheThanhVien_NapTienVaoThe_QuyKhachCanHoTro.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "TheThanhVien_NapTienVaoThe_QuyKhachCanHoTro.png")

        var_stx_app.restart_driver(var_stx_app.driver_customer)





    def donate_money(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.scan_qrcode, time_wait=1)
        except:
            membership_card.membership_card(self, "", "", "")

        action.click(var_stx_app.driver_customer, var_stx_app.donate_money)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_donate_money, time_wait=15)
        except:
            pass


        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Tặng tiền",
                                                      var_stx_app.check_donate_money, "Chọn số tiền muốn chuyển (VNĐ)",
                                                      "TaiKhoan_TheThanhVien_TangTien.png")


    def give_money_to_others(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_donate_money, time_wait=1)
        except:
            membership_card.donate_money(self, "", "", "")


        action.click(var_stx_app.driver_customer, var_stx_app.donate_money_500k)
        action.clear(var_stx_app.driver_customer, var_stx_app.donate_money_vnd_input)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.donate_money_vnd_input, "10000")
        action.send_keys(var_stx_app.driver_customer, var_stx_app.donate_money_note, "Trường test tặng tiền")
        action.send_keys(var_stx_app.driver_customer, var_stx_app.donate_money_sdt, "0977679816")
        action.click(var_stx_app.driver_customer, var_stx_app.check)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.DONATE_MONEY, time_wait=10)
        except:
            action.clear(var_stx_app.driver_customer, var_stx_app.donate_money_sdt)
            action.send_keys(var_stx_app.driver_customer, var_stx_app.donate_money_sdt, "0911223344")
            action.click(var_stx_app.driver_customer, var_stx_app.check)
            action.click(var_stx_app.driver_customer, var_stx_app.DONATE_MONEY)

        action.click(var_stx_app.driver_customer, var_stx_app.igree)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_give_money_to_others, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Tặng tiền",
                                                      var_stx_app.check_give_money_to_others, "Tặng tiền thành công",
                                                      "TheThanhVien_TangTien_TangTienChoNguoiKhac.png")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.igree, time_wait=2.5)
            time.sleep(2)
        except:
            pass


    def history_car(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 106, 2, 0)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 107, 2, 0)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 108, 2, 0)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 109, 2, 0)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 110, 2, 0)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 111, 2, 0)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 112, 2, 0)


        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.scan_qrcode, time_wait=1)
        except:
            membership_card.membership_card(self, "", "", "")

        action.click(var_stx_app.driver_customer, var_stx_app.history_car)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.driver_customer, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Lịch sử thẻ",
                                                      var_stx_app.check_history_car, "Lịch sử thẻ",

                                                      "TaiKhoan_TheThanhVien_LichSuThe.png")
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.history_car_status, time_wait=15)
        except:
            pass

        history_car_tkchinh1 = action.get_text(var_stx_app.driver_customer, var_stx_app.history_car_tkchinh1)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 130, 2, history_car_tkchinh1)

        n = 0
        while (n < 25):
            n = int(n)
            n = n + 1
            n = str(n)

            historycar_status       = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView"
            historycar_time         = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView"
            historycar_money        = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[2]"
            historycar_card_balance = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]"
            historycar_info_vehicle = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[4]"
            historycar_location_from= "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.TextView[2]"
            historycar_location_to  = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.widget.TextView[2]"
            historycar_note         = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[3]/android.widget.TextView[2]"

            n = int(n)
            try:
                historycar_status = action.get_text(var_stx_app.driver_customer, historycar_status, time_wait=1)
                historycar_time = action.get_text(var_stx_app.driver_customer, historycar_time, time_wait=1)
                historycar_money = action.get_text(var_stx_app.driver_customer, historycar_money, time_wait=1)
                historycar_card_balance = action.get_text(var_stx_app.driver_customer, historycar_card_balance, time_wait=1)
                historycar_info_vehicle = action.get_text(var_stx_app.driver_customer, historycar_info_vehicle, time_wait=1)
                historycar_location_from = action.get_text(var_stx_app.driver_customer, historycar_location_from, time_wait=1)
                historycar_location_to = action.get_text(var_stx_app.driver_customer, historycar_location_to, time_wait=1)

                try:
                    historycar_note = action.get_text(var_stx_app.driver_customer, historycar_note, time_wait=1)
                except:
                    historycar_note = "đang mất trường ghi chú"


                if historycar_status == "Thanh toán":
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 131, 2, historycar_status)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 132, 2, historycar_time)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 133, 2, historycar_money)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 134, 2, historycar_card_balance)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 135, 2, historycar_info_vehicle)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 136, 2, historycar_location_from)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 137, 2, historycar_location_to)
                    module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 138, 2, historycar_note)
                    break
            except:
                pass





    def check_info_history_car(self, code, eventname, result, row, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.history_car_tkchinh1, time_wait=1)
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
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + name_image)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)

        if name_image == "TheThanhVien_LichSuThe_DiemDen.png":
            action.click(var_stx_app.driver_customer, var_stx_app.desc_back, time_wait=2)
            time.sleep(2)


    def info_pin(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.scan_qrcode, time_wait=1)
        except:
            membership_card.membership_card(self, "", "", "")

        action.click(var_stx_app.driver_customer, var_stx_app.info_pin)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_info_pin, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Thông tin mã PIN thanh toán",
                                                      var_stx_app.check_info_pin, "Mã PIN thanh toán", "TheThanhVien_ThongTinMaPinThanhToan.png")


    def change_pin_code(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_info_pin, time_wait=1)
        except:
            membership_card.info_pin(self, "", "", "")

        number = random.randint(1000, 9999)
        number = str(number)

        action.click(var_stx_app.driver_customer, var_stx_app.change_pin_code)
        time.sleep(1.5)
        action.clear_only(var_stx_app.driver_customer, var_stx_app.change_pin_code1_input)
        time.sleep(0.5)
        action.send_keys1(var_stx_app.driver_customer, "9999" + number)
        time.sleep(0.5)


        action.clear_only(var_stx_app.driver_customer, var_stx_app.change_pin_code2_input)
        time.sleep(0.5)
        action.send_keys1(var_stx_app.driver_customer, "9999" + number)
        time.sleep(0.5)
        action.click(var_stx_app.driver_customer, var_stx_app.icon_hide1)

        action.click(var_stx_app.driver_customer, var_stx_app.CONFIRM)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_change_pin_code, time_wait=15)
        except:
            pass


        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Thông tin mã PIN thanh toán",
                                                      var_stx_app.check_change_pin_code, "Bạn đã đổi mã PIN thành công. Vui lòng dùng mã PIN mới để thanh toán cuốc khách!",
                                                      "TheThanhVien_ThongTinMaPinThanhToan_DoiMaPhin.png")
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 14, "9999"+number)
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 31, 2, "9999"+number)


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.igree, time_wait=3)
            time.sleep(2)
        except:
            pass


    def check_change_pin_code(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_info_pin, time_wait=1)
        except:
            membership_card.change_pin_code(self, "", "", "")

        code_pin = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 31, 2))


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_hide, time_wait=2)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_back1)
            action.click(var_stx_app.driver_customer, var_stx_app.info_pin)
            action.click(var_stx_app.driver_customer, var_stx_app.icon_hide)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_change_pin_code, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if_in1(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Thẻ thành viên - Thông tin mã PIN thanh toán",
                                       var_stx_app.check_change_pin_code1, code_pin, "TheThanhVien_ThongTinMaPinThanhToan_CheckMaPin.png")

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_back1, time_wait=2)
            time.sleep(2)
            action.click(var_stx_app.driver_customer, var_stx_app.icon_back1, time_wait=2)
            time.sleep(2)
        except:
            pass







class verify_account:


    def verify_account(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.info_account, time_wait=1)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.verify_account, time_wait=15)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_back1)
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)
            action.click(var_stx_app.driver_customer, var_stx_app.verify_account)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_verify_account, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Xác minh tài khoản đã giới thiệu",
                                                      var_stx_app.check_verify_account, "Xác minh mã giới thiệu", "TaiKhoan_XacMinhtaiKhoanDaGioiThieu.png")



    def check_info_verify_account(self, code, eventname, result, type, path_check, desire, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_verify_account, time_wait=1)
        except:
            verify_account.verify_account(self, "", "", "")

        if type == "0":
            var_stx_app.logging.info("--------------")
            var_stx_app.logging.info("Tài khoản(g7) - Xác minh tài khoản đã giới thiệu")
            var_stx_app.logging.info("Mã - " + code)
            var_stx_app.logging.info("Tên sự kiện - " + eventname)
            var_stx_app.logging.info("Kết quả - " + result)
            try:
                check_text = action.get_text(var_stx_app.driver_customer, path_check, time_wait=2)
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, check_text)
                var_stx_app.logging.info(check_text)
                if check_text != desire:
                    var_stx_app.logging.info("True")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    pass
            except:
                pass



        if type == "1":
            var_stx_app.logging.info("--------------")
            var_stx_app.logging.info("Tài khoản(g7) - Xác minh tài khoản đã giới thiệu")
            var_stx_app.logging.info("Mã - " + code)
            var_stx_app.logging.info("Tên sự kiện - " + eventname)
            var_stx_app.logging.info("Kết quả - " + result)
            try:
                check_text = action.get_text(var_stx_app.driver_customer, path_check, time_wait=2)
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, check_text)
                var_stx_app.logging.info(check_text)
                if check_text == desire:
                    var_stx_app.logging.info("True")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    pass

            except:
                pass


        if name_image == "_XacMinhtaiKhoanDaGioiThieu_XacNhan.png":
            action.wait_for(var_stx_app.driver_customer, var_stx_app.desc_back, time_wait=3)
            time.sleep(2)



    def check_info_verify_account1(self, code, eventname, result, name, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_verify_account, time_wait=1)

        except:
            verify_account.verify_account(self, "", "", "")


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Xác minh tài khoản đã giới thiệu")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            check_text = action.get_text(var_stx_app.driver_customer, var_stx_app.verify_account_name, time_wait=10)
            name_customer, phone = map(str.strip, check_text.split("-"))
            print(name_customer, phone)

            if name == "Tên khách hàng":
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, name_customer)
                var_stx_app.logging.info(check_text)
                if name_customer != "":
                    var_stx_app.logging.info("True")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + name_image)
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)

            if name == "Số điện thoại":
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, phone)
                var_stx_app.logging.info(check_text)
                if phone != "":
                    var_stx_app.logging.info("True")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + name_image)
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)

        except:
            var_stx_app.driver_customer.save_screenshot(var_stx_app.imagepath + code + name_image)
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)





class comment:


    def comment(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.info_account, time_wait=1)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.comment, time_wait=15)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_back1)
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)
            action.click(var_stx_app.driver_customer, var_stx_app.comment)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_comment, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Góp ý",
                                                      var_stx_app.check_comment, "G7 Taxi mong muốn nhận được góp ý của bạn để ngày càng tốt hơn", "TaiKhoan_GopY.png")



    def upload_image(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_comment, time_wait=1)
        except:
            comment.comment(self, "", "", "")

        action.click(var_stx_app.driver_customer, var_stx_app.icon_upload_image)
        try:
            action.click(var_stx_app.driver_customer, var_stx_app.recent_image1, time_wait=10)
        except:
            module_other_stx_app.tap_percent(var_stx_app.driver_customer, 0.5, 0.7)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_save, time_wait=10)
        except:
            module_other_stx_app.tap_percent(var_stx_app.driver_customer, 0.95, 0.05)


        homepage_driver.wait_toast_message(var_stx_app.driver_customer, 5)
        module_other_stx_app.write_result_text_try_if_toast_in(var_stx_app.driver_customer, code, eventname, result,
                                                               "Tài khoản(g7) - Góp ý - Thêm ảnh", "", "Lưu ảnh thành công!", "TaiKhoan_GopY_ThemAnh.png")





    def hotline(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_comment, time_wait=1)
        except:
            comment.comment(self, "", "", "")

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Góp ý - hotline",
                                                      var_stx_app.hotline, "HOTLINE", "TaiKhoan_GopY_hotline.png")



    def send_comment(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_comment, time_wait=1)
        except:
            comment.comment(self, "", "", "")

        action.send_keys(var_stx_app.driver_customer, var_stx_app.comment_title, "Trường test góp ý", time_wait=10)
        action.send_keys(var_stx_app.driver_customer, var_stx_app.comment_content, "Không")

        action.wait_for(var_stx_app.driver_customer, var_stx_app.comment_image)
        action.click(var_stx_app.driver_customer, var_stx_app.SEND_COMMENT)

        homepage_driver.wait_toast_message(var_stx_app.driver_customer, 5)
        module_other_stx_app.write_result_text_try_if_toast(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Góp ý",
                                                      "", "Cảm ơn bạn đã gửi góp ý cho chúng tôi", "TaiKhoan_GuiGopY.png")

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.SEND_COMMENT, time_wait=1)
            action.click(var_stx_app.driver_customer, var_stx_app.desc_back)
            time.sleep(2)
        except:
            pass





class switchboard_cskh:

    def switchboard_cskh(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.info_account, time_wait=1)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)


        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.switchboard_cskh, time_wait=15)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_back1)
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.switchboard_cskh, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Tổng đài CSKH",
                                                      var_stx_app.switchboard_cskh, "Tổng đài CSKH", "TaiKhoan_TongDaiCskh.png")






class language:


    def language(self, code, eventname, result, path_language, desire, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.info_account, time_wait=1)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.language, time_wait=10)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_back1)
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)

        action.click(var_stx_app.driver_customer, var_stx_app.language)
        action.click(var_stx_app.driver_customer, path_language, time_wait=10)



        if name_image == "TaiKhoan_NgonNgu_TiengViet.png":
            try:
                action.wait_for(var_stx_app.driver_customer, path_language, time_wait=10)
            except:
                pass

            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Ngôn ngữ",
                                                          path_language, desire, name_image)

            action.click(var_stx_app.driver_customer, var_stx_app.language_x)
            time.sleep(2)

        else:
            try:
                action.wait_for(var_stx_app.driver_customer, var_stx_app.check_language, time_wait=10)
            except:
                pass

            module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Ngôn ngữ",
                                                          var_stx_app.check_language, desire, name_image)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.skip, time_wait=2)
            time.sleep(2)
        except:
            pass




class introduce_share:


    def introduce_share(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.info_account, time_wait=1)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)


        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.language, time_wait=10)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_back1)
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.introduce_share, time_wait=5)
        except:
            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.5, 0.8, 0.5, 0.3, 1000)
            time.sleep(1)
            action.click(var_stx_app.driver_customer, var_stx_app.introduce_share)


        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_introduce_share, time_wait=15)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Giới thiệu / Chia sẻ",
                                                      var_stx_app.check_introduce_share, "Taxi chính hãng", "TaiKhoan_GioiThieuChiaSe.png")



    def introduce_share_button(self, code, eventname, result, button, type, path_check, desire, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_introduce_share, time_wait=1)
        except:
            introduce_share.introduce_share(self, "", "", "")

        action.click(var_stx_app.driver_customer, button, time_wait=15)

        if type == "0":
            time.sleep(3)
            module_other_stx_app.write_result_not_displayed_try(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Giới thiệu / Chia sẻ",
                                                          path_check, name_image)
        if type == "1":
            try:
                action.wait_for(var_stx_app.driver_customer, path_check, time_wait=5)
            except:
                pass

            module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Giới thiệu / Chia sẻ",
                                                          path_check, desire, name_image)
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.cancel1, time_wait=1)
                time.sleep(2)
            except:
                pass


        var_stx_app.driver_customer.back()
        time.sleep(2)

        if name_image == "_GioiThieuChiaSe_ChiaSe.png":
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.desc_back, time_wait=3)
                time.sleep(2)
            except:
                pass




class support:


    def support(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.info_account, time_wait=1)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)


        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.language, time_wait=10)
        except:
            action.click(var_stx_app.driver_customer, var_stx_app.icon_back1)
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)


        try:
            action.click(var_stx_app.driver_customer, var_stx_app.support, time_wait=2)
        except:
            module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.5, 0.8, 0.5, 0.3, 1000)
            time.sleep(1)
            action.click(var_stx_app.driver_customer, var_stx_app.support)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_support, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Hỗ trợ",
                                                      var_stx_app.check_support, "Chọn loại xe", "TaiKhoan_HoTro.png")



    def support_link(self, code, eventname, result, button, path_check, desire, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_support, time_wait=1)
        except:
            support.support(self, "", "", "")

        # action.click(var_stx_app.driver_customer, button, time_wait=10)
        # time.sleep(3)


        module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Hỗ trợ",
                                                      button, "", name_image)
        # try:
        #     action.click(var_stx_app.driver_customer, var_stx_app.desc_back, time_wait=1)
        #     time.sleep(2)
        # except:
        #     var_stx_app.driver_customer.back()
        #     time.sleep(2)



    def support_link_app(self, code, eventname, result, button1, button2, path_check, name_image):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_support, time_wait=1)
        except:
            support.support(self, "", "", "")


        # try:
        #     action.click(var_stx_app.driver_customer, button1, time_wait=2)
        #     time.sleep(3)
        # except:
        #     pass
        #
        # try:
        #     action.click(var_stx_app.driver_customer, button2, time_wait=2)
        #     time.sleep(3)
        # except:
        #     pass
        #
        # if name_image == "HoTro_CapNhatPhanMemTrenIOS.png":
        #     var_stx_app.driver_customer.tap([(230, 220)])
        #     time.sleep(3)


        module_other_stx_app.write_result_text_try_if_other(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Hỗ trợ",
                                                      path_check, "", name_image)

        # var_stx_app.driver_customer.back()
        # time.sleep(3)

        if name_image == "HoTro_CapNhatPhanMemTrenIOS.png":
            try:
                action.click(var_stx_app.driver_customer, var_stx_app.desc_back, time_wait=1)
                action.click(var_stx_app.driver_customer, var_stx_app.desc_back, time_wait=2)
            except:
                pass




class logout:

    def logout(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.desc_back, time_wait=1)
            action.click(var_stx_app.driver_customer, var_stx_app.desc_back, time_wait=2)
            action.click(var_stx_app.driver_customer, var_stx_app.desc_back, time_wait=2)
            action.click(var_stx_app.driver_customer, var_stx_app.desc_back, time_wait=2)
        except:
            pass

        try:
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7, time_wait=1)
            time.sleep(2)
        except:
            pass

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.info_account, time_wait=1)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7)

        module_other_stx_app.swipe_percent(var_stx_app.driver_customer, 0.5, 0.8, 0.5, 0.3, 1000)
        time.sleep(1)
        action.click(var_stx_app.driver_customer, var_stx_app.logout)
        action.click(var_stx_app.driver_customer, var_stx_app.igree)

        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_logout, time_wait=10)
        except:
            pass

        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Đăng xuất",
                                                      var_stx_app.check_logout, "Nhập số điện thoại để trải nghiệm ngay bây giờ !", "TaiKhoan_DangXuat.png")










