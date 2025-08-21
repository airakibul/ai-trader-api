import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "app/__init__.py",
    "app/main.py",
    "app/config.py",
    "app/auth.py",
    "app/models.py",

    "app/routes/__init__.py",
    "app/routes/auth_routes.py",
    "app/routes/ai_routes.py",
    "app/routes/system_routes.py",

    "app/tasks/__init__.py",
    "app/tasks/qa.py",
    "app/tasks/content.py",
    "app/tasks/image.py",

    "app/providers/__init__.py",
    "app/providers/openrouter.py",
    "app/providers/groq.py",
    "app/providers/huggingface.py",
    "app/providers/stability.py",

    ".env",
    "requirements.txt",
    "setup.py",
    "README.md",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
