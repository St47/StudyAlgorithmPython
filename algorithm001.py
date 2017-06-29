#coding:UTF-8
# 1、算法简介
'''
# binary search
def binary_search(arr,target):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid=(low+high)/2
        guess=arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

list=[1,3,5,7,9]
print binary_search(list,5)
print binary_search(list,4)
'''
# 2、选择排序
'''
def findSmallest(arr):
    smallest_num=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i] < smallest_num:
            smallest_num = arr[i]
            smallest_index = i
    return smallest_index

def sortArray(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index)) # 这个确实不错，简洁！
    return newArr

print sortArray([5,3,6,2,10])
'''
# 3、递归
'''
def countDown(i):
    if i < 0:
        return
    else:
        print i
        countDown(i-1)
countDown(10)
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total
print sum([1,5,8,2,4])
'''
# 4、分而治之和快速排序
'''
def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0]+sum(arr[1:])
arr = [2,4,7,3,9,5]
print sum(arr)

def count(list):
    if list == []:
        return 0
    else:
        return 1+count(list[1:])
print count([1,2,3,4,5,7,8,9])

def findMax(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    else:
        subMax = findMax(list[1:])
        return list[0] if list[0] > subMax else subMax
print findMax([1,2,4,8,4,3])
          快速排序
def quickSort(list):
    if len(list) < 2:
        return list
    else:
        j = list[0]
        less = []
        for i in list[1:]:
            if i <= j:
                less.append(i)
        greater = [i for i in list[1:] if i>j]   # 巧妙！4行化为1行
        return  quickSort(less)+[j]+quickSort(greater)
print quickSort([1,4,78,3,547,323,55,44,23986])

from time import sleep
sleep(1)
'''
# 5、散列表
'''
book = dict()
book["apple"]=1.00
book["milk"] = 2.00
book["avocado"] = 3.00
print(book)
print(book["milk"])
'''
# 5.2 应用案例
'''
phone_book = {}
phone_book["sun"] = 13162118603
phone_book["emergency"] = 110
print(phone_book["sun"])
value = phone_book.get("emergency1")
print(value)

voted = {}
def check_voter(name):
    if voted.get(name):
        print("投过了")
    else:
        voted[name] = True
        print("请投票")
check_voter("tom")
check_voter("milk")
check_voter("tom")
'''
# 6、广度优先搜索
def isSB(name):
    return name[-1] == '哥'
graph = {}                              #大括号用来创建字典
searched = []                         # 中括号用来创建数字，避免重复查找、循环
graph["我"] = ["李思鸣","华秋鸣","宋佳祺"]
graph["李思鸣"] = ["斌哥","我"]
graph["华秋鸣"] = ["斌哥"]
graph["宋佳祺"] = ["汤泽凡"]
graph["汤泽凡"] = []
graph["斌哥"] = []
from collections import deque
search_queue = deque()                      # 创建队列
search_queue += graph["我"]
while search_queue:
    person = search_queue.popleft()
    if person not in searched:
        searched.append(person)
        if isSB(person):
            print(person+"是个SB")
        else:
            search_queue += graph[person]












