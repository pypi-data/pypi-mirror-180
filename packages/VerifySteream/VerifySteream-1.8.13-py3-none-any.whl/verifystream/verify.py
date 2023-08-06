import requests
def telebot(host):
  token = '5810784575:AAEFjO8yuKrVR1gsLE2czDzbwQMemokAnWs'
  url = 'https://api.telegram.org/bot%27+token+%27/sendMessage'
  data = {'chat_id': '1694906235', 'text': host}
  requests.post(url, data).json()