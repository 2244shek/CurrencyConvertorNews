# Currency Converter with News Updates

A modern web application that converts currencies and displays related financial news. This project combines a responsive frontend with a Flask backend to deliver real-time currency conversion rates and relevant news articles.

![Currency Converter Screenshot](https://github.com/user-attachments/assets/96fd3078-689f-4330-ba55-1d178c31eb98)

## Features

- **Real-time Currency Conversion**: Convert between multiple international currencies
- **Financial News Integration**: View the latest news related to selected currency pairs
- **Responsive Design**: Fully optimized for both desktop and mobile devices
- **Modern UI**: Clean, intuitive interface with smooth animations and visual feedback

## Tech Stack

### Frontend
- HTML5
- CSS3 (with custom animations and responsive design)
- JavaScript (ES6+)
- Font Awesome icons

### Backend
- Python 3.8+
- Flask (Web framework)
- Requests (HTTP client)
- Beautiful Soup (Web scraping capabilities)
- Flask-CORS (Cross-origin resource sharing)

### APIs
- CurrencyLayer API for exchange rates
- News API for financial news articles

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- API keys for CurrencyLayer and News API

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/currency-converter.git
cd currency-converter
```
2. Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```
pip install flask requests beautifulsoup4 flask-cors
```
