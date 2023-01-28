from bs4 import BeautifulSoup

def main():
	# Input file
	input_path = 'input.xml'

	# Open xml file
	with open(input_path) as input_file:
		xml = BeautifulSoup(input_file, 'xml')

	# Pull tables
	tables = xml.findAll('Table')
	# print(len(tables))

	# Go through tables and create table list
	table_list = []
	for table in tables:
		# Read rows
		rows = table.findAll('Row')
		date = rows[1].text.strip()
		# print(date)

		# Get all rows
		rows_list = []
		for row in rows[3:]:
			row_list = row.text.splitlines()[2:]
			info_list = row_list[0:3]
			data_list = row_list[3:]

			# Goes through data values
			for count_data, data in enumerate(data_list):
				hour = str(count_data // 12)
				minute = str((count_data % 12) * 5)
				row_dict = {
					'tmc_code' : info_list[0],
					'name'     : info_list[1],
					'miles'    : float(info_list[2]),
					'time'     : f'{date} {hour.zfill(2)}:{minute.zfill(2)}',
					'value'    : float(data)
				}
				rows_list.append(row_dict)

		# Adds to table list
		table_list.append(rows_list)

	# Debug printing
	print(table_list)
	print(f'\ntables: {len(table_list)}')
	print(f'data points: {len(table_list) * len(table_list[0])}')

if __name__ == '__main__':
	main()