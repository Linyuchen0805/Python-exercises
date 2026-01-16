def new(x):
    set = {i for i in x}
    return [i for i in set]
print(new([1,3,3,2,4,6,5,7,8,9,9,0,45,78]))
#移除列表中重复的元素可以用集合
#集合用{}表示，里面没有重复的元素
#集合无序，不能索引

#Two functions
import random
def list():
    return [random.randint(1,100) for i in range(10)]

def new ():
    set = {i for i in list()}
    return [i for i in set]
print(new())
        