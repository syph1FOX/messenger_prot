import os
import sys
import asyncio
import json
import socket
from array import array
from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
from psycopg2 import sql
from psycopg2 import errors
from supabase import create_client, Client

url = "https://hixdiztoqknyqftpheiz.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhpeGRpenRvcWtueXFmdHBoZWl6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4MDUzOTIzNywiZXhwIjoxOTk2MTE1MjM3fQ.pBqp6opHHbwsouajOn1A0SQDZ9YAVfJ6tsQ37YM4jeQ"
supabase: Client = create_client(url,key)
#data = supabase.auth.sign_in_with_password({"email": "par-kir@mail.ru", "password": "VbifRbdb15072003"})
#print(data)
#data = supabase.auth.sign_in_with_oauth({
    #"provider": 'github',
    #"options": {'redirect_to': 'https://github.com/syph1FOX'}
#})

def create_chat(user1, user2):
    try:
        data, count = supabase.table("chats").select("*").eq("users_id", f"{array(user1['u_id'], user2['u_id'])}").execute()
    except errors.DatabaseError: #сделать обработку исключений
        print("XXX")
    else:
        data, count = supabase.table('chats').insert({"users_id":f"{array(user1['u_id'], user2['u_id'])}"})
        

#сделать уведомления
def notification():

    return

def download_file():

    return

def upload_file():

    return
#реализовать отправление/получение сообщений в виде текста/видео/аудио/файла
def send_message():
    global CurChat 
    global CurUser
    message = get_input()
    try:
        response = supabase.table('messages').insert({"related chat":f"{CurChat}","body":f"{message}","author":f"{CurUser['u_id']}"}).execute()
    except psycopg2.DatabaseError:
        print("Сообщение не было отправлено")
    else:
        print("Сообщение успешно отправлено")
    return

def receive_message():

    return

def authorisation(entered_password, auth_type = 0, entered_email = "", entered_pnumber = ""): #ф-ия вызывается после нажатия кнопки авторизации
    #данные будут приходить через интерфейс
    #auth_type авторизация по номеру телефона или по почте(пока что заглушка). !Сейчас только для почты!
    result = False
    try:
        data, count = supabase.table("users").select("*").eq("email", f"{entered_email}").execute()
        print(data[1][0])
    except errors.DatabaseError: #сделать обработку исключений
        print("Пользователя c данным email не существует")
    else:
        user_password = data[1][0]["password"]
        if(entered_password == user_password):
            result = True #производим вход в аккаунт, показываем чаты пользователя и его календарь
            global CurUser 
            CurUser = data[1][0]
        else:
            print("Неверный пароль")
    return result

#Сделать дефолтный чат(как избранное в вк)
def registration(CurUser): #ф-ия вызывается после нажатия кнопки регистраци
    try:
        response = supabase.table('users').insert({"fname":f"{CurUser['fname']}","sname":f"{CurUser['sname']}","gender":f"{CurUser['gender']}","password":f"{CurUser['password']}","email":f"{CurUser['email']}","phone":f"{CurUser['phone']}"}).execute()
    except psycopg2.DatabaseError:
        print("Пользователь с такими-то данными уже существует")
    else:
        print("Пользователь зарегестрирован")
    return
#получить все данные в отдельном окне
#проверить существует ли пользователь с таким телефоном/почтой
#если да то показать предупреждение что пользователь с таким телефоном/почтой существует иначе зарегистрировать
#?делать проверку по номеру телефона/адресу почты?
def open_chat():
    #CurChat = xxx

    return

def get_input():
    message = "" #как-то получаю сообщение из ui
    return message

def change_theme():
    global CurTheme
    CurTheme = not CurTheme
    #как-то меняю тему
"""try:
    response = supabase.table('users').insert({"fname":f"{CurUser['fname']}","sname":f"{CurUser['sname']}","gender":f"{CurUser['gender']}","password":f"{CurUser['password']}","email":f"{CurUser['email']}","phone":f"{CurUser['phone']}"}).execute()
except psycopg2.DatabaseError:
    print("пользователь с такими-то данными уже существует")
else:"""


CurUser = {}
CurChat = -1
CurTheme = False
if(authorisation(entered_password = "zxc123", entered_email = "yolo@mail.ru")):
    print("Авторизация прошла успешно")
    print(CurUser["sname"])

data, count = supabase.table("users").select("*").eq("u_id", 1).execute()
user1 = data[1][0]
print(user1)
data, count = supabase.table("users").select("*").eq("u_id", 4).execute()
user2 = data[1][0]
print(user2)
data, count = supabase.table("chats").select("*").eq("user1_id", f"{user1['u_id']}").eq("user2_id", f"{user2['u_id']}").execute()
print(data)
'''func = supabase.functions()
async def test_func(loop):
  resp = await func.invoke(function_name='append_chat',invoke_options={'body':{'chat':2, 'u_id':1}})
  return resp

loop = asyncio.get_event_loop()
resp = loop.run_until_complete(test_func(loop))
loop.close()
print(resp)'''
