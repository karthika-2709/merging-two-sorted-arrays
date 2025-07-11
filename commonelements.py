def commonElements(self, arr1, arr2, arr3):
    arr=arr1+arr2+arr3
    d={}
    n=len(arr)
    for i in arr:
        if i in d:
          d[i]=d[i]+1
        else:
          d[i]=1
    res=[]
    for key in d:
        if(d[key]>=2):
          res.append(key)
    res.sort()
    return res if res else [-1]
