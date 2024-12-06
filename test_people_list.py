import pytest
from people_list import PeopleList

@pytest.fixture
def people_list():
    return PeopleList()

def test_add_person(people_list):
    # Test adding a person
    person_id = people_list.add_person("John Doe", "john.doe@example.com", "+1234567890")
    assert person_id == 1
    assert len(people_list.see_all_people()) == 1

def test_remove_person(people_list):
    # Test removing a person
    person_id = people_list.add_person("Jane Doe", "jane.doe@example.com", "+9876543210")
    assert people_list.remove_person(person_id)
    assert len(people_list.see_all_people()) == 0

def test_find_person(people_list):
    # Test finding a person by name
    person_id = people_list.add_person("John Doe", "john.doe@example.com", "+1234567890")
    person = people_list.find_person(name="John Doe")
    assert person['name'] == "John Doe"
    assert person['email'] == "john.doe@example.com"

def test_validate_person_data(people_list):
    # Test valid and invalid data
    valid = people_list.validate_person_data("Alice Smith", "alice@example.com", "+1122334455")
    assert valid == True

    with pytest.raises(ValueError, match="Invalid email format."):
        people_list.validate_person_data("Bob", "invalid-email", "+1234567890")
    
    with pytest.raises(ValueError, match="Invalid phone number format."):
        people_list.validate_person_data("Charlie", "charlie@example.com", "123")
    
    with pytest.raises(ValueError, match="Name must be a non-empty string."):
        people_list.validate_person_data("", "david@example.com", "+1234567890")

def test_see_all_people(people_list):
    # Test viewing all people
    people_list.add_person("John Doe", "john.doe@example.com", "+1234567890")
    people_list.add_person("Jane Doe", "jane.doe@example.com", "+9876543210")
    all_people = people_list.see_all_people()
    assert len(all_people) == 2
    assert all_people[0]['name'] == "John Doe"
    assert all_people[1]['name'] == "Jane Doe"