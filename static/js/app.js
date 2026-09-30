const form = document.getElementById("chat-form");
const input = document.getElementById("question");
const chatBox = document.getElementById("chat-box");
const sendButton = document.getElementById("send-button");


function addMessage(message, type) {
    const messageElement = document.createElement("div");

    messageElement.className = `message ${type}-message`;

    const label = document.createElement("div");

    label.className = "message-label";

    label.textContent =
        type === "user"
            ? "You"
            : "Assistant";


    const text = document.createElement("div");

    text.className = "message-text";

    text.textContent = message;


    messageElement.appendChild(label);

    messageElement.appendChild(text);

    chatBox.appendChild(messageElement);

    chatBox.scrollTop = chatBox.scrollHeight;
}


function showTyping() {
    const typingElement = document.createElement("div");

    typingElement.id = "typing-message";

    typingElement.className =
        "message bot-message typing-message";

    typingElement.textContent =
        "Assistant is thinking...";

    chatBox.appendChild(typingElement);

    chatBox.scrollTop = chatBox.scrollHeight;
}


function removeTyping() {
    const typingElement =
        document.getElementById("typing-message");

    if (typingElement) {
        typingElement.remove();
    }
}


async function sendQuestion(question) {
    const response = await fetch("/api/chat", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            question
        })
    });


    const data = await response.json();


    if (!response.ok) {
        throw new Error(
            data.error || "Unable to process the question."
        );
    }


    return data;
}


form.addEventListener("submit", async (event) => {
    event.preventDefault();


    const question = input.value.trim();


    if (!question) {
        return;
    }


    addMessage(question, "user");


    input.value = "";

    input.focus();

    sendButton.disabled = true;

    showTyping();


    try {

        const result = await sendQuestion(question);

        removeTyping();

        addMessage(
            result.answer,
            "bot"
        );

    } catch (error) {

        console.error(error);

        removeTyping();

        addMessage(
            "Sorry, something went wrong. Please try again.",
            "bot"
        );

    } finally {

        sendButton.disabled = false;

        input.focus();
    }
});