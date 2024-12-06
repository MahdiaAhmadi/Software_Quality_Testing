import re

class PeopleList:
    def __init__(self):
        self.people = []

    def add_person(self, name, email, phone, country):
        """Add a new person to the list with country-based phone validation."""
        if self.validate_person_data(name, email, phone, country):
            person_id = len(self.people) + 1
            self.people.append({'id': person_id, 'name': name, 'email': email, 'phone': phone, 'country': country})
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

    def validate_person_data(self, name, email, phone, country):
        """Validate the person's data (name, email, phone)."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")
        if not self.validate_phone(phone, country):
            raise ValueError("Invalid phone number format.")
        return True

    def validate_email(self, email):
        """Validate email format."""
        return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email))

    def validate_phone(self, phone, country):
        """Validate phone number (specifically mobile phone numbers) based on the country."""
        country_formats = {
            "US": r"^\d{10}$",  # US phone numbers are 10 digits long
            "IN": r"^[789]\d{9}$",  # Indian phone numbers must start with 7, 8, or 9 and have 10 digits
            "UK": r"^07\d{9}$",  # UK mobile numbers start with 07 and have 10 digits
            "FR": r"^0[1-9]\d{8}$",  # French numbers start with 0 and have 9 digits
            "PT": r"^9[1236]\d{7}$",  # Portuguese mobile numbers
            "BR": r"^\d{2}9\d{8}$",  # Brazilian mobile numbers (e.g., 11987654321)
        }

        if country not in country_formats:
            raise ValueError(f"Phone number validation for {country} is not supported.")

        pattern = country_formats[country]
        return bool(re.fullmatch(pattern, phone))