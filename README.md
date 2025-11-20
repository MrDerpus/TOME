# TOME 📜 🧙‍♂️🔮
## Table Oriented Markup Encoding.
```
Author: MrDerpus
Python version: 3.12.3

TOME Parser v1.0.0
Table Oriented Markup Encoding.

I just wanted a good looking data structure that is easy read.
Also because I saw MEMEs about Ai bros mentioning: TOON.
So I was inspired to create my own parser for my custom data structure.

This combines the simplicity of:
writing in a SQL-like data table structure,
CSV data entry,
and getting the output in a python JSON parser-like format.

It's also made in a day, I expect you to break it very easily.
```


## Rules:
* Header defines the table name and ordered column list.
* Data rows map directly to the column list.
* Indentation is optional.
* Commas "," define the field.
* Leading and trailing whitespace is ignored.
* Lines beginning "#" or ";" are treated as comments.
* A line beginning with "--" will end the parsing early.
* Currently returns all values as strings.

## Proposed changes:
* Make values return their proper type.

## Returns a dictionary in this format:
```python
{
	"table_name": <name>,
	0:{col1: value, col2: value, ...},
	1{...},
	...
}
```

## And can be accessed in python like this:
```python
output = TOME.read(./path/to/file/test.t)
table_name = output["TableName"]
first_item = output[0][...]
```

```ini
; TOME example:
employees[uuid, name]
	c0fb3d3b-2ffc-4eb3-8a2f-8177aeebecd3, John Doe
	ab5573e2-a6eb-4c71-b501-7a9206e43a1f, Jane Doe
	d7efb46c-a512-4eda-b55f-64d7f888faf3, Bill Doe
--
```