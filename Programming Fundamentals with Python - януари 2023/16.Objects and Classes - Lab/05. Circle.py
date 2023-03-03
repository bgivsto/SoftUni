class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.d = diameter

    def calculate_circumference(self):
        return Circle.__pi*self.d

    def calculate_area(self):
        return Circle.__pi*((self.d/2)**2)

    def calculate_area_of_sector(self, angle):
        return ((self.d/2)**2)*angle/360*Circle.__pi