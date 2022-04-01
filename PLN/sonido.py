# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 18:01:49 2022

@author: armma
"""

from gtts import gTTS
from playsound import playsound

s = gTTS("Sample Text")
s.save('sample.mp3')
playsound('sample.mp3')