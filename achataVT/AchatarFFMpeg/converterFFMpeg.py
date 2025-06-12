import subprocess

def Achatar(videoentrada, videosaida):
    arquivo_entrada = videoentrada
    arquivo_saida = videosaida

    subprocess.run([
        "ffmpeg", "-i", arquivo_entrada,
        "-vcodec", "libx264",
        "-crf", "28",
        "-present", "fast",
        "-acodec", "aac",
        "-b:a", "128k",
        arquivo_saida

    ])
