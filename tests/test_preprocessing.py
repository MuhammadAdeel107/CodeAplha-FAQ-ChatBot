from app.services.preprocessing import preprocess_text


def test_preprocess_lowercase():
    result = preprocess_text(
        "HOW CAN I TRACK MY ORDER?"
    )

    assert result == "track order"


def test_preprocess_removes_special_characters():
    result = preprocess_text(
        "How much does shipping cost?!"
    )

    assert "?" not in result
    assert "!" not in result


def test_preprocess_returns_string():
    result = preprocess_text(
        "Hello world"
    )

    assert isinstance(result, str)