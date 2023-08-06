


from subprocess import list2cmdline


def bubble_sort(list):
    for i in range(len(list)):
        for j in range (len(list)-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list

def selection_sort(list): 
    length = len(list)  
    for i in range(length-1):  
        minIndex = i  
        for j in range(i+1, length):  
            if list[j]<list[minIndex]:  
                minIndex = j            
        list[i], list[minIndex] = list[minIndex], list[i]  
    return list

def remove_duplicates(list):
    chk=[]
    for i in range(len(list)-1):
        if a[i] not in chk:
            chk.append(a[i])
    return chk 

def list_intersection(list1,list2):
    int=[]
    for ele in list1:
        if ele in list2 and ele not in int:
            int.append(ele)
    return int

def list_union(list1,list2):
    uni=list1+list2
    remove_duplicates(uni)
    return uni

a=[1,2,3,4,5,6,7]
b=[4,5,6,7,8,9,10]
print(list_union(a,b))