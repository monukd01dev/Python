import ast

def takinginput():
    inputValue = eval(input("Enter the Elements: "))
    return tuple(inputValue)

if __name__ == '__main__':
    l = takinginput()
    print(l)
    for item in l:
        print(item)

