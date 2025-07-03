import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="This page is for DNHT",
    layout="centered",
    initial_sidebar_state="collapsed"
)

custom_css_js = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes typewriter {
    from { width: 0; }
    to { width: 23ch; }
}

@keyframes blink {
    0%, 50% { border-color: #fff; }
    51%, 100% { border-color: transparent; }
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
}

@keyframes sparkle {
    0%, 100% { opacity: 0; transform: scale(0); }
    50% { opacity: 1; transform: scale(1); }
}

.main-container {
    height: 500px;
    width: 700px;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(20px);
    border-radius: 30px;
    padding: 60px 40px;
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.3);
    position: relative;
    overflow: hidden;
}

.main-container::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
    animation: shimmer 3s infinite;
}

@keyframes shimmer {
    0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
    100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
}

.typewriter-text {
    font-size: 2.5rem;
    font-weight: 700;
    color: #fff;
    text-align: center;
    margin-bottom: 40px;
    overflow: hidden;
    border-right: 4px solid #fff;
    white-space: nowrap;
    margin: 0 auto 40px auto;
    animation:
        typewriter 4s steps(26) infinite alternate,
        blink 1s step-end infinite,
        float 3s ease-in-out infinite;
    width: fit-content;
    text-shadow: 0 0 20px rgba(255, 255, 255, 0.5);
}


.question-container {
    position: relative;
    width: 100%;
    height: 100%;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: center;
}

.btn {
    position: absolute;
    padding: 18px 36px;
    font-size: 1.2rem;
    font-weight: 600;
    border: none;
    border-radius: 0px; /* <--- Make buttons rectangular */
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    font-family: 'Poppins', sans-serif;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(10px);
    z-index: 10;
    min-width: 120px;
    text-align: center;
}

#yes-button {
    position: relative; /* not absolute! */
    margin: 0 10px;
    animation: pulse 2s infinite, heartbeat 1.5s infinite;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    box-shadow: 0 0 30px rgba(102, 126, 234, 0.6);
    border-radius: 30px;
}


#yes-button:hover {
    transform: translate(-50%, -50%) scale(1.1);
    box-shadow: 0 0 40px rgba(102, 126, 234, 0.8);
    background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
}

#no-button {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    color: white;
    transition: all 0.4s ease;
    opacity: 0.9;
    border-radius: 30px;
}

#no-button:hover {
    opacity: 1;
    transform: scale(1.05);
}

.hearts {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    overflow: hidden;
}

.heart {
    position: absolute;
    color: rgba(255, 255, 255, 0.7);
    font-size: 20px;
    animation: sparkle 3s infinite;
}

.heart:nth-child(1) { top: 10%; left: 20%; animation-delay: 0s; }
.heart:nth-child(2) { top: 20%; right: 15%; animation-delay: 0.5s; }
.heart:nth-child(3) { bottom: 30%; left: 10%; animation-delay: 1s; }
.heart:nth-child(4) { bottom: 15%; right: 20%; animation-delay: 1.5s; }
.heart:nth-child(5) { top: 60%; left: 80%; animation-delay: 2s; }

.emoji-rain {
    position: fixed;
    top: -50px;
    font-size: 30px;
    animation: fall 3s linear infinite;
    pointer-events: none;
    z-index: 1000;
}

@keyframes fall {
    to {
        transform: translateY(100vh) rotate(360deg);
    }
}

.success-message {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    color: white;
    padding: 30px 50px;
    border-radius: 20px;
    font-size: 1.5rem;
    font-weight: 600;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    z-index: 1001;
    animation: slideIn 0.5s ease-out;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translate(-50%, -60%);
    }
    to {
        opacity: 1;
        transform: translate(-50%, -50%);
    }
}

@media (max-width: 768px) {
    .main-container {
        padding: 40px 20px;
        margin: 20px;
    }

    .typewriter-text {
        font-size: 1.8rem;
    }

    .question-container {
        position: relative;
        width: 300px;
        height: 280px;
    }

    .btn {
        padding: 15px 30px;
        font-size: 1rem;
    }
}
</style>

<div class="main-container">
    <div class="hearts">
        <div class="heart">💖</div>
        <div class="heart">💕</div>
        <div class="heart">💗</div>
        <div class="heart">💓</div>
        <div class="heart">💝</div>
    </div>

    <div class="typewriter-text">Do you love Do Xuan Trong?</div>

    <div class="question-container">
        <button id="yes-button" class="btn" onclick="handleYesClick()">
            Yes, I do!
        </button>
        <button id="no-button" class="btn" onmouseover="moveNoButton()" onclick="handleNoClick()">
            No
        </button>
    </div>
</div>

<script>
let cornerPosition = 0;
let yesClicked = false;

const corners = [
    { top: 'calc(50% - 130px)', left: 'calc(50% - 200px)' }, // Top-left (was 100,150)
    { top: 'calc(50% - 130px)', left: 'calc(50% + 200px - 120px)' }, // Top-right
    { top: 'calc(50% + 130px - 45px)', left: 'calc(50% + 200px - 120px)' }, // Bottom-right
    { top: 'calc(50% + 130px - 45px)', left: 'calc(50% - 200px)' }  // Bottom-left
];


function positionNoButton() {
    const noButton = document.getElementById('no-button');
    if (!noButton) return;

    const position = corners[cornerPosition];

    noButton.style.top = '';
    noButton.style.bottom = '';
    noButton.style.left = '';
    noButton.style.right = '';

    noButton.style.top = position.top;
    noButton.style.left = position.left;
}

function moveNoButton() {

    cornerPosition = (cornerPosition + 1) % corners.length;
    positionNoButton();

    const noButton = document.getElementById('no-button');
    if (noButton) {
        noButton.style.animation = 'none';
        setTimeout(() => {
            noButton.style.animation = '';
        }, 10);
    }
}

function createEmojiRain(emoji) {
    for (let i = 0; i < 50; i++) {
        setTimeout(() => {
            const emojiElement = document.createElement('div');
            emojiElement.className = 'emoji-rain';
            emojiElement.textContent = emoji;
            emojiElement.style.left = Math.random() * 100 + '%';
            emojiElement.style.animationDelay = Math.random() * 2 + 's';
            emojiElement.style.animationDuration = (Math.random() * 3 + 2) + 's';
            document.body.appendChild(emojiElement);

            setTimeout(() => {
                emojiElement.remove();
            }, 5000);
        }, i * 100);
    }
}

function showSuccessMessage() {
    const message = document.createElement('div');
    message.className = 'success-message';
    message.innerHTML = 'I love you too!';
    document.body.appendChild(message);

    setTimeout(() => {
        message.remove();
    }, 3000);
}

function handleYesClick() {
    yesClicked = true;
    createEmojiRain('💖');
    showSuccessMessage();

    // Send event to Streamlit
    window.parent.postMessage({
        type: 'streamlit:componentReady',
        data: { clicked: 'Yes' }
    }, '*');
}

function handleNoClick() {
    createEmojiRain('💔');
    window.parent.postMessage({
        type: 'streamlit:componentReady',
        data: { clicked: 'No' }
    }, '*');
}

setTimeout(() => {
    cornerPosition = 0;
    positionNoButton();
}, 500);
</script>
"""

components.html(custom_css_js, height=600, width=1000, scrolling=True)

st.markdown("""
<style>
.stApp > header {
    background-color: transparent;
}

.stApp {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.success-response {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    color: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 1.2rem;
    font-weight: 600;
    margin: 20px 0;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    animation: slideUp 0.5s ease-out;
}

.warning-response {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    color: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 1.2rem;
    font-weight: 600;
    margin: 20px 0;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    animation: slideUp 0.5s ease-out;
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
""", unsafe_allow_html=True)
