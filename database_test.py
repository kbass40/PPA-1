from database import DBConnection as db
import pytest
from pytest_mock import mocker

def test_mock_database(mocker):
    mocker.patch.object(db, 'get_connection')
    db.get_connection()
    db.get_connection.assert_called_once()


data = db('user','password')
data.print_db()