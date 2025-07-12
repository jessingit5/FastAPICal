from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_calculation_endpoints():
    response = client.get("/calculate?operand1=6&operand2=3&operation=add")
    assert response.status_code == 200
    assert response.json() == {"result": 9}

    response = client.get("/calculate?operand1=6&operand2=3&operation=subtract")
    assert response.status_code == 200
    assert response.json() == {"result": 3}

    response = client.get("/calculate?operand1=6&operand2=3&operation=multiply")
    assert response.status_code == 200
    assert response.json() == {"result": 18}

    response = client.get("/calculate?operand1=6&operand2=3&operation=divide")
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_division_by_zero_endpoint():
    response = client.get("/calculate?operand1=5&operand2=0&operation=divide")
    assert response.status_code == 400
    assert "Division by zero" in response.json()["detail"]

def test_unknown_operation_endpoint():
    response = client.get("/calculate?operand1=5&operand2=3&operation=unknown")
    assert response.status_code == 400
    assert "Unknown operation" in response.json()["detail"]