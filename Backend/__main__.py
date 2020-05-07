from SpectaculaireSpiegel import app

# gunicorn3 --bind=0.0.0.0 --worker-class=gevent --worker-connections=1000 --workers=3 SpectaculaireSpiegel:app

if __name__ == '__main__':
    try:
        app.run(port=8000)
    except OSError as e:
        print(e)
test