"""
Questo modulo implementa un server Flask per l'applicazione di rilevamento delle emozioni.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    """
    Questa funzione è un endpoint Flask che legge una frase dall'input web,
    chiama la funzione emotion_detector, e restituisce i risultati al browser.
    """
    text = request.form['text']
    emotion_result = emotion_detector(text)
    if emotion_result.get("status_code") == 400:
        return jsonify({"error": "Invalid text! Please try again!"}), 400
    return jsonify(emotion_result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
