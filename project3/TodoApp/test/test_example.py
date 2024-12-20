import pytest

def test_equal_or_not_equal():
    assert 3 == 3
    assert 3 !=1
    

def test_is_instance():
    assert isinstance('this is a string', str)
    assert  not isinstance('10', int)

def test_boolean():
    validated = True
    assert validated is True
    assert ('hello' == 'world') is False
    
def test_type():
    assert type('hello' is str)
    assert type('world' is not int)

def test_greater_and_less_than():
    assert 7 > 3
    assert 5 < 6

def test_list():
    num_list = [1,2,3,4,5]
    any_list=[False, False]

    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list )
    assert not any(any_list)



class Student:
    def __init__(self,first_name: str, last_name: str, major: str, years: int):
        self.first_name = first_name
        self.last_name=last_name
        self.major = major
        self.years = years

# def test_person_initialization():
#     p = Student('Preeti','Boddeti','CSE',3)
#     assert p.first_name == 'Preeti','First name should be Preeti'
#     assert p.last_name == 'Boddeti','Last name should be Boddeti'
#     assert p.major == 'CSE'
#     assert p.years == 3


# can work only if pytest is imported
@pytest.fixture
def default_employee():
    return Student('Preeti','Boddeti','CSE',3)

def test_person_initialization(default_employee):
    assert default_employee.first_name == 'Preeti','First name should be Preeti'
    assert default_employee.last_name == 'Boddeti','Last name should be Boddeti'
    assert default_employee.major == 'CSE'
    assert default_employee.years == 3
    