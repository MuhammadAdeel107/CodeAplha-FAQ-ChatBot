from flask import (
    Blueprint,
    current_app,
    jsonify,
    render_template,
    request,
)


chat_bp = Blueprint(
    "chat",
    __name__,
)


@chat_bp.get("/")
def index():
    return render_template("index.html")


@chat_bp.post("/api/chat")
def chat():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify(
            {
                "error": "Request body must be valid JSON."
            }
        ), 400

    question = data.get("question")

    if not isinstance(question, str):
        return jsonify(
            {
                "error": "The 'question' field must be a string."
            }
        ), 400

    question = question.strip()

    if not question:
        return jsonify(
            {
                "error": "Question cannot be empty."
            }
        ), 400

    matcher = current_app.extensions["faq_matcher"]

    result = matcher.find_best_match(question)

    return jsonify(result)