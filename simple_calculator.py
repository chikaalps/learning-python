i = 0
while i <= 3:
    number_1 = int(input("enter your first number"))
    number_2 = int(input("enter your second  number"))
    print("Menu||||")
    print("press 1 for addition")
    print("press 2 for subtraction")
    print("press 3 for floor division")
    print("press 4 for true division")
    print("press 5 for multiplication")
    selection = int(input("please pick from ur menu"))
    if selection == 1:
        print("your addition result is == ", number_1 + number_2)
    elif selection == 2:
        print("your subtraction result is == ", number_1 - number_2)
    elif selection == 3:
        print("floor division result is==", number_1 // number_2)
    elif selection == 4:
        print(""
              "true division result is ==", number_1 / number_2)
    elif selection == 5:
        print(" multiplication result is ==", number_1 * number_2)
    i=i+1
