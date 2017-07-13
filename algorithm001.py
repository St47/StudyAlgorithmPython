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
'''
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
'''
# 7、狄克斯特拉算法
'''
graph = {}
graph["start"] = {}
graph["start"]["A"] = 4
graph["start"]["B"] = 10
# print(graph["start"].keys())
graph["A"] = {}
graph["A"]["C"] = 21
graph["B"] = {}
graph["B"]["D"] = 5
graph["B"]["E"] = 8
graph["C"] = {}
graph["C"]["Fin"] = 4
graph["E"] = {}
graph["E"]["C"] = 12
graph["D"] = {}
graph["D"]["C"] = 5
# print(graph)
graph["Fin"] = {}
infinity = float("inf")
# 存储各节点开销
costs = {}
costs["A"] = 4
costs["B"] = 10
costs["C"] = infinity
costs["D"] = infinity
costs["E"] = infinity
costs["Fin"] = infinity
# 存储各节点的父节点
parents = {}
parents["A"] = "Start"
parents["B"] = "Start"
parents["C"] = None
parents["D"] = None
parents["E"] = None
parents["Fin"] = None
'''
#  练习
# infinity = float("inf")
'''
def Dijkstra_algorithm(graph,parents,costs):
    # 记录处理过的节点
    processed = []
    def find_lowest_cost_node(costs):
        lowest_cost = infinity
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:  # is not in不对
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for node_temp in neighbors:
            if cost + neighbors[node_temp] < costs[node_temp]:
                costs[node_temp] = cost + neighbors[node_temp]
                parents[node_temp] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    print("最短距离是:" + str(costs["Fin"]))
    temp = parents["Fin"]
    str2 = " Fin"
    while temp is not "Start":
        str2 = " " + temp + str2
        temp = parents[temp]
    print("最短路径是:Start" + str2)
'''
# 第一题z
'''
graph = {}
graph["Start"] = {}
graph["Start"]["A"] = 5
graph["Start"]["B"] = 2
graph["A"] = {}
graph["A"]["C"] = 4
graph["A"]["D"] = 2
graph["B"] = {}
graph["B"]["A"] = 8
graph["B"]["D"] = 7
graph["C"] = {}
graph["C"]["D"] = 6
graph["C"]["Fin"] = 3
graph["D"] = {}
graph["D"]["Fin"] = 1
graph["Fin"] = {}

costs = {}
costs["A"] = 5
costs["B"] = 2
costs["C"] = infinity
costs["D"] = infinity
costs["Fin"] = infinity

parents = {}
parents["A"] = "Start"
parents["B"] = "Start"
parents["C"] = None
parents["D"] = None
parents["Fin"] = None
findShortestPath(graph,parents,costs)
'''
# 第二题
'''
graph = {}
graph["Start"] = {}
graph["Start"]["A"] = 10
graph["A"] = {}
graph["A"]["B"] = 20
graph["B"] = {}
graph["B"]["Fin"] = 30
graph["B"]["C"] = 1
graph["C"] = {}
graph["C"]["A"] = 1
graph["Fin"] = {}

costs = {}
costs["A"] = 10
costs["B"] = infinity
costs["C"] = infinity
costs["Fin"] = infinity

parents = {}
parents["A"] = "Start"
parents["B"] = None
parents["C"] = None
parents["Fin"] = None
findShortestPath(graph,parents,costs)
'''
# 8、贪婪算法
'''
people = [1,2,2,4]     # 数组
print(people)
people2 = set([1,2,2,4])        # 集合：不出现重复的,输入数组转化为集合
print(people2)
arr1 = [1,1,2,2,2,3,4,4]
print(arr1)
set1 = set(arr1)
print(set1)
list = {}
list["one"] = set([1,2,3])
for a,b in list.items():
    print (a)
    print(b)
'''
'''
# 广播电台的选择
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
# 需要覆盖的州
state_needed = set()
for a,b in stations.items():
    state_needed = state_needed | b
# 确定使用的电台
stations_final = set()
# 遍历所有的电台
while state_needed:
    station_selected = None
    station_covered = set()
    for a,b in stations.items():
        covered_temp = b & state_needed
        if len(covered_temp) > len(station_covered):
            station_covered = covered_temp
            station_selected = a
    stations_final.add(station_selected)
    state_needed -= station_covered
print(stations_final)
'''
# 自己写个旅行商问题的近似算法
'''
graph = {}
graph["A"] = {}
graph["A"]["B"] = 5
graph["A"]["C"] = 8
graph["A"]["D"] = 12
graph["B"] = {}
graph["B"]["A"] = 5
graph["B"]["C"] = 10
graph["B"]["D"] = 9
graph["C"] = {}
graph["C"]["A"] = 8
graph["C"]["B"] = 10
graph["C"]["D"] = 4
graph["D"] = {}
graph["D"]["A"] = 12
graph["D"]["B"] = 9
graph["D"]["C"] = 4
city_now = "A"
city_remained = ["B","C","D"]
print(city_now)
while city_remained:
    dis = float("inf")
    city_next = None
    for c in city_remained:
        if graph[city_now][c] < dis:
            city_next = c
            dis = graph[city_now][c]
    print(city_next)
    city_now = city_next
    city_remained.remove(city_next)
'''
# 9、动态规划
'''
graph = {}
graph["water"] = [3,10]
graph["book"] = [1,3]
graph["food"] = [2,9]
graph["jacket"] = [2,5]
graph["camera"] = [1,6]
i=0
cells_final = []
values_final = []
for item in graph.keys():
    cells_row = []
    values_row = []
    for j in range(1,7):
        #如果是第一行，先初始化
        if i == 0:
            if graph[item][0] > j:
                value_temp = 0
                cell_temp = set()
            if graph[item][0] <= j:
                value_temp = graph[item][1]
                cell_temp = set([item])
            cells_row.append(cell_temp)
            values_row.append(value_temp)
        #接下来的动态规划
        else:
            if graph[item][0] > j:
                value_temp = values_final[i-1][j-1]
                cell_temp = cells_final[i-1][j-1]
            if graph[item][0] == j:
                if graph[item][1] > values_final[i-1][j-1]:
                    value_temp = graph[item][1]
                    cell_temp = set([item])
                else:
                    value_temp = values_final[i - 1][j - 1]
                    cell_temp = cells_final[i - 1][j - 1]
            if graph[item][0] < j:
                if values_final[i-1][j-1] >=  graph[item][1]+values_final[i-1][j-1-graph[item][0]]:
                    value_temp = values_final[i - 1][j - 1]
                    cell_temp = cells_final[i - 1][j - 1]
                else:
                    value_temp = graph[item][1]+values_final[i-1][j-1-graph[item][0]]
                    cell_temp = cells_final[i - 1][j-1-graph[item][0]] | set([item])
            cells_row.append(cell_temp)
            values_row.append(value_temp)
    cells_final.append(cells_row)
    values_final.append(values_row)
    i += 1
print(values_final[4])
'''
# 最大公共子串、最大公共子序列
'''
def maxSubString(word_a,word_b):
    len_a = len(word_a)
    len_b = len(word_b)
    cell_final = []
    for i in range(0,len_a):
        cell_row = []
        for j in range(0,len_b):
            if i == 0:
                if word_a[i] == word_b[j]:
                    cell_row.append(1)
                else:
                    cell_row.append(0)
            else:
                if word_a[i] == word_b[j]:
                    cell_row.append(1+cell_final[i-1][j-1])
                else:
                    cell_row.append(0)
        cell_final.append(cell_row)
    print(cell_final[len_a-1][len_b-1])
def maxSubSequence(word_a,word_b):
    len_a = len(word_a)
    len_b = len(word_b)
    cell_final = []
    for i in range(0, len_a):
        cell_row = []
        for j in range(0, len_b):
            if i == 0:
                if word_a[i] == word_b[j]:
                    cell_row.append(1)
                else:
                    if j == 0:
                        cell_row.append(0)
                    else:
                        cell_row.append(cell_row[j-1])
            else:
                if word_a[i] == word_b[j]:
                    cell_row.append(1 + cell_final[i - 1][j - 1])
                else:
                    if j == 0:
                        cell_row.append(cell_final[i-1][j])
                    else:
                        cell_row.append(max(cell_final[i-1][j],cell_row[j-1]))
        cell_final.append(cell_row)
    print(cell_final[len_a - 1][len_b - 1])
    print(cell_final)
maxSubSequence("fosh","fish")
'''
'''
# 练习几个技巧
arr = [12,13,14,15]
print(arr[0] if arr[0] > arr[1] else arr[1])
arr1 = [i for i in arr if i > 13]
print(arr1)
arr2 = ["w",123]
print(arr+arr2)
'''
# 10、MapReduce
'''
from functools import reduce
arr1 = [1,2,3,4,5]
arr2 = map(lambda x: x*x, arr1)   # lambda快速定义函数
print(list(arr2))    # 返回的是map对象，要转换为list
red = reduce(lambda x,y:x+y,arr1)
print(red)
'''
# 线性规划（选票问题）
'''
max_votes = 0
x_final = 0
y_final = 0
for x in range(500,751):
    for y in range(300,801):
        if x + 1.5*y <= 1200:
            if 2*x + y <= 1500:
                max_votes = x + y if x + y >= max_votes else max_votes
                x_final = x if x + y >= max_votes else x_final
                y_final = y if x + y >= max_votes else y_final
print(x_final)
print(y_final)
print(max_votes)
'''
# 线性规划（生产利润最大化）
max_profit = 0
x_final = 0
y_final = 0
for x in range(1,5):
    for y in range(1,5):
        if x + 2*y <= 11:
            if 5*x + 2*y <= 20:
                max_profit = 2*x + 3*y if 2*x + 3*y >= max_profit else max_profit
                x_final = x if 2*x + 3*y >= max_profit else x_final
                y_final = y if 2*x + 3*y >= max_profit else y_final
print(x_final)
print(y_final)
print(max_profit)







