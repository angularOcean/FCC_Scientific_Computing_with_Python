#"Arithmetic Formatter Project" by HL
import re

def arithmetic_arranger(problem, varX = False):
    '''This function takes a math problem
    Parameters: a list of strings that are math problem, optionally a true/false boolean
    Returns: a string representation of the math problem now vertically arranged as well as side by side,
     if the second argument is set to true, the answer to the problems is also calculated and displayed'''
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
    for integer in problem:
        isplit = re.split(' ', integer)

        if len(isplit[0]) > 4 or len(isplit[2]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return "Error: Numbers cannot be more than four digits."
        elif re.search('[+-]',isplit[1]) is None:
            print("Error: Operator must be '+' or '-'.")
            return "Error: Operator must be '+' or '-'."

        linedash = ''
        spaceone = ''

        if int(len(isplit[0])) < int(len(isplit[2])):
            for integer in range(int(len(isplit[2]))-int(len(isplit[0]))):
                spaceone = spaceone + ' '
            isplit[0] = spaceone + '  ' + isplit[0]

        elif int(len(isplit[0])) == int(len(isplit[2])):
            isplit[0] = '  ' + isplit[0]

        elif int(len(isplit[0])) > int(len(isplit[2])):
            for integer in range(int(len(isplit[0]))-int(len(isplit[2]))):
                spaceone = spaceone + ' '
            isplit[0] = '  ' + isplit[0]
            isplit[2] = spaceone + isplit[2]

        for integer in range(int(len(isplit[2])+2)):
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

        if varX is True:
            output = None

            if isplit[1] == '+':
                output = isplit[0] + isplit[2]

            if isplit[1] == '-':
                output = isplit[0] - isplit[2]

            output = str(output)
            spacetwo = ''
            if int(len(output)) < int(len(linedash)):
                for integer in range(int(len(linedash))- int(len(output))):
                    spacetwo = spacetwo + ' '
                output = spacetwo + output
            linefour.append(output)
            linefour.append('  ')
    lineone.pop()
    linetwo.pop()
    linethree.pop()
    if varX is True:
        linefour.pop()
        formatter = (' ').join(lineone) + '\n' + (' ').join(linetwo) + '\n' + (' ').join(linethree) + '\n' + (' ').join(linefour)
    else:
        formatter = (' ').join(lineone) + '\n' + (' ').join(linetwo) + '\n' + (' ').join(linethree)

    return formatter

