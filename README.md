# AchataVT

**AchataVT** é um pacote Python que oferece duas formas simples de **comprimir vídeos**:

- `AchatarFFMpeg`: utiliza o FFmpeg via subprocesso (alta performance)
- `AchatarMoviePy`: utiliza a biblioteca MoviePy (mais simples, 100% Python)

Este pacote é ideal para quem precisa reduzir o tamanho de vídeos com apenas algumas linhas de código.

---

## ✅ Instalação

Você pode instalar a partir do repositório local ou do PyPI (se publicado):

```bash
pip install achata-vt
```

Ou clonando o projeto localmente:

```bash
git clone https://github.com/alecsmelo/achata-vt.git
cd achata-vt
pip install -e .
```

---

## ⚙️ Requisitos

- Python 3.7 ou superior
- [FFmpeg](https://ffmpeg.org/) instalado e no PATH (somente para `AchatarFFMpeg`)
- `moviepy` (será instalado automaticamente via `requirements.txt`)

---

## 🚀 Como usar

Os dois módulos possuem uma função chamada `Achatar`, que **requer dois argumentos obrigatórios**:

- `videoentrada`: caminho do vídeo original
- `videosaida`: caminho onde será salvo o vídeo comprimido

---

### 🔹 Usando `AchatarFFMpeg`

Essa abordagem usa o FFmpeg via linha de comando, ideal para quem busca **melhor desempenho e controle**.

```python
from AchatarFFMpeg.converterFFMpeg import Achatar

Achatar("meuvideo.mp4", "comprimido_ffmpeg.mp4")
```

> ⚠️ Certifique-se de que o FFmpeg está instalado no seu sistema e disponível no terminal.

---

### 🔹 Usando `AchatarMoviePy`

Essa versão usa apenas `moviepy`, sem dependência externa além do Python.

```python
from AchatarMoviePy.converterMoviePy import Achatar

Achatar("meuvideo.mp4", "comprimido_moviepy.mp4")
```

> Ideal para scripts simples e compatibilidade multiplataforma.

---

## 🗂️ Estrutura do projeto

```
AchataVT/
├── AchatarFFMpeg/
│   ├── __init__.py
│   └── converterFFMpeg.py  ← função Achatar(videoentrada, videosaida)
├── AchatarMoviePy/
│   ├── __init__.py
│   └── converterMoviePy.py ← função Achatar(videoentrada, videosaida)
├── README.md
├── requirements.txt
└── setup.py
```

---

## 📄 Licença

Distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
