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

def make_posts(all_posts):
    """Takes in a list of dictionaries with posts, converts the data
    in a new structure, returns a new list of dictionaries with the posts"""
    filtered_data = []
    for post in all_posts:
        try:
            link = 'https://vk.com/wall-{owner_id}_{id}'.format(owner_id=owner_id[1:], id=id)
        except:
            link = ''
        try:
            date = dt.fromtimestamp(int(post['date'])).strftime('%d-%m-%Y %H:%M:%S')
        except:
            date = ''
        
        id_ = glom(post,'id',default=None)
        timestamp = glom(post,'date',default=None)
        likes = glom(post, 'likes.count', default=None)
        reposts = glom(post, 'reposts.count', default=None)
        comments = glom(post, 'comments.count', default=None)
        views = glom(post, 'views.count', default=None)
        text = glom(post, 'text', default=None)
        

        all_attachments = []
        try:
            attachments = post['attachments']
            if attachments:
                for att in attachments:
                    if att['type'] == 'video':
                        video_title = att['video']['title']
                        all_attachments.append(video_title)
                    if att['type'] == 'photo':
                        photo = att['photo']['text']
                        all_attachments.append(photo)
        except:
            attachments = ''

        filtered_post = {
            'id': id_,
            'date': date,
            'timestamp': timestamp,
            'likes': likes,
            'reposts': reposts,
            'comments': comments,
            'views': views,
            'text': text,
            'attachments': all_attachments,
            'link': link,
        }
        filtered_data.append(filtered_post)
    
    return filtered_data

def write_csv(data, filename, encoding='utf-8'):
    """Recives data as a list of dictionaries, the file name as a
    string ('*.csv'), encoding(default='utf-8'), returns csv file"""
    with open(filename, 'w', newline='', encoding=encoding) as csvfile:
        fieldnames = ['id', 'date', 'timestamp', 'likes', 'reposts',
                      'views', 'comments', 'text', 'attachments', 'link']

        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(data)

        print('Data written to csv', filename)
    csvfile.close()


all_posts, count_posts = get_all_posts(access_token, owner_id)
pposts = make_posts(all_posts)
#write_csv(pposts,'{owner_id}-{datetime}.csv'.format(owner_id=owner_id[1:], datetime=str(dt.now())[:10]))

def make_a_list_of_messages(posts):
    messages = []
    for post in posts:
        messages.append(post['text'])
    return messages

our_data = make_a_list_of_messages(pposts)
print(our_data)

#nice_posts = pd.read_csv(open('866379-2021-10-04.csv', 'r', encoding='utf-8'),sep=';')
#nice_posts