import math


class Vector:
    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z

    def magnitude(self):
        return math.sqrt(math.pow(self.X, 2) + math.pow(self.Y, 2) + math.pow(self.Z, 2))

    def normalize(self):
        mag = self.magnitude()
        return Vector(self.X / mag, self.Y / mag, self.Z / mag)

    @staticmethod
    def crossproduct(va, vb):
        return Vector(
            va.Y * vb.Z - va.Z * vb.Y,
            va.Z * vb.X - va.X * vb.Z,
            va.X * vb.Y - va.Y * vb.X)

    @staticmethod
    def dotproduct(va, vb):
        return (va.X * vb.X) + (va.Y * vb.Y) + (va.Z * vb.Z)
