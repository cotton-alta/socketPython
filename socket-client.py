import socket
import webbrowser

host = "127.0.0.1" #接続するサーバのIPアドレス指定
port = 8080 #接続要求するポート番号を指定
url = "http://localhost:8080/" #ブラウザ上で開くurlを指定

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4を指定

print(host)

client.connect((host, port)) #接続試行

massage = "helloworld.html" #サーバー側に送信する文字列データを設定

client.sendall(massage.encode('utf-8')) #指定した文字列データをサーバーに送信

webbrowser.open(url) #ブラウザを自動起動
input('終了しますか') #終了指示待ち受け

response = client.recv(4096) #データの受け取り

print(response)