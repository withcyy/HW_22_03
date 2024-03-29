class Country:
    def __init__(self, name, continent, population, dialing_code, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.dialing_code = dialing_code
        self.capital = capital
        self.cities = cities

    def display_info(self):
        print("Country Name:", self.name)
        print("Continent:", self.continent)
        print("Population:", self.population)
        print("Dialing Code:", self.dialing_code)
        print("Capital:", self.capital)
        print("Cities:", ", ".join(self.cities))
        print()

    def update_population(self, new_population):
        self.population = new_population
        print("Population updated successfully.")
        print()

    def add_city(self, city):
        self.cities.append(city)
        print("City added successfully.")
        print()

country = Country("Ukraine", "Europe", "40M", "+380", "Kyiv", ["Lviv", "Kharkiv", "Odessa"])
country.display_info()
country.update_population("45M")
country.add_city("Dnipro")
country.display_info()