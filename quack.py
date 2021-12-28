from PIL import Image
import requests

r = requests.get("https://random-d.uk/api/random")
r_json = r.json()

quack = r_json["url"]

r2 = requests.get(quack, stream=True)
r2_raw = r2.raw

im = Image.open(r2_raw)
im.show()