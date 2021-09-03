from matrix import Matrix
import numpy

class HorizontalVector (Matrix):

    def __init__(self, M , body):
        self.M = M
        self.body=numpy.array(body).reshape(1, M)
        print(self.body)


b= HorizontalVector(4,[20, 30, 40, 50])