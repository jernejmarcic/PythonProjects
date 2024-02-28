import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from collections import Counter

data = {
    "Pia's_number": list(range(1, 109)),
    "Address": [
        'Slovenska cesta 34, 1000 Ljubljana', 'Čopova ulica 42, 1000 Ljubljana', 'Čopova ulica 40, 1000 Ljubljana',
        'Čopova ulica 38, 1000 Ljubljana', 'Čopova ulica 38, 1000 Ljubljana', 'Čopova ulica 14, 1000 Ljubljana',
        'Čopova ulica 12, 1000 Ljubljana', 'Čopova ulica 2, 1000 Ljubljana', 'Slovenska cesta 32, 1101 Ljubljana',
        'Čopova ulica 9, 1000 Ljubljana', 'Čopova ulica 5, 1000 Ljubljana', 'Čopova ulica 3, 1520 Ljubljana',
        'Čopova ulica 1, 1000 Ljubljana', 'Mestni trg 26, 1000 Ljubljana', 'Mestni trg 25, 1000 Ljubljana',
        'Mestni trg 24, 1000 Ljubljana', 'Mestni trg 24, 1000 Ljubljana', 'Mestni trg 23, 1000 Ljubljana',
        'Mestni trg 22, 1000 Ljubljana', 'Mestni trg 21, 1000 Ljubljana', 'Mestni trg 20, 1000 Ljubljana',
        'Mestni trg 19, 1000 Ljubljana', 'Mestni trg 18, 1000 Ljubljana', 'Mestni trg 17, 1000 Ljubljana',
        'Mestni trg 16, 1000 Ljubljana', 'Mestni trg 15, 1000 Ljubljana', 'Mestni trg 14, 1000 Ljubljana',
        'Mestni trg 1, 1000 Ljubljana', 'Mestni trg 2, 1000 Ljubljana', 'Mestni trg 3, 1000 Ljubljana',
        'Mestni trg 4, 1000 Ljubljana', 'Mestni trg 5, 1000 Ljubljana', 'Mestni trg 6, 1000 Ljubljana',
        'Mestni trg 7, 1000 Ljubljana', 'Mestni trg 8, 1000 Ljubljana', 'Mestni trg 9, 1000 Ljubljana',
        'Mestni trg 10, 1000 Ljubljana', 'Mestni trg 11, 1000 Ljubljana', 'Mestni trg 12, 1000 Ljubljana',
        'Mestni trg 13, 1000 Ljubljana', 'Stari trg 1, 1000 Ljubljana', 'Stari trg 5, 1000 Ljubljana',
        'Stari trg 7, 1000 Ljubljana', 'Stari trg 9, 1000 Ljubljana', 'Stari trg 11, 1000 Ljubljana',
        'Stari trg 13, 1000 Ljubljana', 'Stari trg 15, 1000 Ljubljana', 'Stari trg 17, 1000 Ljubljana',
        'Stari trg 17, 1000 Ljubljana', 'Stari trg 19, 1000 Ljubljana', 'Stari trg 2, 1000 Ljubljana',
        'Stari trg 4, 1000 Ljubljana', 'Stari trg 6, 1000 Ljubljana', 'Stari trg 8, 1000 Ljubljana',
        'Stari trg 28, 1000 Ljubljana', 'Stari trg 30, 1000 Ljubljana', 'Stari trg 30, 1000 Ljubljana',
        'Stari trg 34, 1000 Ljubljana', 'Gornji trg 2, 1000 Ljubljana', 'Gornji trg 4, 1000 Ljubljana',
        'Gornji trg 6, 1000 Ljubljana', 'Gornji trg 8, 1000 Ljubljana', 'Gornji trg 10, 1000 Ljubljana',
        'Gornji trg 12, 1000 Ljubljana', 'Gornji trg 14, 1000 Ljubljana', 'Gornji trg 16, 1000 Ljubljana',
        'Gornji trg 18, 1000 Ljubljana', 'Gornji trg 20, 1000 Ljubljana', 'Gornji trg 28, 1000 Ljubljana',
        'Gornji trg 30, 1000 Ljubljana', 'Gornji trg 1, 1000 Ljubljana', 'Gornji trg 3, 1000 Ljubljana',
        'Gornji trg 5, 1000 Ljubljana', 'Gornji trg 7, 1000 Ljubljana', 'Gornji trg 9, 1000 Ljubljana',
        'Gornji trg 11, 1000 Ljubljana', 'Gornji trg 13, 1000 Ljubljana', 'Gornji trg 15, 1000 Ljubljana',
        'Gornji trg 17, 1000 Ljubljana', 'Gornji trg 19, 1000 Ljubljana', 'Gornji trg 21, 1000 Ljubljana',
        'Gornji trg 23, 1000 Ljubljana', 'Gornji trg 25, 1000 Ljubljana'
    ],
   # "Name": [
   #     'Best Western Premier Hotel Slon', 'H&M', 'Müller', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None
   # ],
    "Land_Use": [
        "0b / 1-5d", "0b / 1-3b", "0b / 1-3b", "0bd / 1-3d", "0b / 1-5f", "0bc/ 1-5f", "0ac / 1/2ac", "0-2f",
        "0-4f", "0cb / 1/2f", "0b / 1/2f", "0/1abe / 2/3f", "0ab / 1-3f", "Ob / 1/2f", "Ob / 1/2f", "Oab / 1/2f",
        "O/1b / 2-4f", "0-4e", "0/1a / 2/3f", "0/1a / 2/3f", "0a / 1-3f", "0c / 1-3f", "0c / 1-3fg", "0ab / 1e / 2/3fg",
        "0c / 1-3e", "0-3d", "0-3f", "0-3e", "0a / 2/3g", "0c / 1e / 2/3f", "0a / 1-3g", "0ab / 1-3g", "0ab / 1/2g",
        "0a / 1-3f", "0ab / 1-3g", "0bc / 1/2e", "0a / 1/2g", "0a / 1/2g", "0a / 1-3g", "0b / 1/2f", "0a / 1/2f",
        "0a / 1/2g", "0c / 1/2g", "0c / 1/2g", "0ab / 1/2f", "0bc / 1/2g", "0ac / 1/2g", "0c / 1/2g", "0c / 1/2g",
        "0a / 1/2f", "0af / 1-3f", "0b / 1-3f", "0c / 1/2g", "0a / 1/2g", "missing", "0a / 1-3g", "0a / 1-3g",
        "0a / 1-3f", "0a / 1-3g", "0a / 1-3g", "0a / 1-3g", "0a / 1-3g", "0a / 1-3f", "0c / 1-3g", "missing",
        "0-2e", "0-2f", "0 / 1d", "0 / 1d", "0 / 1f", "0ac / 1/2f", "0a / 1/2g", "0a / 1/2g", "0-4e", "0c / 1/2g",
        "0-2f", "0 / 1g", "0 / 1g", "0c / 1g", "0 / 1f", "0 / 1f", "0 / 1g", "0 / 1g", "0 / 1c", "0 / 9", "0a / 1/2g",
        "0a / 1/2g", "0-2d", "0-2g", "0-2d", "0a / 1/2g", "0a / 1-3g", "0-3f", "0c / 1-3g", "0a / 1/2f", "0a / 1/2g",
        "0-2e", "0c / 1/2f", "0-2e", "0-3g", "0-2g", "0c / 1/2g", "0-2g", "0-2g"
    ]
}

land_use_counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}

# Function to parse and count land use types
def parse_and_count_land_use(land_uses, counts):
    for land_use in land_uses:
        for char in land_use:
            if char in counts:
                counts[char] += 1

# Iterate over the land use data and parse each entry
for land_use_entry in data['Land_Use']:
    if land_use_entry is not None:  # Skip 'missing' entries
        # Splitting each entry by '/' to handle multiple uses in one entry
        land_uses = land_use_entry.replace(' ', '').split('/')
        parse_and_count_land_use(land_uses, land_use_counts)

print(land_use_counts)

def count_total_land_use(land_use_data):
    counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}

    def parse_and_count(land_uses):
        for land_use in land_uses:
            for char in land_use:
                if char in counts:
                    counts[char] += 1

    for entry in land_use_data:
        if entry is not None:
            land_uses = entry.replace(' ', '').split('/')
            parse_and_count(land_uses)

    return counts

def land_use_by_street(addresses, land_use_data):
    street_counts = {}

    def parse_and_count(land_uses, street):
        if street not in street_counts:
            street_counts[street] = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
        for land_use in land_uses:
            for char in land_use:
                if char in street_counts[street]:
                    street_counts[street][char] += 1

    for address, land_use in zip(addresses, land_use_data):
        if land_use is not None:
            street = address.split(',')[0]  # Extracting the street name
            land_uses = land_use.replace(' ', '').split('/')
            parse_and_count(land_uses, street)

    return street_counts

total_counts = count_total_land_use(data['Land_Use'])
print("Total Land Use Counts:", total_counts)

street_counts = land_use_by_street(data['Address'], data['Land_Use'])
print("\nLand Use Counts by Street:")
for street, counts in street_counts.items():
    print(f"{street}: {counts}")

# Initialize a dictionary to hold combined land use counts for each street
combined_street_data = {}

# Iterate over each address and its corresponding land use data
for address, land_use in zip(data["Address"], data["Land_Use"]):
    # Extract the street name from the address
    street_name = ' '.join(address.split()[:2])

    # Initialize the street in the combined data if not already present
    if street_name not in combined_street_data:
        combined_street_data[street_name] = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}

    # Parse the land use data for the current address
    land_use_counts = parse_land_use(land_use)

    # Add the counts to the combined data for the street
    for land_use_type, count in land_use_counts.items():
        combined_street_data[street_name][land_use_type] += count

# Define a function to parse land use strings into count dictionaries
def parse_land_use(land_use_string):
    # Initialize a dictionary to hold counts of each land use type
    counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}

    # Process the land use string to update counts
    # Implement logic here based on how land use data is structured in the string
    # For example, if 'land_use_string' is "0b / 1-3d", you would increment counts['b'] and counts['d']

    return counts

# Print or further process the combined street data
for street, counts in combined_street_data.items():
    print(f"{street}: {counts}")


