def print_score(score: int):
    print(f'The score is {score} points.')


def print_result(score: int):
    result = score + 10
    print(f'Bonus applied: {result}')
    print_score(result)


def main():
    score = 50
    print_result(30)
    print_score(score)


main()