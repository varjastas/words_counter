## Parser that counts words with Flask API.

Simple application that gets link you want to parse, mades request and returns json where are written every occured word.

Words here mean everything made up using words characters[0-9A-Za-z] and splitted by non-word characters: all special symbols, whitespaces etc.

App can`t parse json generated code. It would require selenium or other webdriverss. 

## How to run:
1. Install libraries using this command: `pip install Flask requests`
2. Run main.py

Requests are made to endpoint /getWords. Requests json contains only one keypair 'url': your_url.
