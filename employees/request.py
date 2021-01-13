EMPLOYEES = [
    {
      "id": 1,
      "name": "Tom Bisop",
      "locationId": 1,
      "status": "Ready for delever"
    },
    {
      "id": 2,
      "name": "Jon Edward",
      "locationId": 2,
      "status": "Ready for delever"
    },
    {
      "id": 3,
      "name": "Jeremy Bakker",
      "locationId": 3,
      "status": "Ready for delever"
    },
    {
      "id": 4,
      "name": "Herry Parker",
      "locationId": 2,
      "status": "Ready for delever"
    },
    {
      "name": "Mango",
      "locationId": 2,
      "animalId": 4,
      "id": 5,
      "status": "Ready for delever"
    },
    {
      "name": "Hero",
      "locationId": 2,
      "animalId": 6,
      "id": 6,
      "status": "Ready for delever"
    }
]

def get_all_employees():
      return EMPLOYEES

  # Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee  

def create_employee(employee):

    # get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    #add 1 to whatever the last number is
    new_id = max_id + 1

    # Add an "id" property to the employee dictionary
    employee["id"] = new_id

    #Add the animal dictionary to the list
    EMPLOYEES.append(employee)

    #return the dictionary with 'id' property added

    return employee

def delete_employee(id):
    # Initial -1 value for animal index, in case one isn't found
    employee_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the animal. Store the current index.
            employee_index = index

    # If the animal was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the animal. Update the value.
            EMPLOYEES[index] = new_employee
            break            
