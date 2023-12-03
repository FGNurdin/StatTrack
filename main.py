import os
import json
try:
    import requests
    import shutil
    from bs4 import BeautifulSoup
except:
    os.system('pip install -q requests')
    os.system('pip install -q shutil')
    os.system('pip install -q shutil')


def Banner():
    print("TikTok Stats Scraper".center(shutil.get_terminal_size().columns))
    print("By Nyowo".center(shutil.get_terminal_size().columns))
    print('\n')
    GetRequest()

def GetRequest():
    UserID      = input('\t[?] TikTok UserID = ')

    Headers         = {
        'user-agent'    : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Accept'        : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://www.tiktok.com/@{UserID}'
    }

    r = requests.get(f" https://www.tiktok.com/@{UserID}/api/user/detail", headers=Headers)
#   THE FUNCTION BELOWS USES HTML AS RESPONSE (DEPRECATED)
    #soup = BeautifulSoup(r.text, 'html.parser')
    #data = json.loads(soup.find('script', id="__UNIVERSAL_DATA_FOR_REHYDRATION__").get_text())
    data = json.loads(r.text)
    
    id, uniqueId, signature, follower, followingCount, likes, video, private = SetVar(data)
    PrintOut(id, uniqueId, signature, follower, followingCount, likes, video, private)

def SetVar(data):
    id = data['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']['user']['id']
    uniqueId = data['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']['user']['uniqueId']
    signature = data['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']['user']['signature']
    follower = data['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']['stats']['followerCount']
    followingCount = data['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']['stats']['followingCount']
    likes = data['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']['stats']['heartCount']
    video = data['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']['stats']['videoCount']
    private = data['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']['user']['privateAccount']
    return id,uniqueId,signature,follower,followingCount,likes,video,private

def PrintOut(id, uniqueId, signature, follower, followingCount, likes, video, private):
    print(f" \t [0] Name \t= {uniqueId} ")
    print(f" \t [0] UserID \t= {id}")
    print(f" \t [0] Signature \t= {signature}")
    print(f" \t [0] Followers \t= {follower}".ljust(shutil.get_terminal_size().columns))
    print(f" \t [0] Followings = {followingCount}".ljust(shutil.get_terminal_size().columns))
    print(f" \t [0] Likes \t= {likes}")
    print(f" \t [0] Videos \t= {video}")
    print(f" \t [0] Private \t= {[private]}".ljust(shutil.get_terminal_size().columns))
    
if __name__ == "__main__":
    Banner()