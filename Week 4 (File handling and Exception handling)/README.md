#  Python File Handling & Error Handling Challenges

##  File Read & Write Challenge
This program demonstrates how to **read a file** and then **write a modified version** of its contents into a new file.

### Example:
- Reads content from `input.txt`
- Converts the content into uppercase
- Saves the result in `output.txt`

```python
with open("input.txt", "r") as infile:
    content = infile.read()

modified_content = content.upper()

with open("output.txt", "w") as outfile:
    outfile.write(modified_content)
