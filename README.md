
# Sentiment Analysis Tool

A web-based sentiment analysis tool that analyzes text input or CSV files to determine positive and negative sentiments. It visualizes the sentiment analysis results using charts and lists.

---

## Features
- Analyze individual text inputs for sentiment (positive/negative) and sentiment score.
- Upload and analyze CSV files containing reviews or comments.
- Visualize sentiment distribution using an interactive pie chart.
- Display detailed positive and negative review lists.

---

## Prerequisites
1. **Python 3.x**
2. **Flask**: Install via `pip install flask`.
3. **Pandas**: Install via `pip install pandas`.
4. **Plotly**: Install via `pip install plotly`.

---

## Setup Instructions
1. Clone this repository and navigate to the project folder:
   ```bash
   git clone <repository_url>
   cd sentiment-analysis-tool
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Open the tool in your browser at `http://127.0.0.1:5000`.

---

## Usage
### Text Analysis
1. Enter text in the input field.
2. Click "Analyze Text" to get the sentiment and score.
The analyze_sentiment function processes the text and returns:
Sentiment label (Positive or Negative).
Sentiment score for detailed insights.
   
### CSV Analysis
1. Upload a CSV file containing reviews/comments.
2. View the count of positive/negative reviews and sentiment breakdown in a pie chart.

---
### Technologies Used
1. Backend
Flask: Python-based web framework.
2. Frontend
HTML/CSS: Responsive web design.
Bootstrap: UI styling.
Plotly.js: Interactive pie chart visualization.
3. Libraries
Pandas: For data manipulation.
Plotly: For visualizations.
Flask: Web server.


