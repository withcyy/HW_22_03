class City:
    def __init__(self, name, region, country, population, index, number):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.index = index
        self.number = number

    def display_info(self):
        print("Name: ", self.name)
        print("Region: ", self.region)
        print("Country: ", self.country)
        print("Population: ", self.population)
        print("Index: ", self.index)
        print("Number: ", self.number)
        print()

    def change_index(self, new_index):
        self.index = new_index
        print("Index changed")
        print()

    def change_name(self, new_name):
        self.name = new_name
        print("Name changed")
        print()

city = City("Kiev", "Kiev area", "Ukraine", "4M", "42310", "+380")
city.display_info()
city.change_name("Kiev_v2")
city.change_index("431345")
city.display_info()