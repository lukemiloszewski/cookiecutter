from starlette.testclient import TestClient


class TestHealthRouter:
    ROUTER_URL = "/"

    def test_get_health_payload(self, fixt_client: TestClient) -> None:
        response = fixt_client.get(self.ROUTER_URL)
        assert response.status_code == 200

        response_body = response.json()
        assert isinstance(response_body, dict)
        assert set(response_body.keys()) == {"message"}
