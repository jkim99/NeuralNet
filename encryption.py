import random as r


def main():
    """
    """
    array = ['1', '2', '3', '4', '5', '6', '7', '9', 'A']
    c = Cube(array=array)
    print(c.cube)


class Cube():
    def __init__(self, *args, **kwargs):
        """
        """
        self.cube = []
        self.cube_dem = int(len(kwargs['array']) ** (1 / 3)) + 1
        x = 0
        for i in range(0, self.cube_dem):
            self.cube.append([])
            for j in range(0, self.cube_dem):
                self.cube[i].append([])
                for k in range(0, self.cube_dem):
                    try:
                        self.cube[i][j].append(kwargs['array'][x])
                    except IndexError:
                        self.cube[i][j].append(chr(int(r.uniform(71, 90))))
                    x += 1
        # print('Cube created with a side length of ' + str(self.cube_dem))
        # print(self.cube)

    def copy(self):
        array = []
        for i in range(0, self.cube_dem):
            for j in range(0, self.cube_dem):
                for k in range(0, self.cube_dem):
                    array.append(self.cube[i][j][k])
        return Cube(array=array)

    def read_file(self, file):
        """
        jeff...u had one job!
        """

    def turn_f_side(self, layer, rotations):
        """
        turns front side of cube (going backwards)
        """
        copy_cube = self.copy()
        for j in range(0, self.cube_dem):
            for k in range(0, self.cube_dem):
                self.cube[layer - 1][j][self.cube_dem - k - 1] = \
                    copy_cube.cube[layer - 1][k][j]

    def turn_u_side(self, layer, rotations):
        """
        turns top side of cube (going down)
        """
        copy_cube = self.copy()
        for j in range(0, self.cube_dem):
            for k in range(0, self.cube_dem):
                self.cube[j][layer - 1][self.cube_dem - k - 1] = \
                    copy_cube.cube[k][layer - 1][j]

    def turn_l_side(self, layer, rotations):
        """
        turns left side of cube (going right)
        """
        copy_cube = self.copy()
        for j in range(0, self.cube_dem):
            for k in range(0, self.cube_dem):
                self.cube[j][self.cube_dem - k - 1][layer - 1] = \
                    copy_cube.cube[k][j][layer - 1]


if __name__ == '__main__':
    main()
