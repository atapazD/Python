# Day10 
- objective here is to understand more on functions and passing information between them 
# functions
```python
def my_function(something):
    #do this with something
    #Then do this
    #Finally do this
```
- the above is the standard with a simple input for a function which is entered and then done something too

### Return
```python
def my_function():
    result = 3 * 2
    return result 
```
- ```pyton return ``` is the output of a function where a value will be returned
- if you take the returned value you can also save that result in a value outside of the function 

```python
def my_function():
    result = 3 * 2
    return result

output = my_function()
#here output will store whatever the output is in my_function()
```
### DocStrings
- these are comments that you can write with multiple lines instead of highlight and using "#" you can use """ """. It can also be used to specifically write explainers for functions that are created; this is more what this was designed for and not commenting since its not suggested to use it for comments specifically. Here is an example of a docstring in a function that will display the explanation of the function when potentially calling it out

```python 
def format_name(f_name, l_name):
    """
        This function is designed to format first and last name using title case()
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("DaNiEl", "ZapATA")

length = len(formatted_name)
```