import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(20), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    SuscriptionDate = Column(String(50), nullable=False)

    favoritos = relationship('Favoritos', back_populates='usuario') 

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    personaje_id = Column(Integer, ForeignKey('personajes.id'))
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    vehiculos_id = Column(Integer, ForeignKey('vehiculos.id'))

    usuario = relationship('Usuario', back_populates='favoritos')  
    personajes = relationship('Personajes', back_populates='favoritos')
    planetas = relationship('Planetas', back_populates='favoritos')
    vehiculos = relationship('Vehiculos', back_populates='favoritos')


class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

    favoritos = relationship('Favoritos', back_populates='personajes')

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

    favoritos = relationship('Favoritos', back_populates='planetas')

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

    favoritos = relationship('Favoritos', back_populates='vehiculos')
   
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e