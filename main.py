from flask import Flask, request, jsonify
import requests
from collections import Counter
import re

app = Flask(__name__)

@app.route('/getWords', methods=['POST'])
def get_words():
    data = request.get_json()
    url = data.get('url')

    try:
        # Making request to url 
        response = requests.get(url)
        
        content = response.text

        # Finding all words and counting them
        words = re.findall(r'\w+', content)
        word_count = Counter(words)

        return jsonify(word_count)
    except requests.RequestException as e:
        return jsonify({"error": f"Failed to fetch the URL. Error: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(debug=True)
