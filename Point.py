class Point:
    def __init__(self, id: str, x: float, y: float):
        self.id = id
        self.x = x
        self.y = y

    def __repr__(self):
        return '[' + str(self.x) + ', ' + str(self.y) + ']'

    def in_y(self, y1, y2):
        return y1 <= self.y <= y2
