import json
from pathlib import Path
from typing import Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .preprocessing import preprocess_text


class FAQMatcher:
    def __init__(
        self,
        faq_file: str | Path,
        threshold: float = 0.25,
    ) -> None:
        self.faq_file = Path(faq_file)
        self.threshold = threshold

        self.faqs = self._load_faqs()

        if not self.faqs:
            raise ValueError("FAQ dataset cannot be empty.")

        self.questions = [
            faq["question"]
            for faq in self.faqs
        ]

        self.processed_questions = [
            preprocess_text(question)
            for question in self.questions
        ]

        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            sublinear_tf=True,
        )

        self.question_vectors = self.vectorizer.fit_transform(
            self.processed_questions
        )

    def _load_faqs(self) -> list[dict[str, str]]:
        if not self.faq_file.exists():
            raise FileNotFoundError(
                f"FAQ file not found: {self.faq_file}"
            )

        with self.faq_file.open(
            "r",
            encoding="utf-8",
        ) as file:
            data: Any = json.load(file)

        if not isinstance(data, list):
            raise ValueError(
                "FAQ data must be a JSON list."
            )

        validated_faqs: list[dict[str, str]] = []

        for index, faq in enumerate(data):
            if not isinstance(faq, dict):
                raise ValueError(
                    f"FAQ at index {index} must be an object."
                )

            question = faq.get("question")
            answer = faq.get("answer")

            if not isinstance(question, str) or not question.strip():
                raise ValueError(
                    f"FAQ at index {index} has an invalid question."
                )

            if not isinstance(answer, str) or not answer.strip():
                raise ValueError(
                    f"FAQ at index {index} has an invalid answer."
                )

            validated_faqs.append(
                {
                    "question": question.strip(),
                    "answer": answer.strip(),
                }
            )

        return validated_faqs

    def find_best_match(
        self,
        user_question: str,
    ) -> dict[str, Any]:

        if not isinstance(user_question, str):
            return self._no_match_response(
                "Question must be text."
            )

        user_question = user_question.strip()

        if not user_question:
            return self._no_match_response(
                "Please enter a question."
            )

        processed_question = preprocess_text(
            user_question
        )

        if not processed_question:
            return self._no_match_response(
                "I could not understand your question. "
                "Please try again."
            )

        user_vector = self.vectorizer.transform(
            [processed_question]
        )

        similarity_scores = cosine_similarity(
            user_vector,
            self.question_vectors,
        )[0]

        best_index = int(
            similarity_scores.argmax()
        )

        best_score = float(
            similarity_scores[best_index]
        )

        best_faq = self.faqs[best_index]

        matched = best_score >= self.threshold

        if not matched:
            return {
                "answer": (
                    "Sorry, I could not find a relevant answer. "
                    "Please try asking your question differently."
                ),
                "matched_question": best_faq["question"],
                "score": round(best_score, 4),
                "matched": False,
            }

        return {
            "answer": best_faq["answer"],
            "matched_question": best_faq["question"],
            "score": round(best_score, 4),
            "matched": True,
        }

    @staticmethod
    def _no_match_response(
        message: str,
    ) -> dict[str, Any]:

        return {
            "answer": message,
            "matched_question": None,
            "score": 0.0,
            "matched": False,
        }