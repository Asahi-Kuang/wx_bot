from wxpy import *

bot = Bot()

@bot.register()
def print_others(msg):
    return '[自动回复]您好，邝萌萌暂时不在。稍后与您联系。么么哒(～o￣3￣)～'

embed()