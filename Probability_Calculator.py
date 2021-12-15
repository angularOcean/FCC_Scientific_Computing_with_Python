#"Probability Calculator App" by HL
import copy
import random

#take multiple arguments using keyward arguments **kwargs vs *args
class Hat:
    '''This class represents a hat object which contains balls to be drawn out of as a representation of a combinatorics math problem'''
    def __init__(self, **kwargs):
        '''Initializes the object with a variable number of keywords for a list of colored balls as contents of the hat.
        Keywords must be a dictionary with color of ball as key and number of balls as value'''
        self.contents = []
        for key in kwargs.keys():
            for integer in range(kwargs.get(key)):
                self.contents.append(key)
    def draw(self, number):
        '''Method to draw a specified number of balls out of the hat randomly and return that draw to the user
        Parameters: integer number of balls to draw
        Reeturns: list of balls drawn from hat '''
        draw =[]
        takenout = []
        for integer in range(number):
            if len(self.contents) == 0:
                self.contents.extend(takenout)
                takenout = []
            instance = self.contents.pop(random.randrange(0,len(self.contents)))
            draw.append(instance)
            takenout.append(instance)
        return draw


def experiment(hat, expected_balls, num_balls_drawn , num_experiments ):
    '''This function helps illustrate probability by showing the number of times a specific set of balls is drawn
    from a hat given a specified number of balls to draw and a number of experiments to run
    Parameters: a hat object with contents inside, the expected combination of balls to draw, the number of balls to draw for the experimental set, the number of times to run the random draw
    Returns: A percentage after the specified number of experiments representing how many times the expected set of balls was drawn over the number of experiments representing the approx probabilty  '''
    num_matches = 0
    expected_list =[]
    for keys in expected_balls.keys():
        for integer in range(expected_balls.get(keys)):
            expected_list.append(keys)
    print('expected', expected_list)
    for integer in range(num_experiments):
        hatcopy = copy.deepcopy(hat)
        draw = hatcopy.draw(num_balls_drawn)
        counter = 0
        for integer in range(len(expected_list)):
            if expected_list[integer] in draw:
                draw.remove(expected_list[integer])
                counter = counter + 1
            else:
                break
            if counter == len(expected_list):
                num_matches = num_matches + 1
        hatcopy = None
    print(num_matches,num_experiments,num_matches/num_experiments)
    return num_matches/num_experiments
