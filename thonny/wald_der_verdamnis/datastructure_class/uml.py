class Land:
    def __init__(self,name,continent,language,capital,area,population,internet_tld):
        self.name=name
        self.continent=continent
        self.language=language
        self.capital=capital
        self.area=area
        self.population=population
        self.internet_tld=internet_tld
    def give_info(self):
        print(self.name)
        print(self.continent)
        print(self.language)
        print(self.capital)
        print(self.area)
        print(self.population)
        print(self.internet_tld)
        print()
    def set_area(self,area):
        self.area=area
        print(self.area)
    def set_population(self,population):
        self.population=population
        print(self.population)
land1=Land("Panama","Suedamerika","Spanisch","Panama-Stadt","75.517 km2","4,4 Millionen",".pa")
land2=Land("Philippinen","Asien","Filipino","Manila","300.000 km2","109.035.343",".ph")
land1.give_info()
land2.give_info()