# SoulNest ML Model
SoulNest utilizes a Multinomial Naive Bayes classifier for text classification tasks. This model is particularly suitable for scenarios where the features (in this case, words or tokens) are categorical and independent. The Multinomial Naive Bayes classifier calculates the probability of each class (e.g., "Stress" or "Normal") given a set of features and then predicts the class with the highest probability.

The model is trained on a dataset containing responses, where each response is associated with a label indicating whether it represents a state of "Stress" or "Normal." Before training, the text data undergoes preprocessing steps such as punctuation removal, stop-word removal, and vectorization using techniques like CountVectorizer and TF-IDF (Term Frequency-Inverse Document Frequency) transformation.The Multinomial Naive Bayes model offers a lightweight and efficient solution for text classification tasks, making it well-suited for applications like sentiment analysis, spam detection, and in SoulNest's case, identifying stress-related responses.

## Deployment

1. Add github deployment public key to github which is generated in the the pc/vps.

2. Clone the project

3. Make shure to chnage the `server_name localhost;` in `nginx.conf` before getting changes.

```bash
docker-compose up --build -d
```

## Deployment to vps

Just push chnages normally.

Make shure to have a location `/var/www/python/soulnest_ml_model` in vps and the docker images in your docker hub like `kenura/soul-nest_ml_model:latest`

## Deployment without docker

1. Set up a virtual environment (optional but recommended):

   - On Windows:

     ```bash
     py -m venv .venv
     ```

   - On macOS and Linux:

     ```bash
     python3 -m venv .venv
     ```

2. Activate the virtual environment:

   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source .venv/bin/activate
     ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Once you have completed the installation steps, you can run the Flask application using the `run.py` script:

```bash
python flask_app/app.py
```

or

```bash
source .venv/bin/activate && python flask_app/app.py
```

or

```bash
gunicorn -b 0.0.0.0:8001 -w 4 app.main:app --daemon

server start command
```
