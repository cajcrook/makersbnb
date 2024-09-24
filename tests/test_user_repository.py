from lib.user_repository import UserRepository
from lib.user import User


"""
When I call # all
I get all the Users
"""
def test_all(db_connection):
    db_connection.seed("seeds/users.sql")
    repository = UserRepository(db_connection)
    assert repository.all() == [
    User(1, 'anna123', 'examplepassword'),
    User(2, 'joemumford', 'examplepassword'),
    User(3, 'oliviamotte', 'examplepassword'),
    User(4, 'josephinerichard', 'examplepassword2')
    ]    
                                  
"""
When I call #create 
I create a new space in the database
and I can see it back in #all
"""
def test_create(db_connection):
    db_connection.seed("seeds/users.sql")
    repository = UserRepository(db_connection)
    user = User(None, "test_username", "test_password")
    repository.create(user)  
    assert repository.all() == [
    User(1, 'anna123', 'examplepassword'),
    User(2, 'joemumford', 'examplepassword'),
    User(3, 'oliviamotte', 'examplepassword'),
    User(4, 'josephinerichard', 'examplepassword2'),
    User(5, 'test_username', 'test_password')
    ]    


"""
When I call #find
I get an user based on the id
"""
def test_find(db_connection):
    db_connection.seed("seeds/users.sql")
    repository = UserRepository(db_connection)
    user = repository.find(2)
    assert user == User(2, 'joemumford', 'examplepassword')



