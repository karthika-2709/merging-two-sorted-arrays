# merging-two-sorted-arrays
def merge(nums1,nums2)):
  i=0
  j=0
  arr=[]
  while(i<=nums1 and j<=nums2):
    if(nums[i]==nums[j]):
      arr.append(nums[i])
      i+=1
    if(nums[i]<nums[j]):
      arr.append(nums[i])
      i+=1
    else:
      arr.append(nums[j])
      j+=1
nums1=list(map(int,input().split())
nums2=list(map(int,input().split())
print(merge(nums1,nums2))
