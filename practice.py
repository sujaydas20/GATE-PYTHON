arr=[1,2,3,4,5]
n=len(arr)
total=0
for i in range(n):
   total +=arr[i]+arr[n-1-i]
print(total)