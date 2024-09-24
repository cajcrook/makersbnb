from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    response = page.goto(f"http://{test_web_address}/index")
    assert response.status == 200, f"Unexpected status code: {response.status}"
    p_tag = page.locator("p")
    expect(p_tag).to_have_text("Welcome     to WaterBnB")

def test_log_in_submit_succesful(page,test_web_address,db_connection):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill('input[name="username"]', 'anna123')
    page.fill('input[name="password"]', 'examplepassword')
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
    user_name = page.locator("p:has-text('Welcome')")
    expect(user_name).to_have_text('Welcome to your profile anna123')
    h1_host_header = page.locator("h1:has-text('Host')")
    expect(h1_host_header).to_have_text("Host")
    h3_owned_spaces = page.locator("h3:has-text('My properties')")
    expect(h3_owned_spaces).to_have_text("My properties")
    button_new_listings = page.locator("button:has-text('New Listings')")
    expect(button_new_listings).to_have_text("New Listings")    
    h3_approve_bookings = page.locator("h3:has-text('Approved Bookings')")
    expect(h3_approve_bookings).to_have_text("Approved Bookings")    
    h1_guest_header = page.locator("h1:has-text('Guest')")
    expect(h1_guest_header).to_have_text("Guest")
    h3_place_booking = page.locator("h3:has-text('Place a booking')")
    expect(h3_place_booking).to_have_text("Place a booking")
    button_place_booking = page.locator("button:has-text('Place a Booking')")
    expect(button_place_booking).to_have_text("Place a Booking")    
    h3_future_stays = page.locator("h3:has-text('Future Stays')")
    expect(h3_future_stays).to_have_text("Future Stays")

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
    page.fill('input[name="username"]', 'anna123')
    page.fill('input[name="password"]', 'newpassword')
    page.click('button[type="submit"]')
    assert page.text_content("body") == "Username already registered, Please come back and try again"

def test_no_spaces_listing(page, test_web_address, db_connection):
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/spaces.sql")
    response = page.goto(f"http://{test_web_address}/index/sign_up")
    assert response.status == 200, f"Unexpected status code: {response.status}"
    page.fill('input[name="username"]', 'newuser')
    page.fill('input[name="password"]', 'newpassword')    
    page.click('button[type="submit"]')
    page.wait_for_selector("p")
    user = page.locator("p")
    expect(user).to_have_text("Welcome to your profile\nnewuser")


def test_spaces_listing(page,test_web_address,db_connection):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill('input[name="username"]', 'joemumford')
    page.fill('input[name="password"]', 'examplepassword')
    page.click('button[type="submit"]')
    owned_spaces = page.locator("li:has-text('River Retreat')")
    expect(owned_spaces).to_have_text("River Retreat")

"""
We can render the bookings page
"""
def test_bookings_list_available_spaces(page, test_web_address, db_connection):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/index/1/bookings")
    title = page.locator("p:has-text('This is the bookings page!')")
    expect(title).to_have_text('This is the bookings page!')
    book_a_space = page.locator("h1:has-text('Book a Space')")
    expect(book_a_space).to_have_text('Book a Space')
    expect(book_a_space).to_be_visible()
    space_list = page.locator("h3:has-text('Available Spaces')")
    expect(space_list).to_have_text('Available Spaces')
    form = page.locator("form[action='/index/1/bookings']")
    expect(form).to_be_visible()
    form_title = page.locator("label:has-text('Choose a date:')")
    expect(form_title).to_have_text('Choose a date:')
    spaces_list_available = page.locator("ul")
    expect(spaces_list_available).to_be_visible()



def test_spaces_are_listed_correctly(page, test_web_address, db_connection):
    db_connection.seed("seeds/spaces.sql")
    page.goto(f"http://{test_web_address}/index/1/bookings")
    
    # Expect the correct number of spaces to be listed
    spaces = page.locator("li")
    print(spaces)
    expect(spaces).to_have_count(5)  # You have 5 spaces inserted into the DB

    space_1 = spaces.nth(0)
    space_2 = spaces.nth(1)
    space_3 = spaces.nth(2)
    space_4 = spaces.nth(3)
    space_5 = spaces.nth(4)

    expect(space_1).to_have_text('Ocean Oasis, Small apartment in a big ocean, 534')
    expect(space_2).to_have_text("River Retreat, The retreat on the river, 71")
    expect(space_3).to_have_text("Sea Shed, Not much more than a shed by the sea, 33")
    expect(space_4).to_have_text("Igloo, A cool place to chill out, 101")
    expect(space_5).to_have_text("Waterfall Windows, Do not sleep too close to the edge, 1045")
