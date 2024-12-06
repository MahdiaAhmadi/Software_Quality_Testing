# Quality in Software Management

## 1. Read the CHAPTER 5- Software Testing from Guide to the Software Engineering Body of Knowledge v4.0- SWEBOK- v4.0

## 2. Read the OWASP Application Security Verification Standard (ASVS)

## 3. Develop a simple application, with at least 5 functions

### Purpose of the Application

> The app is essentially a small contact management system with built-in validation. It's useful in contexts like:

- Storing and managing a directory of contacts.
- Ensuring that all data entered into the system adheres to specific formats, especially for phone numbers.
- Quickly searching for and modifying stored information about individuals.

### Application Functionalities

- Add a Person:
  Add a new person to the list with validated name, email, phone, and country, assigning them a unique ID.

- Remove a Person:
  Remove a person from the list using their unique ID.

- View All People:
  Display all stored people along with their details (id, name, email, phone, and country).

- Find a Person:
  Search for a person by their unique ID or name (case-insensitive).

- Validate Input Data:
  Ensure data integrity by validating name, email, and phone based on the specified country format.

## 4. Create unit tests for each of the application’s functions and execute both of them (generate an XML with the Test Execution Result)

> the test of each function is done in the test_people_list.py file.

## 5. ASVS Requirement that I choose

>

    5.1.4 - Verify that structured data is strongly typed and validated against a defined schema including allowed characters, length and pattern (e.g. credit card numbers, e-mail addresses, telephone numbers, or validating that two related fields are reasonable, such as checking that suburb and zip/postcode match).
