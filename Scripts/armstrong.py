def armstrong():
    num = input("Enter any number: ")
    power = len(num)
    sum = 0

    for i in range (len(num)):
        sum += int(num[i])**power
    if sum == int(num):
        print("Armstrong")
    else:
        print("Not an armstrong")
armstrong()