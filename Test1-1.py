def solution(input_string):
    answer = list()

    for i in range(97, 123):
        character = ""
        character = chr(i)
        num = input_string.count(character)
        if (
            num >= 2
            and not input_string.rindex(character) < input_string.index(character) + num
        ):
            answer.append(character)

    answer.sort()
    return "".join(answer) if len(answer) else "N"
