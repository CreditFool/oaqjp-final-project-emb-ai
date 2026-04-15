import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    body = { 
        "raw_document": { "text": text_to_analyze } 
    }

    resp = requests.post(url, headers=header, json=body)
    if resp.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    resp_text = json.loads(resp.text)
    emotions = resp_text["emotionPredictions"][0]["emotion"]

    dominant_emotion = ["", None]
    for key, val in emotions.items():
        if dominant_emotion[1] is None:
            dominant_emotion = [key, val]
        else:
            if val > dominant_emotion[1]:
                dominant_emotion = [key, val]
    
    emotions["dominant_emotion"] = dominant_emotion[0]

    return emotions