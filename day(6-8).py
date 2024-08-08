a=([1,2,3],
   [4,5,6],
   [7,8,9])
for row in a:
    for element in row:
        print(element, end=' ')
    print()


#matrix mul
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j]=matrix1[i][j]*matrix2[i][j]
for row in result:
    print(row)

d=int(input("Enter a decimal number: "))
b=bin(d)[2:]
o=oct(d)[2:]
print("Binary equivalent: ",b)
print("Octal equivalent: ",o)
