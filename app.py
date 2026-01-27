import streamlit as st
from predictor_logic import (
    get_expected_colleges,
    check_selected_college,
    get_top5_colleges
)
from data_loader import load_data

st.set_page_config(
    page_title="APEAMCET College Predictor",
    layout="centered"
)

df = load_data()

st.title("APEAMCET College & Branch Predictor")
st.markdown("Enter your rank and preferences to check feasibility and suggestions.")

# -------------------------------
# USER INPUTS
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    user_rank = st.number_input("Enter Your Rank", min_value=1, step=1)
    region = st.selectbox("🌍 Select Region", sorted(df["INST_REG"].dropna().unique()))
    gender = st.selectbox("🚻 Select Gender", ["BOYS", "GIRLS"])

with col2:
    caste = st.selectbox(
        "🧬 Select Caste",
        ["OC","SC","ST","BCA","BCB","BCC","BCD","BCE","OC_EWS"]
    )

# -------------------------------
# Dynamic dropdowns
# -------------------------------
st.markdown("### 🎯 Preference Selection")

colleges = sorted(df["NAME OF THE INSTITUTION"].dropna().unique())
branches = sorted(df["branch_code"].dropna().unique())

college_pref = st.selectbox(
    "🏫 Select Preferred College (Scroll)",
    ["-- None --"] + colleges
)

branch_pref = st.selectbox(
    "📚 Select Preferred Branch (Scroll)",
    ["-- None --"] + branches
)

# -------------------------------
# BUTTON
# -------------------------------
if st.button("🔍 Predict College & Branch"):

    if user_rank <= 0:
        st.error("Please enter a valid rank.")
    else:
        # -------------------------------
        # FEASIBILITY CHECK FIRST
        # -------------------------------
        status = None

        if college_pref != "-- None --" and branch_pref != "-- None --":

            st.subheader("🎯 Feasibility Result")

            status, message = check_selected_college(
                user_rank, caste, gender,
                college_pref, branch_pref
            )

            if status:
                st.success(message)
            else:
                st.error(message)

        else:
            st.info("Select both College and Branch to check feasibility.")

        # -------------------------------
        # EXPECTED COLLEGES LIST BELOW
        # -------------------------------
        st.subheader("📌 Expected Colleges & Branches You Can Get")

        expected = get_expected_colleges(
            user_rank, caste, gender, region
        )

        if expected.empty:
            st.warning("No colleges found for your rank and category.")
        else:
            # 🔥 REMOVE SIDE SERIAL NUMBERS
            st.dataframe(
                expected.head(15).reset_index(drop=True),
                use_container_width=True
            )

        # -------------------------------
        # TOP 5 FALLBACK
        # -------------------------------
        if college_pref != "-- None --" and branch_pref != "-- None --":
            if status is False:
                st.subheader("🏆 Top 5 Colleges & Branches (Best Options)")

                top5 = get_top5_colleges(
                    user_rank, caste, gender, region
                )

                st.dataframe(
                    top5.reset_index(drop=True),
                    use_container_width=True
                )
