#for i in range(1, 4):
#    j = i * 2
#    print("i is", i, "and j is", j)

def add_underscores(word):
    new_word = "_"
    for i in range(0, len(word)):
        new_word = new_word + word[i] + "_"
    return new_word

phrase = "hello"
print(add_underscores(phrase))
