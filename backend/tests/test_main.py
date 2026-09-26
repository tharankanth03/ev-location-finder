from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_chargers_are_sorted_and_include_distance() -> None:
    response = client.get(
        "/api/v1/chargers",
        params={"latitude": 12.9716, "longitude": 77.5946, "radius_km": 25},
    )
    assert response.status_code == 200
    chargers = response.json()
    assert len(chargers) == 3
    assert chargers[0]["distance_km"] <= chargers[1]["distance_km"]


def test_charger_filters() -> None:
    response = client.get(
        "/api/v1/chargers",
        params={
            "latitude": 12.9716,
            "longitude": 77.5946,
            "connector": "CCS2",
            "available_only": "true",
        },
    )
    assert response.status_code == 200
    assert [charger["id"] for charger in response.json()] == ["blr-001", "blr-002"]


def test_invalid_coordinates_are_rejected() -> None:
    response = client.get(
        "/api/v1/chargers",
        params={"latitude": 120, "longitude": 77},
    )
    assert response.status_code == 422
