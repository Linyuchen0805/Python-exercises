#Method1

import random
init_list = [1,3,4,5,7,9,10,14,16,17,36,57,89]
guessnumber = int(input("please say a number"))

def binarysearch(list,number):
    #未进入递归或递归停止的条件：
    if len(list) == 1:
        if list[0] == number:
            return True
        else:
            return False
    elif len(list) == 0:
        return False
    
    #开始并继续递归：
    else:
        #按照列表长度将列表分为两类
        #第一种，列表长度为奇数
        if len(list)%2 != 0:   
            middle = int((len(list)-1)/2)
            if number < list[middle]:   #如果小于列表中心值，取左半个列表，递归
                list = [ list[i] for i in range(0,middle) ]
                return binarysearch(list,number)
            elif number > list[middle]: #如果大于列表中心值，取右半个列表，递归
                list = [ list[i] for i in range(middle,len(list))]
                return binarysearch(list,number)
            else:                       #等于中间值，搜索完成，返回True
                return True
        #第二种，列表长度为偶数
        elif len(list)%2 == 0:  
            a=int((len(list)/2)-1)
            b=int(len(list)/2)
            if number < list[a]:       #如果小于列表左中心值，取左半个列表，递归
                list = [ list[i] for i in range(0,a)]
                return binarysearch(list,number)
            elif number > list[b]:     #如果大于列表右中心值，取右半个列表，递归
                list = [ list[i] for i in range(b,len(list))]
                return binarysearch(list,number)
            elif number == list[a] or number == list[b]:   #等于中心值，返回Truue
                return True
            else:                      #处于中心值中间，返回False
                return False

print(binarysearch(init_list,guessnumber))


# Method 2

def find(ordered_list, element_to_find):
  start_index = 1
  end_index = len(ordered_list) - 1
  
  while True:
    middle_index = (end_index - start_index) / 2
    
    if middle_index < start_index or middle_index > end_index or middle_index < 0:
      return False
    
    middle_element = ordered_list[middle_index]
    if middle_element == element_to_find:
      return True
    elif middle_element < element_to_find:
      end_index = middle_index
    else:
      start_index = middle_index