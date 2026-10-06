# Basic DevOps Project: Flask + Docker + GitHub Actions

A small Flask API with an automated CI/CD pipeline.

**Flow:** push code -> GitHub Actions runs tests -> builds Docker image -> pushes to GitHub Container Registry (GHCR)

## Endpoints
| Route | Description |
|---|---|
| `GET /` | Welcome message |
| `GET /health` | Health check |
| `GET /api/greet?name=Bob` | Greeting |

## Run locally
```bash
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -v          # run tests
python -m app.main           # run app at http://localhost:5000
```

## Run with Docker
```bash
docker build -t my-devops-app .
docker run -p 5000:5000 my-devops-app
# or
docker compose up --build
```

## CI/CD pipeline
Defined in `.github/workflows/ci.yml`:
1. **test**: installs dependencies and runs pytest (on every push and PR)
2. **build-and-push**: builds the image and pushes it to `ghcr.io/<your-username>/<repo>` (only on `main`)

## Pull and run the published image
```bash
docker run -p 5000:5000 ghcr.io/<your-username>/<repo>:latest
```
