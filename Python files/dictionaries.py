person = {"name": "Alice", "age": 25}
print(person)

person = {"name": "Alice", "age": 25}
person["city"] = "New York"
print(person)

person = {"name": "Alice", "age": 25, "city": "New York"}
del person["city"]
print(person)

person = {"name": "Alice", "age": 25}
contact_info = {"email": "alice@example.com", "phone": "123-456-7890"}
person.update(contact_info)
print(person)

person = {"name": "Alice", "age": 25}
city = person.get("city", "Unknown")
print(city)
