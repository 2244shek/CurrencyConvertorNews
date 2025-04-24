from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to get the currency conversion rate
def get_currency_rate(from_currency, to_currency):
    try:
        # Option 1: Using CurrencyLayer API
        api_key = os.environ.get('CURRENCYLAYER_API_KEY')
        url = f'https://api.currencylayer.com/convert?access_key={api_key}&from={from_currency}&to={to_currency}&amount=1'
        response = requests.get(url)
        data = response.json()
        
        # Check if the API returned an error
        if data.get('success', False) == False:
            # # Fallback to fixed rates for demo purposes
            # fallback_rates = {
            #     'USD': {'EUR': 0.92, 'GBP': 0.79, 'INR': 83.15, 'JPY': 153.81, 'AUD': 1.52},
            #     'EUR': {'USD': 1.09, 'GBP': 0.86, 'INR': 90.54, 'JPY': 167.35, 'AUD': 1.65},
            #     'GBP': {'USD': 1.26, 'EUR': 1.16, 'INR': 104.95, 'JPY': 193.91, 'AUD': 1.91}
            # }
            
            # # Try to get from fallback rates
            # if from_currency in fallback_rates and to_currency in fallback_rates[from_currency]:
            #     return fallback_rates[from_currency][to_currency]
            # elif to_currency in fallback_rates and from_currency in fallback_rates[to_currency]:
            #     return round(1 / fallback_rates[to_currency][from_currency], 4)
            # else:
                return 'Rate unavailable'
        
        return data.get('result', 'Rate unavailable')
    
    except Exception as e:
        print(f"Error getting currency rate: {e}")
        return 'Error fetching rate'

# Function to search for relevant news articles
def get_currency_news(currency_pair):
    try: 
        # Use News API to get relevant news
        api_key = os.environ.get('NEWS_API_KEY')
        # Create a search query for the currency pair
        # query = f"{currency_pair} currency exchange forex"
        url = f'https://newsapi.org/v2/everything?q={currency_pair}&language=en&sortBy=publishedAt&from=2025-03-24&pageSize=5&apiKey={api_key}'
        response = requests.get(url)
        data = response.json()
        
        if data.get('status') != 'ok':
            # Fallback to dummy news for demo purposes
            # return get_dummy_news(currency_pair)
            return [{
                'title': 'Error fetching news !',
                'link': '#',
                'source': ''
            }]
        
        articles = data.get('articles', [])
        if not articles:
            # return get_dummy_news(currency_pair)
            return [{
                'title': 'No news available',
                'link': '#',
                'source': ''
            }]
            
        news = []
        for article in articles[:3]:  # Fetch top 3 news articles
            news.append({
                'title': article['title'],
                'link': article['url'],
                'source': article['source']['name']
            })
        return news
    
    except Exception as e:
        print(f"Error getting news: {e}")
        return [{
            'title': 'Error fetching news !!',
            'link': '#',
            'source': ''
        }]
        # return get_dummy_news(currency_pair)

# def get_dummy_news(currency_pair):
#     # Provide fallback news for demo purposes
#     from_currency, to_currency = currency_pair.split('-')
#     return [
#         {
#             'title': f'Recent trends in {from_currency}/{to_currency} exchange rate',
#             'link': f'https://www.reuters.com/markets/currencies/',
#             'source': 'Reuters'
#         },
#         {
#             'title': f'Economic factors affecting {from_currency} and {to_currency}',
#             'link': f'https://www.bloomberg.com/markets/currencies',
#             'source': 'Bloomberg'
#         },
#         {
#             'title': f'Market analysis: {from_currency} vs {to_currency}',
#             'link': f'https://www.ft.com/currencies',
#             'source': 'Financial Times'
#         }
#     ]

@app.route('/get_currency_data', methods=['POST'])
def get_currency_data():
    try:
        data = request.get_json()
        from_currency = data.get('from', 'USD')
        to_currency = data.get('to', 'EUR')

        # Get the latest currency conversion rate
        rate = get_currency_rate(from_currency, to_currency)

        # Get related news articles
        currency_pair = f'{from_currency}-{to_currency}'
        news = get_currency_news(currency_pair)
        
        return jsonify({
            'rate': rate,
            'news': news
        })
    
    except Exception as e:
        print(f"Error in get_currency_data: {e}")
        return jsonify({
            'error': 'An error occurred processing your request',
            'rate': 'Unavailable',
            'news': []
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
