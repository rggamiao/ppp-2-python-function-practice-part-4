# Write a Python function called max_num()to find the Max of three numbers.

def max_num(a,b,c):
  return max([a,b,c])

print(max_num(1,2,3))
print(max_num(100,50,1))
print(max_num(15,30,2))

def mult_list(lst):
    if len(lst) == 0: ##These lines check if the length of the input list is zero. .
        return 0
        prod = lst[0]
    if len(lst) > 1: ## If the list has more than one element, these lines start a loop that goes through each element of the list starting from the second element. 
for i in lst[1:]:
      prod = prod * i

  return prod
  print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([15]))



def pascal(n):
    triangle = []  
    for i in range(n):
        row = [1]  
        if i > 0:  
            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)  
        triangle.append(row)
        print(' '.join(map(str, row)))


pascal(1)
print("'''")
print("output:")
print("1")
print("'''")

print()  

pascal(5)
print("'''")
print("output:")
print("1")
print("1 1")
print("1 2 1")
print("1 3 3 1")
print("1 4 6 4 1")
print("'''")