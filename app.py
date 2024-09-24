import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User
from lib.spaces_repository import SpacesRepository
from lib.spaces import Spaces
from lib.booking_repository import BookingRepository
from lib.image import Image
from lib.image_repository import ImageRepository
from datetime import datetime
from lib.booking import Booking
# Create a new Flask app
app = Flask(__name__)

# == INDEX route ==
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def post_index():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    username = request.form['username']
    password = request.form['password']
    user_list = repository.all()
    user = [user for user in user_list if user.username == username]
    if user == []:
        return "Login Failed", 401
    elif user[0].password == password:
        return redirect(f'/index/{user[0].id}')
    return "Login Failed", 401

# == User HOMEPAGE route ==
@app.route('/index/<int:id>', methods=['GET'])
def get_homepage(id):
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    user = user_repository.find(id)
    spaces_repository = SpacesRepository(connection)
    spaces_list = spaces_repository.all()
    bookingrepo = BookingRepository(connection)
    list_bookings = bookingrepo.all()
    #host lists preps
    owner_spaces = [space for space in spaces_list if space.user_id == id]
    owner_spaces_id = [space.id for space in spaces_list if space.user_id == user.id]
    owner_bookings = [booking for booking in list_bookings if booking.space_id in owner_spaces_id]
    pending_bookings = [booking for booking in owner_bookings if booking.pending == True]
    approved_bookings = [booking for booking in owner_bookings if booking.approved == True]
    #guest lists preps
    guest_bookings = [booking for booking in list_bookings if booking.guest_id == id]
    approved_guest_bookings = [booking for booking in guest_bookings if booking.approved == True]
    pending_guest_bookings = [booking for booking in guest_bookings if booking.pending == True]
    if user is None:
        return "user not found", 404
    return render_template('user_homepage.html', user=user , pending = pending_bookings , approved = approved_bookings, spaces = owner_spaces, guest_approved = approved_guest_bookings, guest_pending = pending_guest_bookings )

@app.route('/index/sign_up', methods = ['GET'])
def sign_up():
    return render_template('sign_up.html')

@app.route('/index/sign_up', methods = ['POST'])
def get_new_user():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    username = request.form['username']
    password =  request.form['password']
    new_user = User(None,username,password)
    users = user_repository.all()
    already_user = [user for user in users if user.username == username]
    if already_user == []:
        user_repository.create(new_user)
        users = user_repository.all()
        new_user_id = users[-1].id
        return redirect(f'/index/{new_user_id}')
    return 'Username already registered, Please come back and try again', 404

# == BOOKING route ==
@app.route('/index/<id>/bookings', methods=['GET'])
def get_bookings(id):
    connection = get_flask_database_connection(app)
    spaces_repository = SpacesRepository(connection)
    spaces = spaces_repository.all()
    booking_repository = BookingRepository(connection)
    booking = booking_repository.all()
    user_list = UserRepository(connection)
    user = user_list.find(id)
    return render_template('bookings.html',user = user ,booking=booking, spaces=spaces)

@app.route('/index/<id>/bookings', methods=['POST'])
def filter_bookings_by_date(id):
    connection = get_flask_database_connection(app)
    date_str = request.form['date']
    if date_str:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%d-%m-%Y')
        return redirect(f"/index/{id}/bookings/{formatted_date}")

@app.route('/index/<id>/bookings/<date>', methods=['GET'])
def filtered_bookings_by_date_page(id,date):
    connection = get_flask_database_connection(app)
    spaces_repository = SpacesRepository(connection)
    spaces = spaces_repository.all()
    spaces_available = [space for space in spaces if str(date) not in space.dates]
    return render_template('bookings_filtered.html', id = id , date = str(date) , spaces=spaces_available)
# == Space route ==


@app.route('/spaces/<int:id>', methods=['GET'])
def get_space(id):
    connection = get_flask_database_connection(app)
    spaces_repository = SpacesRepository(connection)
    spaces_list = spaces_repository.all()
    space_selected = [space for space in spaces_list if space.id == id]
    user_repository = UserRepository(connection)
    user_list = user_repository.all()
    image_repo = ImageRepository(connection)
    image_list = image_repo.all()
    image = [image for image in image_list if image.space_id == space_selected[0].id]
    if image == []:
        image = ['No image added']
    user = [ user for user in user_list if user.id == space_selected[0].user_id]
    return render_template("space.html",  space = space_selected[0] ,image= image[0], user = user[0] )

# new listing routes
@app.route('/index/<id>/new-listing', methods = ['GET'])
def get_new_listing_page(id):
    return render_template('new_listing.html', id=id)

@app.route('/index/<id>/new-listing', methods = ['POST'])
def create_new_listing(id):
    connection = get_flask_database_connection(app)
    spaces_repository = SpacesRepository(connection)
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    user_id = id
    date = '{}'
    new_space = Spaces(None, name, description, price, date, user_id)
    spaces_repository.create(new_space)

    image_repository = ImageRepository(connection)
    image_url = request.form.get('image')
    spaces_list = spaces_repository.all()
    space_id = spaces_list[-1].id
    new_image = Image(None, image_url, space_id)
    image_repository.create(new_image)
    
    print(new_space)
    return redirect(f'/index/{id}')

@app.route('/<id>/<date>/<space_id>/bookings/request', methods=['POST'])
def create_booking_request(id, date, space_id):
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    
    # Create a new booking instance
    new_booking = Booking(None, id, date, False, True, space_id)
    
    # Insert the new booking into the database
    booking_repo.create(new_booking)
    
    # Redirect to the user's homepage after creating the booking
    return redirect(f'/index/{id}')


@app.route('/index/<id>/update_space', methods = ['GET'])
def update_space(id):
    return render_template('in_development.html', id=id)

@app.route('/index/<id>/user_details', methods = ['GET'])
def get_worki_in_progress_page_user_details(id):
    return render_template('in_development.html', id=id)

@app.route('/index/<id>/approve_bookings', methods = ['GET'])
def approved_bookings_details_list(id):
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    user = user_repository.find(id)
    spaces_repository = SpacesRepository(connection)
    spaces_list = spaces_repository.all()
    bookingrepo = BookingRepository(connection)
    list_bookings = bookingrepo.all()
    owner_spaces = [space for space in spaces_list if space.user_id == int(id)]
    owner_spaces_id = [space.id for space in spaces_list if space.user_id == user.id]
    owner_bookings = [booking for booking in list_bookings if booking.space_id in owner_spaces_id]
    approved_bookings = [booking for booking in owner_bookings if booking.approved == True]
    approved_bookings_spaces_id = [booking.space_id for booking in approved_bookings]
    approved_bookings_spaces = [space for space in owner_spaces if space.id in approved_bookings_spaces_id ]
    
    #return f'{approved_bookings_spaces} /// {approved_bookings} /// {approved_bookings_spaces_id} //'
    return render_template('approved_details_bookings.html', spaces = approved_bookings_spaces , bookings = approved_bookings)




@app.route('/<id>/<bookingID>/approved_booking', methods=['POST'])
def approved_bookings(bookingID,id):
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    space_repo = SpacesRepository(connection)
    booking = booking_repo.find(bookingID)
    space_repo.add_unavailble_dates(booking.start_date,booking.space_id)
    booking_repo.find_and_approved(bookingID)
    return redirect(f'/index/{id}')

@app.route('/<id>/<bookingID>/declined_booking', methods = ['POST'])
def get_worki_in_progress_page_declined_bookings(id, bookingID):
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    booking_repo.find_and_declines(bookingID)
    return redirect(f'/index/{id}')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
