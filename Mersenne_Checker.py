import streamlit as st

# Title
st.title("Mersenne Prime Checker")

# User input
number = st.number_input("Enter a prime number:", min_value=2, step=1, format="%d")

# When button is clicked
if st.button("Check Mersenne Prime"):
    mersenne = 2 ** number - 1
    st.write(f"### Mersenne number is: {mersenne}")

    # Lucas-Lehmer Test
    s = 4
    steps = ""
    for count in range(1, number - 1):
        s = (s * s - 2) % mersenne
        steps += f"Step {count}: s = {s}\n"

    # Show steps
    st.text_area("Lucas-Lehmer Test Steps", steps.strip(), height=300)

    # Final result
    if s == 0:
        st.success(f"✅ 2^{number} - 1 is a Mersenne Prime!")
    else:
        st.error(f"❌ 2^{number} - 1 is NOT a Mersenne Prime.")
