# EV Location Finder

An API foundation for finding electric-vehicle charging locations and
supporting smart route planning. The local MVP includes a validated charger
search endpoint backed by clearly labelled in-memory demo data; PostGIS and
Redis are ready for the next persistence/integration phase.

## Local development

1. Create a local environment file: `Copy-Item .env.example .env`.
2. Set a non-empty `POSTGRES_PASSWORD` in `.env`.
3. Start dependencies with `docker compose --env-file .env -f infra/docker-compose.yml up -d`.
4. Install the Python dependencies with `python -m pip install -r backend/requirements.txt`.
5. Run the API with `uvicorn backend.app.main:app --reload`.

The readiness check is `GET /health`, which returns `{"status":"ok"}`.
OpenAPI documentation is available at `/docs`. Search chargers with:

`GET /api/v1/chargers?latitude=12.9716&longitude=77.5946&radius_km=25`

Optional filters are `connector` (for example `CCS2`) and
`available_only=true`. Results include distance in kilometres and are sorted
nearest first. The bundled locations are demo data, not live availability.

Run the automated checks with `pytest backend/tests`.

## Hosting on Render

This repository includes `Dockerfile` and `render.yaml` for hosting the API as
a Render web service. In Render, choose **New > Blueprint**, connect this
repository, and select `render.yaml`. The service starts without a database
because the current charger data is explicitly demo data held in memory.
Configure `POSTGRES_*`, `DATABASE_URL`, and `REDIS_URL` only when the
persistence integration is added. Render supplies the public HTTPS URL after
the first successful deploy.

The repository can also be run by any Docker-compatible host:

```powershell
docker build -t ev-location-finder .
docker run --rm -p 8000:8000 ev-location-finder
```

The VisionShield repository is a separate project (`tharankanth03/VISIONSHIELD`);
its research assets and application files should remain isolated from this
EV-location-finder service unless an explicit integration contract is added.

## AI-assisted implementation

This project may use AI-assisted development for scaffolding, code generation,
and review. A human maintainer remains responsible for requirements, security,
dependency selection, testing, and production approval. AI-generated changes
must be reviewed and tested before merge; secrets and personal data must never
be supplied to an AI tool.

## Product documents

- [Privacy Policy](docs/PRIVACY_POLICY.md)
- [Terms & Conditions](docs/TERMS_AND_CONDITIONS.md)
- [Brand asset: favicon](web/favicon.svg)

## Configuration and security

`.env` is local-only and ignored by Git. Use a secret manager in hosted
environments, rotate credentials if exposure is suspected, and never commit
production API keys, passwords, or tokens.
