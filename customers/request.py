CUSTOMERS = [
    {
      "email": "sanjeet.p@gmail.com",
      "password": "sanjeet123",
      "name": "sanjeet prasad",
      "id": 1
    },
    {
      "email": "jayna@gmail.com",
      "password": "123456",
      "name": "Jayna Leitze",
      "id": 2
    },
    {
      "email": "alice@gmail.com",
      "password": "123456",
      "name": "Alice Nie",
      "id": 3
    }
]

def get_all_customers():
      return CUSTOMERS

  # Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer  