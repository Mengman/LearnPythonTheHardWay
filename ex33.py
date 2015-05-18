
def set_numbers(size):
    i = 0
    numbers = []

    while i < size:
        print "At the top i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers

numbers = set_numbers(int(raw_input("Enter the size of array: ")))    

print "The numbers: "
for num in numbers:
    print num
