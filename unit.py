import random

class Unit():

    def __init__(self, unit_id = "1000000", unit_code = "", unit_name = "", unit_capacity = 0):
        self.unit_id = unit_id
        self.unit_code = unit_code
        self.unit_name = unit_name
        self.unit_capacity = unit_capacity

    def __str__(self):
        return "Unit ID: {}, Unit code: {}, Unit name: {}, Unit capacity: {}".format(self.unit_id, self.unit_code, self.unit_name, self.unit_capacity)

    def generate_unit_id(self):
        """
        Generates new unit ID for a unit
        :param: None
        :return: an integer number consisting of 7 digits (self.unit_id)
        """
        self.unit_id = (random.randint(1000000, 9999999))
        with open("./unit.txt", "r", encoding='utf8') as unit_file:
            existing_unit_id = []

            for line in unit_file:
                line = line.rstrip()
                existing_unit_id = existing_unit_id + line.split(",")

            # if unit ID already exists, generate new one
            while True:
                if self.unit_id not in existing_unit_id:
                    return self.unit_id
                else:
                    print("Unit ID already exists.")
                    self.unit_id = (random.randint(1000000, 9999999))
                    continue

    def check_unit_exist(self,unit_code):
        """
        Checks if unit already exist in unit.txt
        :param: unit_code
        :return: true if unit exist in unit.txt, false otherwise
        """
        self.unit_code = unit_code
        with open("./unit.txt", "r", encoding='utf8') as unit_file:
            liner = []
            for line in unit_file:
                liner = liner + line.split(",")
            if unit_code not in liner:
                return False
            else:
                return True
