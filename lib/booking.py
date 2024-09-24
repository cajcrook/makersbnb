class Booking:
    def __init__(self, id, guest_id, start_date, approved, pending, space_id):
        self.id = id
        self.guest_id = guest_id
        self.start_date = start_date
        self.approved = approved
        self.pending = pending
        self.space_id = space_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Booking({self.id}, {self.guest_id}, {self.start_date}, {self.approved}, {self.pending}, {self.space_id})"



