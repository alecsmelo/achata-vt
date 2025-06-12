from moviepy.editor import VideoFileClip

def Achatar(videoentrada, videosaida)
    clip = VideoFileClip(videoentrada)
    clip.write_videofile(videosaida)