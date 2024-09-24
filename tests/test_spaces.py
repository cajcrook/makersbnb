from lib.spaces import Spaces

"""
Constructs an id, name, short_description, price_per_night, availability, user_id
"""
def test_construct():
    space = Spaces(1, "test_name", "test_description", 100, "01-09-2024", 2)
    assert space.id == 1
    assert space.name == "test_name"
    assert space.short_description == "test_description"
    assert space.price_per_night == 100
    assert space.dates == "01-09-2024"
    assert space.user_id == 2
    


"""
Spaces with equal contents are equal
"""
def test_compares():
    space_1 = Spaces(1, "test_name", "test_description", 100, "01-09-2024", 2)
    space_2 = Spaces(1, "test_name", "test_description", 100, "01-09-2024", 2)
    assert space_1 == space_2

"""
Spaces can be represented as strings
"""
def test_string():
        space = Spaces(1, "test_name", "test_description", 100, "01-09-2024", 2 )
        assert str(space) == "Spaces(1, test_name, test_description, 100, 01-09-2024, 2)"

