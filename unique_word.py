input_file_name = raw_input('File name: ')
f= open(input_file_name, 'r')


def split_file(input_file_name):
	"""Spliting file into list, counting total amount"""
	for line in f.readlines():
		lines = line.split() 
	len_f= len(lines)
	#return lines
	print lines
	print 'Total amount of words ' + str(len_f)
	return lines
#split_file(input_file_name)

def count_word(input_file_name):
"""Counts unique words"""
	f = file(input_file_name, 'r').read().split()
    	words= sorted(set(f))
    	for word in words:
			print f.count(word), word

split_file(input_file_name)
count_word(input_file_name)

