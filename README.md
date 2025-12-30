# TOME 📜 🧙‍♂️🔮
Table Oriented Markup Encoding.

```
Author: MrDerpus
Python version: 3.12.3

TOME Parser v1.5.0
Table Oriented Markup Encoding.

TOME combines:
- SQL-like table headers.
- CSV row entry.
- Clean Python dictionaries as output.

TOME can freely convert:
    TOME > Python > JSON > Python > TOME > Python > JSON > Python > JSON ...
```

# 🪄 "Whitespace, Multiline comments & proper table declaration standardization (Oh my)" update! v1.5.0
## What was added? <br>
* Changed how tables are declared in TOME script.
* Blank lines inside of TOME tables is now allowed.
* Added Multiline comment support.


### Make sure to read the rules, and see examples to see how to use these new changes.


# 📜 Syntax Spec:

## Table declaration:
A valid table header must follow this syntax:
```ini
table-name[Col_1, Col_2, Col_3, ...]:
```
A line is recognized as a table header if:
- It contains exactly one "["
- Exactly one "]"
- Ends with ":"

---

## Comments
| Type             | Syntax       | Example       | Notes                                   |
|------------------|--------------|---------------|-----------------------------------------|
| Single-line      | `#`          | `# comment`   | Entire line is ignored                  |
| Single-line      | `;`          | `; comment`   | Entire line is ignored                  |
| Multiline start  | `/*`         | `/* ...`      | Everything inside is ignored until `*/` |
| Multiline end    | `*/`         | `... */`      | CLosing line is ignored as well         |

---

## General rules

* Header defines the table name and ordered column list  
* Data rows must map directly to the column list  
* Indentation is optional  
* Leading/trailing whitespace is stripped  
* By default `,` separates fields (unless overridden via `delimiter=`)  
* Lines starting with `#` or `;` are comments  
* `/*` opens a multiline comment block; `*/` closes it  
* `!` immediately stops parsing  
* A valid table header resets the parser for a new table  
* Blank lines inside tables are allowed  
* All values are strings unless typed (`:int`, `:float`, `:bool`, `:str`) 

---

# Demos:

## TOME File structure:
```ini
# Default parsing, will return all values as strings:
employees[uuid, name, age]:
	c0fb3d3b-2ffc-4eb3-8a2f-8177aeebecd3, John Doe, 35
	ab5573e2-a6eb-4c71-b501-7a9206e43a1f, Jane Doe, 21
	d7efb46c-a512-4eda-b55f-64d7f888faf3, Bill Doe, 42


# Strict parsing, only selected columns are type-cast.
# Columns without a type remain as strings.
inventory[serial:str, item, qty:int, price:float, sale:bool]:
	2ffc-4eb3-8a2f, keyboard,  50,  36.99,   true
	a6eb-4c71-b501, monitor,   27,  139.98,  true
	a512-4eda-b55f, mouse,     23,  20.99,   false
! <-- End parsing here and return everything above this line.  


/* Multiline comment example.
car-park[plate, model, time-parked]:
    axx-001, Ford Mustang,  1767077287.1845567
    bxx-002, Toyota Hilux,  1767077388.3949540
    cxx-003, Renault Alpin, 1767077664.6869645
*/


; An example of using the wrong data type in a strict table.
items[name:str, price:int]:
    Hammer, 19
    Saw, 12
    Wrench, cheap
    ;        ^^^ this will throw a TOMEparseError
    ; as it is not the correct data type

; Will provide this error message in your console:
; TOMEparseError @ line 22 in test.tome:
; price expected data type: int, but 'cheap' was given instead.

```

## Python

```python
from main import TOME
import json

# Accessing values in Python: ------------
data:dict = TOME.read(input='./path/to/file.tome')
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

TOME.write(output='new_file.tome', table=data, mode='w')


# Converting formats . . .
# TOME to JSON
data = TOME.read('test.tome')
with open('tome-to-json.json', 'w') as f:
	json.dump(data, f, indent=4)


# JSON to TOME
with open('tome-to-json.json', 'r') as f:
	data = json.load(f)
TOME.write(output='json-to-tome.tome', table=data, mode='w')


# Using the new string parsing method v1.3.0. (updated v1.4.0)
string_input = '''
data-table[serial. item. location. qty:int]:
    00001. m3x10 self tapping screw. shelf-3-10. 100
    00002. 0 OHM SMD resistor. cupboard-2-5. 18
    00003. 16V 33uf through hole capacitor. shelf-1-1. 39
'''

data = TOME.read(from_string=True, input=string_input, delimiter='.')
print(data)


# Using the new dictionary parsing method to return a string v1.4.0.
data_string = TOME.write(to_string=True, table=data, delimiter='.')
print(data_string)

# And again to prove round trip compatibility.
parsed = TOME.read(from_string=True, input=data_string)
print(parsed)

```