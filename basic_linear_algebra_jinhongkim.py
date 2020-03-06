#1
def vector_size_check(*vector_variables):
    emp_list = [] #빈 리스트 생성
    for i in vector_variables:
        temp = len(i)
        emp_list.append(temp) #빈 리스트에 각 vector들의 length 추가
    the_set = set(emp_list) #set로 만들어서 한개의 element만 있는지 확인(중복 제거)
    return len(the_set) == 1

##테스트
print(vector_size_check([1,2,3], [2,3,4], [5,6,3]))

#2
def vector_addition(*vector_variables):
    answer = [sum(t) for t in list(zip(*vector_variables))]
    return answer

##테스트
print(vector_addition([1, 3], [2, 4], [6, 7]))


#3
def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError

    temp = [-1*sum(t) for t in list(zip(*vector_variables))]
    answer = [2*t[0] for t in list(zip(*vector_variables))]

    return vector_addition(temp, answer)

#테스트
print(vector_subtraction([5, 3, 5], [2, 4,5])) # Expected value: [-1, -1]


#4
def scalar_vector_product(alpha, vector_variable):

    return list(map(lambda x: x * alpha, vector_variable))

#테스트
print (scalar_vector_product(5,[1,2,3])) # Expected value: [5, 10, 15]

#5
def matrix_size_check(*matrix_variables):
    return all([len(set(len(matrix[0]) for matrix in matrix_variables)) == 1]) and all([len(matrix_variables[0]) == len(matrix) for matrix in matrix_variables])

#테스트
matrix_x = [[2, 2], [2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
matrix_w = [[2, 5], [1, 1], [2, 2]]

print([len(matrix[0]) for matrix in matrix_variables])

print (matrix_size_check(matrix_x, matrix_y, matrix_z))

#5
def is_matrix_equal(*matrix_variables):

    return all([all([len(set(z)) == 1 for z in zip(*i)]) for i in zip(*matrix_variables)])

##테스트
matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 2], [2, 2]]

print (is_matrix_equal(matrix_x, matrix_y, matrix_y, matrix_y)) # Expected value: False

#6
def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    answer = [[sum(z) for z in zip(*i)] for i in zip(*matrix_variables)]
    return answer

##테스트
matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]

print (matrix_addition(matrix_x, matrix_y)) # Expected value: [[4, 7], [4, 3]]

#7
def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    answer = [[2*z[0]-(sum(z)) for z in zip(*i)] for i in zip(*matrix_variables)]
    return answer

##테스트
matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]

print (matrix_subtraction(matrix_x, matrix_y)) # Expected value: [[0, -3], [0, 1]]

#8
def matrix_transpose(matrix_variable):
    answer = [[z for z in i] for i in zip(*matrix_variable)]
    return answer
##테스트
matrix_w = [[2, 5], [1, 1], [2, 2]]
matrix_transpose(matrix_w)

#9
def scalar_matrix_product(alpha, matrix_variable):

    answer = [[alpha*z for z in i] for i in matrix_variable]
    return answer

##테스트
matrix_x = [[2, 2], [2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
matrix_w = [[2, 5], [1, 1], [2, 2]]

print(scalar_matrix_product(3, matrix_x)) #Expected value: [[6, 6], [6, 6], [6, 6]]
print(scalar_matrix_product(2, matrix_y)) #Expected value: [[4, 10], [4, 2]]
print(scalar_matrix_product(4, matrix_z)) #Expected value: [[8, 16], [20, 12]]
print(scalar_matrix_product(3, matrix_w)) #Expected value: [[6, 15], [3, 3], [6, 6]]

#10
def is_product_availability_matrix(matrix_a, matrix_b):

    return len(matrix_a[0]) == len(matrix_b)

##테스트
matrix_x= [[2, 5], [1, 1]]
matrix_y = [[1, 1, 2], [2, 1, 1]]
matrix_z = [[2, 4], [5, 3], [1, 3]]

print(is_product_availability_matrix(matrix_y, matrix_z)) # Expected value: True
print(is_product_availability_matrix(matrix_z, matrix_x)) # Expected value: True
print(is_product_availability_matrix(matrix_z, matrix_w)) # Expected value: False //matrix_w가없습니다
print(is_product_availability_matrix(matrix_x, matrix_x)) # Expected value: True

#11
def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError

    else:

        answer = [[sum([a*b for a,b in zip(i, column)]) for column in zip(*matrix_b)]
                          for i in matrix_a]
        return answer
#테스트
matrix_x= [[2, 5], [1, 1]]
matrix_y = [[1, 1, 2], [2, 1, 1]]
matrix_z = [[2, 4], [5, 3], [1, 3]]

print(matrix_product(matrix_y, matrix_z)) # Expected value: [[9, 13], [10, 14]]
print(matrix_product(matrix_z, matrix_x)) # Expected value: [[8, 14], [13, 28], [5, 8]]
print(matrix_product(matrix_x, matrix_x)) # Expected value: [[9, 15], [3, 6]]
print(matrix_product(matrix_z, matrix_w)) # Expected value: False
