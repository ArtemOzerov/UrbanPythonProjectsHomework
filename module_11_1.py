from requests import get

response = get("https://avatars.mds.yandex.net/i?id=a50e37aecde40866ec548080b2322c25f69f5791-10576051-images-thumbs&n=13")
print(response)
with open("map.png", "wb") as file:
    file.write(response.content)