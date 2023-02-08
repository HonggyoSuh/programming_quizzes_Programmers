def solution(program):
    program.sort(key=lambda x: (-x[1], -x[0]))
    print(program)
    result = [0 for _ in range(11)]
    count = 0
    next = 0

    while program or count < next:
        print(count)
        if count >= next:
            curr = program.pop()
            result[curr[0]] += count - curr[1]
            next += curr[2]
            program.sort(key=lambda x: (-x[0] if x[1] <= next else -x[0] * next, -x[1]))
            print(program)
            print(curr, count - curr[1], next)
        count += 1

    result[0] = count

    return result


# not working
