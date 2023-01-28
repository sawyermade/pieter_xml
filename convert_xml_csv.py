from bs4 import BeautifulSoup

def main():
	# Inoput file
	input_path = 'input.xml'

	# Open xml file
	with open(input_path) as input_file:
		xml = BeautifulSoup(input_file, 'xml')

	first_row = 3
	rows = xml.findAll('Row')[first_row:]

	limit = 3
	for count_row, row in enumerate(rows):
		if count_row >= limit:
			pass

		row_list = row.text.splitlines()[2:]
		# print(len(row_list))
		# print(row_list)

		info_list = row_list[0:3]
		data_list = row_list[3:]
		# print(info_list)
		# print(data_list)

if __name__ == '__main__':
	main()