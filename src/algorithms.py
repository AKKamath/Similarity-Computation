#!/usr/bin/env python3

def manhattan_distance(a, b):
	return sum(abs(x - y) for x, y in zip(a, b))

def euclidean_distance(a, b):
	return pow(sum(pow(abs(x - y), 2) for x, y in zip(a, b)), 0.5)

def minkowski_distance(a, b, p):
	return pow(float(sum(pow(abs(x - y), p) for x, y in zip(a, b))), 1.0 / float(p))

def chebyshev_distance(a, b):
	return max(abs(x - y) for x, y in zip(a, b))

def pearson_correlation_distance(a, b):
	n = len(a)

	sum_a = sum(a)
	sum_b = sum(b)

	numerator = n * sum(x * y for x, y in zip(a, b)) - sum_a * sum_b

	temp_a = n * sum(x * x for x in a) - sum_a * sum_a
	temp_b = n * sum(y * y for y in b) - sum_b * sum_b

	denominator = pow(temp_a * temp_b, 0.5)
	
	if(denominator == 0):
		return "Divide by zero error"
	
	return 1 - float(numerator) / float(denominator)

def simple_matching_coefficient(a, b):
	m00 = sum(not int(x) and not int(y) for x, y in zip(a, b))
	m01 = sum(not int(x) and int(y) for x, y in zip(a, b))
	m10 = sum(int(x) and not int(y) for x, y in zip(a, b))
	m11 = sum(int(x) and int(y) for x, y in zip(a, b))
	
	if(float(m00 + m01 + m10 + m11) == 0):
		return "Divide by zero error"

	return float(m00 + m11) / float(m00 + m01 + m10 + m11)

def jaccard_coefficient(a, b):
	m01 = sum(not int(x) and int(y) for x, y in zip(a, b))
	m10 = sum(int(x) and not int(y) for x, y in zip(a, b))
	m11 = sum(int(x) and int(y) for x, y in zip(a, b))
	
	if(float(m01 + m10 + m11) == 0):
		return "Divide by zero error"
	
	return float(m11) / float(m01 + m10 + m11)

def tanimoto_coefficient(a, b):
	dot_product = sum(x * y for x, y in zip(a, b))
	temp = sum(x * x for x in a) * sum(y * y for y in b)

	if(float(temp - dot_product) == 0):
		return "Divide by zero error"
	
	return float(dot_product) / float(temp - dot_product)

def cosine_similarity(a, b):
	magnitude_a = pow(sum(x * x for x in a), 0.5)
	magnitude_b = pow(sum(y * y for y in b), 0.5)

	if(float(magnitude_a * magnitude_b) == 0):
		return "Divide by zero error"		
	
	return float(sum(x * y for x, y in zip(a, b))) / float(magnitude_a * magnitude_b)
