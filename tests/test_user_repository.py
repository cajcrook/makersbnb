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
    User(1, 'user1', 'password1'),
    User(2, 'user2', 'password2'),
    User(3, 'user3', 'password3'),
    User(4, 'user4', 'password4')
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
    User(1, 'user1', 'password1'),
    User(2, 'user2', 'password2'),
    User(3, 'user3', 'password3'),
    User(4, 'user4', 'password4'),
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
    assert user == User(2, 'user2', 'password2')



