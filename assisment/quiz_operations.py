def add(user):

    que_list = {}
    for i in range(1):
        que = input("Enter question :")
        que_list[que] = {}
        op_1 = input("Enter option-1 :")
        op_2 = input("Enter option-2 :")
        ans = input("Enter The right answer :")
        que_list[que]["A"] = op_1
        que_list[que]["B"] = op_2
        que_list[que]["Right Answer"] = ans

        temp = 1
        f = open('question.txt', 'a')
        for k in que_list.items():
            temp = temp + 1
            f.write(f"{temp}) {que} \nA :{op_1} \nB :{op_2} \nRIGHT ANS :{ans}\n")
            f.close()


def view():
    with open('question.txt') as f:
        print()
        contents = f.read()
        print(contents)


add()