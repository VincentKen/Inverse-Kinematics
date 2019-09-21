import math
from vector import Vector


class ArmSegment:
    def __init__(self, angle=0, length=0, id=1, previous=None, x=0, y=0):
        self.__x = x
        self.__y = y
        self.__z = 0
        self.__angle = math.radians(angle)
        self.__length = length
        self.__previous = previous
        self.__next = None
        self.__id = id
        self.__maxangle = 2

        if self.__previous is not None:
            self.__previous.setNext(self)

    def getX(self):
        if self.__previous is None:
            return self.__length * math.cos(self.__angle)
        return self.__previous.getX() + self.__length * math.cos(self.__angle + self.__previous.getAngle())

    def getY(self):
        if self.__previous is None:
            return self.__length * math.sin(self.__angle)
        return self.__previous.getY() + (self.__length * math.sin(self.__angle + self.__previous.getAngle()))

    def getZ(self):
        return self.__z

    def getAngle(self):
        if self.__previous is None:
            return self.__angle
        return self.__angle + self.__previous.getAngle()

    def setMaxAngle(self, max):
        self.__maxangle = math.radians(max)
        print(self.__maxangle)

    def rotate(self, angle):
        self.__angle += angle
        if self.__angle > self.__maxangle:
            self.__angle = self.__maxangle
        if self.__angle < -1 * self.__maxangle:
            self.__angle = - 1 * self.__maxangle

    def getPos(self):
        return self.getX(), self.getY(), self.getZ()

    def setNext(self, next):
        self.__next = next

    def getEndSegment(self):
        if self.__next is None:
            return self
        return self.__next.getEndSegment()

    def getID(self):
        return self.__id

    def calcvectors(self, d):
        pos = self.getPos()
        endpos = self.getEndSegment().getPos()
        # first vector is vector from current position to position of end point
        # second is from current position to the destination position
        v1 = Vector(endpos[0] - pos[0], endpos[1] - pos[1], endpos[2] - pos[2])
        v2 = Vector(d[0] - pos[0], d[1] - pos[1], d[2] - pos[2])
        return v1, v2

    def moveto(self, p):
        vectors = self.calcvectors(p)
        normalized1 = vectors[0].normalize()  # normalized vector to end point
        normalized2 = vectors[1].normalize()  # normalized vector to destination
        dot = Vector.dotproduct(normalized1, normalized2)
        cross = Vector.crossproduct(normalized1, normalized2)

        if dot < 0:
            dot *= -1

        deg = math.acos(dot) / normalized1.magnitude() * normalized2.magnitude()

        if cross.Z < 0:
            deg = deg * -1
            # counter clockwise

        self.__next.rotate(deg)
