# Quack
Quackify your terminal with 13 lines of code!

## Overview
This is a short Python program that randomly generates a duck image.

## TLDR
One can replicate the process in a few steps
1) Create a new project directory and add a `quack.py` program
2) Run `pip3 install requests Pillow pyinstaller`
3) Open `quack.py` and add
```py
from PIL import Image
import requests
```

4) Send a GET request to get a random URL by adding
```py
r = requests.get("https://random-d.uk/api/random")
r_json = r.json()
quack = r_json["url"]
```

5) Get the raw duck image data with another GET request (this time, passing `stream=True`)
```py
r2 = requests.get(quack, stream=True)
r2_raw = r2.raw
```

6) Show the image using PIL
```py
im = Image.open(r2_raw)
im.show()
```

7) Run `pyinstaller --onefile quack.py`

8) Remove the `build` directory, move the executable out of `dist`, remove `quack.spec` and `dist`

9) Add the final executable to PATH.

10) You can now type `quack` into the command line and get a duck image