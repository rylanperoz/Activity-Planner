import streamlit as st
import random

# Page setup
st.set_page_config(
    page_title="Activity Planner for Gö",
    page_icon="✨",
    layout="centered"
)

# Title and intro
st.title("✨ Activity Planner for Gö ✨")
st.markdown(
    "Pick the **weather** and your **mood**, and I'll suggest a fun activity for us 😏"
)
st.write("---")

# Smaller headers
st.markdown("#### 🌤️ Weather")
weather = st.selectbox("Choose the weather:", ["Clear skies", "Overcast"])

st.markdown("#### 🧠 Mood")
mood = st.selectbox(
    "How are you feeling?", 
    ["Overwhelmed", "High Engagement", "Energetic", "Quiet Relaxation"]
)

# Activity dictionary
activity_dict = {
    "Overwhelmed": ["🛌 Take some alone time — recharge and relax"],
    "High engagement": {
        "Clear skies": [
            "🌳 Enjoy some quality time in the botanical garden",
        ],
        "Gloomy": [
            "☕ Cozy up at a café and have a good chat",
            "🎨 Painting something silly",
        ]
    },
    "Energetic": {
        "Clear skies": [
            "🚶 Take a lively walk through the city and explore",
        ],
        "Gloomy": [
            "🛒 Go on a fun grocery run",
            "🧁 Baking something sweet together",
        ]
    },
    "Quiet relaxation": {
        "Clear skies": [
            "👀 Sit back and do some relaxing people-watching",
        ],
        "Gloomy": [
            "📚 Browse a bookstore together",
            "🎬 Watch a short film or documentary "
        ]
    }
}

# Bonus surprises with playful messages
bonus_messages = [
    "💌 Psst… secretly, I think you're amazing 😏",
    "🌟 Small adventure tip: take my hand for a surprise twist 😉",
    "🎶 Imagine a fun soundtrack playing while we do this!",
    "🍦 Bonus idea: ice cream afterwards? Just saying…",
    "😂 If we do this, we might laugh way too much"
]

# Button to suggest activity
if st.button("🎉 Suggest Activity"):
    # Choose activity
    if mood == "Overwhelmed":
        activity = activity_dict[mood][0]
    else:
        activity = random.choice(activity_dict[mood][weather])
    st.markdown(f"### ✨ {activity}")

    # 25% chance for bonus message
    if random.random() < 0.25:
        bonus = random.choice(bonus_messages)
        # Pink styled bonus message
        st.markdown(
            f"<p style='color:#FF69B4; font-size:20px;'>✨ {bonus} ✨</p>", 
            unsafe_allow_html=True
        )
        # 🎉 Confetti effect
        st.balloons()

# Footer
st.write("---")
st.markdown("16.09.2025")
