class Planet:
    def __init__(self, name, planet_type, star):
        valid1 = True
        valid2 = True
        for i in [name, planet_type, star]:
            if not isinstance(i, str):
                valid1 = False
                break
            if i == '':
                valid2 = False
                break
        if not valid1:
            raise TypeError('name, planet type, and star must be strings')
        if not valid2:
            raise ValueError('name, planet_type, and star must be non-empty strings')
        self.name = name
        self.planet_type = planet_type
        self.star = star
        
    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'
    
    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'
    
planet_1 = Planet('Mars', 'Rocky', 'Sol')
planet_2 = Planet('Jupiter', 'GasGiant', 'Sol')
planet_3 = Planet('Earth', 'Terrestial', 'Sol')

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())