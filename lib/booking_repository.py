from lib.booking import Booking

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * from bookings")
        bookings = []
        for row in rows:
            item = Booking(row["id"], row["guest_id"], row["start_date"], row["approved"] , row['pending'], row['space_id'])
            bookings.append(item)
        return bookings

    
    def create(self, booking):
        self._connection.execute(
            "INSERT INTO bookings (guest_id, start_date, approved , pending , space_id) VALUES (%s, %s, %s, %s, %s)",
            [booking.guest_id, booking.start_date, booking.approved , booking.pending, booking.space_id]
        )
        return None

    def find(self, booking_id):
        row = self._connection.execute("SELECT * FROM bookings WHERE id = %s", [booking_id])
        if row:
            return Booking(row[0]["id"], row[0]["guest_id"], row[0]["start_date"], row[0]["approved"], row[0]['pending'], row[0]['space_id'])
        return None
    
    def get_by_date(self, selected_date):
        rows = self._connection.execute(
            "SELECT * FROM bookings WHERE start_date = %s", [selected_date]
        )
        bookings = []
        for row in rows:
            item = Booking(row["id"], row["guest_id"], row["start_date"], row["approved"], row['pending'], row['space_id'])
            bookings.append(item)
        return bookings
    
    def find_and_approved(self, booking_id):
        self._connection.execute("UPDATE bookings SET approved = True , pending = False WHERE id = %s", [booking_id])
        return None
    
    def find_and_declines(self, booking_id):
        self._connection.execute("UPDATE bookings SET approved = False , pending = False WHERE id = %s", [booking_id])
        return None
            

