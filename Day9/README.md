# Day 9 
- In day 9 I build a Silent Auction app
## Dictioanries
- work simiilar to dictionaries in real life
    - if you were to look up a word in a dictionary you would find a description of it.
    - think of them as a table
     -  you have a key which is the word, and the value which describes that word
     - ```python {key:value}``` or ```python {"bug": "an error in a program which stops the program", "key": "value"...}```
    - you can add more entries by separating with a comma , and the next key:value pair
    - keep in mind a LIST uses [] 
    - dictionaries have elements that are identified by their keys
        - 
        ```python 
        print(programming_dictionary["bug"])
        # this would access the dictionary 'programming_dictioanry' at the key 'bug'
        
        ```
        - remmember if you are accessing a key, make sure you call that key by its type, in the example above its accessed via a string, you can use a number and even a variable.
    - to use the dictionary and add a value you can
    
    ```python
    programming_dictionary["loop"] = "actiona of doing something over and over again"
    # you can also call an existing key in that dictionary and update the value to something else
    
    ```

    - emptying a dictionary you can just assign the name of the dictionary to {} ie: ```programming_dictionary={}```

    - looping through dictionary
        - if you were to print the dictionary
        ```python
        for key in programming dictionary:
            print(key)
            #in order to get the value of the key as well we need to add the following
            print(programming_dictioanry[key])
        ```
## Nesting
- that idea of putting things into the other
- instead of having a simple value like 
```python
{key:value}
# we can use something like this

{key:[list]
 key2:{dict}}
 # this uses a list as the value to key 1 which is within a dictionary and key 2's value is a dictionary within a dictionary
 ```

- think about how you would access a list within a dictionary
```python 
    
```