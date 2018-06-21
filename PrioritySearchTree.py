import statistics
from typing import List

from Point import Point


class PrioritySearchTree:
    def __init__(self, points: List[Point]):
        self.point = None
        self.mid_y = None
        self.left = None
        self.right = None
        if not points: return

        points.sort(key=lambda p: p.x)
        self.point, points = points[0], points[1:]
        if not points: return

        self.mid_y = statistics.median((p.y for p in points))
        left_points = [p for p in points if p.y <= self.mid_y]
        right_points = [p for p in points if p.y > self.mid_y]
        if left_points: self.left = PrioritySearchTree(left_points)
        if right_points: self.right = PrioritySearchTree(right_points)

    def __repr__(self):
        s = '(' + str(self.point)
        if self.mid_y: s += ' - ' + str(self.mid_y)
        s += '):{' + str(self.left) + ', ' + str(self.right) + '}'
        return s

    def query_by_x(self, x):
        return self.query_by_box(x, float('-Inf'), float('Inf'))

    def query_by_box(self, x, y1, y2):
        result = []
        if self.point.x <= x:
            if self.point.in_y(y1, y2): result += [self.point.id]
            if self.left and self.mid_y >= y1: result += self.left.query_by_box(x, y1, y2)
            if self.right and self.mid_y <= y2: result += self.right.query_by_box(x, y1, y2)
        return result
