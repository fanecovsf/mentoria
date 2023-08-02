class Triangle:
    def __init__(self, aSide, bSide, cSide):
        self.aSide = aSide
        self.bSide = bSide
        self.cSide = cSide

    def area(self):
        p = (self.aSide + self.bSide + self.cSide) / 2

        area = (p*(p-self.aSide)*(p-self.bSide)*(p-self.cSide))**(1/2)

        return area