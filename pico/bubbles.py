
def split_into_bubbles(arith_string):
    """takes in arithmetic string and makes list of bubble-strings"""
    #print("type of arith_string is:", type(arith_string))
    return list(arith_string.split(' + '))

def can_absorb_left(bubble):
    """false if bubble can't absorb left neighbor, for example () or ()() or ()(())"""
    ans = bubble.startswith('((')
    print(bubble, 'left', ans)
    return ans

def can_absorb_right(bubble):
    """false if bubble can't absorb right neighbor, for example () or ()() or (())()"""
    ans = bubble.endswith('))')
    print(bubble, 'right', ans)
    return ans

def absorb_left(absorber, victim):
    """return new bubble made of absorver absorbing victim"""
    return '(' + victim + absorber[1:]

def absorb_right(absorber, victim):
    """return new bubble made of absorber absorbing victim"""
    return absorber[:-2] + victim + ')'

def absorb2(left, right):
    """either the left absorbs the right or the right absorbs the left"""
    if left.endswith('))'):
        print("left!")
        # left eats right if it can
        return left[:-1] + right + ')'
    if right.startswith('(('):
        print("right!")
        # right eats left if it can
        return '(' + left + right[1:]
    # can't absorb; concatenate
    print("concatenate!")
    return left + right

def absorb2(left, right):
    """either the left absorbs the right or the right absorbs the left"""
    if right.startswith('(('):
        print("right!")
        # right eats left if it can
        return '(' + left + right[1:]
    if left.endswith('))'):
        print("left!")
        # left eats right if it can
        return left[:-1] + right + ')'
    # can't absorb; concatenate
    print("concatenate!")
    return left + right

def same_level(left, right):
    """Do they have the same number of parentheses on the joining side?"""
    for i in range(min(len(left), len(right))):
        l = left[-i-1]
        r = right[i]
        if l == '(' and r == ')':
            return True
        if l == r:
            return False

def absorb3(left, right):
    """either the left absorbs the right or the right absorbs the left"""
    if same_level(left, right):
        print("same level!")
        return left + right
    if right.startswith('(('):
        print("right!")
        # right eats left if it can
        return '(' + left + right[1:]
    if left.endswith('))'):
        print("left!")
        # left eats right if it can
        return left[:-1] + right + ')'
    # can't absorb; concatenate
    print("concatenate!")
    return left + right

def level(bubble, left):
    """level of bubble for absorption purposes. left says whether it's a left bubble"""
    for i in range(len(bubble)):
        if left and bubble[-i-1] == '(':
            return i
        if not left and bubble[i] == ')':
            return i

def absorb(left, right):
    """either the left absorbs the right or the right absorbs the left"""
    left_level, right_level = level(left, True), level(right, False)
    if left_level == right_level:
        print("same level!")
        return left + right
    if left_level < right_level:
        print("right!")
        # right eats left if it can
        return '(' + left + right[1:]
    else:
        print("left!")
        # left eats right if it can
        return left[:-1] + right + ')'
    # can't absorb; concatenate
    print("concatenate!")
    return left + right




def answer(bubbles):
    print(bubbles)
    if len(bubbles) < 2:
        return bubbles
    combined = [absorb(bubbles[0], bubbles[1])]
    combined.extend(bubbles[2:])
    return answer(combined)

def old_answer(bubbles):
    print(len(bubbles))
    print(bubbles)
    if len(bubbles) < 2:
        return bubbles
    if not can_absorb_right(bubbles[0]):
        if can_absorb_left(bubbles[1]):
            # combine bubbles and make new list
            new_bubbles = [absorb_left(bubbles[1], bubbles[0])]
            new_bubbles.extend(bubbles[2:])
            return answer(new_bubbles)
        # else they are both non-absorbing, and so should be concatenated.
        new_bubbles = [bubbles[0]+bubbles[1]]
        new_bubbles.extend(bubbles[2:])
        return answer(new_bubbles)
    # first bubble can absorb second -- but should it?
    new_bubbles = [absorb_right(bubbles[0], bubbles[1])]
    new_bubbles.extend(bubbles[2:])
    return answer(new_bubbles)
    #return answer([absorb_right(bubbles[0], bubbles[1])].extend(bubbles[2:]))

def main():
    """Loop taking in aritmetic string and output answer."""
    while(True):
        print("Enter problem:")
        arith = raw_input()
        #print(type(arith))
        bubbles = split_into_bubbles(arith)
        #print(type(bubbles))
        print(answer(bubbles))
    print("bye")

if __name__ == '__main__':
    main()

