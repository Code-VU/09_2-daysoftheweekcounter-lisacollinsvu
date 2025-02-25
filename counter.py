def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    fhand = open(file_name)
    counter = {}
    for line in fhand:
        if line.startswith("From"):
            line = line.split()
            try:
                if line[2] not in counter: counter[line[2]] = 1
                else: counter[line[2]] = counter[line[2]] + 1
            except: next
    print(counter)


## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
