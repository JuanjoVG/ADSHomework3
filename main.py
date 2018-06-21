from Point import Point
from PrioritySearchTree import PrioritySearchTree

pA = Point('A', 2, 2)
pB = Point('B', 1.54, 6)
pC = Point('C', 2, 5)
pD = Point('D', 6, 6)
pE = Point('E', 5, 6)
pF = Point('F', 4, 3)
pG = Point('G', 5.54, 4)
pH = Point('H', 6.52, 2.48)

P = [pA, pB, pC, pD, pE, pF, pG, pH]
pst = PrioritySearchTree(P)


def assert_result(real, expected):
    try:
        assert real == expected
    except AssertionError:
        print('Expected:', expected, 'Real:', real)


assert_result(pst.query_by_x(1), [])
assert_result(pst.query_by_x(1.54), ['B'])
assert_result(pst.query_by_x(1.99), ['B'])
assert_result(pst.query_by_x(2), ['B', 'A', 'C'])
assert_result(pst.query_by_x(3), ['B', 'A', 'C'])
assert_result(pst.query_by_x(5.0000001), ['B', 'A', 'F', 'C', 'E'])
assert_result(pst.query_by_x(7.0), ['B', 'A', 'F', 'H', 'G', 'C', 'E', 'D'])

assert_result(pst.query_by_box(0.5, 0, 100), [])
assert_result(pst.query_by_box(1.6, 0, 100), ['B'])
assert_result(pst.query_by_box(1.6, 0, 5.999), [])
assert_result(pst.query_by_box(2, 1, 6), ['B', 'A', 'C'])
assert_result(pst.query_by_box(5, 0, 5), ['A', 'F', 'C'])
assert_result(pst.query_by_box(6, 2.1, 4.5), ['F', 'G'])
assert_result(pst.query_by_box(5, 2.1, 5), ['F', 'C'])
assert_result(pst.query_by_box(7, 1, 6.5), ['B', 'A', 'F', 'H', 'G', 'C', 'E', 'D'])
assert_result(pst.query_by_box(6, 6, 6), ['B', 'E', 'D'])
