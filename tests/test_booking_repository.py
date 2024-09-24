from lib.booking_repository import BookingRepository
from lib.booking import Booking


"""
When I call # all
I get all the Bookings
"""
def test_all(db_connection):
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    assert repository.all() == [
    Booking(1, 2, '14-09-2024', True, False, 2),
    Booking(2, 1, '17-09-2024', False, True, 2),
    Booking(3, 4, '18-09-2024', True, False, 1),
    Booking(4, 4, '14-09-2024', False, True, 4),
    Booking(5, 1, '19-09-2024', False, True, 3),
    Booking(6, 3, '15-09-2024', True, False, 2),
    Booking(7, 2, '12-09-2024', False, True, 1)
    ]

"""
When I call #create
I create a new booking in the database
and I can see it back in #all
"""
def test_create(db_connection):
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    booking = Booking(None, 0000, "00-00-0000", True, False, 3)
    repository.create(booking)
    assert repository.all() == [
    Booking(1, 2, '14-09-2024', True, False, 2),
    Booking(2, 1, '17-09-2024', False, True, 2),
    Booking(3, 4, '18-09-2024', True, False, 1),
    Booking(4, 4, '14-09-2024', False, True, 4),
    Booking(5, 1, '19-09-2024', False, True, 3),
    Booking(6, 3, '15-09-2024', True, False, 2),
    Booking(7, 2, '12-09-2024', False, True, 1),
    Booking(8, 0000, "00-00-0000", True, False, 3)
    ]


"""
When I call #find
I get an Booking based on the id
"""
def test_find(db_connection):
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    booking = repository.find(2)
    assert booking == Booking(2, 1, '17-09-2024', False, True, 2)




