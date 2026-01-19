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
            action.wait_for(var_stx_app.driver_customer, var_stx_app.history, time_wait=1)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
            action.click(var_stx_app.driver_customer, var_stx_app.account_g7, time_wait=10)
            action.click(var_stx_app.driver_customer, var_stx_app.history_order_car, time_wait=10)
        try:
            action.wait_for(var_stx_app.driver_customer, var_stx_app.check_history_order_car, time_wait=10)
        except:
            pass



        module_other_stx_app.write_result_text_try_if(var_stx_app.driver_customer, code, eventname, result, "Tài khoản(g7) - Lịch sử đặt xe",
                                                      var_stx_app.check_history_order_car, "Lịch sử", "TaiKhoan_LichSuDatXe.png")



    def get_info_history_order_car(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

        var_stx_app.driver_customer.implicitly_wait(0.3)
        try:
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.check_history_order_car)
        except:
            history_order_car.history_order_car(self, "", "", "")

        #Tổng quan
        history_overview_date = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.history_overview_date).text  #Ngày/tháng/Năm
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 15, 2, history_overview_date)

        history_overview_type_car = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.history_overview_type_car).text  #Loại xe
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 16, 2, history_overview_type_car)

        history_overview_status = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.history_overview_status).text  #Trạng thái
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 17, 2, history_overview_status)

        history_overview_time = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.history_overview_time).text  #Giờ phút
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 18, 2, history_overview_time)

        history_overview_location_from = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.history_overview_location_from).text  #Điểm đón
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 19, 2, history_overview_location_from)

        history_overview_location_to = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.history_overview_location_to).text  #Điểm đến
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 20, 2, history_overview_location_to)

        history_overview_pttt = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.history_overview_pttt).text  #Phương thức thanh toán
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 21, 2, history_overview_pttt)


        #Chi tiết
        var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.get_info_history_order_car1).click()
        time.sleep(2.5)

        history_detail_date = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.history_detail_date).text  #Ngày/tháng/Năm - Giờ
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 15, 3, history_detail_date)

        history_detail_type_car = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.history_detail_type_car).text  #Loại xe
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 16, 3, history_detail_type_car)

        history_detail_location_from = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.history_detail_location_from).text  #Điểm đón
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 19, 3, history_detail_location_from)

        history_detail_location_to = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.history_detail_location_to).text  #Điểm đến
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 20, 3, history_detail_location_to)

        history_detail_pttt = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.history_detail_pttt).text  #Phương thức thanh toán
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 21, 3, history_detail_pttt)

        history_detail_km_money = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.history_detail_km_money).text  #Km - Số tiền
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 22, 3, history_detail_km_money)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Tài khoản(g7) - Lịch sử đặt xe")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("True")
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")



    def check_info_order_date(self, code, eventname, result):
        var_stx_app.open_app(var_stx_app.driver_customer)

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
        var_stx_app.open_app(var_stx_app.driver_customer)

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
        var_stx_app.open_app(var_stx_app.driver_customer)

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
        var_stx_app.open_app(var_stx_app.driver_customer)

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
        var_stx_app.open_app(var_stx_app.driver_customer)

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
        var_stx_app.open_app(var_stx_app.driver_customer)

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
        var_stx_app.open_app(var_stx_app.driver_customer)

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
        var_stx_app.open_app(var_stx_app.driver_customer)

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
        var_stx_app.open_app(var_stx_app.driver_customer)

        var_stx_app.driver_customer.implicitly_wait(0.3)
        try:
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.RE_ORDER)
        except:
            history_order_car.get_info_history_order_car(self, "", "", "")

        var_stx_app.driver_customer.implicitly_wait(3)
        #chi tiết cuốc
        location_from1 = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.history_detail_location_from).text
        location_to1 = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.history_detail_location_to).text
        var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.CALL_COMPANY)  #GỌI HÃNG
        var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.RE_ORDER).click()
        time.sleep(1.75)
        var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.ORDER_A_TO_B).click()
        time.sleep(3)

        check_location_from2 = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.location_1)))
        location_from2 = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.location_1).text
        location_to2 = var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.location_2).text

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
            var_stx_app.driver_customer.implicitly_wait(0.3)
            var_stx_app.driver_customer.find_element(By.XPATH, var_stx_app.order_car_back).click()
            time.sleep(2)
        except:
            pass









