def merge(arr,low,high):
  if(low>=high):
    return
  mid=(low+high)//2
  merge(arr,low,mid)
  merge(arr,mid+1,high)
  sort(arr,low,mid,high)
def sort(arr,low,mid,high):
  i=low
  j=mid+1
  k=[]
  while(i<=mid and j<=high):
    if(arr[i]<=arr[j]):
      k.append[i]
      i+=1
    else:
      k.append[j]
      j+=1
  while(i<=mid):
    k.append[i]
    i+=1
  while(j<=high):
    k.append[j]
    j+=1
  for ind,val in enumerate:
    arr[low+ind]=val
arr=list(map(int,input().split())
merge(arr,0,len(arr)-1)
print(arr)
