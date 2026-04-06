class User:
    def __init__(self, first_name, last_name, **kwargs):
        self.f_name = first_name
        self.l_name = last_name
        self.info = kwargs

    def describe_user(self):
        print(f"{self.f_name.title()} {self.l_name.title()} info:")
        print(self.info)

    def greet_user(self):
        print(f"Hello, {self.f_name.title()}!")


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name, privileges, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.privileges = Privileges(privileges)


alice = Admin("alice", "jones", ["can add post"], department="Physics")
alice.privileges.show_privileges()
