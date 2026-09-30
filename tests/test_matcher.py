from pathlib import Path

from app.services.faq_matcher import FAQMatcher


FAQ_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "faqs.json"
)


def create_matcher() -> FAQMatcher:
    return FAQMatcher(
        faq_file=FAQ_FILE,
        threshold=0.20,
    )


def test_delivery_question_matches():
    matcher = create_matcher()

    result = matcher.find_best_match(
        "How much does shipping cost?"
    )

    assert result["matched"] is True
    assert result["matched_question"] is not None
    assert result["answer"]
    assert result["score"] > 0


def test_tracking_question_matches():
    matcher = create_matcher()

    result = matcher.find_best_match(
        "Where can I find my order?"
    )

    assert result["matched"] is True


def test_empty_question():
    matcher = create_matcher()

    result = matcher.find_best_match("")

    assert result["matched"] is False

    assert result["score"] == 0.0