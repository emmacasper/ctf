
def expand_poly(lst):
    """Given list of ns such that x^n = 1, turn it into an array"""
    arr = [0 for n in max(lst)]
    for n in lst:
        arr[n] = 1
    return arr

def formula(poly):
    """the formula the problem uses; takes in array and outputs 0 or 1"""
    if poly[0] == 1:
        return 1
    if poly[64] == 1:
        return 1
    if poly[96] == 1:
        return 1
    if poly[128] == 1 and poly[192] == 1 and poly[255] == 1:
        return 1
    return 0

class LFSR:
    def __init__(self, poly, fun):
        self.poly = expand_poly(lst)
        self.fun = fun
    def rotate():
        """Shift polynomial once and output boolean of end bit"""
        res = poly[-1]
        self.poly.insert(0, fun(self.poly))
        self.poly.pop()
#        newpoly = [fun(self.poly)]
#        newpoly.extend(self.poly[1:-1])
#        self.poly = newpoly
        return res

def ands(poly, nums):
    for num in nums:
        if poly[num] == 0:
            return 0
    return 1



