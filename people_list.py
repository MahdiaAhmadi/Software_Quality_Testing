import re

class PeopleList:
    def __init__(self):
        self.people = []

    def add_person(self, name, email, phone):
        """Add a new person to the list."""
        if self.validate_person_data(name, email, phone):
            person_id = len(self.people) + 1
            self.people.append({'id': person_id, 'name': name, 'email': email, 'phone': phone})
            return person_id
        return None

    def remove_person(self, person_id):
        """Remove a person by their ID."""
        person = self.find_person(person_id)
        if person:
            self.people.remove(person)
            return True
        return False

    def see_all_people(self):
        """Display all people."""
        return self.people

    def find_person(self, person_id=None, name=None):
        """Find a person by ID or name."""
        for person in self.people:
            if person_id and person['id'] == person_id:
                return person
            if name and person['name'].lower() == name.lower():
                return person
        return None

    def validate_person_data(self, name, email, phone):
        """Validate the person's data (name, email, and phone)."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")
        if not self.validate_phone(phone):
            raise ValueError("Invalid phone number format.")
        return True

    def validate_email(self, email):
        """Validate email format."""
        return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email))

    def validate_phone(self, phone):
        """Validate phone number format (e.g., 10-15 digits with optional +)."""
        return bool(re.fullmatch(r"\+?\d{10,15}", phone))