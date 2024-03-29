class Human:
    def __init__(self, name, birthsday, number, city, country, adress):
        self.name = name
        self.birtshday = birthsday
        self.number = number
        self.city = city
        self.country = country
        self.adress = adress

    def display_info(self):
        print("Name: ", self.name)
        print("Birthsday: ", self.birtshday)
        print("Number: ", self.number)
        print("City: ", self.city)
        print("Country: ", self.country)
        print("Adress: ", self.adress)

    def update_number(self, new_number):
        self.number = new_number
        print("Phone number updated successfully.")
        print()


person = Human("Alex Gray", "1999 - 19 - 9", "+123534532", "Kiev", "Ukraine", "st.Class")
person.display_info()
print()
person.update_number("+4234254265")
person.display_info()