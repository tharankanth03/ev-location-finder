# EV Location Finder

An API foundation for finding electric-vehicle charging locations and
supporting smart route planning. The current release exposes a health endpoint
and local PostGIS/Redis development services; application features should be
added behind authenticated, validated API routes.

## Local development

1. Create a local environment file: `Copy-Item .env.example .env`.
2. Set a non-empty `POSTGRES_PASSWORD` in `.env`.
3. Start dependencies with `docker compose --env-file .env -f infra/docker-compose.yml up -d`.
4. Install the Python dependencies with `python -m pip install -r backend/requirements.txt`.
5. Run the API with `uvicorn backend.app.main:app --reload`.

The readiness check is `GET /health`, which returns `{"status":"ok"}`.

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
