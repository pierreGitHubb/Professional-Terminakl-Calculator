import math

print("1. Sum")
print("2. Difference")
print("3. Moltiplication")
print("4. Division")
print("5. Square Root")
print("6. Exponentiation")


choice = input("Choose an oparation: ")



if choice == "Sum":
    def sum(num1, num2):
        board = "-----------------------"
        board1 = "|                     |"
        board2 = "|                     |"
        board3 = "|                     |"
        board4 = "-----------------------"

        a = int(input('Enter a number: '))
        b = int(input('Enter an another number: '))
        result = int(a + b)

        print(board)
        print(board1)
        print("|         " + str(result) + "         |")
        print(board2)
        print(board4)

    sum(0,0)


if choice == "Difference":
    def difference(num1, num2):
        board = "-----------------------"
        board1 = "|                     |"
        board2 = "|                     |"
        board3 = "|                     |"
        board4 = "-----------------------"

        a = int(input('Enter a number: '))
        b = int(input('Enter an another number: '))
        result = int(a - b)

        print(board)
        print(board1)
        print("|         " + str(result) + "         |")
        print(board2)
        print(board4)

    difference(0,0)


if choice == "Moltiplication":
    def multi(num1, num2):
        board = "-----------------------"
        board1 = "|                     |"
        board2 = "|                     |"
        board3 = "|                     |"
        board4 = "-----------------------"

        a = int(input('Enter a number: '))
        b = int(input('Enter an another number: '))
        result = int(a * b)

        print(board)
        print(board1)
        print("|         " + str(result) + "         |")
        print(board2)
        print(board4)

    multi(0,0)

if choice == "Division":
    def divis(num1, num2):
        board = "-----------------------"
        board1 = "|                     |"
        board2 = "|                     |"
        board3 = "|                     |"
        board4 = "-----------------------"

        a = int(input('Enter a number: '))
        b = int(input('Enter an another number: '))
        result = int(a / b)

        print(board)
        print(board1)
        print("|         " + str(result) + "         |")
        print(board2)
        print(board4)

    divis(0,0)


if choice == "Square Root":
    def sqrt(num1, num2):
        board = "-----------------------"
        board1 = "|                     |"
        board2 = "|                     |"
        board3 = "|                     |"
        board4 = "-----------------------"

        a = int(input('Enter a number: '))

        result = int(math.sqrt(a))

        print(board)
        print(board1)
        print("|         " + str(result) + "         |")
        print(board2)
        print(board4)

    sqrt(0,0)


if choice == "Exponentiation":
    def exponent(num1, num2):
        board = "-----------------------"
        board1 = "|                     |"
        board2 = "|                     |"
        board3 = "|                     |"
        board4 = "-----------------------"

        a = int(input('Enter a base number: '))
        b = int(input('Enter an exponent number: '))

        result = int(a ** b)

        print(board)
        print(board1)
        print("|         " + str(result) + "         |")
        print(board2)
        print(board4)

    exponent(0,0)





def board():

    print("     7   8   9     ")
    print("     4   5   6     ")
    print("     1   2   3     ")
    print("         0         ")

board()

# Questo progetto è stato realizato interamente da Pierfrancesco Van Monckhoven