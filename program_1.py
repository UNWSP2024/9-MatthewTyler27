#Matthew Tyler
#10/29/25
#Item Counter

def count_file_lines():
    ######################
    # Add your code here #
    ######################
    with open("names.txt", "r") as names:
        lines = names.readlines()
        print("Number of lines in the file:", len(lines))


# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
