#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 12:38:53 2024

@author: lou
"""

import sqlite3
conn = sqlite3.connect("vimusic.db")
cur = conn.cursor()

cur.execute("SELECT * FROM Song WHERE likedAt IS NOT NULL")
rows = cur.fetchall()
result_list = [list(row) for row in rows]
cur.close()
conn.close()
import os
cwd = os.getcwd()
ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': 'output/%(title)s.%(ext)s',
                'postprocessors': [   {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        },
        {'key': 'EmbedThumbnail'},
        {'key': 'FFmpegMetadata'},
    ],
                
                    }
erreurs = []
titres = []

allIndexesFromDB = [song[0]+"\n" for song in result_list]

from os.path import exists

file_exists = exists("AlreadyDL.txt")
if file_exists:
    with open('AlreadyDL.txt', 'r') as f:  
        alreadyDL = f.readlines()
        alreadyDL = list(dict.fromkeys(alreadyDL))
else:
    alreadyDL = []


from yt_dlp import YoutubeDL
for song in allIndexesFromDB:
    i = song
    with YoutubeDL(ydl_opts) as ydl:
        if i not in alreadyDL:
            try:
                ydl.download("https://www.youtube.com/watch?v="+i)
                with open('AlreadyDL.txt', 'a') as f:  
                    f.write(i)
            except:
                erreurs.append(i)
        