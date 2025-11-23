'''
Author: MrDerpus
Python version: 3.12.3

TOME Parser v1.1.0
Table Oriented Markup Encoding

I just wanted a good looking data structure that is easy to use in python.
Also because I keep seeing MEMEs about TOON.
'''
from sys import exit as kill
class TOME:
	
	@staticmethod
	def read(input_file:str):

		with open(input_file, 'r') as file:
			syntax = {
				'brackets':'[]',       # Characters used to detect the header section.
				'comments':['#', ';'], # Comments, lines to ignore
				'var-type':':',        # Separate values from their data types.
				'end-parse': '!',      # Stop parsing file.
				'new-table': '==',     # Start parsing new table.
				'separator': ','       # The comma delimiter.
			}

			table:dict     = {}   # Table dictionary that is output.
			row_index:int  = -1   # Tracks actual data rows (index starts at 0).
			table_name:str = ''   # Name of current table.
			values:list    = []   # Store values to be added to dictionary.
			data_type:list = []   # Get datatype for table item.
			columns:list   = []   # Store column names for tables.
			table_type:str = ''   # Set to 'dynamic' by default

			
			# Read file line by line, removing the white space from the beginning & end of the line.
			for line in file:
				line = line.strip()

				if line is None or line == '': row_index = -1; continue # Skip empty line.
				elif line[0] in syntax['comments']: continue # Skip commented lines.
				elif line[:2].strip() == syntax['new-table']: row_index = -1; continue # End current table parsing, and get ready to parse new table.
				elif line[:2].strip() == syntax['end-parse']: return table   # End file parsing early, return current parsed data.
				
				row_index += 1

				# Define table and column names
				if row_index == 0:
					table_type = 'dynamic'
					table_name = line.split(syntax['brackets'][0])[0].strip() # Collect table name.
					columns    = line.split(syntax['brackets'][0])[1].split(syntax['brackets'][1])[0].split(syntax['separator']) # I dont suffer from Long-line-itis, I genuinely enjoy it.
					data_type = []

					# create table name, and cleanse items for columns list.
					table[table_name] = []
					
					
					# if table is strongly typed, cast data types in a list to be accessed later in code.
					for i in range(len(columns)):
						if syntax['var-type'] in columns[i]:
							table_type = 'strict'
							_type = columns[i].split(syntax['var-type'])[1].strip().lower()
							_valu = columns[i].split(syntax['var-type'])[0].strip()
							
							# if type is in accepted list, append type to data_type:list.
							if _type in ['str', 'string', 'int', 'integer', 'float', 'boolean', 'bool']:
								if   _type == 'string':  _type = 'str'
								elif _type == 'boolean': _type = 'bool'
								elif _type == 'integer': _type = 'int'
								
								data_type.append(_type)
								columns[i] = _valu
						
						# Set type string if data type is not supported.
						else:
							data_type.append('str')
							columns[i] = columns[i].strip()

					#KEEP BELOW
					#columns   = [ i.strip() for i in columns ]

				# Collect values line and place them into dictionary.
				elif row_index > 0:
					index = row_index-1
					values = [ j.strip() for j in line.split(syntax['separator']) ]

					# Cast variables as their defined data types, and append to dictionary.
					if table_type == 'strict':
						for i in range(len(values)):
							
							if data_type[i]   == 'int':   values[i] = int(values[i])
							elif data_type[i] == 'float': values[i] = float(values[i])
							elif data_type[i] == 'bool': 
								if values[i].lower() in ['true', 'yes']:
									values[i] = True
								else:
									values[i] = False

							else: # Set data type to string to avoid errors.
								values[i] = str(values[i])
					
					# Append to table dictionary.
					table[table_name].append({ columns[j]: values[j] for j in range(len(values)) })
			

			# Return.
			return table