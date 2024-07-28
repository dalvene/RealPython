desserts = ["ice cream", "cookies"]
print(desserts)
desserts.sort()
print(desserts)
print(desserts.index("ice cream"))
food = desserts[:]
food.extend(["broccoli", "turnips"])
print(desserts)
print(food)
food.remove("cookies")
print(food[:2])
cookies = "cookies, cookies, cookies"
breakfast = cookies.split()

def select_num(some_list):
    for n in some_list:
        if 1 <= n <= 20:
            print(n)

numlist = [2, 4, 8, 16, 32, 64]
select_num(numlist)
