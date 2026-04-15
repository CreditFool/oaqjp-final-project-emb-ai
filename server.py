from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotionDetector():
    text_to_analyze = str(request.args.get('textToAnalyze'))
    emotions = emotion_detector(text_to_analyze)
    response = f"For the given statement, the system response is 'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}."

    return response

if __name__ == "__main__":
    app.run(host="localhost", port=5000)