import random
import user
import re


class UserStudent(user.User):
    def __init__(self, user_id="3312", user_name="JDA", user_password="2314", user_role="ST", user_status="enabled",
                 enrolled_units=None):
        if enrolled_units is None:
            enrolled_units = []
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role
        self.user_status = user_status
        self.enrolled_units = enrolled_units
        super().__init__(self.user_id, self.user_name, self.user_password, self.user_role, self.user_status)

        # self.unit_list = []

    def __str__(self):
        return "{},{},{},{},{},{}".format(self.user_id, self.user_name, self.user_password, self.user_role,
                                          self.user_status, self.enrolled_units)

    def student_menu(self):
        """
        Print the menu of student
        :param: None
        :return: None
        """
        print("\nSTUDENT MENU")
        print("1. List all available units information")
        print("2. List all enrolled units")
        print("3. Enrol a unit")
        print("4. Drop a unit")
        print("5. Check the score of a unit")
        print("6. Generate score")
        print("7. Logout")

    def list_available_units(self):
        """
        List out the unit available for student to enrol
        :param: None
        :return: None
        """
        print("These are the available units")
        with open("./unit.txt", "r", encoding='utf8') as f_unit:  # open unit.txt and read each line
            unit_data = f_unit.readlines()

        all_u = []  # store all units
        for line in unit_data:
            info = line.strip().split(",")  # Extract unit information from txt file
            unit_code = info[1]
            unit_name = info[2]
            all_u.append([unit_code, unit_name])  # store the unit info to the list
        for j in self.enrolled_units:  # go through all the enrolled units
            for k in all_u:  # go through all the units
                if j[0] == k[0]:  # mark the units already enrolled
                    k[0] = ""
        for l in all_u:  # print out the units that have not enrolled
            if l[0] != "":
                print(l[0], l[1])

        f_unit.close()

    def list_enrolled_units(self):
        """
        List the unit that student enrolled
        :param: None
        :return: None
        """
        if len(self.enrolled_units) > 0:  # check if enrolled in any unit or not
            print("Here is the list of units you study:")
            for i in self.enrolled_units:  # print out the units
                print(i[0])
        else:
            print("You have not enrol in any unit")

    def enrol_unit(self, unit_code):
        """
        Add a unit to current list of unit enrolled and update the user.txt
        :param: unit code that student want to enrol in
        :return: None
        """
        enrolled = False
        if len(self.enrolled_units) < 3:  # check number of units enrolled
            for i in self.enrolled_units:
                if i[0] == unit_code:  # check if unit already enrolled
                    enrolled = True
                    print("Unit already enrolled")
                    break
            if enrolled is False:
                if self.check_unit_capacity(unit_code, "enrol") is True:  # check unit exist and capacity
                    self.enrolled_units.append((unit_code, -1))  # add unit to enrolled list

                    new_details = self.__str__()
                    self.update_student_details(new_details)  # update student details in txt file
                else:
                    print("Unit enrol fails")
        else:
            print("You have reached max number of unit")

    def drop_unit(self, unit_code):
        """
        Remove a unit from the list of units the student is currently studying and update the user.txt
        :param: unit code that student want to drop
        :return: None
        """
        target_found = False
        if len(self.enrolled_units) > 0:  # check if student is enrolled in any units
            if self.check_unit_capacity(unit_code, "drop"):  # check unit availability and update unit.txt
                for i in self.enrolled_units:  # find the unit in enrolled units list
                    if i[0] == unit_code:
                        self.enrolled_units.remove(i)  # remove unit from enrolled list
                        target_found = True
                        # print("Unit dropped")
                        new_details = self.__str__()  # update student details in txt file
                        self.update_student_details(new_details)
            if target_found is False:  # did not enrol => cannot drop
                print("Unit drop fails")
        else:
            print("You have not enrolled in any units")

    def check_score(self, unit_code="all"):
        """
        Show the score of the unit. If no unit code is given, show all score
        :param: unit code that need to check the score
        :return: None
        """
        have_unit = False
        for i in self.enrolled_units:  # find unit
            if unit_code == "all":  # not unit code given => print all scores
                print("Your score for", i[0], "is", i[1])
            elif i[0] == unit_code:  # found unit => print score
                print("Your score for", unit_code, "is", i[1])
                have_unit = True

        if have_unit is False:  # did not enrol => no score to show
            print("You are not enrolled in this unit to see score")

    def generate_score(self, unit_code):
        """
        Generate score for the unit and update the user.txt
        :param: unit code that need to generate score
        :return: None
        """
        score = random.randint(0, 100)  # generate score
        target_found = False
        for i in range(len(self.enrolled_units)):  # find unit
            if self.enrolled_units[i][0] == unit_code:  # found unit
                target_found = True
                self.enrolled_units[i] = (self.enrolled_units[i][0], score)  # allocate score
                new_details = self.__str__()  # update student details in txt file
                self.update_student_details(new_details)
                print("Score generated")
        if target_found is False:  # unit not enrolled => cannot allocate score
            print("Cannot find unit to generate score")

    def update_student_details(self, new_details):
        """
        Update the user.txt with new details of the student
        :param: new details the need to update for this student
        :return: None
        """
        with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
            lines = read_user_file.readlines()

        for line in lines:
            info = line.split(",")
            if self.user_name == info[1]:  # find line with the student name and remove that line
                lines.remove(line)
                break
        read_user_file.close()

        with open("./user.txt",
                  "w", encoding='utf8') as write_user_file:  # open user.txt and write back each line except the one removed
            write_user_file.writelines(lines)
        write_user_file.close()

        with open("./user.txt", "a", encoding='utf8') as append_user_file:  # open user.txt and append new updated line
            # write user object details as a new line
            append_user_file.write(re.sub(r"[']", r'', str(new_details)) + "\n")  # remove '
        append_user_file.close()

    def check_unit_capacity(self, unit_code, action):
        """
        Check the unit availability and update the unit.txt
        :param: unit code to check the capacity and the action(enrol or drop)
        :return: true if action success, false otherwise
        """
        all_units = []
        with open("./unit.txt", "r", encoding='utf8') as f_unit:  # open unit.txt and read each line
            unit_data = f_unit.readlines()

        for line in unit_data:  # Extract all unit info
            info = line.strip().split(",")
            each_units = [info[0], info[1], info[2], int(info[3])]
            all_units.append(each_units)  # save to all unit list for calculating/checking later
        f_unit.close()
        success = False  # if enrol unit or drop unit success or not
        found_unit = False
        for i in all_units:
            if i[1] == unit_code and i[3] > 0 and action == "enrol":  # check if have unit and capacity
                i[3] -= 1  # have unit => enrol success, capacity -1
                print("Enrol success,", i[1])
                success = True
                found_unit = True
            elif i[1] == unit_code and action == "drop":  # check if have unit
                i[3] += 1  # have unit => drop success, capacity +1
                print("Drop success,", i[1])
                success = True
                found_unit = True
            elif i[1] == unit_code and i[3] == 0 and action == "enrol":  # unit is full
                print("This unit is full, enrol fail")
                success = False
                found_unit = True

        if found_unit is False: # unit is not found in the unit.txt
            success = False
            print("Unit code not found")

        if success:  # write back to unit.txt
            f = open("./unit.txt", "a", encoding='utf8')  # Create a blank file
            f.seek(0)  # sets  point at the beginning of the file
            f.truncate()  # Clear previous content
            for i in all_units:
                f.write(i[0] + ',' + i[1] + ',' + i[2] + ',' + str(i[3]) + '\n')
            f.close()  # Close file

        return success

