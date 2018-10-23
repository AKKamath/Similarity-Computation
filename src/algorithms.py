#!/usr/bin/env python3

def manhattan_distance(a, b):
	return sum(abs(x - y) for x, y in zip(a, b))

def euclidean_distance(a, b):
	return pow(sum(pow(abs(x - y), 2) for x, y in zip(a, b)), 0.5)

def minkowski_distance(a, b, p):
	return pow(sum(pow(abs(x - y), p) for x, y in zip(a, b)), 1 / p)

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

	return 1 - numerator / denominator

def simple_matching_coefficient(a, b):
	m00 = sum(~x & ~y for x, y in zip(a, b))
	m01 = sum(~x & y for x, y in zip(a, b))
	m10 = sum(x & ~y for x, y in zip(a, b))
	m11 = sum(x & y for x, y in zip(a, b))

	return (m00 + m11) / (m00 + m01 + m10 + m11)

def jaccard_coefficient(a, b):
	m01 = sum(~x & y for x, y in zip(a, b))
	m10 = sum(x & ~y for x, y in zip(a, b))
	m11 = sum(x & y for x, y in zip(a, b))

	return m11 / (m01 + m10 + m11)

def tanimoto_coefficient(a, b):
	dot_product = sum(x * y for x, y in zip(a, b))
	temp = sum(x * x for x in a) * sum(y * y for y in b)

	return dot_product / (temp - dot_product)

def cosine_similarity(a, b):
	magnitude_a = pow(sum(x * x for x in a), 0.5)
	magnitude_b = pow(sum(y * y for y in b), 0.5)

	return sum(x * y for x, y in zip(a, b)) / (magnitude_a * magnitude_b)
