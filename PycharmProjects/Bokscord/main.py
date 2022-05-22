import socket
import threading

PORT = 2090
BUF_SIZE = 1024
clnt_imfor = []
clnt_cnt = 0
lock = threading.Lock()
name_tag = '@'


def handle_clnt(clnt_sock):
    for i in range(0, clnt_cnt):
        if clnt_imfor[i][1] == clnt_sock:
            clnt_num = i
            break

    while True:
        clnt_msg = clnt_sock.recv(BUF_SIZE)

        if not clnt_msg:
            lock.acquire()
            delete_imfor(clnt_sock)
            send_name()
            lock.release()
            break
        else:
            clnt_msg = clnt_msg.decode()
            if clnt_msg.startswith('!'):
                room_num = clnt_msg.replace('!', '')
                set_room(room_num, clnt_num)
                send_name()
            else:
                clnt_msg = clnt_imfor[clnt_num][0] + ' : ' + clnt_msg
                if clnt_msg.startswith('@'):
                    clnt_msg = clnt_msg.replace('@', '')
                    send_msg(clnt_msg, clnt_imfor[clnt_num][2])


def delete_imfor(clnt_sock):
    global clnt_cnt
    for i in range(0, clnt_cnt):
        if clnt_sock == clnt_imfor[i][1]:
            print("%s님께서 접속 종료하셨습니다." % clnt_imfor[i][0])
            while i < clnt_cnt - 1:
                clnt_imfor[i][0] = clnt_imfor[i + 1][0]
                clnt_imfor[i][1] = clnt_imfor[i + 1][1]
                clnt_imfor[i][2] = clnt_imfor[i + 1][2]
                i += 1
            break
    clnt_cnt -= 1


def send_name():
    for i in range(0, clnt_cnt):
        clnt_imfor[i][1].send('U_reset\n'.encode())
        for j in range(0, clnt_cnt):
            if clnt_imfor[i][2] == clnt_imfor[j][2]:
                clnt_imfor[i][1].send((clnt_imfor[j][0] + '\n').encode())


def send_msg(msg, send_sock_state):
    for i in range(0, clnt_cnt):
        if clnt_imfor[i][2] == send_sock_state:
            clnt_imfor[i][1].send(msg.encode())


def set_room(room_num, clnt_num):
    lock.acquire()
    clnt_imfor[clnt_num][2] = (int(room_num))
    clnt_imfor[clnt_num][1].send('T_reset'.encode())
    if room_num == '0':
        clnt_imfor[clnt_num][1].send(('main방 입장.').encode())
    else:
        clnt_imfor[clnt_num][1].send(('%s번방 입장.'%room_num).encode())
    print('%s )%d번방 입장.'%(clnt_imfor[clnt_num][0],clnt_imfor[clnt_num][2]))
    lock.release()


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', PORT))
    sock.listen(5)

    while True:
        clnt_sock, addr = sock.accept()

        lock.acquire()

        name = clnt_sock.recv(BUF_SIZE)
        name = name_tag + (name.decode())
        clnt_imfor.insert(clnt_cnt, [name, clnt_sock, 0])
        print('%s 접속(%d번방)'%(clnt_imfor[clnt_cnt][0],clnt_imfor[clnt_cnt][2]))
        clnt_cnt += 1

        lock.release()

        send_name()

        t = threading.Thread(target=handle_clnt, args=(clnt_sock,))
        t.start()
