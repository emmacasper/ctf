#!/usr/bin/env python

import math

# what's up with equations:
# mx + b, unless m = float('nan')
# in which case the equation is x = b

def get_points(x_0, y_0, x_n, y_n, n):
    # gets all points for n-edged polygon with center (x_0, y_0) and one vertex at (y_1, y_1)
    r = math.pow(math.pow(x_0 - x_n, 2) + math.pow(y_0 - y_n, 2), 0.5)
    a = math.acos((x_n - x_0 + 0.0)/r)
    return [(x_0 + r * math.cos(a+2*math.pi*i/n), y_0 + r * math.sin(a+2*math.pi*i/n)) for i in range(n)]

def get_segments(x_0, y_0, x_n, y_n, n):
    # gets all segments for the n-edged polygon
    points = get_points(x_0, y_0, x_n, y_n, n)
    segs = []
    for i in range(len(points) - 1):
        segs.append((points[i], points[i+1]))
    segs.append((points[0], points[-1]))
    return segs

def intersection_point(m1, b1, m2, b2):
    # finds intersection between two line segments and returns point, or None if not intersecting
    # case both are vertical
    if m1 == float('nan') and m2 == float('nan'):
        if b1 == b2:
            pass
            # uh oh infinite overlap they're the same line
        return None
    # case m1 is vertical
    if m1 == float('nan'):
        return (b1, b1 * m2 + b2)
    # case m2 is vertical
    if m2 == float('nan'):
        return (b2, b2 * m1 + b1)
    # normal cases
    # not sure about this one... what if they are the same line???
    if m1 == m2:
        return None
    x = (b2 - b1 + 0.0) / (m1 - m2)
    y = m1 * x + b1
    return (x, y)

def within_bounds(p1, p2, p):
    # given point p on the line going through p1 and p2, is it between them?
    if p[0] < p1[0] and p[0] < p2[0]:
        return False
    if p[1] < p1[1] and p[1] < p2[1]:
        return False
    if p[0] > p1[0] and p[0] > p2[0]:
        return False
    if p[1] > p1[1] and p[1] > p2[1]:
        return False
    return True

def intersect((x1, y1), (x2, y2), m, b):
    # finds point of intersection of line segment using x-y coordinates, and mx+b line, or None
    if x1 == x2:
        slope = float('nan')
        intercept = x1
    else:
        slope = (y1 - y2 + 0.0)/ (x1 - x2)
        intercept = y1 - x1*slope
    p = intersection_point(slope, intercept, m, b)
    if p and within_bounds((x1, y1), (x2, y2), p):
        return p
    return None

def guard_equation(x,y):
    # return slope for guard's line of sight (intercept is 0)
    if x == 0:
        return float('nan')
    if y == 0:
        return 0
    return x*1.0/y

def on_wall((x, y), r):
    #true if point x,y is on the all of radius r
    ans = math.pow(x,2) + math.pow(y,2) == math.pow(r,2)
    if ans:
        print(x, y, "is on hte wall", r)
    else:
        print(x, y, "is not on the wall", r)
    return ans

def drop_poly(clear, blocked, r, n, x0, y0, x1, y1):
    # drops a polygon with n edges at location x0, y0 and vertex at x1, y1
    # moves guards from blocked to clear if the polygon clears their path through the wall at radius r
    edges = get_segments(x0, y0, x1, y1, n)
    for guard in blocked:
        gm, gb = guard_equation(guard[0], guard[1]), 0
        possible = []
        for edge in edges:
            p = intersect(edge[0], edge[1], gm, gb)
            if p is not None:
                possible.append(p)
        if len(possible) == 0:
            continue
        if len(possible) == 1 and on_wall(possible[0], r):
            clear.add(guard)
            blocked.remove(guard)
            continue
        # else there are two of them
        if on_wall(possible[0], r) or on_wall(possible[1], r):
            clear.add(guard)
            blocked.remove(guard)
        # neither is on wall. does polygon cover wall?
        d0 = math.pow(possible[0][0],2) + math.pow(possible[0][1], 2)
        d1 = math.pow(possible[1][0],2) + math.pow(possible[1][1], 2)
        r2 = math.pow(r,2)
        if (d0 > r2 and d1 < r2) or (d0 < r2 and d1 > r2):
            clear.add(guard)
            blocked.remove(guard)

def take_shots(polys, guards, r):
    clear = ()
    blocked = set(guards)
    for poly in polys:
        print("dropping poly", poly)
        drop_poly(clear, blocked, r, poly[4], poly[0], poly[1], poly[2], poly[3])
        if len(blocked) == 0:
            break
        print("clear guards:", clear)
    chance = 1.0
    for guard in clear:
        chance *= guards[2]
    return chance

gs = [(11,0,0.1), (0,11,0.1)]
ps = [(10,0,11,0,3), (0,10,0,10.5,3)]
print(take_shots(ps, gs, 10))


