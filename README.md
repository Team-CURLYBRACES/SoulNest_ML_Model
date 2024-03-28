# SoulNest ML Model

## Deployment

1. Add github deployment public key to github which is generated in the the pc/vps.

2. Clone the project

3. Make shure to chnage the `server_name localhost;` in `nginx.conf` before getting changes.

```bash
docker-compose up --build -d
```

## Deployment to vps

Just push chnages normally.

Make shure to have a location `/var/www/python/SoulNest_ML_Model` in vps.

and the two docker images in your repo like

1. registry.example.com/flaskapp:latest
2. registry.example.com/nginxapp:latest

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
