import requests
from inspect import currentframe, getframeinfo
from colorama import init
init()
from colorama import Fore, Back, Style
import sys
import os
import signal



def edit_message(bot=None,chat_id=None,msg_id=None,text=None,button={}):
            if bot == None:
                   print(Fore.RED+f"You did not specify a keyword (bot = ...) in the 'edit_message' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (bot = ...) в функціі 'edit_message'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)


            if msg_id == None:
                   print(Fore.YELLOW+f"You did not specify a keyword (msg_id = ...) in the 'edit_message' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (msg_id = ...) в функціі 'edit_message'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)

            if chat_id == None:
                   print(Fore.RED+f"You did not specify a keyword (chat_id = ...) in the 'edit_message' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (chat_id = ...) в функціі 'edit_message'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
            if text == None:
                   print(Fore.RED+f"You did not specify a keyword (text = ...) in the 'edit_message' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (text =  ...)  в функціі 'edit_message'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
            url = f'https://api.telegram.org/bot{bot}/editMessageText'
            payload = {
                'chat_id': chat_id,
                'message_id': msg_id,
                'text': text,
                "reply_markup": button

                }
   
            r = requests.post(url,json=payload)
            return r