import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?safe-mode"
    try:
        print("Interrogation de JokesAPI...")
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("-" * 40)
            if data["type"] == "single":
                print(f"Blague : {data['joke']}")
            else:
                print(f"Question : {data['setup']}")
                print(f"Réponse  : {data['delivery']}")
            print("-" * 40)
            
        else:
            print(f"Erreur : Impossible de récupérer la blague (Code {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Une erreur de connexion est survenue : {e}")

if __name__ == "__main__":
    get_joke()
