#n = 1
#while (n < 5):
#    print("n = ", n)
#    n = n + 1
#print("Loop finished")

#for n in range(1, 5):
#    print("n = ", n)
#print("Loop finished")

#for n in range(2, 11):
#    print(n)

#n = 2
#while n < 11:
#    print(n)
#    n = n + 1

#number = input("Enter a number: ")
#for n in [2, 4, 8]:
#    print(int(number) * n)

def invest(amount, rate, time):
    print("principal amount: $" + str(amount))
    print("annual rate of return: " + str(rate))
    for n in range(1, time + 1):
        amount = amount * (1 + rate)
        print(f"year {n}: ${total}")
    print()

invest(100, 0.05, 8)
invest(2000, 0.025, 5)
