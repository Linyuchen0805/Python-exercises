string = input("Say a sentence:")
def reversestring(x):
    return " ".join(x.split(" ")[::-1])
print(reversestring(string))

#string.split("*")可以将一个长字符串按照*分开并返回一个列表，分开后*消失，*可以是字母或者空格
#"*".join(list)可以按照*将列表里的值连在一起并返回一个长字符串，连接后*存在于连接处，*可以是字母或者空格