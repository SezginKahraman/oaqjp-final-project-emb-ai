import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    data = { "raw_document": { "text": text_to_analyse } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   
    response = requests.post(url, json=data, headers=headers)
    print(response.status_code)
    
    if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
                }

    response_data = response.json()
    emotion_data = response_data['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_data, key=emotion_data.get)
    dominant_score = emotion_data[dominant_emotion]
    new_response = {
        'anger': emotion_data['anger'],
        'disgust': emotion_data['disgust'],
        'fear': emotion_data['fear'],
        'joy': emotion_data['joy'],
        'sadness': emotion_data['sadness'],
        'dominant_emotion': dominant_emotion
    }

    return new_response