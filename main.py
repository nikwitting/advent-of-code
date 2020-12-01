def day1():
    text_file = open("day1.txt", "r")
    lines = text_file.readlines()
    costs = [int(i) for i in lines]
    for i, cost in enumerate(costs):
        for cost2 in costs[i:]:
            sum=cost+cost2
            #print(sum)
            if sum==2020:
                print("cost1: " + str(cost) + " cost2: " + str(cost2))
                print(cost*cost2)

def day1b():
    text_file = open("day1.txt", "r")
    lines = text_file.readlines()
    costs = [int(i) for i in lines]
    for i, cost in enumerate(costs):
        for j, cost2 in enumerate(costs[i:]):
            for cost3 in costs[i+j:]:
                sum=cost+cost2+cost3
                #print(sum)
                if sum==2020:
                    print("cost1: " + str(cost) + " cost2: " + str(cost2) + " cost3: " + str(cost3))
                    print(cost*cost2*cost3)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day1()
    day1b()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
