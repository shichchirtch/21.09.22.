class Vec:
    pass
class Tuple(tuple):
    # def __new__(cls, data, *args, **kwargs):
    #     if isinstance(data, (int, float)) or data == None:
    #         arr = [data]
    #         return tuple(arr)
    #     if isinstance(data, tuple):
    #         return tuple(data)
    #     # if not isinstance(data, tuple):
    #     #     return
    #     return super().__new__(cls)

    def __init__(self, obj):
        if len(obj):
            if not isinstance(obj, tuple):
                self.obj = tuple(obj)
            else:
                self.obj= obj
        else:
            self.obj = tuple(obj)

    def __add__(self, other):
        if len(other):
            if not isinstance(other, tuple):
                res = tuple(self)+tuple(other)
                return Tuple(res)
            else:
                res = tuple(self) + other
                return Tuple(res)
        else:
            raise ValueError ("Можно складывать только итерируемые объекты")

f = 1
t = Tuple(f)
print(t)
d = ("hhh")
t = t + d
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
# v = Vec()
# t = t + v
# print(t)
# t = Tuple([1, 2, 3])
# d = "dshaghs"
# t2 = Tuple(d)
# res = t + t2
# print(res)
