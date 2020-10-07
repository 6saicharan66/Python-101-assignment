#python 3.7.1

list =[]
num = int(input("enter no.of elements:"))
for i in range(1, num+1):
  elements=int(input("enter elements:"))
  list.append(elements)
  
list.sort()
  
print("largest element is:", sorted(list)[-2])