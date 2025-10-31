#Matthew Tyler
#10/31/25
#Average Numbers

def sum_numbers_from_file():
    try:
        total = 0
        with open("numbers.txt", "r") as file:
            for number in file:
                try:
                    integer = int(number.strip())
                    total += integer
                except ValueError:
                    print("One of the numbers was not a valid number")
        print("The total is:",total)
    except IOError:
        print("Something Went Wrong")

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()
