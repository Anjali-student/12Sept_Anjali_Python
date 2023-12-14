def add():

    que_list = {}
    for i in range(1):
        que_list[que] = {}
        que_list[que]["A"] = op_1
        que_list[que]["B"] = op_2
        que_list[que]["Right Answer"] = ans

        temp = 1
        for k in que_list.items():
            temp = temp + 1
            print(f"{temp}) {que} \nA :{op_1} \nB :{op_2} \nRIGHT ANS :{ans}\n")





que = input("Enter question :")
op_1 = input("Enter option-1 :")
op_2 = input("Enter option-2 :")
ans = input("Enter The right answer :")
add()
