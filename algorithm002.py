# 冒泡排序
'''
def sortBubble(arr):
    for i in range(1,len(arr)):
        label = True
        for j in range(0,len(arr)-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                label = False
        if label:
            print(arr)
            return
    print(arr)
sortBubble([13,4,29,17,5,1])
'''
