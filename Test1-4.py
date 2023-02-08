from collections import deque


def solution(program):
    answer = []
    queue = deque()
    next = 0
    waitlist = deque()
    running = deque()

    while queue:
        if count == next:
            if len(running) != 0:
                running.pop()
            for i in queue:
                if i[1] <= count:
                    waitlist.append((queue.pop(i), count))

        if len(running) == 0:
            to_run = 0
            max_point = 0
            for index, j in enumerate(waitlist):
                if max_point < j[1]:
                    to_run = j
                    max_point = j[1]
            running.append(waitlist.pop(j))
            next += j[2]

        count += 1
    print(count)
    return answer
