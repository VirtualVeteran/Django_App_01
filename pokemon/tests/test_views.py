import pytest
from unittest.mock import patch, MagicMock


@pytest.mark.django_db
@patch("pokemon.pokeapi.requests.get")
def test_pokemon_detail_returns_pokemon_data(mock_get, client):
    # Arrange
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "name": "pikachu",
        "base_experience": 112,
        "types": [{"type": {"name": "electric"}}],
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    # Act
    response = client.get("/pokemon/pikachu/")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "pikachu"
    assert data["base_experience"] == 112
    assert data["types"] == ["electric"]
