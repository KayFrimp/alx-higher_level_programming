#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    while(len(tuple_a) < 2):
        tuple_a = list(tuple_a)
        tuple_a.append(0)
        tuple_a = tuple(tuple_a)
    while(len(tuple_b) < 2):
        tuple_b = list(tuple_b)
        tuple_b.append(0)
        tuple_b = tuple(tuple_b)
    x1, y1 = tuple_a
    x2, y2 = tuple_b
    return x1 + x2, y1 + y2
