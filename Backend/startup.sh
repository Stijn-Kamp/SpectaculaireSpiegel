#!/bin/bash
exec gunicorn3 --bind=0.0.0.0 --worker-class=gevent --worker-connections=1000 --workers=1 SpectaculaireSpiegel:app
#https://store.nubentos.com/store/apis/info?name=API-nCoV2019&version=1.0.0&provider=admin