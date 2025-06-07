# flask-soccer-scoreboard-week1

# Flask Soccer Scoreboard

A simple CRUD web app that displays live soccer scores fetched from a public API.  
Built with Flask, containerized with Docker, tested with pytest, and deployable via Kubernetes.

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Goals](#goals)  
3. [Tech Stack](#tech-stack)  
4. [Features](#features)  
5. [Architecture & Design Notes](#architecture--design-notes)  
6. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Clone & Install](#clone--install)  
   - [Configuration](#configuration)  
7. [Running the App Locally](#running-the-app-locally)  
8. [Testing](#testing)  
9. [CI/CD Pipeline](#cicd-pipeline)  
10. [Docker & Docker Compose](#docker--docker-compose)  
11. [Kubernetes Deployment](#kubernetes-deployment)  
12. [Contributing](#contributing)  
13. [License](#license)  

---

## Project Overview

**What it is:**  
A Flask-based web application to list, add, update, and delete (“CRUD”) soccer match scores, using data pulled from a free public API (e.g., [Football-Data.org](https://www.football-data.org/)).  

**Why build it:**  
- Practice building a RESTful Flask app  
- Consume and cache external JSON APIs  
- Implement CRUD operations with a relational database  
- Write tests, set up CI/CD, containerize, and deploy to Kubernetes  

---

## Goals

- **Core Functionality:**  
  - Fetch and display live match data  
  - Create, Read, Update, Delete custom match entries  
- **DevOps Skills:**  
  - Dockerize the app & compose local services  
  - Write a GitHub Actions workflow for build/test/deploy  
  - Craft Kubernetes manifests or a Helm chart  
- **Quality & Maintenance:**  
  - 80%+ unit-test coverage with pytest  
  - Clear documentation & design notes  

---

## Tech Stack

- **Backend:** Python 3.x, Flask  
- **Database:** PostgreSQL (or SQLite for dev)  
- **HTTP Client:** `requests` (or `httpx`)  
- **Testing:** pytest, Factory Boy (optional)  
- **CI/CD:** GitHub Actions (or Jenkins)  
- **Containerization:** Docker, Docker Compose  
- **Orchestration:** Kubernetes (YAML or Helm)  

---

## Features

- Retrieve live scores for today’s matches  
- List all stored match records  
- Add a new match manually  
- Edit or delete existing entries  
- Automatic caching of API responses  

---

## Architecture & Design Notes

*(Placeholders — we’ll fill these in as we decide on API endpoints, caching, and DB schema)*

- **API Integration:**  
  - Endpoint(s) used, authentication  
  - Caching strategy (in-memory, Redis, DB-backed)  

- **Database Schema:**  
  ```sql
  Table: matches
  ┌────────────┬───────────┐
  │ Column     │ Type      │
  ├────────────┼───────────┤
  │ id         │ SERIAL PK │
  │ utc_date   │ TIMESTAMP │
  │ home_team  │ TEXT      │
  │ away_team  │ TEXT      │
  │ home_score │ INTEGER   │
  │ away_score │ INTEGER   │
  └────────────┴───────────┘
