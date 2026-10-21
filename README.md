# Cloud Deployment Lab

A small FastAPI application packaged with Docker, deployed on
Render, and tested automatically using GitHub Actions.

## Live API

- Home: https://cloud-deployment-lab-tw8u.onrender.com/
- Health: https://cloud-deployment-lab-tw8u.onrender.com/health
- API docs: https://cloud-deployment-lab-tw8u.onrender.com/docs

The free hosting instance may take time to wake after inactivity.

## Technologies

Python, FastAPI, Uvicorn, Docker, Git, GitHub Actions and Render.

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/` | Returns a welcome message |
| GET | `/health` | Returns `{"status": "ok"}` |
| GET | `/docs` | Interactive API documentation |

## Run with Docker

Install Docker and start its engine, then run:

```bash
docker build -t cloud-deployment-lab .
docker run --rm -p 127.0.0.1:8000:8000 cloud-deployment-lab
```

Open http://127.0.0.1:8000/docs.

## Automated checks

On pushes to main and pull requests, GitHub Actions:

1. Builds the Docker image.
2. Starts a temporary container.
3. Checks that /health returns HTTP 200 and the expected JSON.
4. Displays logs and removes the temporary container.

## Deployment

Render builds the application from the repository's Dockerfile.
The application listens on port 8000, with PORT=8000 configured
in Render and /health used as the health check path.

GitHub Actions tests the application separately. Deployment is
not yet configured to wait for those checks to pass.

## What I practised

- Creating HTTP endpoints.
- Managing Python dependencies.
- Building and running Docker containers.
- Running the container as a non-root user.
- Tracking changes with Git.
- Deploying an application to the cloud.
- Automating a container build and API smoke test.