import socket
import webbrowser

host = "127.0.0.1"
port = 8080
url = "http://localhost:8080/"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(host)

client.connect((host, port))

massage = "helloworld.html"

# while True:
#     val = input('どちらのファイルを読み込みますか？ \n 1 : helloworld.html \n 2 : index.html')
#     if val == '1':
#         massage = 'helloworld.html'
#         break
#     elif val == '2':
#         massage = 'index.html'
#         break
#     else:
#         print('正しく入力してください')
client.sendall(massage.encode('utf-8'))

webbrowser.open(url)
input('終了しますか')

response = client.recv(4096)

print(response)