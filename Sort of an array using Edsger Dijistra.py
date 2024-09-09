def sort(arr):
    low,mid,high = 0,0,len(arr)-1

    while mid <= high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low +=1
            mid+=1
        elif arr[mid] ==1:
            mid+=1
        else:
            arr[high],arr[mid]=arr[mid],arr[high]
            high -=1
print("test case 1",end ="")
arr1=[0,1,2,1,0,2,1,0]
sort(arr1)
print(arr1)
print("test case 2",end ="")
arr2=[2,2,2,2]
sort(arr2)
print(arr2)
print("test case 3",end ="")
arr3=[1,1,1,1]
sort(arr3)
print(arr3)
print("test case 4",end ="")
arr4=[0,0,0,0]
sort(arr4)
print(arr4)
print("test case 5",end ="")
arr5=[2,0,1]
sort(arr5)
print(arr5)
print("test case 6",end ="")
arr6=[]
sort(arr6)
print(arr6)
