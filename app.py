import requests
def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    if response.status_code == 200:
        joke_data = response.json()
        if joke_data["type"] == "single":
            return joke_data["joke"]
        elif joke_data["type"] == "twopart":
            return f"{joke_data['setup']} - {joke_data['delivery']}"
        else:
            return "Failed to retrieve a joke."
if __name__ == "__main__":
    joke = get_joke()
    print(f"Here's a joke for you: {joke}")