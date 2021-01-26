print("Probability Calculator App")
import copy
import random
#take multiple arguments using keyward arguments **kwargs vs *args
class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k in kwargs.keys():
            for i in range(kwargs.get(k)):
                self.contents.append(k)
    def draw(self, number):
        draw =[]
        takenout = []
        for i in range(number):
            if len(self.contents) == 0:
                self.contents.extend(takenout)
                takenout = []
            instance = self.contents.pop(random.randrange(0,len(self.contents)))
            draw.append(instance)
            takenout.append(instance)
        return draw


def experiment(hat, expected_balls, num_balls_drawn , num_experiments ):
    num_matches = 0
    expected_list =[]
    for k in expected_balls.keys():
        for i in range(expected_balls.get(k)):
            expected_list.append(k)
    print('expected', expected_list)
    for i in range(num_experiments):
        hatcopy = copy.deepcopy(hat)
        draw = hatcopy.draw(num_balls_drawn)
        counter = 0
        for i in range(len(expected_list)):
            if expected_list[i] in draw:
                draw.remove(expected_list[i])
                counter = counter + 1
            else:
                break
            if counter == len(expected_list):
                num_matches = num_matches + 1
        hatcopy = None
    print(num_matches,num_experiments,num_matches/num_experiments)
    return num_matches/num_experiments

hat = Hat(blue=4, red=2, green=6)
#print('contents', hat.contents)
#print('taken out', hat.takenout)
print('draw', hat.draw(2))
print('draw', hat.draw(4))
print('draw', hat.draw(20))
#hat = Hat(black=6, red=4, green=3)
#probability = experiment(hat=hat,
#                  expected_balls={"red":2,"green":1},
#                  num_balls_drawn=5,
#                  num_experiments=2000)
#hat2 = Hat(blue=3,red=2,green=6)
#probability2 = experiment(hat=hat2, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
#hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
#probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
