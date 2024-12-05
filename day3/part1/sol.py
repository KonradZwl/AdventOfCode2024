# Part 1 solution
def process_input(data):
    print("Part 1 solution")
    input = ''.join(data).replace('\n', '')
    sum = 0

    # Loop through characters of string looking for the pattern mul(xxx,yyy)
    for i in range(len(input)):

        #Check for the pattern mul(xxx,yyy)
        if input[i:i+4] == "mul(":
            counter = i + 4
            firstNumber = ""
            while input[counter].isdigit():
                firstNumber += input[counter]
                counter += 1

            # Set iterator equal to the counter after reaching last first digit
            i = counter
            SecondNumber = ""

            # If the current character is a comma, then we are looking for the second number
            if (input[i] == ','):
                counter = i + 1
                while input[counter].isdigit():
                    SecondNumber += input[counter]
                    counter += 1

            i = counter
            if (input[i] == ')'):
                print(f"First number: {firstNumber}")
                print(f"Second number: {SecondNumber}")
                sum += int(firstNumber) * int(SecondNumber)

    print(sum)