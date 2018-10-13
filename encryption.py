import math
import random


def main():
    """
    """
    array = ['7', 'A', '3', 'F']
    c = Cube(array=array)


class Cube():
    def __init__(self, *args, **kwargs):
        """
        """
        self.cube = []
        cube_dem = int(len(kwargs['array']) ** (1 / 3)) + 1
        x = 0
        for i in range(0, cube_dem):
            self.cube.append([])
            for j in range(0, cube_dem):
                self.cube[i].append([])
                for k in range(0, cube_dem):
                    try:
                        self.cube[i][j].append(kwargs['array'][x])
                    except IndexError:
                        self.cube[i][j].append(chr(int(
                            random.uniform(71, 90))))
                    x += 1
        print('Cube created with a side length of ' + str(cube_dem))
        print(self.cube)


if __name__ == '__main__':
    main()
