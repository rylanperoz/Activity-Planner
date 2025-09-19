import streamlit as st
import random

# Page setup
st.set_page_config(
    page_title="Activity Planner for Aachen",
    page_icon="✨",
    layout="centered"
)

# Title and intro
st.title("✨ Activity Planner for Aachen ✨")
st.markdown(
    "Pick the Time of Day & your Mood, or try out something Exclusive if you're feeling adventurous 😏"
)
st.write("---")

# Category selection
category = st.radio("Choose a Category:", ["Time & Mood 🌀", "Exclusive Moments 🪄"])

# -----------------------------
# TIME & MOOD PATH
# -----------------------------
if category == "Time & Mood 🌀":
    st.markdown("#### ⏰ Time of Day")
    time_of_day = st.selectbox("Choose the time of day:", ["Morning", "Noon", "Evening", "Night"])

    st.markdown("#### 🧠 Mood")
    mood = st.selectbox(
        "How are you feeling?",
        ["Hungry", "Overwhelmed", "Quiet Relaxation", "High Engagement", "Energetic & Outdoorsy"]
    )

    # Activity dictionary
    activity_dict = {
        "High Engagement": {
            "Morning": ["☕ Morning coffee run & chat"],
            "Noon": ["🌯 Brunch at a local spot"],
            "Evening": ["🍵 Chai & Charcha"],
            "Night": ["🔭 Stargazing"]
        },
        "Energetic & Outdoorsy": {
            "Morning": ["🥕 Explore a nearby farmer's market"],
            "Noon": ["🏛️ Visit some local attractions"],
            "Evening": ["🌳 Explore a nearby park or garden"],
            "Night": ["🍻 Pub Crawl"]
        },
        "Quiet Relaxation": {
            "Morning": ["📖 Read together over coffee"],
            "Noon": ["🎶 Listen to music and people-watch"],
            "Evening": ["🌄 Catch the sunset from Lousberg"],
            "Night": ["🌇 Watch the city wind down from the townhall steps"]
        },
        "Hungry": {
            "Morning": ["🍰 Kaffee & Kuchen"],
            "Noon": ["🥙 Brunch at a local spot"],
            "Evening": ["🍜 Cozy dinner"],
            "Night": ["🍧Ice cream run"]
        }
    }

    if st.button("🎉 Suggest Activity"):
        if mood == "Overwhelmed":
            activity = "🛌 Take some time off to rest & recharge"
        else:
            activity = random.choice(activity_dict[mood][time_of_day])
        st.markdown(f"### 🌟 {activity}")

# -----------------------------
# EXCLUSIVE MOMENTS PATH
# -----------------------------
elif category == "Exclusive Moments 🪄":
    st.markdown(
        "💫 I like the confidence 😏 Here are some special, more personalized activities 💫"
    )

    exclusive_activities = [
        "🎨 Paint something silly",
        "🏙️ Wander around in a nearby city/country",
        "🧁 Whip up something tasty",
        "🎬 Watch a movie",
        "🎶 Make a mini playlist",
        "🏞️ Hike to a quaint cafe in Belgium",
    ]

    if st.button("🔒 Reveal Exclusive Idea"):
        activity = random.choice(exclusive_activities)
        st.markdown(f"### 🔓 {activity}")

# Footer
st.write("---")
st.markdown(
    "<div style='text-align: center;'>📅 19.09.2025 &nbsp;&nbsp;|&nbsp;&nbsp; 📍 Aachen <br>Curated by Subject Rizz for Queen Bee</div>",
    unsafe_allow_html=True
)

