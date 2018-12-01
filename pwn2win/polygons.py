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
    #print("got segments:", segs)
    return segs

def intersection_point(m1, b1, m2, b2):
    # finds intersection between two line segments and returns point, or None if not intersecting
    # case both are vertical
    if math.isnan(m1) and math.isnan(m2):
        #print("ipoint: both are nan")
        if b1 == b2:
            pass
            # uh oh infinite overlap they're the same line
        return None
    # case m1 is vertical
    if math.isnan(m1):
        #print("ipoint: m1 is nan")
        return (b1, b1 * m2 + b2)
    # case m2 is vertical
    if math.isnan(m2):
        #print("ipoint: m2 is nan")
        return (b2, b2 * m1 + b1)
    # normal cases
    # not sure about this one... what if they are the same line???
    if m1 == m2:
        #print("ipoint: same slope")
        return None
    x = (b2 - b1 + 0.0) / (m1 - m2)
    y = m1 * x + b1
    return (x, y)

def within_bounds(p1, p2, p):
    # given point p on the line going through p1 and p2, is it between them?
    #print("checking bounds for", p1, p2, p)
    if p[0] < p1[0] and p[0] < p2[0]:
        return False
    if p[1] < p1[1] and p[1] < p2[1]:
        return False
    if p[0] > p1[0] and p[0] > p2[0]:
        return False
    if p[1] > p1[1] and p[1] > p2[1]:
        return False
    return True

def intersect((x1, y1), (x2, y2), m, b, lst):
    # finds point of intersection of line segment using x-y coordinates, and mx+b line
    # if it does intersect, add it to lst.
    # if the lines are the same, add the two endpoints of the line to lst.
    # case they're both vertical
    if x1 == x2 and math.isnan(m):
        # if they're not in the same horizontal place, nope!
        if b != x1:
            return
        #print("they're both vertical")
        lst.append((x1,y1))
        lst.append((x2,y2))
        return
    # case only one is vertical
    if x1 == x2:
        #print("segment is vertical")
        p = intersection_point(float('nan'), x1, m, b)
        #print("segment vertical point is:", p)
        if p and within_bounds((x1, y1), (x2, y2), p):
            lst.append(p)
        return
    # case they're the same slope, but not vertical
    if (y1 - y2 + 0.0) / (x1 - x2) == m:
        # if they have different intercepts, it doesn't work :(
        if b != m*x1 - y1:
            #print("they're parallel")
            return
        lst.append((x1,y1))
        lst.append((x2,y2))
        return
    slope = (y1 - y2 + 0.0)/ (x1 - x2)
    intercept = y1 - x1*slope
    p = intersection_point(slope, intercept, m, b)
    if p and within_bounds((x1, y1), (x2, y2), p):
        #print("this one overlapped!")
        lst.append(p)
    

def guard_equation(x,y):
    # return slope for guard's line of sight (intercept is 0)
    if x == 0:
        return float('nan')
    if y == 0:
        return 0
    return x*1.0/y

def dist(x, y):
    return math.pow(x, 2) + math.pow(y, 2)

def on_wall((x, y), r):
    #true if point x,y is on the all of radius r
    if math.isnan(x) or math.isnan(y) or math.isnan(r):
        #print("oh no it's nan we dont' know if it's on the walllll")
    ans = math.pow(x,2) + math.pow(y,2) == math.pow(r,2)
    if ans:
        #print(x, y, "is on hte wall", r)
        pass
    else:
        #print(x, y, "is not on the wall", r)
        pass
    return ans

def drop_poly(guards, r, n, x0, y0, x1, y1):
    # drops a polygon with n edges at location x0, y0 and vertex at x1, y1
    # moves guards from blocked to clear if the polygon clears their path through the wall at radius r
    edges = get_segments(x0, y0, x1, y1, n)
    for g in range(len(guards)-1, -1, -1):
        guard = guards[g]
        gm, gb = guard_equation(guard.x, guard.y), 0
        #print("guard:", gm)
        possible = []
        for edge in edges:
            intersect(edge[0], edge[1], gm, gb, possible)
        # polygon misses guard, and also helpful bit of wall
        if len(possible) == 0:
            continue
        # only the corner did something.
        if len(possible) == 1:
            if on_wall(possible[0], guard.d):
                # guard gets squashed :(
                guards.remove(guard)
            if on_wall(possible[0], r):
                # wall got squashed !
                guard.see = True
            continue
        # else there are two of them
        if on_wall(possible[0], guard.d) or on_wall(possible[1], guard.d):
            # guard got squashed by edge of polygon...
            guards.remove(guard)
        # neither is on wall:
        d0 = math.pow(possible[0][0],2) + math.pow(possible[0][1], 2)
        d1 = math.pow(possible[1][0],2) + math.pow(possible[1][1], 2)
        if (d0 > guard.d and d1 < guard.d) or (d0 < guard.d and d1 > guard.d):
            # guard got squashed
            guards.remove(guard)
        # guard is not squashed.
        # is wall squashed by tangent?
        if on_wall(possible[0], r) or on_wall(possible[1], r):
            guard.see = True
        # neither is on wall. 
        #does polygon cover wall?
        r2 = math.pow(r,2)
        if (d0 > r2 and d1 < r2) or (d0 < r2 and d1 > r2):
            guard.see = True

class Guard():
    def __init__(self, x, y, prob):
        self.x = x
        self.y = y
        self.prob = prob
        self.see = False
        self.d = math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

def take_shots(polys, guards, r):
    guard_objs = [Guard(g[0], g[1], g[2]) for g in guards]
    for poly in polys:
        #print("dropping poly", poly)
        drop_poly(guard_objs, r, poly[4], poly[0], poly[1], poly[2], poly[3])
        # all the guards got squashed...
        if len(guard_objs) == 0:
            return 1
    chance = 1.0
    maxdist = 0
    for guard in guard_objs:
        if guard.see:
            chance *= guard.prob
    return chance

gs = [(0,11,0.1)] #[(11,0,0.1), (0,11,0.1)]
ps = [(10,0,11,0,3), (0,10,0,10.5,3)]
print(take_shots(ps, gs, 10))


