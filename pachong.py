# coding:utf-8
'''
爬虫
'''

import urllib
import json
import time

class PaChong():
    def meow(t,m,pr):  #t冷却时间，m代数，pr价格
        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
        n=0
        while n<10000:
            try:
                r=urllib.request.Request('https://api.cryptokitties.co/auctions?offset='+str(n)+'&limit=20&type=sale&status=open&parents=false')
                response = urllib.request.urlopen(r,timeout=5)
                r=json.loads(response.read().decode().translate(non_bmp_map))
                cats=r['auctions']
                if n%200==0:
                    print(n)
                for i in cats:
                    st=i['kitty']
                    price=int(i['current_price'])/(10**18)
                    code=st['id']
                    gen=st['generation']
                    cooltime=st['status']['cooldown_index']

                    if cooltime<=t and gen<=m and price<pr:
                        print('id:',code,'price:',price,'gen:',gen,'cooltime:',cooltime)

                n=n+20
                time.sleep(1)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    PaChong().meow(24,5,100)

