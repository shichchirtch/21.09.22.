class IteratorAttrs:

    def __iter__(self):
        for k in self.__dict__.items():
            yield k

class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model, self.size, self.memory = model, size, memory


phone = SmartPhone("Samsung", (10, 5), 512)
for attr, value in phone:
    print(attr, value)
