import pytest
from people_list import PeopleList

@pytest.fixture
def people_list():
    return PeopleList()

def test_add_person(people_list):
    # Test adding a person with valid data
    person_id = people_list.add_person("John Doe", "john.doe@example.com", "912345678", "PT")
    assert person_id == 1
    assert len(people_list.see_all_people()) == 1

    # Adding another valid person
    person_id = people_list.add_person("Jane Smith", "jane.smith@example.com", "11987654321", "BR")
    assert person_id == 2
    assert len(people_list.see_all_people()) == 2

def test_remove_person(people_list):
    # Test removing a person
    person_id = people_list.add_person("Jane Doe", "jane.doe@example.com", "912345678", "PT")
    assert people_list.remove_person(person_id)
    assert len(people_list.see_all_people()) == 0

def test_find_person(people_list):
    # Test finding a person by name
    person_id = people_list.add_person("John Doe", "john.doe@example.com", "11987654321", "BR")
    person = people_list.find_person(name="John Doe")
    assert person['name'] == "John Doe"
    assert person['email'] == "john.doe@example.com"

def test_validate_person_data(people_list):
    # Test valid and invalid data
    valid = people_list.validate_person_data("Alice Smith", "alice@example.com", "912345678", "PT")
    assert valid is True

    # Invalid email
    with pytest.raises(ValueError, match="Invalid email format."):
        people_list.validate_person_data("Bob", "invalid-email", "912345678", "PT")

    # Invalid phone number for Portugal
    with pytest.raises(ValueError, match="Invalid phone number format."):
        people_list.validate_person_data("Charlie", "charlie@example.com", "12345", "PT")

    # Invalid phone number for Brazil
    with pytest.raises(ValueError, match="Invalid phone number format."):
        people_list.validate_person_data("Diana", "diana@example.com", "987654321", "BR")

    # Invalid name
    with pytest.raises(ValueError, match="Name must be a non-empty string."):
        people_list.validate_person_data("", "david@example.com", "912345678", "PT")

def test_see_all_people(people_list):
    # Test viewing all people
    people_list.add_person("John Doe", "john.doe@example.com", "912345678", "PT")
    people_list.add_person("Jane Smith", "jane.smith@example.com", "11987654321", "BR")
    all_people = people_list.see_all_people()
    assert len(all_people) == 2
    assert all_people[0]['name'] == "John Doe"
    assert all_people[0]['country'] == "PT"
    assert all_people[1]['name'] == "Jane Smith"
    assert all_people[1]['country'] == "BR"