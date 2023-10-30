class Circle:
    _total_circles = 0

    def __init__(self, pointX, pointY, radios):
        self.pointX = pointX
        self.pointY = pointY
        self.radios = radios
        type(self)._total_circles += 1

    @classmethod
    def get_total_circles(cls):
        return cls._total_circles

    @staticmethod
    def calculate_area(radios):
        return 3.14 * (radios * radios)
