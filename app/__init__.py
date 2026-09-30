from flask import Flask

from .config import FAQ_FILE, SIMILARITY_THRESHOLD
from .services.faq_matcher import FAQMatcher


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )

    faq_matcher = FAQMatcher(
        faq_file=FAQ_FILE,
        threshold=SIMILARITY_THRESHOLD,
    )

    app.extensions["faq_matcher"] = faq_matcher

    from .routes.chat import chat_bp

    app.register_blueprint(chat_bp)

    return app