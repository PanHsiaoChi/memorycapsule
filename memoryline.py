from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, ConfirmTemplate, ImageSendMessage, TextMessage,  ButtonsTemplate, TextSendMessage, LocationSendMessage, TemplateSendMessage, MessageTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn


line_bot_api = LineBotApi('CHANNEL_ACCESS_TOKEN')
handler = LineBotApi('CHANNEL_SECRET')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext == '旅店介紹': #完成
        sendHotelIntro(event)

    elif mtext == '客房資訊': #完成
        sendRoomIntro(event)
    
    elif mtext == '入住登記': #完成
        sendReserve(event)

    elif mtext == '沒錯':
        sendYes(event)

    elif mtext == '空間':
        sendSpace(event)
    
    elif mtext == '回憶':
        sendMemory(event)
    
    elif mtext == '現在':
        sendNow(event)

    elif mtext == '物品':
        sendThing(event)

    elif mtext == '再想想':
        sendNo(event)

    elif mtext == '聯絡我們':
        sendContact(event)

def sendHotelIntro(event):  #旅店介紹
    try:
        message = TemplateSendMessage(
            alt_text='旅店介紹',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/eyUZ7vE.jpeg',  #顯示的圖片
                title='您想要聽多長的故事呢？',  #主標題
                text='我們提供簡單快速版本，以及廢話很多版本',  #副標題
                actions=[
                    MessageTemplateAction(  #顯示文字計息
                        label='簡單就好',
                        text='簡單就好'
                    ),
                    MessageTemplateAction(  #顯示文字計息
                        label='來多一點！',
                        text='來多一點！'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


def sendRoomIntro(event):  #客房資訊
    try:
        message = TemplateSendMessage(
            alt_text='客房資訊',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/GA13rdH.png',  #顯示的圖片
                title='目前已登記四間客房資料，您想觀賞哪間呢？',  #主標題
                text='這是其他旅客的房間',  #副標題
                actions=[
                    MessageTemplateAction(  #顯示文字計息
                        label='101房',
                        text='101房'
                    ),
                    MessageTemplateAction(  #顯示文字計息
                        label='202房',
                        text='202房'
                    ),
                    MessageTemplateAction(  #顯示文字計息
                        label='303房',
                        text='303房'
                    ),
                    MessageTemplateAction(  #顯示文字計息
                        label='401房',
                        text='401房'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendReserve(event):  #入住登記
    try:
        message = TemplateSendMessage(
            alt_text='入住登記',
            template=ConfirmTemplate(
                text='了解過我們旅館的經營風格後，您也想入住了嗎？',
                actions=[
                    MessageTemplateAction(  #按鈕選項
                        label='沒錯',
                        text='沒錯'
                    ),
                    MessageTemplateAction(
                        label='再想想',
                        text='再想想'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendYes(event):
    try:
        message = [
        TextSendMessage(
            text='開始填寫入住資料\n請寫下你心目中的那個空間。\n傳送後，再傳送一則訊息「空間」。',
        )
        ]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendSpace(event):
    try:
        message = TextSendMessage(
            text='你們之間的回憶？\n傳送後，再傳送一則訊息「回憶」。',
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendMemory(event):
    try:
        message = TextSendMessage(
            text='現在對你來說，那個地方......\n傳送後，再傳送一則訊息「現在」。',
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendNow(event):
    try:
        message = TextSendMessage(
            text='在這裡，你印象深刻的物品有什麼呢？\n傳送後，再傳送一則訊息「物品」。',
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendThing(event):
    try:
        message =[
        TextSendMessage(
            text='登記完成。\n感謝您的入住登記。\n希望您在前來記憶旅店的這段時間裡，能夠暫時停下向前的腳步，回頭凝視過去。\n記憶旅店隨時歡迎您再度蒞臨。',
        )
        ]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


def sendNo(event):
    try:
        message = TextSendMessage(
            text='等您準備好後隨時可以來呦！',
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


def sendContact(event):  #聯絡我們
    try:
        message = TemplateSendMessage(
            alt_text='聯絡我們',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/eyUZ7vE.jpeg',  #顯示的圖片
                title='您想連絡誰呢？',  #主標題
                text='服務人員算是一種彩蛋',  #副標題
                actions=[
                    MessageTemplateAction(  #顯示文字計息
                        label='memory capsule 記憶旅店',
                        text='memory capsule 記憶旅店'
                    ),
                    MessageTemplateAction(  #顯示文字計息
                        label='記憶旅店的服務人員',
                        text='記憶旅店的服務人員'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

if __name__ == '__main__':
    app.run()
