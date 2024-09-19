data = {'b': 5, 'k': 3, 'a': 8}

# Convert the dictionary keys into a list
keys = list(data.keys())

# Bubble Sort Algorithm
for i in range(len(keys)):
    for j in range(0, len(keys) - i - 1):
        if keys[j] > keys[j + 1]:
            # Swap if the element found is greater than the next element
            keys[j], keys[j + 1] = keys[j + 1], keys[j]

# Create a new dictionary with sorted keys
sorted_data = {}
for key in keys:
    sorted_data[key] = data[key]

print(sorted_data)
