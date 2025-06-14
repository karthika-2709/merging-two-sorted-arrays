# merging-two-sorted-arrays
def merge(nums1,nums2):
  i=0
  j=0
  arr=[]
  while(i<len(nums1) and j<len(nums2)):
    if(nums1[i]==nums2[j]):
      arr.append(nums1[i])
      arr.append(nums2[j])
      i+=1
      j+=1
    elif(nums1[i]<nums2[j]):
      arr.append(nums1[i])
      i+=1
    else:
      arr.append(nums2[j])
      j+=1
  while(i<len(nums1)):
    arr.append(nums1[i])
    i+=1
  while(j<len(nums2)):
    arr.append(nums2[j])
    j+=1
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
print(merge(nums1,nums2))
