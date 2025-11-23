# TOME 📜 🧙‍♂️🔮
## Table Oriented Markup Encoding.
```
Author: MrDerpus
Python version: 3.12.3

TOME Parser v1.1.0
Table Oriented Markup Encoding.

I just wanted a good looking data structure that is easy read.
Also because I saw MEMEs about Ai bros mentioning: TOON.
So I was inspired to create my own parser for my custom data structure.

This combines the simplicity of:
- writing in a SQL-like database structure,
- CSV rows for data entry,
- and receiving clean python friendly dictionaries.
```

# 🪄 A super big update! v1.1.0
What was added? <br>
* Multi-table support.
* Strict typing for table headers (Optional).
* Refactored syntax dictionary.
* Auto-detect new tables (Only if formatting is compatible).
* Clean Python dictionary output structure.

### Make sure to read the rules to see how to use these new changes.



## 📜 Rules:
* Header defines the table name and ordered column list.
* Data rows map directly to the column list.
* Indentation is optional.
* Commas "," separate fields.
* Leading and trailing whitespace is purged for your convenience.
* Lines beginning "#" or ";" are treated as comments.
* A line beginning with "!"  will end the parsing early.
* A line beginning with "==" will tell the parser to start paring a new data table.
* A blank line separating two tables will also automatically trigger parsing for another data table.
* By default, all values are returned as strings, unless specified otherwise.


## TOME returns a dictionary in this format:
```python
{
    'items': [
        {
            'serial': '2ffc-4eb3-8a2f',
            'item': 'keyboard',
            'qty': '50',
            'price': '36.99',
            'sale': 'true'
        },
        {
            'serial': 'a6eb-4c71-b501',
			...
		}
	]
}
```

## Accessing values in Python:
```python
output = TOME.read('./path/to/file/test.t')
first_item_serial = output['items'][0]['serial']
```
---

## Demos:
```ini
# Default parsing, will return all values as strings:
employees[uuid, name, age]
	c0fb3d3b-2ffc-4eb3-8a2f-8177aeebecd3, John Doe, 35
	ab5573e2-a6eb-4c71-b501-7a9206e43a1f, Jane Doe, 21
	d7efb46c-a512-4eda-b55f-64d7f888faf3, Bill Doe, 42

# Strict parsing, only selected columns are type-cast.
# Columns without a type remain as strings.
items[serial:str, item, qty:int, price:float, sale:bool]:
	2ffc-4eb3-8a2f, keyboard,  50,  36.99,   true
	a6eb-4c71-b501, monitor,   27,  139.98,  true
	a512-4eda-b55f, mouse,     23,  20.99,   false

; Supported data types:
; String/str
; Integer/int
; Boolean/bool
; Float
```