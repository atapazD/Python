# Day 6
This day consists of using the [Reeborg](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json) site game to work on while loops and creating functions to solve challenges. Hurdle 1-4 and the Maze challenge specfically. 
## Functions
Link for built in [functions](https://docs.python.org/3/library/functions.html)

- Functions are distinguishable by the () ie: 
```python 
print()
```
```python 
len("hello")
```

- How about making our own functions?
    - we need to use ```def``` to define our functions
    ```python 
    def my_function():
        print ("this is my function")
    
    my_function() #this calls the function, and since it doesn't need an input we can leave it blank within the parenthesis
    ```

## Indentation
Every line that comes after a function() must be indented so that the code remains in the function code block
```python
def my_function():
    #this is in 
    #this is in
        #this is in
#this is not
#this is not either
```
You can of course use tabs to indent instead of spaces. There is a debate on them but ultimately achieve the same thing. The official python guide it says spaces are preferred. Also in python3 it disallows the mixture of tabs and spaces.


### While loop

In a For loop we've seen:
```python
for item in list:
    #do something to each item

for number in range(a,b):
    print(number)
```


In a while loop we would run a code until something stops the function from iterating:
```python
number_of_hurdles=6
while number_of_hurdles > 0: 
    #this sets the while loop, 6 > 0 , jumps, then subtracts 1 to number_of_hurdles, prints the number_of_hurdles, now it would be 5>0.... and so on.
    jump()
    number_of_hurdles-= 1
    print(number_of_hurdles)
```
Typically while loops have some condition in its definition:
```python
while something_is_true:
    #do this
    #Then do this
    #Then do this
```
When do we use For loops or while loops?
- For loops are when we need to iterate over something
    - you set how many times something will run
- While loops are good to carry out functionality many times until a condition changes
    - they continue running until a condtition changes; if something never changes then it can become an infinite loop.
