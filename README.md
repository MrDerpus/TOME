# TOME 📜 🧙‍♂️🔮
## Table Oriented Markup Encoding.
```
Author: MrDerpus
Python version: 3.12.3

TOME Parser v1.2.0
Table Oriented Markup Encoding.

I just wanted a good looking data structure that is easy to read.
Also because I saw MEMEs about Ai bros mentioning: TOON.
So I was inspired to create my own parser for my custom data structure.

TOME combines:
- SQL-like table headers.
- CSV row entry.
- Clean Python dictionaries as output. 
```

# 🪄 Another super big update! v1.2.0
What was added? <br>
* TOME.write, allows you to write/append to TOME files.
* TOME <=> JSON compatibility !!!
* Strict typing now works 100% You WILL comply! (optional)
* Added detailed error messages.
* Fixed bugs that caused crashes when parsing input files.

### Make sure to read the rules to see how to use these new changes.



# 📜 Rules:
* Header defines the table name and ordered column list.
* Data rows map directly to the column list.
* Indentation is optional.
* Commas "," separate fields.
* Leading and trailing whitespace is purged for your convenience.
* Lines beginning "#" or ";" are treated as comments.
* A line beginning with "!"  will end the parsing early.
* A line beginning with "==" will tell the parser to start parsing a new data table.
* A blank line separating two tables will also automatically trigger parsing for another data table.
* By default, all values are returned as strings, unless specified otherwise.
---

# Demos:

## TOME File structure:
```ini
# This is a commented line.
; this is also a commented line.

# Default parsing, will return all values as strings:
employees[uuid, name, age]
	c0fb3d3b-2ffc-4eb3-8a2f-8177aeebecd3, John Doe, 35
	ab5573e2-a6eb-4c71-b501-7a9206e43a1f, Jane Doe, 21
	d7efb46c-a512-4eda-b55f-64d7f888faf3, Bill Doe, 42

# Strict parsing, only selected columns are type-cast.
# Columns without a type remain as strings.
inventory[serial:str, item, qty:int, price:float, sale:bool]:
	2ffc-4eb3-8a2f, keyboard,  50,  36.99,   true
	a6eb-4c71-b501, monitor,   27,  139.98,  true
	a512-4eda-b55f, mouse,     23,  20.99,   false

! ;<-- End parsing here and return everything above this line.  

; An example of using the wrong data type in a strict table.
items[name:str, price:int]:
    Hammer, 19
    Saw, 12
    Wrench, cheap
    ;        ^^^ this will throw a TOMEparseError
    ; as it is not the correct data type

; Will provide this error message in your console:
; TOMEparseError @ line 12 in test.tome:
; price expected data type: int, but 'cheap' was given instead.

; Supported data types:
; String/str
; Integer/int
; Boolean/bool
; Float
```

## Python

```python
from main import TOME
import json

# Accessing values in Python: ------------
data:dict = TOME.read('./path/to/file/test.tome')
''' returns dictionary in this format:
{
    'items': [
        {
            'serial': '2ffc-4eb3-8a2f',
            'item': 'keyboard',
            'qty': 50,
            'price': 36.99,
            'sale': True
        },
        {
            'serial': 'a6eb-4c71-b501',
			...
		}
	]
}
'''

first_item_serial = data['items'][0]['serial']
print(first_item_serial)
# output: '2ffc-4eb3-8a2f' ---------------

# Editing/Adding existing values and creating a file with TOME.write()
data['new_table'] = [
    {
        'name': 'John Doe',
        'age': 28,
        'favourite_song': 'Simple Man - Shinedown'
    },
    {
        'name': 'Jane Doe',
        'age': 30,
        'favourite_song': 'Higher - Creed'
    },
    {
        'name': 'Will Doe',
        'age': 26,
        'favourite_song': 'H. - Tool'
    }
]

TOME.write('new_file.tome', data, 'w')


# Converting formats . . .
# TOME to JSON
data = TOME.read('test.tome')
with open('tome-to-json.json', 'w') as f:
	json.dump(data, f, indent=4)

# JSON to TOME
with open('tome-to-json.json', 'r') as f:
	data = json.load(f)
TOME.write('json-to-tome.tome', data, 'w')
```