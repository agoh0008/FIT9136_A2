import random
class User:
    def __init__(self,user_id = "10000",user_name = "admin",user_password = "password",
                 user_role = "AD",user_status = "enabled"):
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role
        self.user_status = user_status

    def __str__(self):
        return f"{self.user_id} {self.user_name} {self.user_password}" \
               f" {self.user_role} {self.user_status}"

    def generate_user_id(self):
        '''
        Randomly generate user_id
        :param: None
        :return: user_id
        '''
        self.user_id = (random.randint(10000, 99999))
        with open("./user.txt", "r", encoding='utf8') as user_file:
            liner = []
            for line in user_file:
                line = line.rstrip()
                liner = liner + line.split(",")
            while True:
                if self.user_id not in liner:
                    user_file.close()
                    return self.user_id
                else:
                    self.user_id = (random.randint(10000, 99999))
                    continue

    def check_username_exist(self, user_name):
        '''
        Checking username 
        :param user_name:
        :return: boolean(True, False)
        '''
        self.user_name = user_name
        with open("./user.txt", "r", encoding='utf8') as user_file:
            liner = []
            liner_username = []
            for line in user_file:
                liner = line.split(",")
                liner_username.append(liner[1])
            if user_name not in liner_username:
                return False
            else:
                return True

    def encrypt(self,user_password):
        '''
        encrypt the password
        :param user_password:
        :return: en_pass (an encrypted password)
        '''
        list_pass = []
        list_pass_ord = []
        step2 = []
        step4 = []
        j=0
        str_1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        str_2 = "!#$%&()*+-./:;<=>?@\^_`{|}~"
        str_1list = []
        str_2list = []
        str_1list.extend(str_1)
        str_2list.extend(str_2)
        en_set1 = []
        en_set2 = []

        self.user_password = user_password
        list_pass.extend(user_password)
        for letter in list_pass:
          list_pass_ord.append(ord(letter))
        for num in list_pass_ord:
          step2.append(num%len(str_1list))
        for i in step2:
            en_set1.append(str_1list[i])
        while j < len(list_pass):
          step4.append(j%len(str_2list))
          j+=1
        for j in step4:
            en_set2.append(str_2list[j])
        en_pass = "^^^"+"".join("{}{}".format(x, y) for x, y in zip(en_set1, en_set2))+"$$$"
        return en_pass

    def login(self,user_name,user_password):
        '''
        checking username and password in the user.txt
        :param user_name:
        :param user_password:
        :return:  line(user information), None(if username is not be found)
        '''
        self.user_name = user_name
        self.user_password = user_password
        with open("./user.txt", "r", encoding='utf8') as user_file:
            for line in user_file:
                line = line.rstrip()
                liner = line.split(",")
                if liner[1] != user_name:
                    continue
                else:
                    if liner[2] != user_password:
                        return None
                    elif liner[4] == "disabled":
                        print("User is disable...Please contact admin")
                        return None
                    else:
                        return line
