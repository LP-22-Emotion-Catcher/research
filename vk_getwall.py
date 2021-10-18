import csv # для сохранения информации в CSV
import httpx # для запроса
import pandas as pd # для визуализации результатов
import pydantic # для работы с результатами парсинга 
import random # для рандомизации временного интервала
import time # для задержки между запросами

from config import access_token, owner_id # настройки для запроса
from datetime import datetime as dt # для перевода даты из timestamp
from glom import glom # для безопасного получения значений словаря

def getjson(url, data=None):
    response = httpx.get(url, params=data)
    return response.json()

def get_all_posts(access_token, owner_id, count=100, offset=0):
    """takes access_token, owner_id (group_id), count(default=100), offset(default=0)
    and returns all posts from vk group in a list of dictionaries
    and the number of posts in second variable"""
    
    all_posts = []
    while True:
        time.sleep(random.random())
        wall = getjson("https://api.vk.com/method/wall.get", {
            "owner_id" : owner_id,
            "count": count,
            "access_token": access_token,
            "offset": offset,
            "v": '5.131'
        })
        count_posts = wall['response']['count']
        posts = wall['response']['items']

        all_posts.extend(posts)

        if len(all_posts) >= count_posts:
            break
        else:
            offset += 100

    return all_posts, count_posts




def get_all_posts2(access_token, owner_id, count=1, offset=0):
    """takes access_token, owner_id (group_id), count(default=100), offset(default=0)
    and returns all posts from vk group in a list of dictionaries
    and the number of posts in second variable"""
    wall = getjson("https://api.vk.com/method/wall.get", {
            "owner_id" : owner_id,
            "count": count,
            "access_token": access_token,
            "offset": offset,
            "v": '5.131'
        })
    return wall


answer = get_all_posts2(access_token, owner_id, count=100, offset=0)
print(answer)


