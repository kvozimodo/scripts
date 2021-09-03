from matrix import Matrix
import numpy

class VerticalVector (Matrix):

    def __init__(self, M , body):
        self.M = M
        self.body=numpy.array(body).reshape(M, 1)
        print(self.body)


b = VerticalVector(4,[20, 30, 40, 50])