class Rectangle:

    def __init__(self, h, w):
        self.height = h
        self.width = w
        self.area = self.calc_area()
        self.perimeter = self.calc_perimeter()
    
    def calc_area(self):
        return self.height*self.width
    def calc_perimeter(self):
        return 2*(self.height+self.width)
