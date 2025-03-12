# Random Number Generator

Python uses what's called the Mersenne Twister as a number generator.
- Random module allows to use different random number generators. 
```python
    import random

    random.randint(1,10)
    #This requires input (a,b) so it will use the numbers between those numbers specified
```


 
## Module
- How can we split code so we don't have a large file with lines of code.
- We can do so by using Modules!
- If we want to use our module we need to import that module
    ```python
        import random
        import my_module

    ```
- When we call the module typicaly you use the name of the module itself, like ```random.random``` where the first random is calling the module itself and then calling a sub module within the main module.


# Lists

- Lists are data structures where we can store items inside and can be any data type and be mixed ie:boolean, ints etc..
- They typically sit in ```[]``` like this ``` fruit=[apple,pear,blueberry]``` and you use [] to put stuff in and get stuff out.
    - ie: ```fruit[1] #will give the item in the 1 index. [0,1,2,3...]```
- Lists can be related data and they can have order in the list
- we can use a function to add a single item to the end of a list
    - append()
    - ```fruit.append('raspberry')```
- extend()
    - ```fruit.extend(['raspberry', 'strawberry', 'melon'])```

Check out [Data Structure]("https://docs.python.org/3/tutorial/datastructures.html") from python Docs for more information and other methods for lists