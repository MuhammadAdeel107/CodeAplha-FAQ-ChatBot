from app import create_app


def create_test_client():
    app = create_app()

    app.config.update(
        TESTING=True
    )

    return app.test_client()


def test_home_page():
    client = create_test_client()

    response = client.get("/")

    assert response.status_code == 200

    assert b"FAQ Assistant" in response.data


def test_chat_api():
    client = create_test_client()

    response = client.post(
        "/api/chat",
        json={
            "question": "How much does shipping cost?"
        },
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["matched"] is True

    assert "answer" in data


def test_empty_question():
    client = create_test_client()

    response = client.post(
        "/api/chat",
        json={
            "question": ""
        },
    )

    assert response.status_code == 400