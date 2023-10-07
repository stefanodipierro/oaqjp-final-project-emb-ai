# emotion_detection.py 
# Import the necessary packages
import requests  # Import the requests library
import json  # Import the json library



def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inout_json = { "raw_document": { "text": text_to_analyze } }

    # Send the request to the API
    response = requests.post(url, json=inout_json, headers=headers)
    if not text_to_analyze:  # controlla se text_to_analyze è vuoto
        return {"status_code": 400, "error": "Invalid text! Please try again!"}
    

    
    if response.status_code == 200:
        # If the request was successful, parse and return the response
        return response.json().get('text', 'No text field in response')
    else:
        # If the request failed, raise an exception or return an error message
        response.raise_for_status()  # This will raise a requests.exceptions.HTTPError if the request failed

        # Assume the response text is a JSON string
    response_dict = json.loads(response.text)

    # Assume the emotion scores are stored in the response dictionary
    emotion_scores = response_dict.get('emotion', {})

    # Extract the required emotions and their scores
    emotions = {emotion: score for emotion, score in emotion_scores.items() if emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']}

    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Prepare the output dictionary
    output = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }

    return output
    