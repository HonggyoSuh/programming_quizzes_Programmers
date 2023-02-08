def solution(queries):
    answer = []
    hashmap = {1: "RR", 2: "Rr", 3: "Rr", 4: "rr"}

    for i, j in queries:
        if i == 1:
            answer.append("Rr")
        elif i == 2:
            answer.append(hashmap[j])
        else:
            div = j - 1
            for x in range(i):
                a, b = divmod(div, 4)
                if b == 0 or b == 3:
                    answer.append(hashmap[b + 1])
                    break
                if a == 0:
                    answer.append("Rr")
                    break
                div = a

    return answer


# not working
