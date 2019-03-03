
pk = [99, 1235, 865, 990, 5, 1443, 895, 1477]

def to_binary_backwards(x):
    res = []
    for i in range(8):
        res.append(x % 2 == 1)
        x = x//2
    return res

def encrypt(c):
    binary = to_binary_backwards(ord(c))
    return sum([pk[i] for i in range(8) if binary[i]])

