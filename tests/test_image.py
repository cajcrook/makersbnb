from lib.image import Image
from lib.image_repository import ImageRepository

"""
Constructs an id, image_url and space_id
"""
def test_image_construction():
    image = Image(6, "https://www.guideoftheworld.com/wp-content/uploads/map/us_state_alaska_political_map.jpg", 3)
    assert image.id == 6
    assert image.image_url == "https://www.guideoftheworld.com/wp-content/uploads/map/us_state_alaska_political_map.jpg"
    assert image.space_id == 3

"""
Images with equal contents are equal
"""
def test_image_comparison():
    image_1 = Image(6, "https://www.guideoftheworld.com/wp-content/uploads/map/us_state_alaska_political_map.jpg", 3)
    image_2 = Image(6, "https://www.guideoftheworld.com/wp-content/uploads/map/us_state_alaska_political_map.jpg", 3)
    assert image_1 == image_2

"""
Image information can be represented as a string
"""
def test_image_info_string():
    image = Image(6, "https://www.guideoftheworld.com/wp-content/uploads/map/us_state_alaska_political_map.jpg", 3)
    assert str(image) == "Image(6, https://www.guideoftheworld.com/wp-content/uploads/map/us_state_alaska_political_map.jpg, 3)"