# Write a Python function called max_num()to find the Max of three numbers.

def max_num(a,b,c):
  return max([a,b,c])

print(max_num(1,2,3))
print(max_num(100,50,1))
print(max_num(15,30,2))



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