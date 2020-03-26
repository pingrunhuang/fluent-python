class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def pong(self):
        print('pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):

    def ping(self):
        '''
        In Python 2, the first line of D.pingpong would be written as super(D, self).ping() instead of su per().ping().
        '''
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping() # call the B cause it comes first
        self.pong()
        super().pong()
        C.pong(self)


if __name__ == "__main__":
    '''__mro__: method resolution order'''
    d = D()
    d.ping()
    