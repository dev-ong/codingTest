def solution(survey, choices):
    types = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    answer = ''
    for i in range(len(survey)):
        score = choices[i] - 4
        if score > 0:  # 동의
            types[str(survey[i][1])] += score
        elif score <= 0:  # 비동의
            types[str(survey[i][0])] += score * -1

    if types["R"] >= types["T"]:
        answer += 'R'
    else:
        answer += 'T'

    if types["C"] >= types["F"]:
        answer += 'C'
    else:
        answer += 'F'

    if types["J"] >= types["M"]:
        answer += 'J'
    else:
        answer += 'M'

    if types["A"] >= types["N"]:
        answer += 'A'
    else:
        answer += 'N'

    return answer