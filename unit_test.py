import unittest
import user_student
import user
import user_admin
import user_teacher
import unit


class TestStringMethods(unittest.TestCase):
    user_file = open("./user.txt", "w")
    user_file.write(f"17315,admin,^^^Y!J#2$2%6&X(1)M*$$$,AD,enabled\n"
                    f"27170,teach1,^^^Y!J#2$2%6&X(1)M*$$$,TA,enabled,[COM101]\n"
                    f"62393,teach2,^^^Y!J#2$2%6&X(1)M*$$$,TA,enabled,[PSY101]\n"
                    f"22206,teach3,^^^Y!J#2$2%6&X(1)M*$$$,TA,disabled,[CHE101,FIT101]\n"
                    f"17604,stu1,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 99), (PSY101, 43), (CHE101, 20)]\n"
                    f"61098,stu2,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 32), (PSY101, 80), (CHE101, 45)]\n"
                    F"21974,stu3,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 71), (PSY101, 9), (CHE101, 36)]\n"
                    F"70156,stu4,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 94), (PSY101, 29), (CHE101, 50)]\n"
                    F"63476,stu5,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 79), (FIT101, 33)]\n"
                    F"84227,stu6,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 77), (CIV101, 34)]\n"
                    F"40478,stu7,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 22), (PSY101, 36), (CHE101, 95)]\n"
                    F"98248,stu8,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 55)]\n"
                    F"94791,stu9,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 56), (PSY101, 44), (CHE101, 60)]\n"
                    F"25724,stu10,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, -1), (PSY101, 76), (CHE101, 65)]\n"
                    )
    user_file.close()
    unit_file = open("./unit.txt", "w")
    unit_file.write(f"1000000,COM101,Introduction to Computer Science,100\n"
                    f"1123123,PSY101,Introduction to Psychology,100\n"
                    f"1234,FIT101,Java,100\n"
                    f"432,CIV101,Roof,0\n"
                    f"5467893,CHE101,Introduction to Chemistry,100\n")
    unit_file.close()

    """
    Student class test cases
    """
    def test_show_menu(self):
        user_student.UserStudent().student_menu()

    def test_list_available_units(self):
        user_student.UserStudent().list_available_units()

    def test_list_enrolled_units(self):
        user_student.UserStudent().list_enrolled_units()

    def test_drop_unit(self):
        stu1 = user_student.UserStudent("17604", "stu1", "^^^Y!J#2$2%6&X(1)M*$$$", "ST", "enabled",
                                        [("COM101", 99), ("PSY101", 43), ("CHEM101", 20)])
        stu1.drop_unit("COM101")  # drop valid unit
        with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
            lines = read_user_file.readlines()
            have_user = False
            check = "17604,stu1,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(PSY101, 43), (CHEM101, 20)]\n"
            if check in lines:  # check user.txt to see that the unit is removed from enrol list
                have_user = True
        read_user_file.close()
        self.assertTrue(have_user)

        stu1.drop_unit("FIT101")  # drop unit with invalid unit code
        with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
            lines = read_user_file.readlines()
            have_user = False
            check = "17604,stu1,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(PSY101, 43), (CHEM101, 20)]\n"
            if check in lines:  # check user.txt to see that the enrol list did not change
                have_user = True
        read_user_file.close()
        self.assertTrue(have_user)

    def test_enrol_unit(self):
        stu2 = user_student.UserStudent("61098", "stu2", "^^^Y!J#2$2%6&X(1)M*$$$", "ST", "enabled",
                                        [("COM101", 32)])
        stu2.enrol_unit("PSY101")  # enrol valid unit
        with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
            lines = read_user_file.readlines()
            unit_enrolled1 = False
            check = "61098,stu2,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 32), (PSY101, -1)]\n"
            if check in lines:  # check the user.txt to see that the unit is added to the enrol list
                unit_enrolled1 = True
        read_user_file.close()
        self.assertTrue(unit_enrolled1)

        stu2.enrol_unit("FIT101")  # enrol in unit with invalid unit code
        with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
            lines = read_user_file.readlines()
            unit_enrolled2 = False
            check = "61098,stu2,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 32), (PSY101, -1)]\n"
            if check in lines:  # check user.txt to see that the unit is not added to the enrol list
                unit_enrolled2 = True
        read_user_file.close()
        self.assertTrue(unit_enrolled2)

    def test_update_student_details(self):
        student5 = user_student.UserStudent(94791, 'stu9', '^^^Y!J#2$2%6&X(1)M*$$$', 'ST', 'enabled',
                                            [('COM101', 56), ('PSY101', 44), ('CHE101', 60)])
        student5.update_student_details(
            "'94791','stu9','^^^Y!J#2$2%6&X(1)M*$$$','ST','enabled',[('COM101', 56), ('CHE101', 60)]")
        with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
            lines = read_user_file.readlines()
            student_details_updated = False
            check = "94791,stu9,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 56), (CHE101, 60)]\n"
            if check in lines:  # check user.txt to see whether the details are updated
                student_details_updated = True
        read_user_file.close()
        self.assertTrue(student_details_updated)

    def test_check_unit_capacity(self):
        student2 = user_student.UserStudent(98248, 'stu8', '^^^Y!J#2$2%6&X(1)M*$$$', 'ST', 'enabled', [('COM101', 55)])
        result1 = student2.check_unit_capacity("CIV101", "enrol")  # enrol in unit that is full
        self.assertFalse(result1)
        result2 = student2.check_unit_capacity("PSY101", "enrol")  # enrol in unit that is not full
        self.assertTrue(result2)
        result3 = student2.check_unit_capacity("PSY101", "drop")  # drop a valid unit
        self.assertTrue(result3)
        result4 = student2.check_unit_capacity("MCD101", "drop")  # drop a invalid unit
        self.assertFalse(result4)

    def test_generate_score(self):
        student10 = user_student.UserStudent(25724, 'stu10', '^^^Y!J#2$2%6&X(1)M*$$$', 'ST', 'enabled',
                                             [('COM101', -1), ('PSY101', 76), ('CHE101', 65)])
        student10.generate_score('COM101')
        with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
            lines = read_user_file.readlines()
            student_score_updated = False
            check = "25724,stu10,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, -1), (PSY101, 76), (CHE101, 65)]\n"
            if check not in lines:  # check user.txt to see whether the score is still -1 or not
                student_score_updated = True
        read_user_file.close()
        self.assertTrue(student_score_updated)

    """
    Teacher class test cases
    """
    def test_teacher_menu(self):
        user_teacher.UserTeacher().teacher_menu()

    def test_list_teach_unit(self):
        user_teacher.UserTeacher().list_teach_units()

    def test_list_enrol_students(self):
        user_teacher.UserTeacher().list_enrol_students("COM101")

    def test_show_unit_avg_max_min_score(self):
        user_teacher.UserTeacher().show_unit_avg_max_min_score("COM101")

    def test_add_teach_unit(self):
        teacher1 = user_teacher.UserTeacher(62393, 'teach2', '^^^Y!J#2$2%6&X(1)M*$$$', 'TA', 'enabled', ['PSY101'])
        unit1 = unit.Unit("988", "FIT2023", "Mathlab", 50)  # unit obj
        teacher1.add_teach_unit(unit1)
        with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
            lines = read_user_file.readlines()
            unit_added = False
            check1 = "62393,teach2,^^^Y!J#2$2%6&X(1)M*$$$,TA,enabled,[PSY101, FIT2023]\n"
            if check1 in lines:  # check user.txt if unit is added to teach list
                unit_added = True
        read_user_file.close()
        self.assertTrue(unit_added)

        with open("./unit.txt", "r", encoding='utf8') as read_unit_file:  # open user.txt and read each line
            lines = read_unit_file.readlines()
            have_unit = False
            check = "988,FIT2023,Mathlab,50\n"
            if check in lines:  # check unit.txt if the unit is added
                have_unit = True
        read_unit_file.close()
        self.assertTrue(have_unit)

    def test_delete_unit(self):
        teacher3 = user_teacher.UserTeacher(22206, "teach3", "^^^Y!J#2$2%6&X(1)M*$$$", "TA", "disabled",
                                            ["CHE101", "FIT101"])
        teacher3.delete_teach_unit("FIT101")  # valid unit code to delete
        with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
            lines = read_user_file.readlines()
            unit_deleted1 = False
            check2 = "22206,teach3,^^^Y!J#2$2%6&X(1)M*$$$,TA,disabled,[CHE101]\n"
            check3 = "63476,stu5,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 79)]\n"
            if check2 in lines and check3 in lines:  # check user.txt if the unit is removed from the enrol and teach list
                unit_deleted1 = True
        read_user_file.close()
        self.assertTrue(unit_deleted1)

        teacher3.delete_teach_unit("ENG101")  # invalid unit code to delete
        with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
            lines = read_user_file.readlines()
            unit_deleted2 = False
            check4 = "22206,teach3,^^^Y!J#2$2%6&X(1)M*$$$,TA,disabled,[CHE101]\n"
            if check4 in lines:  # check user.txt if the unit is removed from teach list
                unit_deleted2 = True
        read_user_file.close()
        self.assertTrue(unit_deleted2)

    def test_remove_unit(self):
        teacher9 = user_teacher.UserTeacher()
        teacher9.remove_unit("CIV101")
        with open("./unit.txt", "r", encoding='utf8') as read_unit_file:  # open unit.txt and read each line
            lines = read_unit_file.readlines()
            unit_removed = False
            check = "432,CIV101,Roof,100\n"
            if check not in lines:  # search unit.txt for the removed unit
                unit_removed = True
        read_unit_file.close()
        self.assertTrue(unit_removed)

    def test_update_teacher_details(self):
        teacher5 = user_teacher.UserTeacher(22206, 'teach3', '^^^Y!J#2$2%6&X(1)M*$$$', 'TA', 'disabled',
                                            ['CHE101', 'FIT101'])
        teacher5.update_teacher_details(
            "'22206','teach3','^^^Y!J#2$2%6&X(1)M*$$$','TA','disabled',['CHE101','FIT101','CIV101']")
        with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
            lines = read_user_file.readlines()
            teacher_details_updated = False
            check = "22206,teach3,^^^Y!J#2$2%6&X(1)M*$$$,TA,disabled,[CHE101,FIT101,CIV101]\n"
            if check in lines:  # find in user.txt to see if the details are updated
                teacher_details_updated = True
        read_user_file.close()
        self.assertTrue(teacher_details_updated)

    """
    Unit class test cases
    """
    def test_generate_unit_id(self):
        #unit.Unit().generate_unit_id()
        unit1 = unit.Unit()
        id1 = unit1.generate_unit_id()
        self.assertEqual(type(id1), int)

    def test_check_unit_exist(self):
        unit_check = unit.Unit("1000000", "COM101", "Introduction to Computer Science", "100")
        unit_check.check_unit_exist("COM101")
        with open("./unit.txt", "r", encoding='utf8') as read_unit_file:  # open user.txt and read each line
            lines = read_unit_file.readlines()
            unit_found = False
            check = "1000000,COM101,Introduction to Computer Science,100\n"
            if check in lines:  # find line with the student name and ensure it's disabled
                unit_found = True
        read_unit_file.close()
        self.assertTrue(unit_found)

    """
    User class test cases
    """
    def test_generate_user_id(self):
        user1 = user.User()
        id1 = user1.generate_user_id()
        self.assertEqual(type(id1), int)  # check if the generated value is an integer

    def test_check_username_exist(self):
        new_admin = user.User("123", "Admin1", "123", "AD", "enabled")
        new1 = new_admin.check_username_exist("stu1")  # valid user name
        new2 = new_admin.check_username_exist("stu99")  # invalid user name
        self.assertTrue(new1)
        self.assertFalse(new2)

    def test_encrypt(self):
        user1 = user.User()
        id1 = user1.encrypt('password')
        self.assertEqual(id1, "^^^Y!J#2$2%6&X(1)M*$$$")

    def test_login(self):
        user1 = user.User()
        id1 = user1.login('admin', '^^^Y!J#2$2%6&X(1)M*$$$')  # valid login
        id2 = user1.login('admin123', '^^^Y!J#2$2%6&X(1)M*$$$')  # invalid login
        self.assertEqual(id1, '17315,admin,^^^Y!J#2$2%6&X(1)M*$$$,AD,enabled')
        self.assertEqual(id2, None)

    """
    User admin class test cases
    """
    def test_admin_menu(self):
        user_admin.UserAdmin().admin_menu()

    def test_search_user(self):
        user_admin.UserAdmin().search_user("stu1")

    def test_list_all_users(self):
        user_admin.UserAdmin().list_all_users()

    def test_list_all_units(self):
        user_admin.UserAdmin().list_all_units()

    def test_enable_disable_user(self):
        admin3 = user_admin.UserAdmin(17315, 'admin', '^^^Y!J#2$2%6&X(1)M*$$$', 'AD', 'enabled')
        admin3.enable_disable_user("stu3")
        with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
            lines = read_user_file.readlines()
            user_disabled = False
            check = "21974,stu3,^^^Y!J#2$2%6&X(1)M*$$$,ST,disabled,[(COM101, 71), (PSY101, 9), (CHE101, 36)]\n"
            if check in lines:  # find line with the student name and ensure it's disabled
                user_disabled = True
        read_user_file.close()
        self.assertTrue(user_disabled)

    def test_add_user(self):
        new_admin = user_admin.UserAdmin("56789", "ad11", "password", "AD", "enabled")
        user_admin.UserAdmin().add_user(new_admin)
        with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
            lines = read_user_file.readlines()
            user_found = False
            check = "56789,ad11,^^^Y!J#2$2%6&X(1)M*$$$,AD,enabled\n"
            if check in lines:  # find line with the student name and ensure it's added
                user_found = True
        read_user_file.close()
        self.assertTrue(user_found)

    def test_delete_user(self):
        admin = user_admin.UserAdmin("17315", "admin", "^^^Y!J#2$2%6&X(1)M*$$$", "AD", "enabled")
        admin.delete_user("stu4")
        with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
            lines = read_user_file.readlines()
            user_deleted = False
            check = "70156,stu4,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 94), (PSY101, 29), (CHE101, 50)]\n"
            if check not in lines:  # find line with the student name and ensure it's disabled
                user_deleted = True
        read_user_file.close()
        self.assertTrue(user_deleted)


if __name__ == "__main__":
    unittest.main()
