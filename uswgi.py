from app import app
from app import load_model_to_app

load_model_to_app()

if __name__ == "__main__":
    app.run()