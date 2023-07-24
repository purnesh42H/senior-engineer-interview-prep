import unittest

'''
Square Terminal is a credit card terminal for payments. The company is looking to create a new version of the Square Terminal. During the screen selection process, you are asked to print a testing pattern on the screens on the Square Terminal.

For simplicity's sake, you are told that the requirements of this screen is a NxN pixel square (no pun intended), 8 bit depth and only supports grayscale (0,255).  

In order to test the quality and functionality of the screen, you must create a black and white vertical stripe pattern with each stripe being M wide. The first stripe will be black.  


1) Given a pattern of size N and a stripe width of M, generate the black and white stripe pattern. 

Sample Test Cases (format: size N, width M):
Test1 Input: 2,1
Test1 Output:
0 255
0 255

Test2 Input:  4, 2
Test2 Output:
0 0 255 255
0 0 255 255
0 0 255 255
0 0 255 255

Test3 Input: 7, 1
Test3 Output:
0 255 0 255 0 255 0
0 255 0 255 0 255 0
0 255 0 255 0 255 0
0 255 0 255 0 255 0
0 255 0 255 0 255 0
0 255 0 255 0 255 0
0 255 0 255 0 255 0
'''

'''
N = 4, M = 2
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
'''

class SquarePattern(object):

    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.color_map = {"black": 0, "white": 255}
        self.square = [[0 for j in range(N)] for i in range(N)]

    def print_square(self):
        if not self.square:
            return self.square
        
        stripe = "black"

        for i in range(self.N):
            for j in range(0, self.N, self.M):
                self._fill_stripe(i, j, stripe)
                stripe = self._get_next_stripe(stripe)

        return self.square

    def _get_next_stripe(self, stripe):
        if stripe == "black":
            return "white" # white
        else:
            return "black"

    def _fill_stripe(self, row, col, stripe):
        for i in range(self.M):
            self.square[row][col] = self.color_map[stripe]
            col += 1

class SquarePatternTest(unittest.TestCase):

    def test_print_square(self):
        square_pattern = SquarePattern(4, 2)
        exp_pattern = [[0, 0, 255, 255], [0, 0, 255, 255], [0, 0, 255, 255], [0, 0, 255, 255]]
        self.assertListEqual(exp_pattern, square_pattern.print_square())

        square_pattern = SquarePattern(2, 1)
        exp_pattern = [[0, 255], [0, 255]]
        self.assertListEqual(exp_pattern, square_pattern.print_square())


if __name__ == "__main__":
    unittest.main()
