import user
import re

class UserAdmin(user.User):

    def __init__(self, user_id="10000", user_name = "admin", user_password = "password", user_role = "AD", user_status = "enabled"):
        super().__init__(user_id, user_name, user_password, user_role, user_status)
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role
        self.user_status = user_status

    def __str__(self):
        return "User ID: {}, User name: {}, User password: {}, User role: {}, " \
               "User status: {}".format(self.user_id, self.user_name,
                                        self.user_password, self.user_role, self.user_status)

    def admin_menu(self):
        """
        Print the menu of admin
        :param: None
        :return: None
        """
        print(f"ADMIN MENU:\n"
              f"1. Search user information\n"
              f"2. List all users' information\n"
              f"3. List all units' information\n"
              f"4. Enable/Disable user\n"
              f"5. Add user\n"
              f"6. Delete user\n"
              f"7. Log out")

    def search_user(self, user_name):
        """
        Searches for user within user.txt file
        :param: user_name
        :return: None
        """
        user_found = self.check_username_exist(user_name)

        with open("./user.txt", "r", encoding='utf8') as f:
            for line in f:
                user_data = line.strip().split(",")

                if user_data[1] == user_name and user_data[3] == "TA":
                    user_info = f"User ID: {user_data[0]}, User name: {user_data[1]}, User password: {user_data[2]}, "\
                                f"User role: {user_data[3]}, User status: {user_data[4]}, Units taught: {user_data[5]}"
                    break
                elif user_data[1] == user_name and user_data[3] == "ST":
                    user_info = f"User ID: {user_data[0]}, User name: {user_data[1]}, User password: {user_data[2]}, "\
                            f"User role: {user_data[3]}, User status: {user_data[4]}, Units enrolled: {user_data[5:]}"
                    break
                elif user_data[1] == user_name and user_data[3] == "AD":
                    user_info = UserAdmin(user_id=user_data[0], user_name=user_data[1],
                                          user_password=user_data[2], user_role=user_data[3],
                                          user_status=user_data[4])
                    break

        if user_found:
            print(user_info)
        else:
            print(f"No user found with user name: {user_name}")

    def list_all_users(self):
        """
        Lists all users in user.txt file
        :param: None
        :return: None
        """
        with open("./user.txt", "r", encoding='utf8') as f_user:
            user_data = f_user.readlines()

        for line in user_data:
            user_info = line.rstrip()
            user_info = user_info.split(",")
            if len(user_info) == 5:
                print(f"User ID: {user_info[0]}, User name: {user_info[1]}, User password: {user_info[2]}, "
                                f"User role: {user_info[3]}, User status: {user_info[4]}")
            elif len(user_info) > 5:
                if user_info[3] == "TA":
                    print(f"User ID: {user_info[0]}, User name: {user_info[1]}, User password: {user_info[2]}, "
                          f"User role: {user_info[3]}, User status: {user_info[4]}, Units taught: {user_info[5]}")
                elif user_info[3] == "ST":
                    print(f"User ID: {user_info[0]}, User name: {user_info[1]}, User password: {user_info[2]}, "
                          f"User role: {user_info[3]}, User status: {user_info[4]}, Units enrolled: {user_info[5:]}")


    def list_all_units(self):
        """
        Lists all units in unit.txt file
        :param: None
        :return: None
        """
        with open("./unit.txt", "r", encoding='utf8') as f_unit:
            unit_data = f_unit.readlines()

        for line in unit_data:
            # Extract unit information from the line
            info = line.strip().split(",")
            unit_id = info[0].split(",")
            unit_code = info[1].split(",")
            unit_name = info[2].split(",")
            unit_capacity = info[3].split(",")

            # Print list of units
            print("Unit ID: {}, Unit code: {}, Unit name: {}, Capacity: {}".format("".join(map(str, unit_id)),
                                                                                   "".join(map(str, unit_code)),
                                                                                   "".join(map(str, unit_name)),
                                                                                   "".join(map(str, unit_capacity))))

    def enable_disable_user(self, user_name):
        """
        Changes user status from enabled to disabled (or vice versa)
        :param: user_name
        :return: None
        """
        user_found = self.check_username_exist(user_name)
        if user_found:
            with open("./user.txt", "r", encoding='utf8') as user_file:
                lines = user_file.readlines()

            # iterates over range of indices of the lines list and split line into list of strings
            for i in range(len(lines)):
                user_info = lines[i].strip().split(",")
                if user_info[1] == user_name:
                    if "enabled" in user_info:
                        lines[i] = lines[i].replace("enabled", 'disabled')
                        print(f"User {user_name} has been disabled.")
                    elif "disabled" in user_info:
                        lines[i] = lines[i].replace("disabled", "enabled")
                        print(f"User {user_name} has been enabled.")

            with open("./user.txt", "w", encoding='utf8') as user_file:
                user_file.writelines(lines)

        else:
            print(f"No user found with user name: {user_name}")

    def add_user(self, user_obj):
        """
        Adds a new user to user.txt file
        :param: user_obj
        :return: None
        """

        # open file in append mode
        user_obj.user_password = self.encrypt(user_obj.user_password)

        with open("./user.txt", "a", encoding='utf8') as f_user:
            # write user object details as a new line
            if user_obj.user_role == "TA":
                f_user.write(f"{user_obj.user_id},{user_obj.user_name},{user_obj.user_password},"
                             f"{user_obj.user_role},{user_obj.user_status}\n")
            elif user_obj.user_role == "ST":
                f_user.write(f"{user_obj.user_id},{user_obj.user_name},{user_obj.user_password},"
                             f"{user_obj.user_role},{user_obj.user_status}\n")
            elif user_obj.user_role == "AD":
                f_user.write(f"{user_obj.user_id},{user_obj.user_name},{user_obj.user_password},"
                             f"{user_obj.user_role},{user_obj.user_status}\n")
            f_user.close()


    def delete_user(self, user_name):
        """
        Deletes an existing user from user.txt file
        :param: user_name
        :return: None
        """
        user_found = self.check_username_exist(user_name)

        with open("./user.txt", "r", encoding='utf8') as user_file:
            a=[]
            for user_line in user_file:
                user_line = user_line.strip().split(",")

                # identifies if user's role is a Teacher
                if user_line[1] == user_name and user_line[3] == "TA":
                    # set index i to 5
                    i = 5
                    # identify exact unit code that teacher teaches
                    # while loop runs until i reaches length of user_line list (which is unit teacher teaches)
                    while i < len(user_line):
                        unit = user_line[i]
                        unit = unit.strip("[]\n'").split(',')
                        i +=1
                        a = a + unit

        # Delete unit from unit.txt:
        # Read the contents of unit.txt into a list
        with open('./unit.txt', 'r', encoding='utf8') as unit_file:
            unit_list = unit_file.readlines()

        # Remove any lines that contain unit:
        unit_list = [line for line in unit_list if not any(unit_code in line for unit_code in a)]

        # Write the updated list back to unit.txt
        with open('./unit.txt', 'w', encoding='utf8') as unit_file:
            unit_file.writelines(unit_list)

        # Remove student enrollment:

        with open("./user.txt", 'r', encoding='utf8') as f:
            user_lines = f.readlines()

        # Iterate through the list of students and modify their enrollment information
        pattern = r'\(\s*([A-Z]{3}\d{3})\s*,\s*(\d{1,2})\s*\)'

        for i, line in enumerate(user_lines):
            user_info = line.strip().split(",")
            if user_info[3] == "ST":
                enrollment = re.findall(pattern, line)
                for subject, grade in enrollment[:]:
                    if subject in a:
                        enrollment.remove((subject, grade))
                enrollment_str = '[' + ', '.join([f"({subj}, {grade})" for subj, grade in enrollment]) + ']'
                user_lines[i] = f"{user_info[0]},{user_info[1]},{user_info[2]},{user_info[3]},{user_info[4]},{enrollment_str}\n"

        # Write the updated user.txt file
        with open("./user.txt", 'w', encoding='utf8') as f:
            f.writelines(user_lines)

        # Delete user from user.txt completely:
        with open("./user.txt", "r", encoding='utf8') as user_file:
            lines = user_file.readlines()
            if user_found:
                for line in lines:
                    if line.split(',')[1] == user_name:
                        lines.remove(line)
                        print(f"User {user_name} has been deleted.")
                with open("./user.txt", "w", encoding='utf8') as user_file:
                    user_file.writelines(lines)

            else:
                print(f"No user found with user name: {user_name}")