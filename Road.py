class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self, weigth=25, thikness=5):
        return f"{self._length} M * {self._width} M * {weight} кг * {thickness} см =" \
               f" {(self._length * self._width * weight * thickness) / 1000} т"

road_1 = Road(5000, 20)
print(road_1.get_full_profit())