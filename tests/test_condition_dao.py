import pytest
from unittest.mock import MagicMock, patch
from app.dao.condition_dao import get_all_conditions


@pytest.fixture
def mock_db():
    """
    Fixture to mock the database connection and conditions collection.
    """
    mock_db = MagicMock()
    mock_db.conditions.distinct.return_value = ["C001", "C002", "C003"]
    return mock_db


@patch("app.dao.condition_dao.get_db")
def test_get_all_conditions(mock_get_db, mock_db):
    """
    Test for the `get_all_conditions` function to verify it retrieves
    all unique conditions from the database and formats them correctly.
    """
    # Mock `get_db` to return the mock database
    mock_get_db.return_value = mock_db

    # Call the function to test
    result = get_all_conditions()

    # Assert `get_db` was called
    mock_get_db.assert_called_once()

    # Assert the mock database's `distinct` method was called on "code"
    mock_db.conditions.distinct.assert_called_once_with("code")

    # Assert the result matches the expected output
    assert result == [
        {"condition_code": "C001"},
        {"condition_code": "C002"},
        {"condition_code": "C003"},
    ]
