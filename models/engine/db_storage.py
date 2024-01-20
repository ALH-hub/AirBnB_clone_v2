"""definition of the DBStorage engine"""

from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """the db storage engine"""

    __engine = None
    __session = None

    def __init__(self):
        """initialize the engine"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                             
                                             pool_pre_ping=True)
        if getenv("HBNB_DEV" == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """querry the current database session
        
        Return:
        the querried classes in the formate: <class-name> <object-id> = obj
        """
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in objs}
    
    def new(self, obj):
        """add object to database"""
        self.__session.add(obj)

    def save(self):
        """commit changes to the database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete object from database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """initialize a new session by crating all tables from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close the database session"""
        self.__session.close()
