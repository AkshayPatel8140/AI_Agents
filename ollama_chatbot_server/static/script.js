async function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    if (!message) return;

    appendChat("👤 You", message);
    input.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    });
    const data = await response.json();
    appendChat("🤖 AI", data.reply);
    // speak(data.reply);
}

function appendChat(sender, text) {
    const chat = document.getElementById("chat");
    chat.innerHTML += `${sender}: ${text}\n\n`;
    chat.scrollTop = chat.scrollHeight;
}

function speak(text) {
    const synth = window.speechSynthesis;
    const utter = new SpeechSynthesisUtterance(text);
    synth.speak(utter);
}

function startVoiceInput() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";
    recognition.interimResults = false;

    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        document.getElementById("userInput").value = transcript;
        sendMessage();
    };

    recognition.onerror = (event) => {
        alert("Speech recognition error: " + event.error);
    };

    recognition.start();
}