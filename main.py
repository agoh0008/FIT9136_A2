'''
Group No. 49
Group member:
29796431 Alexandra Goh
33516553 Kwansajee Sathong
27208001 Sothearith Tith
There are 7 classes and 46 functions
'''

import user
import user_admin
import user_student
import user_teacher
import unit
import re

def main_menu():
	'''
	print login menu
	:param: None
	:return: None
	'''
	print("\nWelcome to Monash Student Information Management System")
	print("Login: login to the program")
	print("Exit: exit the program\n")

def generate_test_data():
	'''
	write user information into user.txt and unit information into unit.txt
	:param: None
	:return: None
	'''
	user_file = open("./user.txt", "w", encoding="utf-8")
	user_file.write(f"17315,admin,^^^Y!J#2$2%6&X(1)M*$$$,AD,enabled\n"
					f"27170,teach1,^^^Y!J#2$2%6&X(1)M*$$$,TA,enabled,[COM101]\n"
					f"62393,teach2,^^^Y!J#2$2%6&X(1)M*$$$,TA,enabled,[PSY101]\n"
					f"22206,teach3,^^^Y!J#2$2%6&X(1)M*$$$,TA,enabled,[CHE101]\n"
					f"17604,stu1,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 99), (PSY101, 43), (CHE101, 20)]\n"
					f"61098,stu2,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 32), (PSY101, 80), (CHE101, 45)]\n"
					f"21974,stu3,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 71), (PSY101, 9), (CHE101, 36)]\n"
					f"70156,stu4,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 94), (PSY101, 29), (CHE101, 50)]\n"
					f"63476,stu5,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 79), (PSY101, 49), (CHE101, 72)]\n"
					f"84227,stu6,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 77), (PSY101, 34), (CHE101, 98)]\n"
					f"40478,stu7,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 22), (PSY101, 36), (CHE101, 95)]\n"
					f"98248,stu8,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 55), (PSY101, 28), (CHE101, 4)]\n"
					f"94791,stu9,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 56), (PSY101, 44), (CHE101, 60)]\n"
					f"25724,stu10,^^^Y!J#2$2%6&X(1)M*$$$,ST,enabled,[(COM101, 7), (PSY101, 76), (CHE101, 65)]\n"
					)
	user_file.close()
	unit_file = open("./unit.txt", "w", encoding="utf-8")
	unit_file.write(f"1000000,COM101,Introduction to Computer Science,100\n"
					f"1123123,PSY101,Introduction to Psychology,100\n"
					f"5467893,CHE101,Introduction to Chemistry,100\n")
	unit_file.close()

def main():
	'''
	main function
	:param: None
	:return: None
	'''
	generate_test_data()
	def begin():
		'''
		start the program after generate the data
		:param: None
		:return: None
		'''
		main_menu()
		start = (input("1. Login\n2. Exit\nEnter number: ")).lower()
		if start == "1": #login

			list = []
			user1 = user.User()
			user1.user_name = (input("Username: ").lower())
			user1.user_password = input("Password: ")
			user1.user_password = (user1.encrypt(user1.user_password))
			approve = user1.login(user1.user_name.lower(), user1.user_password)

			if approve is None:
				print("Invalid username or password. Try again. ")
				if __name__ == "__main__":
					begin()
			else:
				list = approve.split(",")
				print("Login success... ...")
				if list[3] == "AD":
					a = True
					while a is True:
						user_admin1 = user_admin.UserAdmin(list[0], list[1], list[2], list[3], list[4])
						user_admin1.admin_menu()
						admin_opt = input("Enter menu number: ").strip()
						if admin_opt == "1":  # Search
							search_user = (input("Searching username: ").lower()).strip()
							user_admin1.search_user(search_user)
							continue
						elif admin_opt == "2":  # List all user
							user_admin1.list_all_users()
							continue
						elif admin_opt == "3":  # List all unit
							user_admin1.list_all_units()
							continue
						elif admin_opt == "4":  # Mod Status
							status_user = (input("Enter username to enabled or disabled: ").lower()).strip()
							user_admin1.enable_disable_user(status_user)
							continue
						elif admin_opt == "5":  # Add user
							user_id = user1.generate_user_id()
							while True:
								user_name = (input("Enter new username: ").lower()).strip()
								if user_name == "": # if input is empty
									print("Invalid input, Username cannot be empty: ")
									continue
								user_checker = bool(
									re.match(r'^(?!_{1,}$)[A-Za-z0-9_]*$', user_name))  # check username char
								if user_checker is True:
									check_exist = user1.check_username_exist(user_name)  # check existed
									if check_exist is False:
										break
									elif check_exist is True:
										print("Username Exist!")
										continue
								elif user_checker is False:
									print(f"Invalid Username, Username can contain only characters, "
										  f"numbers and underscores. Underscores must be paired with "
										  f"characters and numbers.")
									continue
							user_password = input("Enter user password: ")  # password
							while True:
								user_role = input("Enter user role:\n1.Teacher\n2.Student\nEnter:  ").strip()
								if user_role == "1" or user_role == "2":
									break
								else:
									print("Invalid input")
									continue
							while True:
								print("Enter user status\n1. enabled\n2. disabled")  # status
								user_status_opt = (input("Enter: ")).strip()
								if user_status_opt == "1":
									user_status = "enabled"
									break
								elif user_status_opt == "2":
									user_status = "disabled"
									break
								else:
									print("Invalid input!")
									continue
							if user_role == "1":  # role: teacher
								user_role = "TA"
								user_admin1.add_user(
									user_teacher.UserTeacher(user_id, user_name, user_password, user_role, user_status))
							elif user_role == "2":  # role: student
								user_role = "ST"
								user_admin1.add_user(
									user_student.UserStudent(user_id, user_name, user_password, user_role, user_status))
							continue

						elif admin_opt == "6":  # Delete user
							while True:
								del_user = (input("Enter username: ").lower()).strip()
								if del_user == "":
									print("Invalid option!")
									continue
								elif del_user == "admin":
									print("Cannot delete admin!!!\n")
									break
								else:
									user_admin1.delete_user(del_user)
									break

						elif admin_opt == "7":  # log out
							print("logging out...\n")
							a = False
							if __name__ == "__main__":
								begin()
						else:
							print("Invalid input!")
							continue

				elif list[3] == "TA":
					teach_units = re.findall(r'\[(.*?)\]', approve)  # extracting unit info
					t_units = []  # stor all units info
					for i in teach_units:  # reconstruct unit info for writing and calling student class
						f = teach_units[0].strip("[]").split(",")
						t_units.append(i)
					user_teacher1 = user_teacher.UserTeacher(list[0], list[1], list[2], list[3], list[4], t_units)
					a = True
					while a is True:
						user_teacher1.teacher_menu()
						unit1 = unit.Unit()
						teacher_opt = input("Enter menu number: ").strip()
						if teacher_opt == "1":  # list unit info
							user_teacher1.list_teach_units()
							continue
						elif teacher_opt == "2":  # add unit
							unit_id = unit1.generate_unit_id()
							while True:
								while True:
									unit_code = (input("Enter new unit code: ").upper()).strip()
									pattern = (r'^[a-zA-Z]{3}\d{3}$')
									if re.match(pattern, unit_code): #check unit code format 3 alphabets and 3 numbers
										break
									else:
										print(
											"Invalid input!, Unitcode format should be 3 letters followed by 3 numbers only")
										continue
								unit_exist = unit1.check_unit_exist(unit_code) #check unit code exist
								if unit_exist == False:
									while True:
										unit_name = input("Enter new unit name: ").strip()
										if unit_name == "": #unit name cannot be empty
											print("Please enter unit name")
											continue
										else:
											break
									while True:
										try:
											unit_capacity = (input("Enter new unit capacity: ")).strip()
											unit_capacity = int(unit_capacity)
											if unit_capacity <= 0: #check capacity, must more than 0
												print("Invalid input, Capacity must more than 0")
												continue
											break
										except ValueError: #checking when the input is not integer
											print("Invalid input!")
											continue
									user_teacher1.add_teach_unit(
										unit.Unit(unit_id, unit_code, unit_name, unit_capacity))
									break
								elif unit_exist == True: #check unit code
									print("Unit code already exists. Try again.")
									continue
							continue
						elif teacher_opt == "3":  # delete unit
							while True:
								del_unit_code = (input("Enter unit code: ").upper()).strip()
								if del_unit_code == "":
									print("Invalid input, unit code cannot be empty.")
									continue
								else:
									user_teacher1.delete_teach_unit(del_unit_code)
									break
							continue
						elif teacher_opt == "4":  # list student
							unit_code = (input("Enter unit code: ").upper()).strip()
							user_teacher1.list_enrol_students(unit_code)
							continue
						elif teacher_opt == "5":  # avg min max
							unit_code = (input("Enter unit code: ").upper()).strip()
							user_teacher1.show_unit_avg_max_min_score(unit_code)
							continue
						elif teacher_opt == "6":  # log out
							print("logging out...\n")
							a = False
							if __name__ == "__main__":
								begin()
						else:
							print("Invalid input!")
							continue

				elif list[3] == "ST":
					all_units = re.findall(r'\([^)]*\)', approve)  # extracting unit info
					s_units = []  # store all units info
					for i in all_units:  # reconstruct unit info for writing and calling student class
						f = i.strip("()").split(", ")
						if len(f) == 2:
							s_units.append((f[0], int(f[1])))
					user_student1 = user_student.UserStudent(list[0], list[1], list[2], list[3], list[4], s_units)#send info to student class
					a = True
					while a is True:
						user_student1.student_menu()
						student_opt = input("Enter menu number: ").strip()
						if student_opt == "1":  # list available unit
							user_student1.list_available_units()
							continue
						elif student_opt == "2":
							user_student1.list_enrolled_units()  # list enrol unit
							continue
						elif student_opt == "3":  # enrol drop
							while True:
								unit_code = (input("Enter unit code to enrol: ").upper()).strip()
								if unit_code == "":
									print("Please enter unit code")
									continue
								else:
									user_student1.enrol_unit(unit_code)
									break
							continue
						elif student_opt == "4":  # drop unit
							unit_code = (input("Enter unit code to drop: ").upper()).strip()
							user_student1.drop_unit(unit_code)
							continue
						elif student_opt == "5":  # check score
							unit_code = (input("Enter unit code: ").upper()).strip()
							user_student1.check_score(unit_code)
							continue
						elif student_opt == "6":  # generate score
							unit_code = (input("Enter unit code: ").upper()).strip()
							user_student1.generate_score(unit_code)
							continue
						elif student_opt == "7":  # log out
							print("logging out...\n")
							a = False
							if __name__ == "__main__":
								begin()
						else:
							print("Invalid input!")
							continue
		elif start == "2": #Exit
			print("Exit the program...")
		elif start == "": #check if input is empty
			print("You did not enter anything.")
			if __name__ == "__main__": # go back begin function
				begin()
		else:
			print("Invalid option")
			if __name__ == "__main__":
				begin()
	begin()

if __name__ == "__main__":
	main()