import user
import re


class UserTeacher(user.User):

    def __init__(self, user_id="2332", user_name="SDC", user_password="2344", user_role="TA", user_status="enabled",
                 teach_units=None):
        if teach_units is None:
            teach_units = []
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role
        self.user_status = user_status
        self.teach_units = teach_units
        super().__init__(user_id, user_name, user_password, user_role, user_status)

    def __str__(self):
        return "{},{},{},{},{},{}".format(self.user_id, self.user_name, self.user_password, self.user_role,
                                          self.user_status, self.teach_units)

    def teacher_menu(self):
        """
        List the options user can use
        :param: None
        :return: None
        """
        print("\nTEACHER MENU")
        print("1. List all teaching units")
        print("2. Add a unit")
        print("3. Delete a unit")
        print("4. List all students’ information and scores of one unit")
        print("5. Show the avg/max/min score of one unit")
        print("6. Logout")

    def list_teach_units(self):
        """
        List the unit the teacher is currently teaching
        :param: None
        :return: None
        """
        if len(self.teach_units) > 0:  # check teach any unit or not
            print("Here is the list of units you teach:")
            for i in self.teach_units:
                print(i.strip())
        else:
            print("You have not teach any unit")

    def add_teach_unit(self, unit_obj):
        """
        Add new unit to the list of units the teacher is currently teaching and update user.txt & unit.txt
        :param: unit object containing all unit info
        :return: None
        """
        with open("./unit.txt", "a", encoding='utf8') as append_unit:  # open unit.txt and append new unit
            append_unit.write(
                f"{unit_obj.unit_id},{unit_obj.unit_code},{unit_obj.unit_name},{unit_obj.unit_capacity}\n")
        append_unit.close()
        self.teach_units.append(unit_obj.unit_code)
        new_details = self.__str__()  # update teacher details in txt file
        self.update_teacher_details(new_details)
        print("Unit", unit_obj.unit_code, "added")

    def delete_teach_unit(self, unit_code):
        """
        Remove the unit from the list of units the teacher is currently teaching, remove the unit from unit.txt and
        remove the unit from any students enrolled in it, update the user.txt
        :param: unit code to be deleted
        :return: None
        """
        unit_found = False
        for i in self.teach_units:  # find unit in teach unit list
            if i == unit_code:  # unit found
                unit_found = True
                self.teach_units.remove(i)  # remove from teach unit list
                self.remove_unit(i)  # remove unit from unit.txt
                print("Unit", unit_code, "removed")
                self.update_teacher_details(self.__str__())  # update teacher details
                break
        if unit_found is False:  # unit not found
            print("No unit found to remove")
        else:  # update student details who are enrolled in the unit in user.txt
            with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
                lines = read_user_file.readlines()

            to_pop = []  # store student details who are enrolled in the unit
            for line in lines:
                if unit_code in line and "ST" in line:  # extract student details
                    to_pop.append(line)
            read_user_file.close()

            with open("./user.txt", "w", encoding='utf8') as write_user_file:  # open user.txt and write
                for i in lines:
                    if i in to_pop:  # skip those are enrolled in the unit
                        continue
                    else:
                        write_user_file.write(i)
            write_user_file.close()

            with open("./user.txt",
                      "a", encoding='utf8') as append_user_file:  # append the student who are enrolled in the unit with new details
                for m in to_pop:
                    info = m.split(",")
                    all_units = re.findall(r'\([^)]*\)', m)  # extracting unit info
                    units = []  # stor all units info
                    for i in all_units:  # reconstruct unit info for writing and calling student class
                        f = i.strip("()").split(", ")
                        if f[0] != unit_code and len(f) == 2:  # keep the other units
                            units.append((f[0], int(f[1])))
                    t = ("{},{},{},{},{},{}".format(info[0], info[1], info[2], info[3], info[4], units))
                    append_user_file.write(re.sub(r"[']", r'', str(t) + "\n"))  # remove '
            append_user_file.close()

    def list_enrol_students(self, unit_code):
        """
        List all students who are enrolled in this unit and their information
        :param: unit code that teacher wanted to see students who enrolled in it
        :return: None
        """
        with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
            lines = read_user_file.readlines()

        have_student = False
        print("These are the students:")
        for line in lines:
            if unit_code in line:  # check each student for the given unit code
                x = line.split(",")
                all_units = re.findall(r'\([^)]*\)', line)  # get all units
                for i in all_units:  # get the wanted unit code
                    f = i.strip("()").split(", ")
                    if f[0] == unit_code and len(f) == 2 and x[3] == 'ST':  # found unit => display student info
                        have_student = True
                        if int(f[1]) == -1:  # score -1 => student not yet completed this unit
                            print("Name:", x[1], " ID:", x[0], "Score: Not yet completed")
                        else:
                            print("Name:", x[1], " ID:", x[0], "Score:", f[1])
        read_user_file.close()

        if have_student is False:  # no students enrol in this unit
            print("No student enrol in this unit")

    def show_unit_avg_max_min_score(self, unit_code):
        """
        Show the average, min and max score of the unit
        :param: unit code that teacher wanted to see the avg, min, max score
        :return: None
        """
        with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
            lines = read_user_file.readlines()

        found_unit = False
        num_student = 0  # count the number of students
        score = []  # store all the score
        neg_score = 0  # count the number of negative score
        for line in lines:  # check for the given unit code in each line
            if unit_code in line:
                found_unit = True
                all_units = re.findall(r'\([^)]*\)', line)  # get all units
                for i in all_units:  # get the wanted unit code
                    f = i.strip("()").split(", ")
                    if f[0] == unit_code and len(f) == 2:  # found unit => start calculation
                        num_student += 1
                        if int(f[1]) < 0:  # student has negative score
                            neg_score += 1
                        else:
                            score.append(int(f[1]))

        if num_student == 0 and found_unit is True:  # have unit but no student enrol in it
            print("No student enrol in this unit")
        elif found_unit is False:  # invalid unit code
            print("No unit found")
        elif len(score) == 0 and neg_score == 0:  #
            print("No score generated due to no student enrolled in this unit")
        elif len(score) == 0 and neg_score > 0:  # students who are enrolled have complete this unit yet
            print("There are", neg_score, "students that have not completed the unit")
            print("The average, max and min score for this unit is 0")
        else:
            avg = sum(score) / len(score)
            print("The average score for this unit is", round(avg, 2))
            print("The max score for this unit is", max(score))
            print("The min score for this unit is", min(score))

        read_user_file.close()

    def remove_unit(self, unit_code):
        """
        Remove the unit from the unit.txt
        :param: unit code to remove
        :return: None
        """
        all_units = []  # store all unit information
        with open("./unit.txt", "r", encoding='utf8') as f_unit:  # open unit.txt and read each line
            unit_data = f_unit.readlines()

        for line in unit_data:  # Extract all unit information
            info = line.strip().split(",")
            each_units = [info[0], info[1], info[2], int(info[3])]
            all_units.append(each_units)
        f_unit.close()

        success = False # if unit is removed successfully or not
        for i in all_units:
            if i[1] == unit_code:   # remove the unit successfully
                all_units.remove(i)
                success = True

        if success:  # write back to unit.txt if unit is removed
            f = open("./unit.txt", "a", encoding='utf8')  # Create a blank file
            f.seek(0)  # sets  point at the beginning of the file
            f.truncate()  # Clear previous content
            for i in all_units: # write to unit.txt
                f.write(i[0] + ',' + i[1] + ',' + i[2] + ',' + str(i[3]) + '\n')
            f.close()  # Close file

    def update_teacher_details(self, new_details):
        """
        Update the details of the teacher and write to user.txt
        :param: new details to be updated for this teacher
        :return: None
        """
        with open("./user.txt", "r", encoding='utf8') as read_user_file:  # open user.txt and read each line
            lines = read_user_file.readlines()

        for line in lines:
            info = line.split(",")
            if self.user_name == info[1]:  # find line with the teacher name and remove that line
                lines.remove(line)
                break
        read_user_file.close()

        with open("./user.txt",
                  "w", encoding='utf8') as write_user_file:  # open user.txt and write back each line except the one removed
            write_user_file.writelines(lines)
        write_user_file.close()

        with open("./user.txt", "a", encoding='utf8') as append_user_file:  # open user.txt and append new updated line
            # write user object details as a new line
            append_user_file.write(re.sub(r"[']", r'', str(new_details).strip()) + "\n")  # remove '
        append_user_file.close()

