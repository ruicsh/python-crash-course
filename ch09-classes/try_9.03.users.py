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


alice = User("alice", "jones", age=29, eye_color="brown")
bob = User("bob", "smith", age=32, eye_color="green")
users = [alice, bob]
for user in users:
    user.describe_user()
    user.greet_user()
