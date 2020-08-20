# Quiz_02
def factorsFilter(inputInt):

    outputInt = 0

    for i in range(1, inputInt + 1):
        constraint = (i % 3 != 0 and i % 5 != 0) or i % 15 == 0
        if constraint:
            outputInt += 1

    return outputInt


# result
testInt = 15
print(f'QUIZ_02.: {testInt} >> {factorsFilter(testInt)}')
   
