from lib.spaces_repository import SpacesRepository
from lib.spaces import Spaces


"""
When I call Spaces # all
I get all the Spaces from the Spaces table
"""
def test_all(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = SpacesRepository(db_connection)
    assert repository.all() == [
    Spaces(1,'Ocean Oasis', 'Small apartment in a big ocean',534, ["18-09-2024"], 1),
    Spaces(2,'River Retreat', 'The retreat on the river',71, ["14-09-2024","15-09-2024"], 2),
    Spaces(3,'Sea Shed', 'Not much more than a shed by the sea',33, ["19-09-2024"], 3),
    Spaces(4, 'Igloo', 'A cool place to chill out',101, [], 4),
    Spaces(5, 'Waterfall Windows', 'Do not sleep too close to the edge',1045, ["15-09-2024"], 1)
]    


"""
When I call #create 
I create a new space in the database
and I can see it back in #all
"""
def test_create(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = SpacesRepository(db_connection)
    space = Spaces(None, "test_name", "test_description", 9, [], 2)
    repository.create(space)  
    assert repository.all() == [
    Spaces(1,'Ocean Oasis', 'Small apartment in a big ocean',534, ["18-09-2024"], 1),
    Spaces(2,'River Retreat', 'The retreat on the river',71, ["14-09-2024","15-09-2024"], 2),
    Spaces(3,'Sea Shed', 'Not much more than a shed by the sea',33, ["19-09-2024"], 3),
    Spaces(4, 'Igloo', 'A cool place to chill out',101, [], 4),
    Spaces(5, 'Waterfall Windows', 'Do not sleep too close to the edge',1045, ["15-09-2024"], 1),
    Spaces(6, 'test_name', 'test_description', 9, [], 2)
]    

"""
When I call #find
I get an space based on the id
"""
def test_find(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = SpacesRepository(db_connection)
    space = repository.find(2)
    assert space == Spaces(2,'River Retreat', 'The retreat on the river',71, ["14-09-2024","15-09-2024"], 2)