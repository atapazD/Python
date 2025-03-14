# Goals for Day 5
- Building a password generator
## Loops
### For Loop
- By using a For Loop we can go through a list and perform an action with each individual item
```python 
fruits=['apple','peach', 'pear']
for fruit in fruits:
    print(fruit)
```
- You can also manipulate the items in the list using a for loop like:
```python
print(fruit + ' pie')
```
## Range()

- using for loops with the range() function
    - range() function is good for setting a range ```python Range(a,b)``` and using a loop to iterate over the range like 
    ```python 
    for i in range(1,10):
        print(i)
    ```
    - this will only pring 1 through 9 so if we want to include 10 we need to add 1 more so it would look like this:
    ```python 
    for i in range(1,11):
        print(i)
    ```
    
