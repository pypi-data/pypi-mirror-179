class A:

    def funA(self):
        print("A")

    def funB(self):
        self.funA()


class B(A):

    def funA(self):
        print("B")


elemA = A()

elemB = B()

elemA.funB()
elemB.funB()