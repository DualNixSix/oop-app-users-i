class user:
    def __init__(self, name, email, dl):
        self.name = name
        self.email = email 
        self.dl = dl 
    def __str__(self):
        return f"My Name is {self.name}"


Alice = user("Alice", "Alice@mail.com", 12345)
Bob = user("Bob", "Bob@mail.com", 54321)
