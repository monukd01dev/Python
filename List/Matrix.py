# matrix = []
# matrix_size = [int(i) for i in input("Enter the size of matrix : ").split()][:2]

# row,col = matrix_size
# for x in range(row):
#         matrix.append([int(item) for item in input(f"Enter the row {x+1} : ").split()][:col])
# print(matrix)

# # step_1
matrix =[]
matrix_size = [int(item) for item in input("Enter the size of Matrix : ").split()[:2]]
row,col = matrix_size

# # step_2
# for i in range(1,row+1):
#     new_row=[]
#     for x in range(1,col+1) : 
#         new_row.append(int(input(f"Enter the value for row({i}),col({x}) : ")))
#     matrix.append(new_row)


# print(matrix)

# taking the matrix value in one line
l = [int(i) for i in input("Enter the matrix : ").split()[:row*col]]
print(l)
for i in range(row):
    begin = i*col
    end =  (i+1)*col
    matrix.append(l[begin:end])
print(matrix)