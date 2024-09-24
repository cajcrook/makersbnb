from lib.booking import Booking

"""
Constructs an id, guest_id, start_date, approved 
"""
def test_construct():
    booking = Booking(1, "guest_id", "start_date", True, False, 1)
    assert booking.id == 1
    assert booking.guest_id == "guest_id"
    assert booking.start_date == "start_date"
    assert booking.approved == True
    assert booking.pending == False
    assert booking.space_id == 1


"""
bookings with equal contents are equal
"""

def test_compares():
    booking_1 = Booking(1, "guest_id", "start_date", True, False, 1)
    booking_2 = Booking(1, "guest_id", "start_date", True, False, 1)
    assert booking_1 ==  booking_2

"""
bookings can be represented as strings
"""
def test_string():
        booking = Booking(1, "guest_id", "start_date", True, False, 1)
        assert str(booking) == "Booking(1, guest_id, start_date, True, False, 1)"


