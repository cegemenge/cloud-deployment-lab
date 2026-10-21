Cloud Deployment Lab

A small Python API built with FastAPI, packaged with Docker,
deployed on Render, and tested automatically using GitHub Actions.

LIVE APPLICATION

Home:
https://cloud-deployment-lab-tw8u.onrender.com/

Health check:
https://cloud-deployment-lab-tw8u.onrender.com/health

Interactive API documentation:
https://cloud-deployment-lab-tw8u.onrender.com/docs

The free hosting instance may take time to wake after inactivity.

TECHNOLOGIES

Python
FastAPI
Uvicorn
Docker
Git
GitHub
GitHub Actions
Render

API ENDPOINTS

GET /
Returns:
{"message":"My cloud deployment pipeline is working!"}

GET /health
Returns:
{"status":"ok"}

GET /docs
Opens the interactive API documentation.

PROJECT FILES

main.py
Defines the API endpoints.

requirements.txt
Lists the application's Python dependencies.

Dockerfile
Defines how to build and run the application container.

.dockerignore
Excludes unnecessary files from the Docker build context.

.gitignore
Excludes local environments and other unnecessary files from Git.

.github/workflows/ci.yml
Defines the automated build and API health check.

README.md
Explains the project and how to run it.

RUN LOCALLY WITH PYTHON ON WINDOWS

Create a Python environment:

python -m venv .venv

Install dependencies:

.\.venv\Scripts\python.exe -m pip install -r requirements.txt

Start the development server:

.\.venv\Scripts\python.exe -m uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs

Press Ctrl+C in the terminal to stop the server.

RUN WITH DOCKER

Start Docker Desktop and wait for its engine to run.

Build the image:

docker build -t cloud-deployment-lab .

Start a container:

docker run --rm -p 127.0.0.1:8000:8000 cloud-deployment-lab

Open:
http://127.0.0.1:8000/docs

Press Ctrl+C to stop the container.

AUTOMATED CHECKS

GitHub Actions runs on pushes to main and on pull requests.

The workflow:

1. Downloads the repository.
2. Builds the Docker image.
3. Starts a temporary API container.
4. Checks that /health returns HTTP 200.
5. Checks that the response is {"status":"ok"}.
6. Displays the container logs.
7. Removes the temporary container.

These checks verify that the container builds and the health
endpoint works. They do not test every application behaviour.

CLOUD DEPLOYMENT

Render builds the application using the repository's Dockerfile.

Deployment settings:

Branch: main
Runtime: Docker
Dockerfile path: ./Dockerfile
PORT environment variable: 8000
Health check path: /health
Auto-Deploy: After CI Checks Pass

The application listens on 0.0.0.0:8000 inside the container.
It runs as a non-root user.

DELIVERY PROCESS

1. Make a code change.
2. Save and commit the change with Git.
3. Push the commit to GitHub.
4. GitHub Actions builds and tests the container.
5. Render waits for the checks to pass.
6. Render builds and deploys the updated application.
7. Verify the update using the public URL.

A failed CI check blocks automatic deployment.
Manual deployments are controlled separately.

VERIFIED RESULT

A change to the home endpoint passed the automated checks and
appeared on the public application:

{"message":"My cloud deployment pipeline is working!"}

WHAT I PRACTISED

Creating a Python API.
Managing Python dependencies and virtual environments.
Building and running Docker containers.
Mapping container ports to the local computer.
Running an application as a non-root user.
Tracking changes with Git.
Publishing a repository on GitHub.
Deploying a containerized application to Render.
Creating automated checks with GitHub Actions.
Configuring deployment to wait for passing checks.
Checking the deployed application.

LIMITATIONS

This is a learning project with two simple API endpoints.

It does not include a database, user authentication, comprehensive
tests, or external uptime monitoring.

The free hosting instance may sleep when inactive.

REPOSITORY

https://github.com/cegemenge/cloud-deployment-lab
