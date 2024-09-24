from lib.image import Image

class ImageRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * from images")
        images = []
        for row in rows:
            item = Image(row["id"], row["image_url"], row["space_id"])
            images.append(item)
        return images
    
    def create(self, image):
        self._connection.execute(
            "INSERT INTO images (image_url, space_id) VALUES (%s, %s)",
            [image.image_url, image.space_id])
    
    