print("Arithmetic Formatter Project")
import re
import sys
def arithmetic_arranger(problem, x = False):
    formatter = None
    lineone = []
    linetwo = []
    linethree = []
    linefour = []
    if type(problem) != list:
        problem = [problem]
    if len(problem) > 5:
        print("Error: Too many problems.")
        return "Error: Too many problems."
    for i in problem:
        isplit = re.split(' ', i)

        if len(isplit[0]) > 4 or len(isplit[2]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return "Error: Numbers cannot be more than four digits."
        elif re.search('[+-]',isplit[1]) is None:
            print("Error: Operator must be '+' or '-'.")
            return "Error: Operator must be '+' or '-'."

        linedash = ''
        spaceone = ''

        if int(len(isplit[0])) < int(len(isplit[2])):
            for i in range(int(len(isplit[2]))-int(len(isplit[0]))):
                spaceone = spaceone + ' '
            isplit[0] = spaceone + '  ' + isplit[0]

        elif int(len(isplit[0])) == int(len(isplit[2])):
            isplit[0] = '  ' + isplit[0]

        elif int(len(isplit[0])) > int(len(isplit[2])):
            for i in range(int(len(isplit[0]))-int(len(isplit[2]))):
                spaceone = spaceone + ' '
            isplit[0] = '  ' + isplit[0]
            isplit[2] = spaceone + isplit[2]

        for i in range(int(len(isplit[2])+2)):
            linedash = linedash + '-'

        lineone.append(isplit[0])
        lineone.append('  ')
        linetwo.append(isplit[1] )
        linetwo.append(isplit[2])
        linetwo.append('  ')
        linethree.append(linedash)
        linethree.append('  ')

        try:
            isplit[0] = int(isplit[0])
            isplit[2] = int(isplit[2])
        except:
            print("Error: Numbers must only contain digits.")
            return "Error: Numbers must only contain digits."

        if x is True:
            output = None

            if isplit[1] == '+':
                output = isplit[0] + isplit[2]

            if isplit[1] == '-':
                output = isplit[0] - isplit[2]

            output = str(output)
            spacetwo = ''
            if int(len(output)) < int(len(linedash)):
                for i in range(int(len(linedash))- int(len(output))):
                    spacetwo = spacetwo + ' '
                output = spacetwo + output
            linefour.append(output)
            linefour.append('  ')
    lineone.pop()
    linetwo.pop()
    linethree.pop()
    if x is True:
        linefour.pop()
        formatter = (' ').join(lineone) + '\n' + (' ').join(linetwo) + '\n' + (' ').join(linethree) + '\n' + (' ').join(linefour)
    else:
       formatter = (' ').join(lineone) + '\n' + (' ').join(linetwo) + '\n' + (' ').join(linethree)

    print(formatter)
    return formatter

test1 = (["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
test2 = (["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
test3 = (["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
test4 = (["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
test5 = (["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
test6 = (["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
test7 = (["32 - 698", "1 - 3801", "45 + 43", "123 + 49"])
arithmetic_arranger(test1)
arithmetic_arranger(test2)
arithmetic_arranger(test3)
arithmetic_arranger(test4)
arithmetic_arranger(test5)
arithmetic_arranger(test6)
arithmetic_arranger(test7, True)
