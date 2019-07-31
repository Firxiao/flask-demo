import os
from app import create_app

# Get the configuration from the environment variable
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)
