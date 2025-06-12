from setuptools import setup, find_packages

setup(
    name="achata-vt",
    version="0.1.0",
    author="Alecsandro F Melo",
    author_email="aferreiramelo@email.com",
    description="Pacote para compressão de vídeos com FFmpeg e MoviePy",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/alecsmelo/achata-vt",  # troque se tiver um repositório
    packages=find_packages(),  # inclui AchatarFFMpeg e AchatarMoviePy
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Multimedia :: Video",
    ],
    python_requires=">=3.7",
    install_requires=open("requirements.txt").read().splitlines(),
)
