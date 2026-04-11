document.addEventListener('DOMContentLoaded', () => {
    // 1. File Upload Interaction
    const fileInput = document.getElementById('resume');
    const labelText = document.getElementById('file-label-text');
    const wrapper = document.querySelector('.file-input-wrapper');

    if (fileInput) {
        fileInput.addEventListener('change', (e) => {
            if (e.target.files[0]) {
                labelText.innerHTML = `Ready to analyze: <b>${e.target.files[0].name}</b>`;
                wrapper.style.borderColor = "var(--primary)";
                wrapper.style.background = "var(--primary-light)";
            }
        });
    }

    // 2. Button Loading State
    const form = document.getElementById('uploadForm');
    const btn = document.getElementById('analyzeBtn');
    if (form) {
        form.addEventListener('submit', () => {
            btn.innerHTML = `<i class="fas fa-spinner fa-spin"></i> Analyzing...`;
            btn.style.opacity = "0.7";
            btn.style.pointerEvents = "none";
        });
    }
});

// 3. Chatbot Logic
function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");
    const text = input.value.trim();

    if (!text) return;

    // Append User message
    appendMessage('user', text);
    input.value = "";

    // Typing indicator
    const tempId = "loading-" + Date.now();
    chatBox.innerHTML += `<div class="msg bot" id="${tempId}">Thinking...</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;

    // Call Backend
    const formData = new URLSearchParams();
    formData.append("message", text);
    formData.append("role", window.resumeContext.prediction);
    window.resumeContext.missing_skills.forEach(s => formData.append("missing_skills", s));

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById(tempId).remove();
        appendMessage('bot', data.reply);
    })
    .catch(() => {
        document.getElementById(tempId).innerHTML = "Sorry, I encountered an error.";
    });
}

function appendMessage(type, text) {
    const chatBox = document.getElementById("chat-box");
    const div = document.createElement("div");
    div.className = `msg ${type}`;
    div.innerHTML = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}