class Spaces:
    def __init__(self, id, name, short_description, price_per_night, dates, user_id):
        self.id = id
        self.name = name
        self.short_description = short_description
        self.price_per_night = price_per_night
        self.dates = dates
        self.user_id = user_id
        
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Spaces({self.id}, {self.name}, {self.short_description}, {self.price_per_night}, {self.dates}, {self.user_id})"
    
