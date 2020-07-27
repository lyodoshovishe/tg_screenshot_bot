## Screenshot Telegram Bot
### Setup

Copy .env.example to .env and fill your parameters.

Run container:
```
docker-compose up -d
```

### VirtualEnv for Development code hinting

```
pip install virtualenv
сd ./app
virtualenv --python=python3 --prompt="venv" venv
source ./venv/bin/activate
pip install -r ./requirements.txt
```
