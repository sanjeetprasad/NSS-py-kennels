EMPLOYEES = [
    {
      "id": 1,
      "name": "Tom Bisop",
      "locationId": 1
    },
    {
      "id": 2,
      "name": "Jon Edward",
      "locationId": 2
    },
    {
      "id": 3,
      "name": "Jeremy Bakker",
      "locationId": 3
    },
    {
      "id": 4,
      "name": "Herry Parker",
      "locationId": 2
    },
    {
      "name": "Mango",
      "locationId": 2,
      "animalId": 4,
      "id": 5
    },
    {
      "name": "Hero",
      "locationId": 2,
      "animalId": 6,
      "id": 6
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