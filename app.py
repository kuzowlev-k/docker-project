from flask import Flask, request, render_template_string
import pytz
from datetime import datetime

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Текущее московское время</title>
    <style>
        body {
            background-color: {{ bg_color }};
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            transition: background-color 0.3s ease;
        }
        .time-container {
            background: rgba(255, 255, 255, 0.85);
            padding: 40px 60px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            text-align: center;
        }
        h1 {
            font-size: 48px;
            margin: 0;
            color: #333;
        }
        .time {
            font-size: 72px;
            font-weight: bold;
            color: #2c3e50;
            margin: 20px 0;
        }
        .date {
            font-size: 24px;
            color: #7f8c8d;
        }
        .hint {
            margin-top: 20px;
            font-size: 14px;
            color: #95a5a6;
        }
    </style>
</head>
<body>
    <div class="time-container">
        <h1>Московское время</h1>
        <div class="time">{{ current_time }}</div>
        <div class="date">{{ current_date }}</div>
        <div class="hint">Измените цвет фона: ?bg=red, ?bg=blue, ?bg=green и т.д.</div>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    bg_color = request.args.get('bg', '#f0f0f0')
    
    valid_colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 
                   'pink', 'cyan', 'black', 'white', 'gray', 'lightblue', 'lightgreen']
    
    if not bg_color.startswith('#') and bg_color not in valid_colors:
        bg_color = '#f0f0f0'
    
    moscow_tz = pytz.timezone('Europe/Moscow')
    now = datetime.now(moscow_tz)
    
    current_time = now.strftime('%H:%M:%S')
    current_date = now.strftime('%d %B %Y')
    
    return render_template_string(
        HTML_TEMPLATE,
        bg_color=bg_color,
        current_time=current_time,
        current_date=current_date
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
