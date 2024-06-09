def function_1():
    word1 = "Wahhh"


def function_2():
    global word2  # This makes word2 a global variable, you can't assign it to "Wahhh" yet.
    word2 = "Wahhh"  # Now we can assign it to "Wahhh"


function_1()  # Sets word1 to "Wahhh"
print(word1)  # This causes the code to crash since it can't even find word1

function_2()  # Sets word2 to "Wahhh"
print(word2)  # Prints "Wahhh" since word2 is a global variable
