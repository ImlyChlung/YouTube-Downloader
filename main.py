import yt_dlp

# 請將此 URL 替換成你想下載的影片網址
video_url = "https://www.youtube.com/watch?v=2sW08zLO8S8"

ydl_opts = {
   
    "format": "best[ext=mp4]",
    "outtmpl": "%(title)s.%(ext)s",  # 輸出檔案的命名模板
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

