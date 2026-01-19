import login_stx_app
import var_stx_app
import module_other_stx_app
import openpyxl
import homepage_g7
import favorite_spot_g7
import promotion_g7
import account_g7
import homepage_driver

path_user = var_stx_app.checklistpath
username = path_user.split("/")[2]
# print(username)






def get_datachecklist(code):
    wordbook = openpyxl.load_workbook(var_stx_app.checklistpath)
    sheet = wordbook.get_sheet_by_name("Checklist")
    rownum = 9
    while (rownum < 3000):
        rownum += 1
        rownum = str(rownum)
        if sheet["A" + rownum].value == code:
            tensukien = sheet["B" + rownum].value
            ketqua = sheet["E" + rownum].value
            print(tensukien)
            print(ketqua)
            module_other_stx_app.writeData(var_stx_app.path_luutamthoi, "Sheet1", 42, 2, tensukien)
            module_other_stx_app.writeData(var_stx_app.path_luutamthoi, "Sheet1", 43, 2, ketqua)
            return tensukien, ketqua
        rownum = int(rownum)




class CaseIdStxApp:

    def Login01(self):
        module_other_stx_app.get_datachecklist("Login01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        login_stx_app.g7.change_language(self, "Login01", eventname, result, var_stx_app.language2, "Do you have an account?", "_G7_DoiNgonNgu_TiengAnh.png")



    def Login02(self):
        module_other_stx_app.get_datachecklist("Login02")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        login_stx_app.g7.change_language(self, "Login02", eventname, result, var_stx_app.language3, "你有没有账号?", "_G7_DoiNgonNgu_TiengTrung.png")



    def Login03(self):
        module_other_stx_app.get_datachecklist("Login03")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        login_stx_app.g7.change_language(self, "Login03", eventname, result, var_stx_app.language4, "まだアカウントをお持ちではありませんか?", "_G7_DoiNgonNgu_TiengNhat.png")



    def Login04(self):
        module_other_stx_app.get_datachecklist("Login04")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        login_stx_app.g7.change_language(self, "Login04", eventname, result, var_stx_app.language5, "계정이 없나요?", "_G7_DoiNgonNgu_TiengHan.png")



    def Login05(self):
        module_other_stx_app.get_datachecklist("Login05")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        login_stx_app.g7.change_language(self, "Login05", eventname, result, var_stx_app.language1, "Bạn chưa có tài khoản?", "_G7_DoiNgonNgu_TiengViet.png")


    def Login06(self):
        module_other_stx_app.get_datachecklist("Login06")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        login_stx_app.g7.register(self, "Login06", eventname, result)


    def Login07(self):
        module_other_stx_app.get_datachecklist("Login07")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        login_stx_app.g7.login_sdt(self, "Login07", eventname, result, "0834219363", var_stx_app.check_phone_wrong, "Tôi đồng ý với Điều khoản sử dụng và Chính sách bảo mật dữ liệu cá nhân của ứng dụng G7",
                                   "_G7_DangNhap_SoDienThoaiSai.png")


    def Login08(self):
        module_other_stx_app.get_datachecklist("Login08")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        login_stx_app.g7.login_sdt(self, "Login08", eventname, result, "0359667694", var_stx_app.check_phone_correct, "Nhập mã với 4 chữ số đã gửi tới ***9667694",
                                   "_G7_DangNhap_SoDienThoaiDung.png")


    def Login09(self):
        module_other_stx_app.get_datachecklist("Login09")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        login_stx_app.driver_g7.check_login_driver_g7(self, "Login09", eventname, result, "auto372", "atgmj12345", "30A38711", var_stx_app.g7_driver_wrong,
                                   "Thông tin đăng nhập không đúng", "_LaiXeG7_DangNhapSai.png")


    def Login10(self):
        if username == "truongtq.BA":
            module_other_stx_app.get_datachecklist("Login10")
            eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
            result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
            login_stx_app.driver_g7.check_login_driver_g7(self, "Login10", eventname, result, "auto383", "atgmj123", "30A38753", var_stx_app.g7_driver_check_drive,
                                       "Đinh Mạnh Cường 92", "_LaiXeG7_DangNhapDung.png")

        else:
            module_other_stx_app.get_datachecklist("Login10")
            eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
            result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
            login_stx_app.driver_g7.check_login_driver_g7(self, "Login10", eventname, result, "auto376", "atgmj123", "30E03503", var_stx_app.g7_driver_check_drive,
                                       "Nguyễn Văn Tài 90 ", "_LaiXeG7_DangNhapDung.png")


    def HomePage01(self):
        module_other_stx_app.get_datachecklist("HomePage01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.icon_map(self, "HomePage01", eventname, result)


    def HomePage02(self):
        module_other_stx_app.get_datachecklist("HomePage02")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.icon_destination(self, "HomePage02", eventname, result, "Nhà riêng", var_stx_app.home_before, var_stx_app.home_before1,
                                               11, -1, "_TrangChu_NhaRieng.png")


    def HomePage03(self):
        module_other_stx_app.get_datachecklist("HomePage03")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.icon_destination(self, "HomePage03", eventname, result, "Cơ quan", var_stx_app.company_before, var_stx_app.company_before1,
                                               9, -1, "_TrangChu_CoQuan.png")


    def HomePage04(self):
        module_other_stx_app.get_datachecklist("HomePage04")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.icon_destination(self, "HomePage04", eventname, result, "Trường học", var_stx_app.school_before, var_stx_app.school_before1,
                                               12, -1, "_TrangChu_TruongHoc.png")



    def HomePage05(self):
        module_other_stx_app.get_datachecklist("HomePage05")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.icon_add_adress(self, "HomePage05", eventname, result)


    def HomePage06(self):
        module_other_stx_app.get_datachecklist("HomePage06")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_info_accout(self, "HomePage06", eventname, result, var_stx_app.change_account_sdt_name, var_stx_app.change_account_sdt_name_data,
                                                "Số điện thoại: ", "0359667694", "_TrangChu_ThayDoiTaiKhoan_SoDienThoai.png")

    def HomePage07(self):
        module_other_stx_app.get_datachecklist("HomePage07")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_info_accout(self, "HomePage07", eventname, result, var_stx_app.change_account_referral_name, var_stx_app.change_account_referral_data,
                                                "Mã giới thiệu của quý khách:", "0359667694", "_TrangChu_ThayDoiTaiKhoan_MaGioiThieu.png")

    def HomePage08(self):
        module_other_stx_app.get_datachecklist("HomePage08")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.change_accout_skip(self, "HomePage08", eventname, result)


    def HomePage09(self):
        module_other_stx_app.get_datachecklist("HomePage09")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.change_accout_update(self, "HomePage09", eventname, result)



    def HomePage10(self):
        pass
        # module_other_stx_app.get_datachecklist("HomePage10")
        # eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        # result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        # homepage_g7.home_page.icon_current_location(self, "HomePage10", eventname, result)



    def HomePage11(self):
        pass
        # module_other_stx_app.get_datachecklist("HomePage11")
        # eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        # result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        # homepage_g7.home_page.book_a_car_quickly(self, "HomePage11", eventname, result)


    def HomePage12(self):
        module_other_stx_app.get_datachecklist("HomePage12")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.icon_record(self, "HomePage12", eventname, result)


    def HomePage12_1(self):
        module_other_stx_app.get_datachecklist("HomePage12_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.icon_location_to(self, "HomePage12_1", eventname, result)


    def HomePage12_2(self):
        module_other_stx_app.get_datachecklist("HomePage12_2")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_location_from(self, "HomePage12_2", eventname, result)


    def HomePage13(self):
        module_other_stx_app.get_datachecklist("HomePage13")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.icon_destination1(self, "HomePage13", eventname, result)


    def HomePage14(self):
        module_other_stx_app.get_datachecklist("HomePage14")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.icon_pick_up_point(self, "HomePage14", eventname, result)


    def HomePage15(self):
        module_other_stx_app.get_datachecklist("HomePage15")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.edit_location(self, "HomePage15", eventname, result, var_stx_app.location_1, var_stx_app.search_location_input,
                                            "21 ô chợ dừa", var_stx_app.location_1, "21 Ô Chợ Dừa, phường Ô Chợ Dừa, thành phố Hà Nội",
                                            "_TrangChu_DatXe_DiemDon_Sua.png")


    def HomePage16(self):
        module_other_stx_app.get_datachecklist("HomePage16")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.edit_location(self, "HomePage16", eventname, result, var_stx_app.location_2, var_stx_app.search_location_input,
                                            "10 Mai Dịch", var_stx_app.location_2, "10 Mai Dịch, phường Phú Diễn, thành phố Hà Nội",
                                            "_TrangChu_DatXe_DiemDen_Sua.png")


    def HomePage17(self):
        module_other_stx_app.get_datachecklist("HomePage17")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.edit_location(self, "HomePage17", eventname, result, var_stx_app.location_2_icon, var_stx_app.search_location_input,
                                            "45 Đặng Văn Ngữ, phường Kim Liên, thành phố Hà Nội", var_stx_app.location_3, "45 Đặng Văn Ngữ, phường Kim Liên, thành phố Hà Nội",
                                            "_TrangChu_DatXe_ThemDiemThu2.png")

    def HomePage18(self):
        module_other_stx_app.get_datachecklist("HomePage18")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.icon_change_position_2_location(self, "HomePage18", eventname, result)


    def HomePage19(self):
        module_other_stx_app.get_datachecklist("HomePage19")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.icon_delete_location2(self, "HomePage19", eventname, result)


    def HomePage20(self):
        module_other_stx_app.get_datachecklist("HomePage20")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.icon_info_vehicle(self, "HomePage20", eventname, result)


    def HomePage21(self):
        module_other_stx_app.get_datachecklist("HomePage21")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.book_for_you(self, "HomePage21", eventname, result)


    def HomePage21_1(self):
        module_other_stx_app.get_datachecklist("HomePage21_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.Prioritize_highways(self, "HomePage21_1", eventname, result)


    def HomePage21_2(self):
        module_other_stx_app.get_datachecklist("HomePage21_2")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.Book(self, "HomePage21_2", eventname, result)



    def HomePage22(self):
        module_other_stx_app.get_datachecklist("HomePage22")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.book_car_cancel(self, "HomePage22", eventname, result)


    def HomePage23(self):
        module_other_stx_app.get_datachecklist("HomePage23")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.book_car_see_car(self, "HomePage23", eventname, result, "1")


    def HomePage24(self):
        module_other_stx_app.get_datachecklist("HomePage24")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.get_info_order(self, "HomePage24", eventname, result)


    def HomePage25(self):
        module_other_stx_app.get_datachecklist("HomePage25")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.order_car_icon(self, "HomePage25", eventname, result, "0", var_stx_app.order_car_icon_sos,  "",
                                             var_stx_app.order_car_icon_sos, "",  "_ManHinhDatCuoc_IconSOS.png")


    def HomePage26(self):
        module_other_stx_app.get_datachecklist("HomePage26")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.order_car_icon(self, "HomePage26", eventname, result, "3", var_stx_app.order_car_icon_location_current,
                                             "", var_stx_app.order_car_icon_location_current, "",  "_ManHinhDatCuoc_IconViTriHienTai.png")


    def HomePage27(self):
        module_other_stx_app.get_datachecklist("HomePage27")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.order_car_icon(self, "HomePage27", eventname, result, "1", var_stx_app.order_car_icon_fee,
                                             var_stx_app.order_car_icon_fee_x, var_stx_app.check_order_car_icon_fee,
                                             "Tổng tiền thanh toán",  "_ManHinhDatCuoc_IconCuocPhi.png")


    def HomePage28(self):
        module_other_stx_app.get_datachecklist("HomePage28")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.order_car_icon(self, "HomePage28", eventname, result, "1", var_stx_app.info_order_see_detail_b,
                                             var_stx_app.icon_back1, var_stx_app.check_order_car_see_detail,
                                             "Chi tiết chuyến đi",  "_ManHinhDatCuoc_XemChiTiet.png")

    def HomePage28_1(self):
        module_other_stx_app.get_datachecklist("HomePage28_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.order_car_icon(self, "HomePage28_1", eventname, result, "7", var_stx_app.order_car_issue_invoice,
                                             var_stx_app.icon_back1, var_stx_app.order_car_issue_invoice,
                                             "Tôi muốn xuất hóa đơn điện tử",  "_ManHinhDatCuoc_ToiMuonXuatHoaDonDienTu.png")



    def HomePage29(self):
        module_other_stx_app.get_datachecklist("HomePage29")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.order_car_icon(self, "HomePage29", eventname, result, "6", var_stx_app.report_safety_incidents,
                                             var_stx_app.icon_back1, var_stx_app.report_safety_incidents,
                                             "Báo cáo sự cố an toàn",  "_ManHinhDatCuoc_BaoCaoSuCoAnToan.png")

    def HomePage30(self):
        module_other_stx_app.get_datachecklist("HomePage30")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.order_car_icon(self, "HomePage30", eventname, result, "8", var_stx_app.share_trip,
                                             var_stx_app.icon_back1, var_stx_app.share_trip,
                                             "Chia sẻ chuyến đi",  "_ManHinhDatCuoc_ChiSeChuyenDi.png")



    def HomePage31(self):
        module_other_stx_app.get_datachecklist("HomePage31")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.order_car_icon(self, "HomePage31", eventname, result, "2", var_stx_app.overview_icon_show,
                                             var_stx_app.overview_icon_show, var_stx_app.space1, "",  "_ManHinhDatCuoc_IconAn.png")


    def HomePage32(self):
        module_other_stx_app.get_datachecklist("HomePage32")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_info_order_other(self, "HomePage32", eventname, result, 13, 2, "Thời gian dự kiến")


    def HomePage33(self):
        module_other_stx_app.get_datachecklist("HomePage33")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_info_order_distance(self, "HomePage33", eventname, result)


    def HomePage34(self):
        module_other_stx_app.get_datachecklist("HomePage34")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_info_order_fee(self, "HomePage34", eventname, result)


    def HomePage35(self):
        module_other_stx_app.get_datachecklist("HomePage35")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_info_order_promotion(self, "HomePage35", eventname, result)


    def HomePage36(self):
        module_other_stx_app.get_datachecklist("HomePage36")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_info_order_price(self, "HomePage36", eventname, result)


    def HomePage37(self):
        module_other_stx_app.get_datachecklist("HomePage37")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_info_order_location_from(self, "HomePage37", eventname, result)


    def HomePage38(self):
        module_other_stx_app.get_datachecklist("HomePage38")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_info_order_location_to(self, "HomePage38", eventname, result)


    def HomePage39(self):
        module_other_stx_app.get_datachecklist("HomePage39")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_info_order_star(self, "HomePage39", eventname, result)


    def HomePage40(self):
        module_other_stx_app.get_datachecklist("HomePage40")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_info_order_liscense_plate(self, "HomePage40", eventname, result)


    def HomePage41(self):
        module_other_stx_app.get_datachecklist("HomePage41")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_info_order_type_vehicle(self, "HomePage41", eventname, result)


    def HomePage42(self):
        module_other_stx_app.get_datachecklist("HomePage42")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_info_order_other(self, "HomePage42", eventname, result, 11, 4, "Tên lái xe")


    def HomePage42_1(self):
        module_other_stx_app.get_datachecklist("HomePage42_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_info_order_other(self, "HomePage42_1", eventname, result, 90, 4, "Số điện thoại")



    def HomePage43(self):
        module_other_stx_app.get_datachecklist("HomePage43")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_info_order_number(self, "HomePage43", eventname, result)



    def HomePage43_1(self):
        module_other_stx_app.get_datachecklist("HomePage43_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_info_order_color_vehicle(self, "HomePage43_1", eventname, result)


    def HomePage43_2(self):
        module_other_stx_app.get_datachecklist("HomePage43_2")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_info_order_call(self, "HomePage43_2", eventname, result)



    def HomePage44(self):
        module_other_stx_app.get_datachecklist("HomePage44")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_15(self, "HomePage44", eventname, result)



    def HomePage45(self):
        module_other_stx_app.get_datachecklist("HomePage45")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_20_order_100(self, "HomePage45", eventname, result, "14, Nguyễn Cảnh Dị hà nội", "17 Thụy Khuê tây hồ", "1")


    def HomePage46(self):
        module_other_stx_app.get_datachecklist("HomePage46")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_20_order_100(self, "HomePage46", eventname, result, "14, Nguyễn Cảnh Dị hà nội", "121 Đại Từ, phường định công", "0")


    def HomePage47(self):
        module_other_stx_app.get_datachecklist("HomePage47")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_20_max_50k(self, "HomePage47", eventname, result, "14, Nguyễn Cảnh Dị hà nội", "trà chanh bờ kè")


    def HomePage48(self):
        module_other_stx_app.get_datachecklist("HomePage48")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_20_max_50k(self, "HomePage48", eventname, result, "14, Nguyễn Cảnh Dị hà nội", "898 Chùa Láng hà nội")


    def HomePage49(self):
        module_other_stx_app.get_datachecklist("HomePage49")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_30_apply_for_customer(self, "HomePage49", eventname, result, "Trả tiền theo APP",
                                                             var_stx_app.check_book_a_car_clocktaxi, "Chương trình khuyến mại không hợp lệ, quý khách vui lòng xem thêm điều kiện áp dụng")



    def HomePage50(self):
        module_other_stx_app.get_datachecklist("HomePage50")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_30_apply_for_customer(self, "HomePage50", eventname, result, "Đồng hồ Taxi",
                                                             var_stx_app.check_book_a_car_quickly,
                                                             "G7 Taxi đang tìm kiếm lái xe. Bạn vui lòng đợi trong giây lát…")


    def HomePage51(self):
        module_other_stx_app.get_datachecklist("HomePage51")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_35_by_card(self, "HomePage51", eventname, result, "TIỀN MẶT")


    def HomePage52(self):
        module_other_stx_app.get_datachecklist("HomePage52")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_35_by_card(self, "HomePage52", eventname, result, "THẺ THÀNH VIÊN G7 TAXI")


    def HomePage53(self):
        module_other_stx_app.get_datachecklist("HomePage53")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_25_for_10km(self, "HomePage53", eventname, result, "duoi10km")


    def HomePage54(self):
        module_other_stx_app.get_datachecklist("HomePage54")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_25_for_10km(self, "HomePage54", eventname, result, "tren10km")


    def HomePage55(self):
        module_other_stx_app.get_datachecklist("HomePage55")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_30_inner_city(self, "HomePage55", eventname, result, "noithanh")


    def HomePage56(self):
        module_other_stx_app.get_datachecklist("HomePage56")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_30_inner_city(self, "HomePage56", eventname, result, "ngoaithanh")




    def HomePage57(self):
        module_other_stx_app.get_datachecklist("HomePage57")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_15k(self, "HomePage57", eventname, result)


    def HomePage58(self):
        module_other_stx_app.get_datachecklist("HomePage58")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_20k_order_100k(self, "HomePage58", eventname, result, "14, Nguyễn Cảnh Dị, hà nội", "103 Mai Dịch, hà nội", "1")


    def HomePage59(self):
        module_other_stx_app.get_datachecklist("HomePage59")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_20k_order_100k(self, "HomePage59", eventname, result, "14, Nguyễn Cảnh Dị, hà nội", "Giáp Bát, hà nội", "0")



    def HomePage60(self):
        module_other_stx_app.get_datachecklist("HomePage60")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_30k_apply_for_clock(self, "HomePage60", eventname, result, "Đồng hồ Taxi",
                                                            var_stx_app.check_book_a_car_quickly, "G7 Taxi đang tìm kiếm lái xe. Bạn vui lòng đợi trong giây lát…")

    def HomePage61(self):
        module_other_stx_app.get_datachecklist("HomePage61")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_30k_apply_for_clock(self, "HomePage61", eventname, result, "Trả tiền theo APP",
                                                            var_stx_app.check_book_a_car_clocktaxi, "Chương trình khuyến mại không hợp lệ, quý khách vui lòng xem thêm điều kiện áp dụng")

    def HomePage62(self):
        module_other_stx_app.get_datachecklist("HomePage62")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_35k_by_card(self, "HomePage62", eventname, result, "THẺ THÀNH VIÊN G7 TAXI")


    def HomePage63(self):
        module_other_stx_app.get_datachecklist("HomePage63")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_35k_by_card(self, "HomePage63", eventname, result, "TIỀN MẶT")


    def HomePage64(self):
        module_other_stx_app.get_datachecklist("HomePage64")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_50k_inner_city(self, "HomePage64", eventname, result, "noithanh")


    def HomePage65(self):
        module_other_stx_app.get_datachecklist("HomePage65")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.discount_50k_inner_city(self, "HomePage65", eventname, result, "ngoaithanh")



    def HomePage66(self):
        module_other_stx_app.get_datachecklist("HomePage66")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.book_car_inner_city(self, "HomePage66", eventname, result)



    def HomePage67(self):
        module_other_stx_app.get_datachecklist("HomePage67")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.book_car_inner_airport(self, "HomePage67", eventname, result)



    def HomePage68(self):
        module_other_stx_app.get_datachecklist("HomePage68")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.electronic_invoice_save(self, "HomePage68", eventname, result)



    def HomePage69(self):
        module_other_stx_app.get_datachecklist("HomePage69")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_electronic_invoice_customer(self, "HomePage69", eventname, result)


    def HomePage70(self):
        module_other_stx_app.get_datachecklist("HomePage70")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.home_page.check_electronic_invoice_drive(self, "HomePage70", eventname, result)




    def FavoriteSpot01(self):
        module_other_stx_app.get_datachecklist("FavoriteSpot01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        favorite_spot_g7.favorite_spot.check_location_home(self, "FavoriteSpot01", eventname, result)




    def FavoriteSpot02(self):
        module_other_stx_app.get_datachecklist("FavoriteSpot02")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        favorite_spot_g7.favorite_spot.search_spot_from(self, "FavoriteSpot02", eventname, result)


    def FavoriteSpot03(self):
        module_other_stx_app.get_datachecklist("FavoriteSpot03")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        favorite_spot_g7.favorite_spot.add_favorite_spot(self, "FavoriteSpot03", eventname, result)


    def FavoriteSpot04(self):
        module_other_stx_app.get_datachecklist("FavoriteSpot04")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        favorite_spot_g7.favorite_spot.choose_favorite_spot(self, "FavoriteSpot04", eventname, result)


    def FavoriteSpot05(self):
        module_other_stx_app.get_datachecklist("FavoriteSpot05")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        favorite_spot_g7.favorite_spot.favorite_edit(self, "FavoriteSpot05", eventname, result)


    def FavoriteSpot06(self):
        module_other_stx_app.get_datachecklist("FavoriteSpot06")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        favorite_spot_g7.favorite_spot.favorite_delete(self, "FavoriteSpot06", eventname, result)


    def FavoriteSpot07(self):
        module_other_stx_app.get_datachecklist("FavoriteSpot07")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        favorite_spot_g7.favorite_spot.favorite_spot_edit(self, "FavoriteSpot07", eventname, result, "Nhà riêng", "Điểm yêu thích(g7) - Nhà riêng",
                                                          var_stx_app.check_home_edit, "_DiemYeuThich_SuaNhaRieng.png")


    def FavoriteSpot08(self):
        module_other_stx_app.get_datachecklist("FavoriteSpot08")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        favorite_spot_g7.favorite_spot.select_spot_to(self, "FavoriteSpot08", eventname, result, "Nhà riêng", "Điểm yêu thích(g7) - Nhà riêng",
                                                          var_stx_app.location_2, 0, 9, "_DiemYeuThich_ChonNhaRieng.png")


    def FavoriteSpot09(self):
        module_other_stx_app.get_datachecklist("FavoriteSpot09")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        favorite_spot_g7.favorite_spot.favorite_spot_edit(self, "FavoriteSpot09", eventname, result, "Cơ quan", "Điểm yêu thích(g7) - Cơ quan",
                                                          var_stx_app.check_company_edit, "_DiemYeuThich_SuaCoQuan.png")


    def FavoriteSpot10(self):
        module_other_stx_app.get_datachecklist("FavoriteSpot10")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        favorite_spot_g7.favorite_spot.select_spot_to(self, "FavoriteSpot10", eventname, result, "Cơ quan", "Điểm yêu thích(g7) - Cơ quan",
                                                          var_stx_app.location_2, 0, 7, "_DiemYeuThich_ChonCoQuan.png")


    def FavoriteSpot11(self):
        module_other_stx_app.get_datachecklist("FavoriteSpot11")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        favorite_spot_g7.favorite_spot.favorite_spot_edit(self, "FavoriteSpot11", eventname, result, "Trường học", "Điểm yêu thích(g7) - Trường học",
                                                          var_stx_app.check_school_edit, "_DiemYeuThich_SuaTruongHoc.png")


    def FavoriteSpot12(self):
        module_other_stx_app.get_datachecklist("FavoriteSpot12")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        favorite_spot_g7.favorite_spot.select_spot_to(self, "FavoriteSpot12", eventname, result, "Trường học", "Điểm yêu thích(g7) - Trường học",
                                                          var_stx_app.location_2, 0, 10, "_DiemYeuThich_ChonTruongHoc.png")


    def Promotion01(self):
        module_other_stx_app.get_datachecklist("Promotion01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        promotion_g7.promotion.use_now(self, "Promotion01", eventname, result)


    def Promotion02(self):
        module_other_stx_app.get_datachecklist("Promotion02")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        promotion_g7.promotion.check_info_promotion(self, "Promotion02", eventname, result, var_stx_app.promotion_name, "_KhuyenMai_Ten.png")


    def Promotion03(self):
        module_other_stx_app.get_datachecklist("Promotion03")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        promotion_g7.promotion.check_info_promotion(self, "Promotion03", eventname, result, var_stx_app.promotion_decrease, "_KhuyenMai_Giam.png")


    def Promotion04(self):
        module_other_stx_app.get_datachecklist("Promotion04")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        promotion_g7.promotion.check_info_promotion(self, "Promotion04", eventname, result, var_stx_app.promotion_code, "_KhuyenMai_MaGiamGia.png")


    def Promotion05(self):
        module_other_stx_app.get_datachecklist("Promotion05")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        promotion_g7.promotion.check_info_promotion(self, "Promotion05", eventname, result, var_stx_app.promotion_expiration_date, "_KhuyenMai_NgayHetHan.png")


    def Promotion06(self):
        module_other_stx_app.get_datachecklist("Promotion06")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        promotion_g7.promotion.check_info_promotion(self, "Promotion06", eventname, result, var_stx_app.promotion_apply, "_KhuyenMai_HangApDung.png")


    def Promotion07(self):
        module_other_stx_app.get_datachecklist("Promotion07")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        promotion_g7.promotion.check_info_promotion(self, "Promotion07", eventname, result, var_stx_app.promotion_time_use, "_KhuyenMai_SoLanSuDung.png")


    def Account01(self):
        module_other_stx_app.get_datachecklist("Account01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.info_account.icon_edit(self, "Account01", eventname, result)



    def Account02(self):
        module_other_stx_app.get_datachecklist("Account02")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.info_account.check_info_account(self, "Account02", eventname, result)



    def Account03(self):
        module_other_stx_app.get_datachecklist("Account03")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.history_order_car(self, "Account03", eventname, result)


    def Account04(self):
        module_other_stx_app.get_datachecklist("Account04")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.get_info_history_order_car(self, "Account04", eventname, result)


    def Account05(self):
        module_other_stx_app.get_datachecklist("Account05")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.check_info_order_date(self, "Account05", eventname, result)


    def Account06(self):
        module_other_stx_app.get_datachecklist("Account06")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.check_info_order_type_vehicle(self, "Account06", eventname, result)


    def Account07(self):
        module_other_stx_app.get_datachecklist("Account07")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.check_info_order_status(self, "Account07", eventname, result)


    def Account08(self):
        module_other_stx_app.get_datachecklist("Account08")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.check_info_order_time(self, "Account08", eventname, result)


    def Account09(self):
        module_other_stx_app.get_datachecklist("Account09")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.check_info_order_locationfrom(self, "Account09", eventname, result)


    def Account10(self):
        module_other_stx_app.get_datachecklist("Account10")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.check_info_order_locationto(self, "Account10", eventname, result)


    def Account11(self):
        module_other_stx_app.get_datachecklist("Account11")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.check_info_order_pttt(self, "Account11", eventname, result)


    def Account12(self):
        module_other_stx_app.get_datachecklist("Account12")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.check_info_order_km_money(self, "Account12", eventname, result)



    def Account12_1(self):
        module_other_stx_app.get_datachecklist("Account12_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.check_info_order_other(self, "Account12_1", eventname, result, "Số hiệu - Biển số xe", 32)


    def Account12_2(self):
        module_other_stx_app.get_datachecklist("Account12_2")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.check_info_order_other(self, "Account12_2", eventname, result, "Tên lái xe - Công ty", 33)


    def Account12_3(self):
        module_other_stx_app.get_datachecklist("Account12_3")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.check_info_order_other(self, "Account12_3", eventname, result, "Số điện thoại", 34)


    def Account12_4(self):
        module_other_stx_app.get_datachecklist("Account12_4")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.check_info_order_other(self, "Account12_4", eventname, result, "Thời gian thực hiện", 35)



    def Account12_5(self):
        module_other_stx_app.get_datachecklist("Account12_5")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.info_order_icon_payment(self, "Account12_5", eventname, result)


    def Account12_6(self):
        module_other_stx_app.get_datachecklist("Account12_6")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.info_order_icon_hd(self, "Account12_6", eventname, result)



    def Account13(self):
        module_other_stx_app.get_datachecklist("Account13")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.call_company(self, "Account13", eventname, result)


    def Account13_1(self):
        module_other_stx_app.get_datachecklist("Account13_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.history_order_car.re_order(self, "Account13_1", eventname, result)


    def Account14(self):
        module_other_stx_app.get_datachecklist("Account14")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.notification.notification(self, "Account14", eventname, result)


    def Account15(self):
        module_other_stx_app.get_datachecklist("Account15")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.membership_card(self, "Account15", eventname, result)


    def Account16(self):
        module_other_stx_app.get_datachecklist("Account16")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_membership_card(self, "Account16", eventname, result, var_stx_app.membership_card_serial,
                                                              var_stx_app.membership_card_serial1, "TaiKhoan_TheThanhVien_SoSerial.png")

    def Account17(self):
        module_other_stx_app.get_datachecklist("Account17")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_membership_card(self, "Account17", eventname, result, var_stx_app.membership_card_name,
                                                              var_stx_app.membership_card_name1, "TaiKhoan_TheThanhVien_TenKhachHang.png")

    def Account18(self):
        module_other_stx_app.get_datachecklist("Account18")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_membership_card(self, "Account18", eventname, result, var_stx_app.membership_card_expired,
                                                              var_stx_app.membership_card_expired1, "TaiKhoan_TheThanhVien_HetHan.png")


    def Account19(self):
        module_other_stx_app.get_datachecklist("Account19")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_membership_card(self, "Account19", eventname, result, var_stx_app.membership_card_rank,
                                                              var_stx_app.membership_card_rank1, "TaiKhoan_TheThanhVien_Hang.png")


    def Account20(self):
        module_other_stx_app.get_datachecklist("Account20")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_membership_card(self, "Account20", eventname, result, var_stx_app.membership_card_tkchinh,
                                                              var_stx_app.membership_card_tkchinh, "TaiKhoan_TheThanhVien_TkChinh.png")


    def Account21(self):
        module_other_stx_app.get_datachecklist("Account21")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_membership_card(self, "Account21", eventname, result, var_stx_app.membership_card_tkphu,
                                                              var_stx_app.membership_card_tkphu, "TaiKhoan_TheThanhVien_TkPhu.png")

    def Account22(self):
        module_other_stx_app.get_datachecklist("Account22")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.scan_qrcode(self, "Account22", eventname, result)


    def Account23(self):
        module_other_stx_app.get_datachecklist("Account23")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.reload_the_card(self, "Account23", eventname, result)


    def Account24(self):
        module_other_stx_app.get_datachecklist("Account24")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_reload_the_card(self, "Account24", eventname, result, var_stx_app.reload_the_card_chutk_name, var_stx_app.reload_the_card_chutk_data,
                                                              "Chủ tài khoản:", "TheThanhVien_NapTienVaoThe_ChuTaiKhoan.png")

    def Account25(self):
        module_other_stx_app.get_datachecklist("Account25")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_reload_the_card(self, "Account25", eventname, result, var_stx_app.reload_the_card_stk_name, var_stx_app.reload_the_card_stk_data,
                                                              "Số tài khoản:", "TheThanhVien_NapTienVaoThe_SoTaiKhoan.png")

    def Account26(self):
        module_other_stx_app.get_datachecklist("Account26")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_reload_the_card_bank(self, "Account26", eventname, result)


    def Account27(self):
        module_other_stx_app.get_datachecklist("Account27")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_icon_membership_card_new(self, "Account27", eventname, result, var_stx_app.qr_coppy, "Đã sao chép vào bộ nhớ tạm.", "Sao chép thành công:",
                                                              "TheThanhVien_NapTienVaoThe_IconCoppy.png")

    def Account28(self):
        module_other_stx_app.get_datachecklist("Account28")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_icon_membership_card_new(self, "Account28", eventname, result, var_stx_app.qr_save, "Lưu ảnh thành công!", "Đã sao chép vào bộ nhớ tạm.",
                                                              "TheThanhVien_NapTienVaoThe_LưuMaQrCode.png")

    def Account29(self):
        module_other_stx_app.get_datachecklist("Account29")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_icon_help_membership_card(self, "Account29", eventname, result)


    def Account30(self):
        module_other_stx_app.get_datachecklist("Account30")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.donate_money(self, "Account30", eventname, result)


    def Account31(self):
        module_other_stx_app.get_datachecklist("Account31")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.give_money_to_others(self, "Account31", eventname, result)


    def Account32(self):
        module_other_stx_app.get_datachecklist("Account32")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.history_car(self, "Account32", eventname, result)


    def Account33(self):
        module_other_stx_app.get_datachecklist("Account33")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_history_car(self, "Account33", eventname, result, 130, "TheThanhVien_LichSuThe_TaiKhoanChinh1.png")


    def Account34(self):
        module_other_stx_app.get_datachecklist("Account34")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_history_car(self, "Account34", eventname, result, 131, "TheThanhVien_LichSuThe_Trangthai.png")


    def Account35(self):
        module_other_stx_app.get_datachecklist("Account35")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_history_car(self, "Account35", eventname, result, 132, "TheThanhVien_LichSuThe_ThoiGian.png")


    def Account36(self):
        module_other_stx_app.get_datachecklist("Account36")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_history_car(self, "Account36", eventname, result, 133, "TheThanhVien_LichSuThe_SoTien.png")


    def Account37(self):
        module_other_stx_app.get_datachecklist("Account37")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_history_car(self, "Account37", eventname, result, 134, "TheThanhVien_LichSuThe_SoDuThe.png")


    def Account38(self):
        module_other_stx_app.get_datachecklist("Account38")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_history_car(self, "Account38", eventname, result, 135, "TheThanhVien_LichSuThe_ThongTinXe.png")


    def Account39(self):
        module_other_stx_app.get_datachecklist("Account39")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_history_car(self, "Account39", eventname, result, 136, "TheThanhVien_LichSuThe_DiemDon.png")


    def Account40(self):
        module_other_stx_app.get_datachecklist("Account40")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_history_car(self, "Account40", eventname, result, 137, "TheThanhVien_LichSuThe_DiemDen.png")


    def Account40_1(self):
        module_other_stx_app.get_datachecklist("Account40_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_info_history_car(self, "Account40_1", eventname, result, 138, "TheThanhVien_LichSuThe_GhiChu.png")


    def Account41(self):
        module_other_stx_app.get_datachecklist("Account41")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.info_pin(self, "Account41", eventname, result)


    def Account42(self):
        module_other_stx_app.get_datachecklist("Account42")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.change_pin_code(self, "Account42", eventname, result)



    def Account43(self):
        module_other_stx_app.get_datachecklist("Account43")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.membership_card.check_change_pin_code(self, "Account43", eventname, result)



    def Account44(self):
        module_other_stx_app.get_datachecklist("Account44")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.verify_account.verify_account(self, "Account44", eventname, result)


    def Account45(self):
        module_other_stx_app.get_datachecklist("Account45")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.verify_account.check_info_verify_account1(self, "Account45", eventname, result, "Tên khách hàng",
                                                             "_XacMinhtaiKhoanDaGioiThieu_TenKhachHang.png")


    def Account46(self):
        module_other_stx_app.get_datachecklist("Account46")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.verify_account.check_info_verify_account1(self, "Account46", eventname, result, "Số điện thoại",
                                                             "_XacMinhtaiKhoanDaGioiThieu_SoDienThoai.png")


    def Account47(self):
        module_other_stx_app.get_datachecklist("Account47")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.verify_account.check_info_verify_account(self, "Account47", eventname, result, "0", var_stx_app.verify_account_code_introduce,
                                                              "", "_XacMinhtaiKhoanDaGioiThieu_MaGioiThieu.png")


    def Account48(self):
        module_other_stx_app.get_datachecklist("Account48")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.verify_account.check_info_verify_account(self, "Account48", eventname, result, "1", var_stx_app.cancel,
                                                              "Từ chối", "_XacMinhtaiKhoanDaGioiThieu_TuChoi.png")


    def Account49(self):
        module_other_stx_app.get_datachecklist("Account49")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.verify_account.check_info_verify_account(self, "Account49", eventname, result, "1", var_stx_app.confirm1,
                                                              "Xác nhận", "_XacMinhtaiKhoanDaGioiThieu_XacNhan.png")


    def Account50(self):
        module_other_stx_app.get_datachecklist("Account50")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.comment.comment(self, "Account50", eventname, result)


    def Account50_1(self):
        module_other_stx_app.get_datachecklist("Account50_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.comment.upload_image(self, "Account50_1", eventname, result)


    def Account51(self):
        module_other_stx_app.get_datachecklist("Account51")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.comment.hotline(self, "Account51", eventname, result)


    def Account51_1(self):
        module_other_stx_app.get_datachecklist("Account51_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.comment.send_comment(self, "Account51_1", eventname, result)


    def Account51_2(self):
        module_other_stx_app.get_datachecklist("Account51_2")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.switchboard_cskh.switchboard_cskh(self, "Account51_2", eventname, result)



    def Account52(self):
        module_other_stx_app.get_datachecklist("Account52")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.language.language(self, "Account52", eventname, result, var_stx_app.language_english,
                                     'Bạn có muốn chọn ngôn ngữ "Tiếng Anh - English" này không?', "TaiKhoan_NgonNgu_TiengAnh.png")


    def Account53(self):
        module_other_stx_app.get_datachecklist("Account53")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.language.language(self, "Account53", eventname, result, var_stx_app.language_china,
                                     'Bạn có muốn chọn ngôn ngữ "Tiếng Trung - 中国語" này không?', "TaiKhoan_NgonNgu_TiengTrung.png")


    def Account54(self):
        module_other_stx_app.get_datachecklist("Account54")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.language.language(self, "Account54", eventname, result, var_stx_app.language_japan,
                                     'Bạn có muốn chọn ngôn ngữ "Tiếng Nhật - 日本語" này không?', "TaiKhoan_NgonNgu_TiengNhat.png")


    def Account55(self):
        module_other_stx_app.get_datachecklist("Account55")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.language.language(self, "Account55", eventname, result, var_stx_app.language_korea,
                                     'Bạn có muốn chọn ngôn ngữ "Tiếng Hàn - 한국인" này không?', "TaiKhoan_NgonNgu_TiengHan.png")


    def Account56(self):
        module_other_stx_app.get_datachecklist("Account56")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.language.language(self, "Account56", eventname, result, var_stx_app.language_vietnam,
                                     "Tiếng Việt - Tiếng Việt", "TaiKhoan_NgonNgu_TiengViet.png")


    def Account57(self):
        module_other_stx_app.get_datachecklist("Account57")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.introduce_share.introduce_share(self, "Account57", eventname, result)


    def Account58(self):
        module_other_stx_app.get_datachecklist("Account58")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.introduce_share.introduce_share_button(self, "Account58", eventname, result, var_stx_app.REVIEW, "0", var_stx_app.REVIEW,
                                                          "ĐÁNH GIÁ", "_GioiThieuChiaSe_DanhGia.png")


    def Account59(self):
        module_other_stx_app.get_datachecklist("Account59")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.introduce_share.introduce_share_button(self, "Account59", eventname, result, var_stx_app.SHARE, "1", var_stx_app.check_SHARE,
                                                          "Messaging", "_GioiThieuChiaSe_ChiaSe.png")


    def Account60(self):
        module_other_stx_app.get_datachecklist("Account60")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.support.support(self, "Account60", eventname, result)



    def Account61(self):
        module_other_stx_app.get_datachecklist("Account61")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.support.support_link(self, "Account61", eventname, result, var_stx_app.support_button1, var_stx_app.check_support_button,
                                        "Bạn có thể chọn loại xe bằng cách chạm vào biểu tượng của loại xe tương ứng. Loại xe được chọn sẽ được hiển thị nổi bật hơn.",
                                        "HoTro_ChonLoaiXe.png")


    def Account62(self):
        module_other_stx_app.get_datachecklist("Account62")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.support.support_link(self, "Account62", eventname, result, var_stx_app.support_button2, var_stx_app.check_support_button,
                                        "Cách 1: Di chuyển bản đồ tới vị trí mà bạn mong muốn. Sau đó, bấm vào “Chọn điểm đón” để xác nhận. Bạn cũng có thể đổi vị trí",
                                        "HoTro_ChonDiemDonDiemDen.png")


    def Account63(self):
        module_other_stx_app.get_datachecklist("Account63")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.support.support_link(self, "Account63", eventname, result, var_stx_app.support_button3, var_stx_app.check_support_button,
                                        "Thông tin đặt xe của bạn sẽ được hiển thị trên màn hình. Tại đây, bạn có thể:",
                                        "HoTro_XacNhanThongTin.png")


    def Account64(self):
        module_other_stx_app.get_datachecklist("Account64")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.support.support_link(self, "Account64", eventname, result, var_stx_app.support_button4, var_stx_app.check_support_button,
                                        "- Taxi Dùng Thử sẽ tiến hành tìm kiếm lái xe gần nhất thỏa mãn yêu cầu của bạn.",
                                        "HoTro_ThongTinLaiXe.png")


    def Account65(self):
        module_other_stx_app.get_datachecklist("Account65")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.support.support_link(self, "Account65", eventname, result, var_stx_app.support_button5, var_stx_app.check_support_button,
                                        "- Khi lái xe đã đón bạn, vui lòng bấm “Gặp xe” để lái xe xác nhận đã đón đúng bạn.", "HoTro_HoanThanhChuyenDi.png")


    def Account66(self):
        module_other_stx_app.get_datachecklist("Account66")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.support.support_link(self, "Account66", eventname, result, var_stx_app.support_button6, var_stx_app.check_support_button,
                                        "- Sau khi đặt lịch thành công, ứng dụng sẽ luôn hiển thị “Có lịch đặt” trên menu cho đến khi hết hạn hoặc bị hủy.",
                                        "HoTro_NhacNho.png")


    def Account67(self):
        module_other_stx_app.get_datachecklist("Account67")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.support.support_link(self, "Account67", eventname, result, var_stx_app.support_button7, var_stx_app.check_support_button,
                                        "- Chuyến đặt lịch khả dụng sẽ được đặt trên đầu danh sách cùng với trạng thái “Đặt lịch” màu xanh.",
                                        "HoTro_ChuyenDatLich.png")


    def Account68(self):
        module_other_stx_app.get_datachecklist("Account68")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.support.support_link(self, "Account68", eventname, result, var_stx_app.support_button8, var_stx_app.check_support_button,
                                        "- Thông tin chi tiết của chuyến đặt lịch sẽ được hiển thị.", "HoTro_HuyChuyenDi.png")


    def Account69(self):
        module_other_stx_app.get_datachecklist("Account69")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.support.support_link_app(self, "Account69", eventname, result, var_stx_app.support_button9, var_stx_app.support_button9,
                                        var_stx_app.support_button9, "HoTro_CapNhatPhanMemTrenAndroid.png")


    def Account70(self):
        module_other_stx_app.get_datachecklist("Account70")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.support.support_link_app(self, "Account70", eventname, result, var_stx_app.support_button10, var_stx_app.support_button10,
                                        var_stx_app.support_button10, "HoTro_CapNhatPhanMemTrenIOS.png")


    def Account71(self):
        module_other_stx_app.get_datachecklist("Account71")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        account_g7.logout.logout(self, "Account71", eventname, result)





    def App01(self):
        module_other_stx_app.get_datachecklist("App01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.web_app.search_tax_code(self, "App01", eventname, result)


    def App02(self):
        module_other_stx_app.get_datachecklist("App02")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.web_app.fill_electronic_invoice(self, "App02", eventname, result)


    def App03(self):
        module_other_stx_app.get_datachecklist("App03")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.web_app.not_fill_electronic_invoice(self, "App03", eventname, result)


    def App04(self):
        module_other_stx_app.get_datachecklist("App04")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.web_app.card_company_auto_export(self, "App04", eventname, result, var_stx_app.data['web_app']['address3'],
                                                     "8880999016579311", "_XuatHoaDonDienTu_case3.png")


    def App05(self):
        module_other_stx_app.get_datachecklist("App05")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.web_app.card_company_auto_export(self, "App05", eventname, result, var_stx_app.data['web_app']['address4'],
                                                     "9999992992097925", "_XuatHoaDonDienTu_case4.png")



    def Home01(self):
        module_other_stx_app.get_datachecklist("Home01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.waiting_for_a_passenger(self, "Home01", eventname, result)


    def Home02(self):
        module_other_stx_app.get_datachecklist("Home02")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_display_icon(self, "Home02", eventname, result, var_stx_app.icon_wifi,
                                                                   "_TrangChu_IconWifi.png")


    def Home03(self):
        module_other_stx_app.get_datachecklist("Home03")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_display_icon_current_location(self, "Home03", eventname, result)


    def Home04(self):
        module_other_stx_app.get_datachecklist("Home04")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_display_icon_traffic_light(self, "Home04", eventname, result)


    def Home05(self):
        module_other_stx_app.get_datachecklist("Home05")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_display_icon_xeplot(self, "Home05", eventname, result)


    def Home06(self):
        module_other_stx_app.get_datachecklist("Home06")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_display_icon_cuocpho(self, "Home06", eventname, result)


    def Home07(self):
        module_other_stx_app.get_datachecklist("Home07")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_icon_help(self, "Home07", eventname, result)


    def Home08(self):
        module_other_stx_app.get_datachecklist("Home08")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.status(self, "Home08", eventname, result, "ĐÃ NGHỈ", "_TrangChu_DaNghi.png")


    def Home09(self):
        module_other_stx_app.get_datachecklist("Home09")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.status(self, "Home09", eventname, result, "SẴN SÀNG", "_TrangChu_SanSang.png")



    def Home09_1(self):
        module_other_stx_app.get_datachecklist("Home09_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_location_car(self, "Home09_1", eventname, result)


    def Home09_2(self):
        module_other_stx_app.get_datachecklist("Home09_2")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_over_map(self, "Home09_2", eventname, result)



    def Home10(self):
        module_other_stx_app.get_datachecklist("Home10")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.get_info_drive(self, "Home10", eventname, result)


    def Home11(self):
        module_other_stx_app.get_datachecklist("Home11")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_info_drive_name(self, "Home11", eventname, result)


    def Home12(self):
        module_other_stx_app.get_datachecklist("Home12")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_info_drive_type_vehicle(self, "Home12", eventname, result)


    def Home13(self):
        module_other_stx_app.get_datachecklist("Home13")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_info_drive_version(self, "Home13", eventname, result)


    def Home14(self):
        module_other_stx_app.get_datachecklist("Home14")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_info_drive_star(self, "Home14", eventname, result)


    def Home15(self):
        module_other_stx_app.get_datachecklist("Home15")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_info_drive_liscense_plate(self, "Home15", eventname, result)


    def Home16(self):
        module_other_stx_app.get_datachecklist("Home16")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.change_password(self, "Home16", eventname, result)


    def Home17(self):
        module_other_stx_app.get_datachecklist("Home17")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.driver_dispatching(self, "Home17", eventname, result)


    def Home18(self):
        module_other_stx_app.get_datachecklist("Home18")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.binhanh_parking_lot(self, "Home18", eventname, result)


    def Home19(self):
        module_other_stx_app.get_datachecklist("Home19")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_info_binhanh_parking_lot(self, "Home19", eventname, result, "0", var_stx_app.binhanh_parking_lot_parking_lot,
                                                                               "_SanhBinhAnh_BaiCho.png")


    def Home20(self):
        module_other_stx_app.get_datachecklist("Home20")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_info_binhanh_parking_lot(self, "Home20", eventname, result, "0", var_stx_app.binhanh_parking_lot_stt1,
                                                                               "_SanhBinhAnh_SoThuTu.png")

    def Home21(self):
        module_other_stx_app.get_datachecklist("Home21")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_info_binhanh_parking_lot(self, "Home21", eventname, result, "0", var_stx_app.binhanh_parking_lot_type_vehicle,
                                                                               "_SanhBinhAnh_LoaiXe.png")

    def Home22(self):
        module_other_stx_app.get_datachecklist("Home22")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_info_binhanh_parking_lot(self, "Home22", eventname, result, "0", var_stx_app.binhanh_parking_lot_stt2,
                                                                               "_SanhBinhAnh_STT.png")

    def Home23(self):
        module_other_stx_app.get_datachecklist("Home23")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_info_binhanh_parking_lot(self, "Home23", eventname, result, "0", var_stx_app.binhanh_parking_lot_code_dam,
                                                                               "_SanhBinhAnh_MaDam.png")

    def Home24(self):
        module_other_stx_app.get_datachecklist("Home24")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_info_binhanh_parking_lot(self, "Home24", eventname, result, "1", var_stx_app.binhanh_parking_lot_location,
                                                                               "_SanhBinhAnh_ViTritruc.png")


    def Home25(self):
        module_other_stx_app.get_datachecklist("Home25")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.cancel_drive(self, "Home25", eventname, result)


    def Home25_1(self):
        module_other_stx_app.get_datachecklist("Home25_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.driver_dispatching_create_order(self, "Home25_1", eventname, result)


    def Home26(self):
        module_other_stx_app.get_datachecklist("Home26")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.create_order(self, "Home26", eventname, result)


    def Home27(self):
        module_other_stx_app.get_datachecklist("Home27")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.create_order_back(self, "Home27", eventname, result)



    def Home28(self):
        module_other_stx_app.get_datachecklist("Home28")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.create_order_search(self, "Home28", eventname, result, "diachidon", var_stx_app.create_order_location1_input,
                                                                    "Ngõ 115 Hồng Hà", var_stx_app.check_create_order_location1, "Ngõ 115 Đường Hồng Hà", "_TaoCuoc_DiaChiDon.png")


    def Home29(self):
        module_other_stx_app.get_datachecklist("Home29")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.create_order_search(self, "Home29", eventname, result, "diachitra", var_stx_app.create_order_location2_input,
                                                                    "214 Bạch Mai", var_stx_app.check_create_order_location2, "214 Bạch Mai", "_TaoCuoc_DiaChiTra.png")



    def Home30(self):
        module_other_stx_app.get_datachecklist("Home30")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.create_order_note(self, "Home30", eventname, result)


    def Home30_1(self):
        module_other_stx_app.get_datachecklist("Home30_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.create_order_type(self, "Home30_1", eventname, result)


    def Home31(self):
        module_other_stx_app.get_datachecklist("Home31")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.create_order_icon_wifi(self, "Home31", eventname, result)


    def Home32(self):
        module_other_stx_app.get_datachecklist("Home32")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.create_order_icon_location(self, "Home32", eventname, result)


    def Home33(self):
        module_other_stx_app.get_datachecklist("Home33")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.create_order_icon_trafic(self, "Home33", eventname, result)


    def Home34(self):
        module_other_stx_app.get_datachecklist("Home34")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.create_order_create_order(self, "Home34", eventname, result)


    def Home35(self):
        module_other_stx_app.get_datachecklist("Home35")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.create_order_see_route(self, "Home35", eventname, result)


    def Home36(self):
        module_other_stx_app.get_datachecklist("Home36")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.create_order_see_route_icon(self, "Home36", eventname, result, "0",
                                                                            var_stx_app.see_route_location1, "_TaoCuoc_XemLoTrinh_DiemDon.png")


    def Home37(self):
        module_other_stx_app.get_datachecklist("Home37")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.create_order_see_route_icon(self, "Home37", eventname, result, "0",
                                                                            var_stx_app.see_route_location2, "_TaoCuoc_XemLoTrinh_DiemTra.png")

    def Home38(self):
        module_other_stx_app.get_datachecklist("Home38")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.create_order_see_route_icon(self, "Home38", eventname, result, "2",
                                                                            var_stx_app.see_route_icon_wifi, "_TaoCuoc_XemLoTrinh_IconWifi.png")


    def Home39(self):
        module_other_stx_app.get_datachecklist("Home39")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.create_order_see_route_icon(self, "Home39", eventname, result, "0",
                                                                            var_stx_app.see_route_icon_location, "_TaoCuoc_XemLoTrinh_IconViTriHienTai.png")


    def Home40(self):
        module_other_stx_app.get_datachecklist("Home40")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.create_order_see_route_icon(self, "Home40", eventname, result, "0",
                                                                            var_stx_app.see_route_icon_traffic_light, "_TaoCuoc_XemLoTrinh_IconDenGiaoThong.png")

    def Home41(self):
        module_other_stx_app.get_datachecklist("Home41")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.create_order_see_route_icon(self, "Home41", eventname, result, "1",
                                                                            var_stx_app.see_route_icon_navigation, "_TaoCuoc_XemLoTrinh_IconDieuHuong.png")


    def Home42(self):
        pass
        # module_other_stx_app.get_datachecklist("Home42")
        # eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        # result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        # homepage_driver.waiting_for_a_passenger.see_route_search_location2(self, "Home42", eventname, result)


    def Home42_1(self):
        module_other_stx_app.get_datachecklist("Home42_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.get_info_g7taxihn(self, "Home42_1", eventname, result)



    def Home42_2(self):
        module_other_stx_app.get_datachecklist("Home42_2")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_get_info_g7taxihn_other(self, "Home42_2", eventname, result, "K.Cách", 94)


    def Home42_3(self):
        module_other_stx_app.get_datachecklist("Home42_3")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_get_info_g7taxihn_other(self, "Home42_3", eventname, result, "TG chờ", 95)


    def Home42_4(self):
        module_other_stx_app.get_datachecklist("Home42_4")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_get_info_g7taxihn_number_money(self, "Home42_4", eventname, result)




    def Home42_5(self):
        module_other_stx_app.get_datachecklist("Home42_5")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_get_info_g7taxihn_other(self, "Home42_5", eventname, result, "Cước di chuyển", 97)



    def Home42_6(self):
        module_other_stx_app.get_datachecklist("Home42_6")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_get_info_g7taxihn_other(self, "Home42_6", eventname, result, "Khoảng cách", 98)


    def Home42_7(self):
        module_other_stx_app.get_datachecklist("Home42_7")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_get_info_g7taxihn_other(self, "Home42_7", eventname, result, "Cước chờ", 99)


    def Home42_8(self):
        module_other_stx_app.get_datachecklist("Home42_8")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_get_info_g7taxihn_other(self, "Home42_8", eventname, result, "Thời gian chờ", 100)



    def Home43(self):
        module_other_stx_app.get_datachecklist("Home43")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.see_route_drop_off_passengers(self, "Home43", eventname, result)


    def Home43_1(self):
        module_other_stx_app.get_datachecklist("Home43_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.add_money_fee(self, "Home43_1", eventname, result)



    def Home44(self):
        module_other_stx_app.get_datachecklist("Home44")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.add_fee(self, "Home44", eventname, result)


    def Home45(self):
        module_other_stx_app.get_datachecklist("Home45")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.add_fee_edit(self, "Home45", eventname, result)


    def Home46(self):
        module_other_stx_app.get_datachecklist("Home46")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.add_fee_delete(self, "Home46", eventname, result)



    def Home47(self):
        module_other_stx_app.get_datachecklist("Home47")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.collected_from_customers1(self, "Home47", eventname, result)



    def Home48(self):
        module_other_stx_app.get_datachecklist("Home48")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.cash(self, "Home48", eventname, result)



    def Home48_1(self):
        module_other_stx_app.get_datachecklist("Home48_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_info_end(self, "Home48_1", eventname, result)



    def Home48_2(self):
        module_other_stx_app.get_datachecklist("Home48_2")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.scan_qr(self, "Home48_2", eventname, result)


    def Home48_3(self):
        module_other_stx_app.get_datachecklist("Home48_3")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.fill_sec(self, "Home48_3", eventname, result)


    def Home48_4(self):
        module_other_stx_app.get_datachecklist("Home48_4")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_info_sec(self, "Home48_4", eventname, result)


    def Home48_5(self):
        module_other_stx_app.get_datachecklist("Home48_5")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.info_sec_hd(self, "Home48_5", eventname, result)


    def Home48_6(self):
        module_other_stx_app.get_datachecklist("Home48_6")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.info_sec_send_info(self, "Home48_6", eventname, result)



    def Home48_7(self):
        module_other_stx_app.get_datachecklist("Home48_7")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.end(self, "Home48_7", eventname, result)






    def Home49(self):
        module_other_stx_app.get_datachecklist("Home49")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.card_pay_transfer(self, "Home49", eventname, result)


    def Home50(self):
        module_other_stx_app.get_datachecklist("Home50")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.card_pay_g7_check_info(self, "Home50", eventname, result)


    def Home51(self):
        module_other_stx_app.get_datachecklist("Home51")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.collected_from_customers(self, "Home51", eventname, result)


    def Home52(self):
        module_other_stx_app.get_datachecklist("Home52")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.pay_card(self, "Home52", eventname, result)


    def Home53(self):
        module_other_stx_app.get_datachecklist("Home53")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_order_fixed(self, "Home53", eventname, result)


    def Home54(self):
        module_other_stx_app.get_datachecklist("Home54")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.order_fixed_refuse(self, "Home54", eventname, result)


    def Home55(self):
        module_other_stx_app.get_datachecklist("Home55")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.order_fixed_receive_app(self, "Home55", eventname, result)


    def Home56(self):
        module_other_stx_app.get_datachecklist("Home56")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.order_fixed_see_detail(self, "Home56", eventname, result)


    def Home57(self):
        module_other_stx_app.get_datachecklist("Home57")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.detail_if(self, "Home57", eventname, result, 55, "Địa chỉ đón")


    def Home58(self):
        module_other_stx_app.get_datachecklist("Home58")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.detail_other(self, "Home58", eventname, result, 55, "Địa chỉ trả")


    def Home59(self):
        module_other_stx_app.get_datachecklist("Home59")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.detail_other(self, "Home59", eventname, result, 55, "Cước chuyến đi")


    def Home60(self):
        module_other_stx_app.get_datachecklist("Home60")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.detail_note(self, "Home60", eventname, result)


    def Home61(self):
        module_other_stx_app.get_datachecklist("Home61")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.detail_other(self, "Home61", eventname, result, 61, "Phương thức thanh toán")


    def Home62(self):
        module_other_stx_app.get_datachecklist("Home62")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.detail_if_cv(self, "Home62", eventname, result, 56, "Nguồn cuốc")


    def Home63(self):
        module_other_stx_app.get_datachecklist("Home63")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.detail_if(self, "Home63", eventname, result, 57, "Số điện thoại")


    def Home64(self):
        module_other_stx_app.get_datachecklist("Home64")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.detail_cancel(self, "Home64", eventname, result)


    def Home65(self):
        module_other_stx_app.get_datachecklist("Home65")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.order_fixed_location_vehicle(self, "Home65", eventname, result)


    def Home66(self):
        module_other_stx_app.get_datachecklist("Home66")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.order_fixed_location_customer(self, "Home66", eventname, result)


    def Home67(self):
        module_other_stx_app.get_datachecklist("Home67")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.order_fixed_see_customer(self, "Home67", eventname, result)


    def Home68(self):
        pass
        # module_other_stx_app.get_datachecklist("Home68")
        # eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        # result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        # homepage_driver.waiting_for_a_passenger.check_info_confirm_pay_money(self, "Home68", eventname, result, 67, 160, 655, 275,
        #                                                                       "_XacNhanTienThanhToan_DiaChiDon.png")

    def Home69(self):
        pass
        # module_other_stx_app.get_datachecklist("Home69")
        # eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        # result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        # homepage_driver.waiting_for_a_passenger.check_info_confirm_pay_money(self, "Home69", eventname, result, 70, 350, 888, 420,
        #                                                                       "_XacNhanTienThanhToan_DiaChiTra.png")

    def Home70(self):
        pass
        # module_other_stx_app.get_datachecklist("Home70")
        # eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        # result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        # homepage_driver.waiting_for_a_passenger.check_info_confirm_pay_money(self, "Home70", eventname, result, 70, 495, 333, 550,
        #                                                                       "_XacNhanTienThanhToan_ThuCuaKhach.png")

    def Home71(self):
        pass
        # module_other_stx_app.get_datachecklist("Home71")
        # eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        # result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        # homepage_driver.waiting_for_a_passenger.confirm_pay_money_note(self, "Home71", eventname, result)


    def Home72(self):
        pass
        # module_other_stx_app.get_datachecklist("Home72")
        # eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        # result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        # homepage_driver.waiting_for_a_passenger.confirm_pay_money_confirm(self, "Home72", eventname, result)


    def Home73(self):
        module_other_stx_app.get_datachecklist("Home73")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_confirm_pay_money_confirm(self, "Home73", eventname, result, var_stx_app.Fixed_location_from,
                                                                              "_Fixed_DiaChiDon.png")

    def Home74(self):
        module_other_stx_app.get_datachecklist("Home74")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_confirm_pay_money_confirm(self, "Home74", eventname, result, var_stx_app.Fixed_location_to,
                                                                              "_Fixed_DiaChiTra.png")

    def Home75(self):
        module_other_stx_app.get_datachecklist("Home75")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_confirm_pay_money_confirm(self, "Home75", eventname, result, var_stx_app.Fixed_collected_from_customers,
                                                                              "_Fixed_ThuCuaKhach.png")


    def Home76(self):
        module_other_stx_app.get_datachecklist("Home76")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_confirm_pay_money_confirm(self, "Home76", eventname, result, var_stx_app.Fixed_call_customer,
                                                                              "_Fixed_GoiKhachHang.png")


    def Home77(self):
        module_other_stx_app.get_datachecklist("Home77")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.electronic_contract(self, "Home77", eventname, result)


    def Home78(self):
        module_other_stx_app.get_datachecklist("Home78")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_confirm_pay_money_confirm(self, "Home78", eventname, result, var_stx_app.Fixed_pttt,
                                                                              "_Fixed_PhuongThucThanhToan.png")

    def Home79(self):
        module_other_stx_app.get_datachecklist("Home79")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_confirm_pay_money_confirm(self, "Home79", eventname, result, var_stx_app.Fixed_orgirin,
                                                                              "_Fixed_NguonCuoc.png")

    def Home79_1(self):
        module_other_stx_app.get_datachecklist("Home79_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.check_confirm_pay_money_confirm(self, "Home79_1", eventname, result, var_stx_app.Fixed_type_order,
                                                                              "_Fixed_LoaiCuoc.png")


    def Home80(self):
        module_other_stx_app.get_datachecklist("Home80")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.wrong_customer(self, "Home80", eventname, result)



    def Home81(self):
        module_other_stx_app.get_datachecklist("Home81")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.wrong_customer_return_guests(self, "Home81", eventname, result)


    def Home82(self):
        module_other_stx_app.get_datachecklist("Home82")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.waiting_for_a_passenger.return_guests(self, "Home82", eventname, result)



    def Notification01(self):
        module_other_stx_app.get_datachecklist("Notification01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.notification.notification(self, "Notification01", eventname, result)


    def Notification02(self):
        module_other_stx_app.get_datachecklist("Notification02")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.notification.notification_search(self, "Notification02", eventname, result)


    def Notification03(self):
        module_other_stx_app.get_datachecklist("Notification03")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.notification.check_info_notification(self, "Notification03", eventname, result, var_stx_app.notification_genaral, "0", "_ThongBao_Chung.png")


    def Notification04(self):
        module_other_stx_app.get_datachecklist("Notification04")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.notification.check_info_notification_detail(self, "Notification04", eventname, result, var_stx_app.notification_genaral, "_ThongBao_Chung_ChiTiet.png")


    def Notification05(self):
        module_other_stx_app.get_datachecklist("Notification05")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.notification.check_info_notification(self, "Notification05", eventname, result, var_stx_app.notification_private, "0", "_ThongBao_CaNhan.png")


    def Notification06(self):
        module_other_stx_app.get_datachecklist("Notification06")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.notification.check_info_notification_detail(self, "Notification06", eventname, result, var_stx_app.notification_private, "_ThongBao_CaNhan_ChiTiet.png")


    def Notification07(self):
        module_other_stx_app.get_datachecklist("Notification07")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.notification.check_info_notification(self, "Notification07", eventname, result, var_stx_app.notification_customer, "1", "_ThongBao_CuocKhach.png")


    def Notification08(self):
        module_other_stx_app.get_datachecklist("Notification08")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.notification.check_info_notification_detail(self, "Notification08", eventname, result, var_stx_app.notification_customer, "_ThongBao_CuocKhach_ChiTiet.png")



    def Notification09(self):
        module_other_stx_app.get_datachecklist("Notification09")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.notification.check_info_notification(self, "Notification09", eventname, result, var_stx_app.notification_important, "0", "_ThongBao_QuanTrong.png")


    def Notification10(self):
        module_other_stx_app.get_datachecklist("Notification10")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.notification.check_info_notification_detail(self, "Notification10", eventname, result, var_stx_app.notification_important, "_ThongBao_QuanTrong_ChiTiet.png")



    def History01(self):
        module_other_stx_app.get_datachecklist("History01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.history(self, "History01", eventname, result)


    def History02(self):
        module_other_stx_app.get_datachecklist("History02")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.history_calendar(self, "History02", eventname, result)


    def History02_1(self):
        module_other_stx_app.get_datachecklist("History02_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.history_detail_check_time_fill(self, "History02_1", eventname, result)


    def History03(self):
        module_other_stx_app.get_datachecklist("History03")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.history_detail_status(self, "History03", eventname, result)


    def History04(self):
        module_other_stx_app.get_datachecklist("History04")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.get_info_history_detail(self, "History04", eventname, result)


    def History05(self):
        module_other_stx_app.get_datachecklist("History05")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_other(self, "History05", eventname, result, 65, 2)


    def History06(self):
        module_other_stx_app.get_datachecklist("History06")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_other(self, "History06", eventname, result, 66, 2)


    def History07(self):
        module_other_stx_app.get_datachecklist("History07")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_if(self, "History07", eventname, result, 67, 2, 76, 3)


    def History08(self):
        module_other_stx_app.get_datachecklist("History08")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_hoe_source(self, "History08", eventname, result)


    def History09(self):
        module_other_stx_app.get_datachecklist("History09")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_if(self, "History09", eventname, result, 69, 2, 69, 3)


    def History10(self):
        module_other_stx_app.get_datachecklist("History10")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_if(self, "History10", eventname, result, 70, 2, 70, 3)


    def History11(self):
        module_other_stx_app.get_datachecklist("History11")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_if(self, "History11", eventname, result, 71, 2, 71, 3)


    def History12(self):
        module_other_stx_app.get_datachecklist("History12")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_if(self, "History12", eventname, result, 72, 2, 72, 3)


    def History13(self):
        module_other_stx_app.get_datachecklist("History13")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_if(self, "History13", eventname, result, 73, 2, 73, 3)


    def History13_1(self):
        module_other_stx_app.get_datachecklist("History13_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_other(self, "History13_1", eventname, result, 114, 3)


    def History13_2(self):
        module_other_stx_app.get_datachecklist("History13_2")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_other(self, "History13_2", eventname, result, 115, 3)


    def History13_3(self):
        module_other_stx_app.get_datachecklist("History13_3")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_other(self, "History13_3", eventname, result, 116, 3)


    def History13_4(self):
        module_other_stx_app.get_datachecklist("History13_4")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_other(self, "History13_4", eventname, result, 117, 3)


    def History13_5(self):
        module_other_stx_app.get_datachecklist("History13_5")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_other(self, "History13_5", eventname, result, 118, 3)


    def History14(self):
        module_other_stx_app.get_datachecklist("History14")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_time(self, "History14", eventname, result)


    def History15(self):
        module_other_stx_app.get_datachecklist("History15")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_other1(self, "History15", eventname, result, 74, 3)


    def History16(self):
        module_other_stx_app.get_datachecklist("History16")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_other1(self, "History16", eventname, result, 75, 3)


    def History17(self):
        module_other_stx_app.get_datachecklist("History17")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_other1(self, "History17", eventname, result, 78, 3)


    def History18(self):
        module_other_stx_app.get_datachecklist("History18")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_info_history_pay(self, "History18", eventname, result)


    def History19(self):
        module_other_stx_app.get_datachecklist("History19")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.history_detail_qr(self, "History19", eventname, result)


    def History19_1(self):
        module_other_stx_app.get_datachecklist("History19_1")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.history_detail_qr1(self, "History19_1", eventname, result)


    def History19_2(self):
        module_other_stx_app.get_datachecklist("History19_2")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_fee(self, "History19_2", eventname, result)


    def History20(self):
        module_other_stx_app.get_datachecklist("History20")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.statistical(self, "History20", eventname, result)


    def History21(self):
        module_other_stx_app.get_datachecklist("History21")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.statistical_sum_order(self, "History21", eventname, result)


    def History22(self):
        module_other_stx_app.get_datachecklist("History22")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_statistical_other(self, "History22", eventname, result, var_stx_app.statistical_dt, "_LichSu_ThongKe_DoanhThu.png")


    def History23(self):
        module_other_stx_app.get_datachecklist("History23")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_statistical_other(self, "History23", eventname, result, var_stx_app.statistical1, "_LichSu_ThongKe_HoanThanh.png")


    def History24(self):
        module_other_stx_app.get_datachecklist("History24")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_statistical_other(self, "History24", eventname, result, var_stx_app.statistical2, "_LichSu_ThongKe_QuaGioKhongNhan.png")


    def History25(self):
        module_other_stx_app.get_datachecklist("History25")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_statistical_other(self, "History25", eventname, result, var_stx_app.statistical3, "_LichSu_ThongKe_TuChoi.png")


    def History26(self):
        module_other_stx_app.get_datachecklist("History26")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_statistical_other(self, "History26", eventname, result, var_stx_app.statistical4, "_LichSu_ThongKe_Huy.png")


    def History27(self):
        module_other_stx_app.get_datachecklist("History27")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_statistical_other(self, "History27", eventname, result, var_stx_app.statistical5, "_LichSu_ThongKe_NhamKhach.png")


    def History28(self):
        module_other_stx_app.get_datachecklist("History28")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.history.check_statistical_other(self, "History28", eventname, result, var_stx_app.statistical5, "_LichSu_ThongKe_KhongDuocChon.png")



    def AccountWallet01(self):
        module_other_stx_app.get_datachecklist("AccountWallet01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.account_wallet.account_wallet(self, "AccountWallet01", eventname, result)


    def AccountWallet02(self):
        module_other_stx_app.get_datachecklist("AccountWallet02")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.account_wallet.account_wallet_calendar(self, "AccountWallet02", eventname, result)


    def AccountWallet03(self):
        module_other_stx_app.get_datachecklist("AccountWallet03")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.account_wallet.check_info_account_wallet_other(self, "AccountWallet03", eventname, result,
                                                                       var_stx_app.account_wallet_balance1, "_ViTaiKhoan_SoDu.png")

    def AccountWallet04(self):
        module_other_stx_app.get_datachecklist("AccountWallet04")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.account_wallet.check_info_account_wallet_other(self, "AccountWallet04", eventname, result,
                                                                       var_stx_app.account_wallet_day, "_ViTaiKhoan_NgayThangNam.png")


    def AccountWallet05(self):
        module_other_stx_app.get_datachecklist("AccountWallet05")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.account_wallet.check_info_account_wallet_other(self, "AccountWallet05", eventname, result,
                                                                       var_stx_app.account_wallet_money, "_ViTaiKhoan_HinhThuc.png")

    def AccountWallet06(self):
        module_other_stx_app.get_datachecklist("AccountWallet06")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.account_wallet.check_info_account_wallet_other(self, "AccountWallet06", eventname, result,
                                                                       var_stx_app.account_wallet_code_gd, "_ViTaiKhoan_MaGiaoDich.png")

    def AccountWallet07(self):
        module_other_stx_app.get_datachecklist("AccountWallet07")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.account_wallet.check_info_account_wallet_other(self, "AccountWallet07", eventname, result,
                                                                       var_stx_app.account_wallet_time, "_ViTaiKhoan_ThoiGian.png")


    def AccountWallet08(self):
        module_other_stx_app.get_datachecklist("AccountWallet08")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.account_wallet.check_info_account_wallet_other(self, "AccountWallet08", eventname, result,
                                                                       var_stx_app.account_wallet_balance2, "_ViTaiKhoan_SoDu.png")


    def AccountWallet09(self):
        module_other_stx_app.get_datachecklist("AccountWallet09")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.account_wallet.check_info_account_wallet_other(self, "AccountWallet09", eventname, result,
                                                                       var_stx_app.account_wallet_note, "_ViTaiKhoan_GhiChu.png")



    def CashWallet01(self):
        module_other_stx_app.get_datachecklist("CashWallet01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.cash_wallet.cash_wallet(self, "CashWallet01", eventname, result)


    def CashWallet02(self):
        module_other_stx_app.get_datachecklist("CashWallet02")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.cash_wallet.cash_wallet_calendar(self, "CashWallet02", eventname, result)


    def CashWallet03(self):
        pass
        # module_other_stx_app.get_datachecklist("CashWallet03")
        # eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        # result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        # homepage_driver.cash_wallet.cash_wallet_transfer_money(self, "CashWallet03", eventname, result)


    def CashWallet04(self):
        module_other_stx_app.get_datachecklist("CashWallet04")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.cash_wallet.check_info_cash_wallet_other(self, "CashWallet04", eventname, result,
                                                                       var_stx_app.cash_wallet_balance1, "_ViTienMat_SoDu.png")


    def CashWallet05(self):
        module_other_stx_app.get_datachecklist("CashWallet05")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.cash_wallet.check_info_cash_wallet_other(self, "CashWallet05", eventname, result,
                                                                       var_stx_app.cash_wallet_day, "_ViTienMat_NgayThangNam.png")


    def CashWallet06(self):
        module_other_stx_app.get_datachecklist("CashWallet06")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.cash_wallet.check_info_cash_wallet_other(self, "CashWallet06", eventname, result,
                                                                       var_stx_app.cash_wallet_money, "_ViTienMat_SoTien.png")

    def CashWallet07(self):
        module_other_stx_app.get_datachecklist("CashWallet07")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.cash_wallet.check_info_cash_wallet_other(self, "CashWallet07", eventname, result,
                                                                       var_stx_app.cash_wallet_code_gd, "_ViTienMat_MaGd.png")

    def CashWallet08(self):
        module_other_stx_app.get_datachecklist("CashWallet08")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.cash_wallet.check_info_cash_wallet_other(self, "CashWallet08", eventname, result,
                                                                       var_stx_app.cash_wallet_time, "_ViTienMat_ThoiGian.png")


    def CashWallet09(self):
        module_other_stx_app.get_datachecklist("CashWallet09")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.cash_wallet.check_info_cash_wallet_other(self, "CashWallet09", eventname, result,
                                                                       var_stx_app.cash_wallet_balance2, "_ViTienMat_SoDu.png")


    def CashWallet10(self):
        module_other_stx_app.get_datachecklist("CashWallet10")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.cash_wallet.check_info_cash_wallet_other(self, "CashWallet10", eventname, result,
                                                                       var_stx_app.cash_wallet_note, "_ViTienMat_GhiChu.png")



    def TripPayment01(self):
        module_other_stx_app.get_datachecklist("TripPayment01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.trip_payment.trip_payment(self, "TripPayment01", eventname, result)


    def TripPayment02(self):
        module_other_stx_app.get_datachecklist("TripPayment02")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.trip_payment.trip_payment_address(self, "TripPayment02", eventname, result)


    def TripPayment03(self):
        module_other_stx_app.get_datachecklist("TripPayment03")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.trip_payment.trip_payment_qr_drive(self, "TripPayment03", eventname, result)


    def TripPayment04(self):
        module_other_stx_app.get_datachecklist("TripPayment04")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.trip_payment.trip_payment_qr_customer(self, "TripPayment04", eventname, result)



    def VnPayWallet01(self):
        module_other_stx_app.get_datachecklist("VnPayWallet01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.vnpay_wallet.vnpay_wallet(self, "VnPayWallet01", eventname, result)


    def VnPayWallet02(self):
        module_other_stx_app.get_datachecklist("VnPayWallet02")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.vnpay_wallet.vnpay_wallet_link(self, "VnPayWallet02", eventname, result)



    def Setting01(self):
        module_other_stx_app.get_datachecklist("Setting01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.setting.setting(self, "Setting01", eventname, result)


    def Setting02(self):
        module_other_stx_app.get_datachecklist("Setting02")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.setting.setting_vesion(self, "Setting02", eventname, result)


    def Setting03(self):
        module_other_stx_app.get_datachecklist("Setting03")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.setting.setting_checkbox(self, "Setting03", eventname, result,
                                                 "Luôn phát âm thanh lớn", "_CaiDat_LuonPhatAmThanhLon.png")


    def Setting04(self):
        module_other_stx_app.get_datachecklist("Setting04")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.setting.setting_sync(self, "Setting04", eventname, result)


    def Setting05(self):
        module_other_stx_app.get_datachecklist("Setting05")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.setting.setting_send_error(self, "Setting05", eventname, result)


    def Setting06(self):
        module_other_stx_app.get_datachecklist("Setting06")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.setting.setting_checkbox(self, "Setting06", eventname, result,
                                                 "Đọc địa chỉ cuốc app", "_CaiDat_DocDiaChiCuocApp.png")


    def Setting07(self):
        module_other_stx_app.get_datachecklist("Setting07")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.setting.setting_checkbox(self, "Setting07", eventname, result,
                                                 "Đọc địa chỉ cuốc đàm", "_CaiDat_DocDiaChiCuocDam.png")

    def Setting08(self):
        module_other_stx_app.get_datachecklist("Setting08")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.setting.setting_blu(self, "Setting08", eventname, result)


    def Setting09(self):
        module_other_stx_app.get_datachecklist("Setting09")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.setting.setting_checkbox(self, "Setting09", eventname, result,
                                                 "Mở ứng dụng khi mất kết nối mạng, GPS", "_CaiDat_MoUngDungKhiMatKetNoiMangGPS.png")

    def Setting10(self):
        module_other_stx_app.get_datachecklist("Setting10")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.setting.setting_checkbox(self, "Setting10", eventname, result,
                                                 "Luôn sáng màn hình", "_CaiDat_LuonSangManHinh.png")


    def Setting11(self):
        module_other_stx_app.get_datachecklist("Setting11")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.setting.setting_change_size_word(self, "Setting11", eventname, result)


    def Report01(self):
        module_other_stx_app.get_datachecklist("Report01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.report.report(self, "Report01", eventname, result)


    def Report02(self):
        module_other_stx_app.get_datachecklist("Report02")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.report.report_violate(self, "Report02", eventname, result)


    def Report03(self):
        module_other_stx_app.get_datachecklist("Report03")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.report.check_report_violate_statistical(self, "Report03", eventname, result)


    def Report04(self):
        module_other_stx_app.get_datachecklist("Report04")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.report.check_report_violate(self, "Report04", eventname, result, var_stx_app.violate_histort,
                                                    var_stx_app.not_result1, "Không có kết quả nào được tìm thấy!", "_BaoCao_ViPham_LichSuKhoa.png")


    def Report05(self):
        module_other_stx_app.get_datachecklist("Report05")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.report.check_report_violate_violate(self, "Report05", eventname, result)

    def Report06(self):
        pass
        # module_other_stx_app.get_datachecklist("Report06")
        # eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        # result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        # homepage_driver.report.report_fee_dam(self, "Report06", eventname, result)


    def Report07(self):
        module_other_stx_app.get_datachecklist("Report07")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.report.customer_payment_report(self, "Report07", eventname, result)


    def Report08(self):
        module_other_stx_app.get_datachecklist("Report08")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.report.customer_payment_report_carlender(self, "Report08", eventname, result)


    def Report09(self):
        module_other_stx_app.get_datachecklist("Report09")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.report.check_info_customer_payment_report(self, "Report09", eventname, result, 180, "BaoCaoThanhToanCuocKhach_NgayThangNam.png")


    def Report10(self):
        module_other_stx_app.get_datachecklist("Report10")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.report.check_info_customer_payment_report(self, "Report10", eventname, result, 181, "BaoCaoThanhToanCuocKhach_ThoiGian.png")


    def Report11(self):
        module_other_stx_app.get_datachecklist("Report11")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.report.check_info_customer_payment_report(self, "Report11", eventname, result, 182, "BaoCaoThanhToanCuocKhach_DiemDon.png")


    def Report12(self):
        module_other_stx_app.get_datachecklist("Report12")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.report.check_info_customer_payment_report(self, "Report12", eventname, result, 183, "BaoCaoThanhToanCuocKhach_DiemTra.png")


    def Report13(self):
        module_other_stx_app.get_datachecklist("Report13")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.report.check_info_customer_payment_report(self, "Report13", eventname, result, 184, "BaoCaoThanhToanCuocKhach_ThanhToanThe.png")


    def Report14(self):
        module_other_stx_app.get_datachecklist("Report14")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.report.check_info_customer_payment_report(self, "Report14", eventname, result, 185, "BaoCaoThanhToanCuocKhach_ThanhToanTienMat.png")


    def Report15(self):
        module_other_stx_app.get_datachecklist("Report15")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.report.check_info_customer_payment_report(self, "Report15", eventname, result, 186, "BaoCaoThanhToanCuocKhach_Ca.png")


    def Report16(self):
        module_other_stx_app.get_datachecklist("Report16")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.report.check_info_customer_payment_report(self, "Report16", eventname, result, 187, "BaoCaoThanhToanCuocKhach_TrangThai.png")



    def Help01(self):
        module_other_stx_app.get_datachecklist("Help01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.help.help(self, "Help01", eventname, result)


    def Help02(self):
        module_other_stx_app.get_datachecklist("Help02")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.help.help_comments(self, "Help02", eventname, result)


    def Help03(self):
        module_other_stx_app.get_datachecklist("Help03")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.help.help_comments_sdt(self, "Help03", eventname, result)


    def Help04(self):
        module_other_stx_app.get_datachecklist("Help04")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.help.help_comments_send(self, "Help04", eventname, result)


    def Help05(self):
        module_other_stx_app.get_datachecklist("Help05")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.help.help_comments_help(self, "Help05", eventname, result)



    def Logout01(self):
        module_other_stx_app.get_datachecklist("Logout01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_driver.end_of_shift.end_of_shift(self, "Logout01", eventname, result)




    def Web01(self):
        module_other_stx_app.get_datachecklist("Web01")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.web_app.check_not_fill_electronic_invoice(self, "Web01", eventname, result)




    def Web02(self):
        module_other_stx_app.get_datachecklist("Web02")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.web_app.check_fill_electronic_invoice(self, "Web02", eventname, result)


    def Web03(self):
        module_other_stx_app.get_datachecklist("Web03")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.web_app.check_card_company_auto_export(self, "Web03", eventname, result)



    def Web04(self):
        module_other_stx_app.get_datachecklist("Web04")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.web_app.check_card_company_not_auto_export(self, "Web04", eventname, result)


    def Web05(self):
        module_other_stx_app.get_datachecklist("Web05")
        eventname = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 42, 2))
        result = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, 'Sheet1', 43, 2))
        homepage_g7.web_app.check_pttt(self, "Web05", eventname, result)







