import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user_name = Column(String(300), nullable=False)
    first_name = Column(String(300), nullable=False)
    last_name = Column(String(300), nullable=False)
    email = Column(String(300), nullable=False)
    password = Column(String(300), nullable=False)
    fav_id = Column(Integer, ForeignKey("favorites.id"))
    favorites = relationship("Favorites")

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    birth_year = Column(String(300))
    gender = Column(String(300))
    height = Column(Integer)
    skin_color = Column(String(300))
    eye_color = Column(String(300))
    add_to_fav = Column(Boolean)

class FavCharacter(Base):
    __tablename__ = "favcharacter"
    id = Column(Integer, primary_key=True)
    id_of_fav = Column(Integer, ForeignKey("character.filter_by(add_to_fav=True)"))
    character = relationship(Character)

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    climate = Column(String(300))
    population = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)
    add_to_fav = Column(Boolean)

class FavPlanet(Base):
    __tablename__ = "favplanet"
    id = Column(Integer, primary_key=True)
    id_of_fav = Column(Integer, ForeignKey("planet.filter_by(add_to_fav=True)"))
    planet = relationship(Planet)

class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    max_atmosphering_speed = Column(Integer)
    cost_in_credits = Column(Integer)
    cargo_capacity = Column(Integer)
    passangers = Column(Integer)
    vehicle_class = Column(String(300))
    add_to_fav = Column(Boolean)

class FavVehicle(Base):
    __tablename__ = "favvehicle"
    id = Column(Integer, primary_key=True)
    id_of_fav = Column(Integer, ForeignKey("vehicle.filter_by(add_to_fav=True)"))
    vehicle = relationship(Vehicle)

class Favorites(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)
    id_char = Column(Integer, ForeignKey("favcharacter.id"))
    id_plan = Column(Integer, ForeignKey("favplanet.id"))
    id_vehic = Column(Integer, ForeignKey("favvehicle.id"))
    favchar = relationship(FavCharacter)
    favplan = relationship(FavPlanet)
    favvehic = relationship(FavVehicle)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
