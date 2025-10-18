# Simple Frontend + Backend Docker Compose

This project contains a minimal Flask backend and a static frontend served by nginx. Use docker-compose to build and run both services.

Run (Windows - PowerShell):

1. Make sure Docker Desktop is installed and running. Start Docker Desktop from the Start menu.

2. Open PowerShell as Administrator (right-click -> Run as administrator) to ensure the docker client can access the daemon pipe, then:

```powershell
cd 'C:\Users\ahmed\Desktop\WinterArc\docker_project_week14'
docker-compose up --build
```

Or run detached and view logs:

```powershell
docker-compose up --build -d
docker-compose logs -f
```

Visit the frontend at: http://localhost:8080
Backend API: http://localhost:5000/api

Troubleshooting notes:

- If you see an error mentioning the docker engine pipe (e.g. "The system cannot find the file specified"), Docker Desktop is likely not running or your shell needs elevated permissions. Ensure Docker Desktop is running and retry in an elevated PowerShell.
- If using WSL2-based Docker, ensure your WSL2 distro is running and Docker Desktop integration for your distro is enabled.

Capturing screenshots for submission:

- Run the above `docker-compose up --build` in a terminal and take screenshots of:
  - The full build/start output from `docker-compose up --build`.
  - `docker ps` output showing running containers.
  - Optionally, the browser showing http://localhost:8080 with the message.
- Save PNG files into `screenshots/` (e.g. `screenshots/compose_build.png`, `screenshots/docker_ps.png`).

Helper script (automates log capture and screenshot)

- There's a PowerShell helper at `scripts/run_and_capture.ps1` which will:
  - Run `docker-compose up --build -d`
  - Save `docker-compose logs` to `screenshots/compose_logs.txt`
  - Save `docker ps` output to `screenshots/docker_ps.txt`
  - Capture a fullscreen PNG to `screenshots/compose_screenshot.png`

Usage (Run PowerShell as Administrator and ensure Docker Desktop is running):

```powershell
cd 'C:\Users\ahmed\Desktop\WinterArc\docker_project_week14'
.\scripts\run_and_capture.ps1
```

Note: the script requires elevated PowerShell on Windows and that Docker Desktop is running. If screenshot capture fails, take manual screenshots using the Snipping Tool and save them into `screenshots/`.

Git & submission:

- Initialize a git repo (if not already):

```powershell
git init
git add .
git commit -m "Add simple frontend/backend with Dockerfiles and docker-compose"
```

- Push to a GitHub repo (create an empty repo on GitHub first), then:

```powershell
git remote add origin https://github.com/<your-user>/<your-repo>.git
git branch -M main
git push -u origin main
```
