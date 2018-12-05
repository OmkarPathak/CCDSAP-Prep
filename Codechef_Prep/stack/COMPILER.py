for _ in range(int(input())):
    symbol = input()
    count = 0
    stack = []
    result = 0
    for sym in symbol:
        if sym == '<':
            stack.append(sym)
        elif sym == '>':
            if stack == []:
                result += (count * 2)
                count = 0
                break
            else:
                stack.pop()
                count += 1
                if stack == []:
                    result += (count * 2)
                    count = 0
    if stack == []:
        result += (count * 2)
    print(result)