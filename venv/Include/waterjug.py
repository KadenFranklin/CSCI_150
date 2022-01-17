from typing import *
class Waterjug:
    def __init__(self, capacity: int, contents: int):
        self.capacity = capacity
        self.contents = contents

    def __repr__(self):
        return f"Waterjug({self.capacity}, {self.contents})"

    def fill(self):
        x = self.capacity
        self.contents = x

    def empty(self):
        self.contents = 0

    def pour(self, other: 'Waterjug'):
        x = self.contents
        other.contents += x
        self.contents -= x
        if self.contents < 0:
            self.contents = 0
        if other.contents > other.capacity :
            y = other.contents - other.capacity
            self.contents += y
            other.contents = other.capacity

def test():
    check_bool = False
    a = Waterjug(4, 0)
    b = Waterjug(3, 0)

    a.fill()
    if a.contents == 4:
        check_bool = False
    else:
        check_bool = True

    a.pour(b)
    if a.contents == 1 and b.contents == 3:
        check_bool = False
    else:
        check_bool = True

    b.empty()
    if b.contents == 0:
        check_bool = False
    else:
        check_bool = True

    a.pour(b)
    if a.contents == 0 and b.contents == 1:
        check_bool = False
    else:
        check_bool = True

    a.fill()
    if a.contents == 4:
        check_bool = False
    else:
        check_bool = True

    a.pour(b)
    if (a.contents == 2 and a.capacity == 4) \
            and (b.contents == 3 and b.capacity == 3):
        check_bool = False
    else:
        check_bool = True

    if check_bool == False :
        print("All tests passed.")

    if check_bool == True:
        print("Test failed.")

if __name__ == '__main__':
    test()
