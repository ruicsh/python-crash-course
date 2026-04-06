class User:
    def __init__(self, first_name, last_name, **kwargs):
        self.f_name = first_name
        self.l_name = last_name
        self.info = kwargs
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.f_name.title()} {self.l_name.title()} info:")
        print(self.info)

    def greet_user(self):
        print(f"Hello, {self.f_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


alice = User("alice", "jones", age=29, eye_color="brown")
alice.increment_login_attempts()
alice.increment_login_attempts()
alice.increment_login_attempts()
alice.increment_login_attempts()
print(f"{alice.f_name.title()} has {alice.login_attempts} failed login attempts.")

alice.reset_login_attempts()
print(f"{alice.f_name.title()} has {alice.login_attempts} failed login attempts.")
