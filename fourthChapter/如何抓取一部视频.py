
"""
<video src='不能播放的视频.mp4'></video>
一般的视频网站是怎么做的？
用户上传 ——》 转码（把视频做处理，2k，1080，720，480）-》切片处理（把单个的文件进行拆分）  
用户在拉动进度条的时候，只把视频的片段发送给用户

需要一个文件记录：1、视频播放顺序  2、 视频存放的路径
M3U8 txt json =>文本

想要抓取一个视频：
1、找到m3u8(各种手段)
2、提供m3u8下载到ts文件
3、可以通过各种手段(不仅仅是编程手段)，把ts为念合并成为一个MP4文件


"""
