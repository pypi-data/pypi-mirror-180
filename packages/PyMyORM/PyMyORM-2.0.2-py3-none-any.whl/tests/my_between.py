from pymyorm.database import Database
from config import db
from models.user import User


if __name__ == '__main__':

    Database.connect(**db)

    all = User.find().where('time', 'between', ['2022-07-29', '2022-07-29 20:00:00']).all()
    for one in all:
        print(one)
