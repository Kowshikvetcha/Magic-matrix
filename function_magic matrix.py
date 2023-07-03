
order= int(input("Enter the order of Matrix: "))
def user_input():
    print("Enter the items of matrix row vice: ")
    matrix = []
    for i in range(order):
        temp = []
        for j in range(order):
            temp.append(int(input()))
        matrix.append(temp)
    return matrix
def magic_matrix():
    diagonal1_sum = 0
    diagonal2_sum = 0
    row_sum = []
    for i in range(order):
        # print(i)
        sum1 = 0

        for j in range(order):
            # print(j)
            sum1 = sum1 + matrix[i][j]
            # row_sum.append(sum1)
            if i == j:
                diagonal1_sum = diagonal1_sum + matrix[i][j]
                # print(diagonal1_sum)
                # print(i,j)
                # print(matrix[i][j])
            if i + j == order - 1:
                diagonal2_sum = diagonal2_sum + matrix[i][j]
        # print(row_sum)
        # print(diagonal1_sum,diagonal2_sum)
        row_sum.append(sum1)
    print("Sum of the Rows: ", row_sum)
    print("Print Sum of the diagonals: ", diagonal1_sum, diagonal2_sum)
    if row_sum[0] == row_sum[1] & diagonal1_sum == diagonal2_sum:
        print("Magic Square Matrix")
    else:
        print("Not a Magic Square Matrix")

def dispaly_result(result):
    if result:
        print("Magic Square Matrix")
    else:
        print("Not a Magic Square Matrix")

def display_matrix(matrix):
    for i in range(order):
        for j in range(order):
            print(matrix[i][j], end=" ")
        print()

#columns = int(input("Enter the number of colunms: "))

#i=1
#j=1

matrix = user_input()
display_matrix(matrix)
magic_matrix()
#output = display_result(result)
'''
for i in range(order):
    temp =[]
    for j in range(order):
        temp.append(int(input()))
    matrix.append(temp)
'''

'''
for i in range(order):
    for j in range(order):
        print(matrix[i][j], end=" ")
    print()
'''

'''
diagonal1_sum = 0
diagonal2_sum = 0
row_sum = []
for i in range(order):
    #print(i)
    sum1 = 0

    for j in range(order):
        #print(j)
        sum1 = sum1 + matrix[i][j]
    #row_sum.append(sum1)
        if i == j:
                diagonal1_sum = diagonal1_sum +matrix[i][j]
                #print(diagonal1_sum)
                #print(i,j)
                #print(matrix[i][j])
        if i +j == order-1:
                diagonal2_sum = diagonal2_sum + matrix[i][j]
    #print(row_sum)
    #print(diagonal1_sum,diagonal2_sum)
    row_sum.append(sum1)
print("Sum of the Rows: ",row_sum)
print("Print Sum of the diagonals: ",diagonal1_sum,diagonal2_sum)
'''

'''
if row_sum[0] == row_sum[1] & diagonal1_sum == diagonal2_sum :
    print("Magic Square Matrix")
else :
    print("Not a Magic Square Matrix")
'''