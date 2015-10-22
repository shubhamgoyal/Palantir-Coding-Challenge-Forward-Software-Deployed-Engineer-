def get_complement(str):
	str_list = list(str)
	complement_list = []
	for c in str_list:
		if c == 'P':
			complement_list.append('T')
		else:
			complement_list.append('P')
	complement_str = ''.join(complement_list)
	return complement_str

def get_input_matrix(num_rows):
	matrix = []
	for i in range(num_rows):
   		matrix.append(raw_input())
   	return matrix

def get_number_of_rows_in_matrix():
	return int(raw_input().split()[0])

def get_matrix_including_complements_of_rows(matrix):
	matrix_with_complements = matrix[:]
   	for row in matrix:
   		matrix_with_complements.append(get_complement(row))
   	return matrix_with_complements

def make_dictionary_of_row_value_counts(l):
	d = {}
   	for i in l:
   		if i not in d:
   			d[i] = 1
   		else:
   			d[i] = d[i] + 1
   	return d

def get_max_value(d):
	return d[max(d, key=lambda i: d[i])]

if __name__ == '__main__':
	r = get_number_of_rows_in_matrix()
	matrix = get_input_matrix(r)
	matrix_with_complements = get_matrix_including_complements_of_rows(matrix)
	matrix_dict = make_dictionary_of_row_value_counts(matrix_with_complements)
	num_repetitive_rows = get_max_value(matrix_dict)
	print num_repetitive_rows