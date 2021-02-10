'''

'''

for tc in range(4):
    x1, y1, x2, y2, a1, b1, a2, b2 = map(int, input().split())

    output = 'a'

    if a2 < x1 or x2 < a1 or y1 > b2 or y2 < b1:
        output = 'd'

    if y1 == b2:
        if x1 == a2 or a1 == x2:
            output = 'c'
        else:
            output = 'b'
    if a1 == x2:
        if b1 == y2 or y1 == b2:
            output = 'c'
        else:
            output = 'b'
    if b1 == y2:
        if a1 == x2 or x1 == a2:
            output = 'c'
        else:
            output = 'b'
    if a2 == x1:
        if b1 == y2 or y1 == b2:
            output = 'c'
        else:
            output = 'b'

    print(output)