class Image:
    def __init__(self, id, image_url, space_id):
        self.id = id
        self.image_url = image_url
        self.space_id = space_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Image({self.id}, {self.image_url}, {self.space_id})"