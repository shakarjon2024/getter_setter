class User:
    def __init__(self, username, email, age):
        self._username = username
        self._email = email
        self.__age = age


    @property
    def username(self):
        return  self._username

    @username.setter
    def username(self, name):
        if name.islower():
            self._username = name
            print(" name muvaffaqiyatli ozgardi")
        else:
            print("ozgartirib bolmaydi")



    @property
    def email(self):
        return self._email


    @email.setter
    def email(self, value):
        if '@' in value:
            self._email = value
            print(" email muvaffaqiyatli ozgardi")
        else:
            print("ozgartirib bolmaydi")



    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self, value):
        if value < 0:
            self.__age = value
            print('age muvaffaqiyatli ozgerdi.')
        else:
            print("Yosh 0 dan kichik bola olmaydi.")


p1 = User("Tom", "difn@gmail.com", 10)
print(f"p1.username, {p1.username}")

p1.username = 'tomjon'
print(f"p1.username = {p1.username}")

print(f"p1.email = {p1.email}")

p1.email = "ajsdn@gmail.com"
print(f"p1.email = {p1.email}")

print(f"p1.age = {p1.age}")
