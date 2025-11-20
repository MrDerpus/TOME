'''
Author: MrDerpus
Python version: 3.12.3

TOME Parser v1.0.0
Table Oriented Markup Encoding

I just wanted a good looking data structure that is easy to use in python.
Also because I keep seeing MEMEs 



Reads a structured table with this format:
	TableName[col1, col2, col3]:
		value1, value2, value3
		value1, value2, value3
		...

Syntax rules:
	> Header defines the table name and ordered column list.
	> Data rows map directly to the column list.
	> Indentation is optional.
	> Commas "," define the field.
	> Leading and trailing whitespace is ignored.
	> Lines beginning "#" or ";" are treated as comments.
	> A line beginning with "--" will end the parsing early.
	> Currently returns all values as strings.

Proposed changes:
	> Make values return their proper type.

Returns a dictionary in this format:
	{
		"table_name": <name>,
		0:{col1: value, col2: value, ...},
		1{...},
		...
	}

And can be accessed like this:
	output = DataParser.read(./path/to/file/test.t)
	table_name = output["TableName"]
	first_item = output[0][...]
'''




class TOME:
	
	@staticmethod
	def read(input_file:str):

		with open(input_file, 'r') as file:
			row_index = -1  # Tracks actual data rows (index starts at 0).
			brackets = '[]' # Characters used to detect the header section.
			
			# Read file line by line, removing the white space from the line.
			for line in file:
				line = line.strip()

				if line == '' or line is None: continue # skip empty line.
				elif line[0] in ['#', ';']:    continue # skip commented lines.
				elif line[:2].strip() == '--': return table # end file.
				
				row_index += 1

				# Define table and column names
				if row_index == 0:
					table_name:str = line.split(brackets[0])[0].strip() # Collect table name.
					columns:list   = line.split(brackets[0])[1].split(brackets[1])[0].split(',') # I dont suffer from Long-line-itis, I genuinely enjoy it.
					table:dict = { 'table_name': table_name }

					# Cleanse items in columns.
					columns = [ i.strip() for i in columns ]
				


				# Collect values line and place them into dictionary
				elif row_index > 0:
					index = row_index-1
					table[index] = {}

					# Cleanse values of rouge whitespace.
					values = [ j.strip() for j in line.split(',') ]

					# Add values to dictionary.
					table[index] = { columns[j]: values[j] for j in range(len(values)) }			
			
			# Return.
			return table


# Output debug mode

if 1==2:

	from rich.traceback import install; install(show_locals=True)
	from rich.console   import Console; Print = Console().print

	output = TOME.read('test.t')
	Print(output)