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

def day2():
    text_file = open("day2.txt", "r")
    lines = text_file.readlines()

    lines2 = [i.split() for i in lines]
    validcount=0
    for line in lines2:
        limit=line[0].split("-")
        min=int(limit[0])
        max=int(limit[1])
        char=line[1][0]
        password=line[2]
        if password.count(char)>=min and password.count(char)<=max:
            validcount+=1
            print(line)
    print("Number of valid passwords: "+str(validcount))

def day2b():
    text_file = open("day2.txt", "r")
    lines = text_file.readlines()

    lines2 = [i.split() for i in lines]
    validcount=0
    for line in lines2:
        limit=line[0].split("-")
        min=int(limit[0])
        max=int(limit[1])
        char=line[1][0]
        password=line[2]
        if bool(password[min-1]==char) != bool(password[max-1]==char):
            validcount+=1
            print(line)
    print("Number of valid passwords: "+str(validcount))

if __name__ == '__main__':
    #day1()
    #day1b()
    #day2()
    day2b()

