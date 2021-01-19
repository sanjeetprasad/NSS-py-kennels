import sqlite3
import json
from models import Location


# LOCATIONS = [
#     {
#       "id": 1,
#       "name": "Nashville North",
#       "address": "8422 Johnson Pike",
#       "status": "Ready for discharge"
#     },
#     {
#       "id": 2,
#       "name": "Nashville South",
#       "address": "209 Emory Drive",
#       "status": "Ready for discharge"
#     },
#     {
#       "id": 3,
#       "name": "Nashville East",
#       "address": "209 Emory Drive",
#       "status": "Ready for discharge"
#     }
# ]

def get_all_locations():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
            
        FROM location l
        """)

        # Initialize an empty list to hold all animal representations
        locations = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(locations)

  # Function with a single parameter
def get_single_location(id):
    # # Variable to hold the found animal, if it exists
    # requested_location = None

    # # Iterate the ANIMALS list above. Very similar to the
    # # for..of loops you used in JavaScript.
    # for location in LOCATIONS:
    #     # Dictionaries in Python use [] notation to find a key
    #     # instead of the dot notation that JavaScript used.
    #     if location["id"] == id:
    #         requested_location = location

    # return requested_location 

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        WHERE l.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        location = Location(data['id'], data['name'], data['address'])
                            

        return json.dumps(location.__dict__)

def create_location(location):

    max_id = LOCATIONS[-1]["id"]

    new_id = max_id + 1

    location["id"] = new_id

    LOCATIONS.append(location)

    return location


def delete_location(id):
    # Initial -1 value for animal index, in case one isn't found
    location_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the animal. Store the current index.
            location_index = index

    # If the animal was found, use pop(int) to remove it from list
    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the animal. Update the value.
            LOCATIONS[index] = new_location
            break            