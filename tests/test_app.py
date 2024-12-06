from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    response = page.goto(f"http://{test_web_address}/index")
    assert response.status == 200, f"Unexpected status code: {response.status}"
    # p_tag = page.locator("p")
    # expect(p_tag).to_have_text("Welcome     to WaterBnB")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Welcome to MakersBnB")



def test_log_in_submit_succesful(page,test_web_address,db_connection):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill('input[name="username"]', 'user1')
    page.fill('input[name="password"]', 'password1')
    page.click('button[type="submit"]')
    assert page.url == f"http://{test_web_address}/index/1"



def test_log_in_submit_unsuccesful(page,test_web_address,db_connection):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill('input[name="username"]', 'wrong_user')
    page.fill('input[name="password"]', 'wrongpassword')
    page.click('button[type="submit"]')
    assert page.text_content("body") == "Login Failed"

"""
We can render the homepage
"""
def test_get_homepage(page, test_web_address, db_connection):
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/spaces.sql")
    response = page.goto(f"http://{test_web_address}/index/1")
    assert response.status == 200, f"Unexpected status code: {response.status}"
    h1_welcome = page.locator("h1:has-text('Welcome')")
    expect(h1_welcome).to_have_text('Welcome')
    h2_username = page.locator("h2:has-text('user1')")
    expect(h2_username).to_have_text("user1")
    h2_hosting = page.locator("h2:has-text('Hosting')")
    expect(h2_hosting).to_have_text("Hosting")
    button_new_listings = page.locator("button:has-text('New Listing')")
    expect(button_new_listings).to_have_text("New Listing")    
    h3_approved_bookings = page.locator("h3:has-text('Approved Bookings')")
    expect(h3_approved_bookings).to_have_text("Approved Bookings")    
    # h1_guest_header = page.locator("h1:has-text('Guest')")
    # expect(h1_guest_header).to_have_text("Guest")
    # h3_place_booking = page.locator("h3:has-text('Place a booking')")
    # expect(h3_place_booking).to_have_text("Place a booking")
    # button_place_booking = page.locator("button:has-text('Place a Booking')")
    # expect(button_place_booking).to_have_text("Place a Booking")    
    # h3_future_stays = page.locator("h3:has-text('Future Stays')")
    # expect(h3_future_stays).to_have_text("Future Stays")

def test_sign_up_new_user(page, test_web_address,db_connection):
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/spaces.sql")
    response = page.goto(f"http://{test_web_address}/index/sign_up")
    assert response.status == 200, f"Unexpected status code: {response.status}"
    page.fill('input[name="username"]', 'newuser')
    page.fill('input[name="password"]', 'newpassword')
    page.click('button[type="submit"]')
    assert page.url == f"http://{test_web_address}/index/5"# 5 as the user database initally got 4 users so new one should always be 5th

def test_failed_sign_up(page, test_web_address,db_connection):
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/spaces.sql")
    response = page.goto(f"http://{test_web_address}/index/sign_up")
    assert response.status == 200, f"Unexpected status code: {response.status}"
    page.fill('input[name="username"]', 'user1')
    page.fill('input[name="password"]', 'password1')
    page.click('button[type="submit"]')
    assert page.text_content("h2") == "Username already exists please try again"

# def test_new_user_signs_up(page, test_web_address, db_connection):
#     db_connection.seed("seeds/users.sql")
#     db_connection.seed("seeds/spaces.sql")
#     response = page.goto(f"http://{test_web_address}/index/sign_up")
#     assert response.status == 200, f"Unexpected status code: {response.status}"
#     page.fill('input[name="username"]', 'user6')
#     page.fill('input[name="password"]', 'password6')    
#     page.click('button[type="submit"]')
#     page.wait_for_selector("h2")
#     user = page.locator("h2")
#     expect(user).to_have_text("user6")


def test_spaces_listing(page,test_web_address,db_connection):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill('input[name="username"]', 'user2')
    page.fill('input[name="password"]', 'password2')
    page.click('button[type="submit"]')
    owned_spaces = page.locator("li:has-text('River Retreat')")
    expect(owned_spaces).to_have_text("River Retreat")

"""
We can render the bookings page
"""
def test_bookings_list_available_spaces(page, test_web_address, db_connection):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/index/1/bookings")
    title = page.locator("h2:has-text('Book a Space')")
    expect(title).to_have_text('Book a Space')
    form_title = page.locator("label:has-text('Choose a date:')")
    expect(form_title).to_have_text('Choose a date:')
    # book_a_space = page.locator("h1:has-text('Book a Space')")
    # expect(book_a_space).to_have_text('Book a Space')
    # expect(book_a_space).to_be_visible()
    # space_list = page.locator("h3:has-text('Available Spaces')")
    # expect(space_list).to_have_text('Available Spaces')
    # form = page.locator("form[action='/index/1/bookings']")
    # expect(form).to_be_visible()
    # spaces_list_available = page.locator("ul")
    # expect(spaces_list_available).to_be_visible()
    # button_view_space = page.locator("button:has-text('View')")
    # expect(button_view_space).to_have_text("View")    



def test_spaces_are_listed_correctly(page, test_web_address, db_connection):
    db_connection.seed("seeds/spaces.sql")
    page.goto(f"http://{test_web_address}/index/1/bookings")
    spaces = page.locator("li")
    print(spaces)
    expect(spaces).to_have_count(5) 
    space_1 = spaces.nth(0)
    space_2 = spaces.nth(1)
    space_3 = spaces.nth(2)
    space_4 = spaces.nth(3)
    space_5 = spaces.nth(4)
    expect(space_1).to_have_text('Ocean Oasis Small apartment in a big ocean £534 View')
    expect(space_2).to_have_text("River Retreat The retreat on the river £71 View")
    expect(space_3).to_have_text("Sea Shed Not much more than a shed by the sea £33 View")
    expect(space_4).to_have_text("Igloo A cool place to chill out £101 View")
    expect(space_5).to_have_text("Waterfall Windows Do not sleep too close to the edge £1045 View")
