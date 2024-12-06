from lib.image import Image
from lib.image_repository import ImageRepository

"""
When I call # all, I get all images
"""
def test_image_all(db_connection):
    db_connection.seed("seeds/images.sql")
    repository = ImageRepository(db_connection)
    assert repository.all() == [
        Image(1, 'https://i.pinimg.com/originals/12/e5/e2/12e5e2ff898d74466e4be09d98d5c8bf.jpg',1),
        Image(2, 'https://mybestplace.com/uploads/2021/07/Drina-River-House-Serbia-COVER.jpg',2),
        Image(3, 'https://vwartclub.com/media/projects/6572/1.jpg',3),
        Image(4, 'https://wodnesprawy.pl/wp-content/uploads/2023/12/Wodne-Sprawy_27_2023-7.jpg',4),
        Image(5, 'https://thermohouse.co.uk/wp-content/uploads/2019/04/hero-image.jpg',5)
    ]


"""
When I call # create, 
I create a new image in the database
and I can see it back in # all
"""
def test_image_create(db_connection):
    db_connection.seed("seeds/images.sql")
    repository = ImageRepository(db_connection)
    image = Image(None, "https://www.guideoftheworld.com/wp-content/uploads/map/us_state_alaska_political_map.jpg", 3)
    repository.create(image)
    assert repository.all() == [
        Image(1, 'https://i.pinimg.com/originals/12/e5/e2/12e5e2ff898d74466e4be09d98d5c8bf.jpg',1),
        Image(2, 'https://mybestplace.com/uploads/2021/07/Drina-River-House-Serbia-COVER.jpg',2),
        Image(3, 'https://vwartclub.com/media/projects/6572/1.jpg',3),
        Image(4, 'https://wodnesprawy.pl/wp-content/uploads/2023/12/Wodne-Sprawy_27_2023-7.jpg',4),
        Image(5, 'https://thermohouse.co.uk/wp-content/uploads/2019/04/hero-image.jpg',5),
        Image(6, 'https://www.guideoftheworld.com/wp-content/uploads/map/us_state_alaska_political_map.jpg', 3)
    ]
