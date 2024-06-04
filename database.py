class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = {}
        self.load()

    def load(self):
        with open(self.filename, "r") as file:
            for line in file:
                email, password, name, created = line.strip().split(";")
                self.users[email] = (password, name, created)

    def add_user(self, email, password, name):
        if email not in self.users:
            self.users[email] = (password, name, "2024-06-04")  # Assuming creation date is today
            self.save()

    def validate(self, email, password):
        if email in self.users:
            return self.users[email][0] == password
        return False

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        return None

    def save(self):
        with open(self.filename, "w") as file:
            for email, (password, name, created) in self.users.items():
                file.write(f"{email};{password};{name};{created}\n")
