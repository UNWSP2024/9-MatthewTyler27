#Matthew Tyler
#10/31/25
#Total Numnber

import random

def random_numbers():
    while True:
        count = int(input("How many random numbers would you like(1-1000)?"))
        if count < 0 or count > 1000:
            print("Please enter a valid number")
        else:
            break
    
    with open("random_number.txt", "w") as file:
        for i in range(count):
            numbers = random.randint(1, 500)
            file.write(str(numbers)+"\n")
            
            

if __name__ == '__main__':
    random_numbers()
