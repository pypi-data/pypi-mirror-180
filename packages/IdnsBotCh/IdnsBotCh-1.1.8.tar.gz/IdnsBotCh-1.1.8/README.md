# IdnsBotCh

这是一套Idns聊天机器人框架

```python
#模块导入
import IdnsBotCh

#发送一条helloworld
IdnsBotCh.Bot.send_msg("helloworld")

#如果有人发送hello，回复你好
if IdnsBotCh.Bot.get_msg=="hello":
    IdnsBotCh.Bot.send_msg("你好")
```