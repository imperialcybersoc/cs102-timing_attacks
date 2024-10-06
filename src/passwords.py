class PassObject:
    def __init__(self):
        self.passwords = ["password", "password123", "password1234", "password12345", "password123456"]

    def get_password(self, index):
        if index < 0 or index >= len(self.passwords):
            raise ValueError("index out of range")
        return self.passwords[index]

fred = PassObject()