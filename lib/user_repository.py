from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * from users")
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["password"])
            users.append(item)
        return users

    
    def create(self, user):
        self._connection.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            [user.username, user.password]
        )
        return None

    def find(self, user_id):
        row = self._connection.execute("SELECT * FROM users WHERE id = %s", [user_id])
        if row:
            return User(row[0]["id"], row[0]["username"], row[0]["password"])
        return None
    
    def find_by_username(self, username):
        row = self._connection.execute("SELECT * FROM users WHERE username = %s", [username])
        if row:
            return User(row[0]["id"], row[0]["username"], row[0]["password"])
        return None