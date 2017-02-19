# Vector operations

def elementwise_multiplication(vec_a, vec_b):
	len_a = len(vec_a)
	assert(len_a == len(vec_b))
	result = [None] * len_a
	for i in range(len_a):
		result[i] = vec_a[i] * vec_b[i]
	return result

def elementwise_sum(vec_a, vec_b):
	len_a = len(vec_a)
	assert(len_a == len(vec_b))
	result = [None] * len_a
	for i in range(len_a):
		result[i] = vec_a[i] + vec_b[i]
	return result

def vector_sum(vec_a):
	result = 0
	for i in range(len(a)):
		result += vec_a[i]
	return result

def vector_average(vec_a):
	sum = vector_sum(vec_a)
	return sum/len(vec_a)

a = [1, 2, 3]
b = [1, 2, 3]

print(elementwise_multiplication(a, b))
print(elementwise_sum(a, b))
print(vector_sum(a))
print(vector_average(a))
print(vector_sum(elementwise_multiplication(a, b)))