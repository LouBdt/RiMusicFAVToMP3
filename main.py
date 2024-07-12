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
from yt_dlp import YoutubeDL
for song in result_list:
    i = song[0]
    with YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download("https://www.youtube.com/watch?v="+i)
        except:
            erreurs.append(i)