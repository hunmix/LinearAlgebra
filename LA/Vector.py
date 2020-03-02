from ._global import EPSILON
import math

class Vector:
    def __init__(self, list):
        self._values = list

    @classmethod
    def zero(cls, dim):
        # 返回dim维零向量
        return cls([0] * dim)
    
    def norm(self):
        return math.sqrt(sum(e ** 2 for e in self))

    def normalize(self):
        if (self.norm() < EPSILON):
            raise ZeroDivisionError("Normalize error！ norm is zero.")
        return self / self.norm()

    def dot(self, another):
        assert len(self) == len(another), "Length of vectors must be same"
        return sum(a * b for a, b in zip(self, another))

    def __add__(self, another):
        # 加法
        assert len(self) == len(another), "Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, another)])

    def __sub__(self, another):
        # 减法
        assert len(self) == len(another), "Length if vectors must be same"
        return Vector([a - b for a, b in zip(self, another)])

    def __mul__(self, k):
        # 乘法
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        # 右乘
        return self * k

    def __truediv__(self, k):
        # 除
        return (1 / k) * self

    def __iter__(self):
        return self._values.__iter__()

    def __pos__(self):
        # 取正
        return 1 * self

    def __neg__(self):
        # 取负
        return -1 * self

    def __getitem__(self, index):
        # 取向量的第index个元素
        return self._values[index]

    def __len__(self):
        # 返回向量长度
        return len(self._values)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(",".join(str(e) for e in self._values))
