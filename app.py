import streamlit as st

st.title("Just-in-Time Knowledge Assistant")

st.subheader("Active Case Context")
claim_type = st.selectbox("Claim Type", ["Flood", "Fire", "Health"])
state = st.selectbox("State", ["Florida", "California", "Texas"])

st.divider()

st.subheader("Suggested Policy Guidance")

if claim_type == "Flood" and state == "Florida":
    st.success(
        "Flood insurance claims in Florida require proof of loss "
        "submission within 30 days.\n\n"
        "Source: FEMA_Flood_Policy.pdf\n"
        "Page 12, Section 4.2"
    )
else:
    st.info(
        "No high-risk policy conflicts detected.\n\n"
        "Source: Internal SOP Claims Handbook\n"
        "Page 3, Section 1.1"
    )
