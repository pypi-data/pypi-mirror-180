# bonfire




bonfire this framework for [Telegram Bot API](https://core.telegram.org/bots/api) built on [requests](https://requests.readthedocs.io/en/latest/) <br>

**instaling**
```python 
git clone https://github.com/Help-urself/bonfire
```
or

```python 
pip install bonfire-tg


```


## Examples
<details>
  <summary> Click </summary>




### Simple [`send_message`](https://core.telegram.org/method/messages.sendMessage) request

```python
#git clone
import os
import sys
sys.path.append(os.path.abspath('you path to bonfire'))
from bonfire import *
from bonfire.methods import *

token = "TOKEN"
msg = message(token)


@bot.handler(token,command="/start")#command handler
def start():
    send_message(token,chat_id=msg.chat_id,text=f"<b>Hello </b> @{msg.author_username}",parse_mode='HTML')#send message



if __name__ == '__main__':
 while True:
  if bot.status(token) == "ok": #do not edit everything in startup
       bot.start_command(sys.modules[__name__])    
       bot.end_status(token)
 bot.start(token).start()

```

```python
#git clone
import os
import sys
from bonfire import *
from bonfire.methods import *

token = "TOKEN"
msg = message(token)


@bot.handler(token,command="/start")#command handler
def start():
    send_message(token,chat_id=msg.chat_id,text=f"<b>Hello </b> @{msg.author_username}",parse_mode='HTML')#send message



if __name__ == '__main__':
 while True:
  if bot.status(token) == "ok": #do not edit everything in startup
       bot.start_command(sys.modules[__name__])    
       bot.end_status(token)
 bot.start(token).start()

```

  </details>
  

    
   </details>