"""
date:2023-10-23
author:zhou
代码简介：抓取文章页面中的视频并下载保存
分析：先知道文章url和视频url。发现在页面源代码中没有视频url，则视频为ajax加载。
在f12页面元素中知道:视频url='https://video.pearvideo.com/mp4/short/20170608/cont-1086370-10520212-hd.mp4',视频打得开。
但是视频的请求后相应的  url='https://video.pearvideo.com/mp4/short/20170608/1698045284584-10520212-hd.mp4',视频经过简单加密。
"""

import requests
#获取
url=r'https://www.pearvideo.com/video_1086370'
contId=url.split('_')[1]
# print(contId)
videoRqUrl=f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.29272018246906484'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
    'Referer':url,#防盗链：溯源，找这个视频的链接是不是从他的上一级跳转过来的
}

videoResp=requests.get(url=videoRqUrl,headers=headers)
# print(videoResp.json())
dic=videoResp.json()
videoResp.close()
videoRespUrl=dic['videoInfo']['videos']['srcUrl']
systemTime=dic['systemTime']
print(videoRespUrl)
videoUrl=videoRespUrl.replace(systemTime,f'cont-{contId}')
print(videoUrl)

#下载视频
with open(file='./thirdChapter/梨视频.mp4',mode='wb') as f:
    f.write(requests.get(videoUrl).content)
f.close()

