from app import create_app

app = create_app()

if __name__ == '__main__':
    # Notre méthode principale (main) pour lancer l'application Flask
    app.run(host="localhost", port=8000, debug=True)  # On lance l'application Flask en mode debug sur le port 8000 de localhost