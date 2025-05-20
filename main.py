from flask import Flask, render_template
import os # Import the os module to access environment variables

app = Flask(__name__)

@app.route('/')
def home_page():
    # Make sure index.html is inside a 'templates' folder
    return render_template('index.html')

if __name__ == '__main__':
    # Get the port from the environment variable, default to 5000 if not found (e.g., for local testing)
    port = int(os.environ.get('PORT', 5000))
    # Run the app, binding to 0.0.0.0 and the specified port
    # Set debug=False for production environments
    print(f"Starting Flask server on http://0.0.0.0:{port}")
    app.run(host='0.0.0.0', port=port, debug=False) # Changed host, port, and debug
