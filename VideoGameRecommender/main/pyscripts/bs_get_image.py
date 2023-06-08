from bs4 import BeautifulSoup
import requests

def get_image(game_name):

    url = f"https://www.metacritic.com/game/pc/{'-'.join(game_name.lower().split())}"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'})
    soup = BeautifulSoup(response.content, 'html.parser')
    image = soup.find('img', class_='product_image large_image')['src']
    return image

if __name__ == "__main__":
    print(get_image('Grand Theft Auto V'))