import socket
import os
import time
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

host = "127.0.0.1" #ホスト名
port = 8080 #ポート番号
HELLOWORLD_HTML = "helloworld.html" #HTMLファイル
NOTFOUND_HTML = "notfound.html" #HTMLファイル
fileExistence = True

if  os.path.isfile("helloworld.html"):

	fileExistence = True
else:
	fileExistence = False

#接続の設定
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4を指定
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serection = serversocket.bind((host, port))
serversocket.listen(5) #待ち受け
print('Wait...')

while True:
	clientsocket, client_address = serversocket.accept() #クライアントからのデータ受信
	rcmsg = clientsocket.recv(1024).decode("UTF-8") #受信データの変換
	print('rcmsg : ' + rcmsg)

	if rcmsg == '': #受信データがなかった場合break
		break

	if fileExistence == True:
		fin = open(HELLOWORLD_HTML, "rt") #HTMLファイルを開く
		msg = fin.read()
		fin.close()
		msg = "HTTP/1.1 200 OK\n\n" + msg #ステータスラインを付加
		
		clientsocket.sendall(msg.encode("cp932")) #HTMLファイルを出力
		print('True')
	else:
		fin = open(NOTFOUND_HTML, "rt")
		msg_fa = fin.read()
		fin.close()
		msg_fa = "HTTP/1.1 404 Not Found\n\n" + msg_fa

		clientsocket.sendall(msg_fa.encode("cp932"))
		print('file is not find...')

	# else:
	# elif rcmsg == 'index.html' or fileExistence == False:
	# 	fin = open(NOTFOUND_HTML, "rt")
	# 	msg_fa = fin.read()
	# 	fin.close()
	# 	msg_fa = "HTTP/1.1 404 Not Found\n\n" + msg_fa

	# 	clientsocket.sendall(msg_fa.encode("cp932"))
	# 	print('file is not find...')

	print('Received -> %s' % (rcmsg)) #受信データの出力

clientsocket.close() #ソケットを閉じる
