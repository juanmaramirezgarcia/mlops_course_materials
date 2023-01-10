# Model Scoring Deployed in Flask

## Steps
1. model.py: Train a model and save a model.pkl file
2. app.py: Create Flask app that will expose a POST method

The docker container is going to expose the model in http://localhost:5000/api

You can check it through different ways:
- request.py: this script uses requests python library to send POST method to the model
- Curl: you can use curl from a terminal in your computer (please be careful with the differences for curl between linux/windows)
- Talend: you can use any API tester helper in your browser.
