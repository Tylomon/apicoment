from fastapi import FastAPI
from google_play_scraper import app

import pandas as pd
# Librerias Necesarias para trabajo y cadenas de texto
import re
import string

#Funciones Operativas

def extraccion():
    result = app(
    'com.clarocolombia.miclaro',
    lang='es', 
    country='co')
    comentarios=result['comments']
    return comentarios

def dictionario():
    receptor=extraccion()
    comentarios_dict=dict(enumerate(set(receptor)))
    return comentarios_dict 

def NLP():
    perri2=[1,2]
    return  perri2

perri=[1,2]

appli=FastAPI()
#coment
@appli.get('/')
def rea_root():
    return {"Bienvenido":"API extraccion y calificacion de Comentarios para la aplicacion mi claro"}

@appli.get('/comments')
def visualize_comments():   
    return dictionario()

@appli.post('/comments')
def visualize_Ncomments(n):
    number=int(n)
    print(type(number))
    receptor=extraccion()
    comentarios_dict=dict(enumerate(set(receptor[0:number])))  
    return comentarios_dict

@appli.get('/calification')
def calification():
    return perri

@appli.post('/calification')
def calification(n):
    return perri