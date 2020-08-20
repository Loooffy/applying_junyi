# Quiz_01_A
def reverseStrA(inputStr):

    return inputStr[::-1]


# Quiz_01_B
def reverseStrB(inputStr):

    chars = inputStr.split(' ')
    reverseCharOrder = ' '.join(chars[::-1])
    
    return reverseStrA(reverseCharOrder)


# results
testStrA = 'junyiacademy'
testStrB = 'flipped class room is important'
print('QUIZ_01.A: ' + testStrA + ' >> ' + reverseStrA(testStrA))
print('QUIZ_02.B: ' + testStrB + ' >> ' + reverseStrB(testStrB))
   
