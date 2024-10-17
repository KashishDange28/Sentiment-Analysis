from flask import Flask, request, jsonify, render_template
import pandas as pd
import plotly
import plotly.graph_objs as go
import json
from sentiment_analy import analyze_sentiment, get_sentiment_counts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_input = request.form['user_input']
    
    # Call analyze_sentiment to get both sentiment and score
    sentiment, score = analyze_sentiment(user_input)
    
    return jsonify({'result': sentiment, 'score': score})

@app.route('/analyze_csv', methods=['POST'])
def analyze_csv():
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file uploaded.'}), 400

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file)

    review_columns = ['review', 'Reviews', 'Sentiment', 'Feedback', 'comment']
    review_column = next((col for col in review_columns if col in df.columns), None)

    if review_column is None:
        return jsonify({'error': 'CSV file must contain one of the following columns: review, Reviews, Sentiment, Feedback, comment.'}), 400

    reviews = df[review_column].dropna().tolist()

    positive_reviews = []
    negative_reviews = []

    for review in reviews:
        sentiment, score = analyze_sentiment(review)
        if sentiment == 'positive':
            positive_reviews.append(review)
        elif sentiment == 'negative':
            negative_reviews.append(review)

    positive_count = len(positive_reviews)
    negative_count = len(negative_reviews)

    labels = ['Positive', 'Negative']
    values = [positive_count, negative_count]
    colors = ['#28a745', '#dc3545']

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors), hole=.3)])
    pie_chart = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return jsonify({
        'positive': positive_count,
        'negative': negative_count,
        'positive_reviews': positive_reviews,
        'negative_reviews': negative_reviews,
        'pie_chart': pie_chart
    })

if __name__ == '__main__':
    app.run(debug=True)
