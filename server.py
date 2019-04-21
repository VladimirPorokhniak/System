import socket
import telebot

timeout = 10
ip = socket.gethostbyname(socket.getfqdn())
print(ip)
host = "0.0.0.0"
port = 12345
TOKEN = '895685216:AAGzsN7x9oZP_YRL6tZNoQp1VoCPpVIZ9F8'
Chat_id = 448157691
Computer = True

addr = (host, port)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(addr)
bot = telebot.TeleBot(TOKEN)

while True:
    server.settimeout(timeout)
    try:
        d = server.recvfrom(1024)
        received = d[0]
        print(received.decode('utf-8'))
        Computer = True
    except socket.timeout:
        if Computer:
            bot.send_message(Chat_id, "Компьютер выключен!")
            Computer = False


server.close()
