def add_new_highscore(inventory):
    print("Wprowadz swoje imię ")
    name = input()

    score = [name, sum(inventory.values())]

    score_to_file = score[0] + '|' + str(score[1])
    return score_to_file


def save_file(save_score):
    try:
        with open('some.csv', 'a') as highscore_write:
            highscore_write.write(save_score + "\n")
    except:
        with open('some.csv', 'w') as highscore_write:
            highscore_write.write(save_score + "\n")


def read_file():
    with open('some.csv', encoding='utf-8-sig') as csvfile:
        to_split = csvfile.readlines()
        splitted = [line.strip().split("|") for line in to_split]
    return splitted


def print_highscore(splitted):
    sorted_list = sorted(splitted, key=lambda item: int(item[1]))
    for score in sorted_list[0:5]:
        print(score)
