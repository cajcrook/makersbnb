from lib.spaces import Spaces


class SpacesRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        # Execute the query
        cursor = self._connection.execute("SELECT * FROM spaces")

        # Process rows one at a time
        spaces_list = []
        for row in cursor:
            dates = row["dates"]
            if isinstance(dates, str):
                # Convert PostgreSQL string array format to Python list
                dates = dates.strip('{}').split(',')
                dates = [date.strip() for date in dates]  # Clean up any extra whitespace

            spaces_list.append(Spaces(row["id"], row["name"], row["short_description"], row["price_per_night"], dates, row["user_id"]))

        return spaces_list

    def add_unavailble_dates(self,date,id):
        self._connection.execute('UPDATE spaces SET dates = array_append(dates , %s) where id= %s',[date,id])
        return None


    def create(self, spaces):
        dates = spaces.dates if spaces.dates else '{}'
        self._connection.execute("INSERT INTO spaces (name, short_description, price_per_night, dates, user_id) VALUES (%s, %s, %s, %s, %s)",
                                 [spaces.name, spaces.short_description, spaces.price_per_night,dates, spaces.user_id])
        return None


    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE id = %s', [id])
        row = rows[0]
        return Spaces(row["id"], row["name"], row["short_description"], row["price_per_night"], row["dates"], row["user_id"])
    