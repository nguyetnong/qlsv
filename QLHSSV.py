class Student():
    def __init__(self, MSSV, Hoten, BOD, Address, Cls):
        self.MSSV = MSSV
        self.Hoten = Hoten
        self.BOD = BOD
        self.Adddress = Address
        self.Cls = Cls

    def Xemthongtin(self):
        print(self.MSSV)
        print(self.Hoten)
        print(self.BOD)
        print(self.Adddress)
        print(self.Cls)

class Students_List():
    def __init__(self):
        self.students_list =[]

    def ThemThongtinSinhVien(self):
        student_id = input("Nhập MSSV : ")
        ho_ten = input("Nhập họ tên : ") # huy  Huu
        ngay_sinh = input("Nhập ngày sinh : ")
        dia_chi = input("Nhập địa chỉ : ")
        lop_hoc = input("Nhập lóp học : ")
        student_A = Student(MSSV=student_id, Hoten= ho_ten, BOD= ngay_sinh, Address= dia_chi, Cls= lop_hoc)
        self.students_list.append(student_A)

    def XemDanhsachSinhvien(self):
        for student in self.students_list:
            student.Xemthongtin()

    def XemThongtin_1_SinhVien(self):
        mssv = input("Nhập MSSV cân tìm : ")
        exists = False
        for student in self.students_list:
            if student.MSSV == mssv:
                student.Xemthongtin()
                exists = True
                break

        if exists == False:
            print("Không tồn tại MSSV này")
            
    def UpdateThongTinSinhVien(self):
        mssv_update = input("Nhập MSSV cần update : ")
        idx = 0
        for student in self.students_list:
            print(student.MSSV)
            if student.MSSV == mssv_update:
                hoten = input("Nhập ho tên mới : ")
                self.students_list[idx].Hoten = hoten
            else:
                idx += 1
    def xoathonhtinsinhvien(self):
        mssv_canxoa=input("nhap mssv cần xóa: ")
        for student in self.students_list:
             if student.MSSV == mssv_canxoa:
                student.Xemthongtin()
                self.students_list.remove(student)
manager = Students_List()              
while True:
    
    action=int(input("nhập hoạt động của bạn: "))
    if action==1:
        manager .ThemThongtinSinhVien()
    elif action==2:
        manager.XemDanhsachSinhvien()
    elif action==3:
        manager.XemThongtin_1_SinhVien()
    elif action==4:
        manager.xoathonhtinsinhvien()
    elif action==5: 
        manager.UpdateThongTinSinhVien()
    






