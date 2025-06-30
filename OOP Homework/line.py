class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        # d = sqrt((x_2 - x_1)^2 + (y_2 - y_1)^2)
        x_1, y_1 = self.coor1
        x_2, y_2 = self.coor2
        return ((x_2 - x_1)**2 + (y_2 - y_1)**2)**0.5

    def slope(self):
        # m = (y_2 - y_1) / (x_2 - x_1)
        x_1, y_1 = self.coor1
        x_2, y_2 = self.coor2
        return (y_2 - y_1) / (x_2 - x_1)

coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())