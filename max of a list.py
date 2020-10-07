list =[]

num = int(input("enter no.of elements:"))

for i in range(1, num+1):

  elements=int(input("enter elements:"))

  list.append(elements)

  

print("largest element is:", max(list))

