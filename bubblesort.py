def bubblesort(self,arr):
  for i in range(len(arr)-1,-1,-1):
    for j in range(0,i):
      if(arr[j]>arr[j+1]):
        arr[j],arr[j+1]=arr[j+1],arr[j]
  return arr
