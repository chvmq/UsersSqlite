email_list_check = ['@mail.ru', '@gmail.com', '@yandex.ru']
import sqlite3 as sq

class User:
    def __init__(self, connect):
        self.cur = connect.cursor()
        self.name = None
        self.age = None
        self.email = None

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        try:
            int_age = int(age)
            if int_age in range(14, 100):
                self.age = int_age
            else:
                self.age = 19
        except ValueError:
            self.age = 19

    def setEmail(self, email):
        self.cur.execute(f'''select * from users where email = "{email}";''')
        row_existing = self.cur.fetchone()
        if row_existing:
            raise Exception('already exists')
        else:
            for mail in email_list_check:
                if mail in email:
                    self.email = email
                    break
                else:
                    self.email = ''

        # try:
        #     self.cur.execute(f"select * from users where email = {email}")
        #     row_exist = self.cur.fetchone()
        #     if row_exist:
        #         raise Exception('already existing...')
        #     else:
        #         for mail in email_list_check:
        #             if mail in email:
        #                 self.email = email
        #                 break
        #             else:
        #                 self.email = ''
        # except:
        #     pass

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getEmail(self):
        return self.email