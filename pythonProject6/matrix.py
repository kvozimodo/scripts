import numpy


class Matrix():


    def __init__(self, M, N, body):
        self.M = M
        self.N = N
        self.body=numpy.array(body).reshape(M, N)
        print(self.body)

    def is_identity(self):
        flag = True
        for i in range(self.N):
            for j in range(self.M):
                if self.body[self.N-1][self.M-1] != 1:
                    flag = False
        return flag


    def is_square(self):
        flag = True
        if self.M != self.N:
            flag = False
        return flag


    def is_zero(self):
        flag = True
        for i in range(self.N):
            for j in range(self.M):
                if self.body[self.N-1][self.M-1] != 0:
                    flag = False
        return flag

    def is_diagonal(self):
        return numpy.count_nonzero(self.body- numpy.diag(numpy.diagonal(self.body)))

    def transpose(self):
        self.body.transpose()

    @staticmethod
    def sum(a,b):
        c = a.body + b.body
        return c

    @staticmethod
    def mul(a, b):
        c = a.body.dot(b.body)
        return c

    @staticmethod
    def sub(a, b):
        c = a.body-b.body
        return c
a=Matrix(2,2,[20, 30, 40, 50])
b=Matrix(2,2,[20, 30, 40, 50])
print(a.is_zero())
a.transpose()
print(a.body.transpose())
print(Matrix.sum(a,b))
print(Matrix.sub(a,b))