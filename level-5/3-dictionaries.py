# Dictionaries in Python: Key-Value Powerhouse

    # In Python, dictionaries are versatile data structures used to store and organize information in a flexible and efficient manner. 
    # They map unique keys to specific values, enabling fast retrieval and modification based on keys.

# Key Characteristics:

    # Unordered: Unlike lists, dictionaries do not maintain a defined insertion order when iterating (except in Python 3.7+). Accessing items is always via keys.
    # Mutable: You can freely add, remove, or update key-value pairs after creation.
    # Key Type: Keys must be immutable data types like strings, numbers, or tuples (to ensure uniqueness).
    # Value Type: Values can be any Python object, allowing diverse data storage.

    # Creation:

        # Curly Braces Syntax: my_dict = {"key1": value1, "key2": value2}
        # dict() Function: my_dict = dict(key1=value1, key2=value2)
        
    # Accessing Elements:

        # Use square brackets [] with the key: value = my_dict["key1"]
        # get() Method (handles missing keys gracefully): value = my_dict.get("key3", default_value)
        
    # Adding and Modifying:

        # Assignment: my_dict["new_key"] = new_value (adds or updates)
        # update() Method: my_dict.update({"another_key": another_value})
        
    # Removing Elements:

        # del Keyword: del my_dict["key1"]
        # pop() Method: removed_value = my_dict.pop("key2") (returns and removes value)
        # popitem() Method: removed_pair = my_dict.popitem() (returns and removes last pair)
        
    # Iteration:

        # Loop over keys: for key in my_dict:
        # Loop over key-value pairs: for key, value in my_dict.items():

# Example:
phonebook = {"Alice": "123-4567", "Bob": "890-1234", "Charlie": "567-8901"}

# Access Alice's number:
alice_number = phonebook["Alice"]
print(alice_number)  # Output: 123-4567

# Add David's number:
phonebook["David"] = "222-3333"

# Iterate over key-value pairs:
for name, number in phonebook.items():
    print(f"{name}: {number}")


# Example 2
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

ep1.update(ep2)
ep1.clear()
ep1.pop(122)
ep1.popitem()
del ep1[122]
print(ep1) 

# Applications:
    
    # User profiles: Store personalized data, settings, and preferences.
    # Configuration files: Manage application settings and options.
    # Caching data: Improve performance by storing frequently accessed values.
    # Representing real-world relationships: Model connections between entities (e.g., social networks).