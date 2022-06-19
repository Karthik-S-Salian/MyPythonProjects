from math import sqrt, pi


def area_triangle(side_1, side_2, side_3):
    s = (side_1 + side_2 + side_3) / 2
    return sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))


def area_circle(radius):
    return pi * radius * radius


def circumference(radius):
    return pi * 2 * radius


def area_sphere(radius):
    return 4 * pi * radius * radius


def volume_sphere(radius):
    return 4 * pi * radius * radius * radius / 3


def volume_cube(length):
    return length * length * length


def volume_cuboid(length, breadth, height):
    return length * breadth * height
