"""
server to handling text input to get emotion score 
based on the input text
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/", methods=["GET"])
def home():
    """
    Handle index route to serve index.html page
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_handler():
    """
    Handle request to score the input text with argument
    textToAnalyze
    """
    text_to_analyze = str(request.args.get('textToAnalyze'))
    emotions = emotion_detector(text_to_analyze)

    if emotions['dominant_emotion'] is None:
        response = "Invalid text! Please try again!."
    else:
        response = f"For the given statement, the system " \
        f"response is 'anger': {emotions['anger']}, " \
        f"'disgust': {emotions['disgust']}, " \
        f"'fear': {emotions['fear']}, 'joy': {emotions['joy']} " \
        f"and 'sadness': {emotions['sadness']}. " \
        f"The dominant emotion is {emotions['dominant_emotion']}."

    return response

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
