#Validate subsequence
arr = [5,1,22,25,6,-1,8,10]
subarr= [1,6,-1,10]

def fun(arr,subarr):
  i=0#initialization for arr index
  j=0#initialization for subarr index
  while i<len(arr) and j<len(subarr):
    if arr[i]==subarr[j]:
      j+=1
    i+=1
  if j == len(subarr): #index of subarr will increase if there is  matching element exist in arr if no matching element exist then j will not  increment and j != len(subarr).
    return True
  else:
    return False

print(fun(arr,subarr))


  
  
  
  