from model import User, Reservation, db, connect_to_db
from data import times

def create_user(email):
    """Create and return a new user."""

    user = User( 
                email=email,
                )

    return user

def create_reservation(user_id, date, time):
    """Create Reservation"""
    reservation = Reservation(
        user_id = user_id,
        date = date,
        time=time
    )
    return reservation

def get_user_by_email(email):
    """Returns user from email"""
    return User.query.filter(User.email == email).first()

def get_reservations(user_id):
    """Returns all a User's Reservations"""
    reservations = Reservation.query.filter(Reservation.user_id == user_id).all()
    res_dic = {}
    res_list = []
    for reservation in reservations:
         res_list.append([str(reservation.date), str(reservation.time)])
    res_dic['reservations'] = res_list
    return res_dic

def get_all_reservations_times(date):
    """return all reserved times for specific date"""
    reserved_times = Reservation.query.filter(Reservation.date == date).all()
    return reserved_times

def create_avaliable_times_dict(date):
   timesdic = {}
   reserved_times = get_all_reservations_times(date)
   avaliable_times = times.times
   for rtime in reserved_times:
        rtime.time = str(rtime.time)
        if rtime.time in avaliable_times:
            avaliable_times.remove(rtime.time)
        else:
            continue
   timesdic['avaliable'] = avaliable_times
   return timesdic
   





if __name__ == '__main__':
    from server import app
    connect_to_db(app)