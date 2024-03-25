# SoulNest ML Model

## SSH Access

```bash
ssh root@139.59.221.132
```

IPv4 : `178.128.93.119`

Username: `root`

Reserved IP: `139.59.221.132`

Project dir: `/var/www/python`

## File moving command

```bash
rsync -avz --exclude '.venv' --exclude '.git' --exclude '__pycache__' ./ root@139.59.221.132:/var/www/python/SoulNest_ML_Model/
```

### Working one

## Installation

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
#