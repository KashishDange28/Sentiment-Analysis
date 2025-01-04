def analyze_sentiment(text):
    positive_keywords = ['great', 'fantastic', 'love', 'excellent', 'satisfied', 'good', 'great', 'nice', 'kind', 
                     'outstanding', 'amazing', 'awesome', 'perfect', 'superb', 'wonderful', 'incredible', 'marvelous', 
                     'impressive', 'delightful', 'happy', 'enjoyable']

    negative_keywords = ['terrible', 'bad', 'broke', 'not worth', 'hate', 'bad', 'not good', 'not great', 
                     'awful', 'disappointing', 'horrible', 'poor', 'frustrating', 'unhelpful', 'regrettable', 
                     'unacceptable', 'miserable', 'dreadful', 'unpleasant']

    text_lower = text.lower()

    positive_score = sum(text_lower.count(keyword) for keyword in positive_keywords)
    negative_score = sum(text_lower.count(keyword) for keyword in negative_keywords)

    if positive_score > negative_score:
        return 'positive', positive_score - negative_score
    elif negative_score > positive_score:
        return 'negative', negative_score - positive_score
    else:
        return 'neutral', 0  # Neutral if neither has a higher score

def get_sentiment_counts(reviews):
    positive_count = sum(1 for review in reviews if analyze_sentiment(review)[0] == 'positive')
    negative_count = sum(1 for review in reviews if analyze_sentiment(review)[0] == 'negative')
    return positive_count, negative_count
