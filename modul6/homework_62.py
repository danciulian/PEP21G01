class CarFactory():
    """Class to track series and car numbers"""


    def __init__(self, start_series: int, car_numbers: int):
        self.start_series = start_series
        self.car_numbers = car_numbers
        lot_start = start_series // 20 + 1  # if start_series % 20 else 0
        lot_end = (start_series + car_numbers) // 20 + 1
        self.lot = list(range(lot_start, lot_end + 1))
        self.car_series = list(range(start_series, start_series + car_numbers + 1))


    def __iter__(self):
        return CarIter(self.lot)


    def get_right_steering_wheel(self):
        right_steering_wheel = []

        for cars in self.car_series:
            if cars % 2 == 0:
                right_steering_wheel.append(cars)
        print(right_steering_wheel)


    def get_left_steering_wheel(self):
        left_steering_wheel = []
        for cars in self.car_series:
            if cars % 2 != 0:
                left_steering_wheel.append(cars)
        print(left_steering_wheel)


class CarIter():
    """Class for iterating all series """

    def __init__(self, lot: list):
        self.lot = lot

    def __iter__(self):
        return self

    def __next__(self):
        if not self.lot:
            raise StopIteration
        else:
            return self.lot.pop(0)


cars = CarFactory(314, 90)
print(cars.lot)
cars.get_right_steering_wheel()
cars.get_left_steering_wheel()

with open('file', 'w') as file:
    for x in cars.lot:
        file.write(str(x) + '\n')
