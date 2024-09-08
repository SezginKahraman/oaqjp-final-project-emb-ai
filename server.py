"""
    Flask server initiation
    """

from flask import Flask, request
from emotion_detection import emotion_detector
# Flask uygulaması
app = Flask(__name__)
@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Analyze emotions from the provided text input.

    This endpoint accepts a POST request with a string of text and returns
    the emotion analysis in JSON format by calling the external Watson API.

    Returns:
        JSON: The emotion analysis of the text or an error message if the
        request fails.
    """
    if request.is_json:
        data = request.get_json()
        text = data.get('text', None)  # Text parametresini alıyoruz
        # emotion_detector fonksiyonunu çağırıyoruz
        result = emotion_detector(text)
        if result["dominant_emotion"] is None:
            return 'Invalid text! Please try again!.'
        response_string = 'For the given statement, the system response is anger: '
        response_string += f'{result["anger"]}, '
        response_string += f'disgust: {result["disgust"]}, fear: {result["fear"]}, '
        response_string += f'joy: {result["joy"]} and sadness: {result["sadness"]}'
        response_string += f'. The dominant emotion is {result["dominant_emotion"]}.'
        return response_string
    return 'Request must be JSON'
if __name__ == '__main__':
    app.run(debug=True)
