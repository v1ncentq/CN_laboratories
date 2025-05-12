import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/jokes/random"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            joke = response.json()
            print("Анекдот:")
            print(joke.get('setup', 'Немає тексту анекдоту'))
            print(joke.get('punchline', 'Немає кульмінації'))
        else:
            print(f"Помилка: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Помилка з'єднання: {e}")

if __name__ == "__main__":
    get_random_joke()