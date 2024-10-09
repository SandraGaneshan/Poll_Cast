import streamlit as st

# Set Streamlit page configuration
st.set_page_config(
    page_title="Polling App",
    page_icon="🗳️",
    layout="centered",
    initial_sidebar_state="expanded"
)


# Add custom CSS for background and theme
def add_custom_css():
    st.markdown("""
        <style>
        /* Background image */
        body {
            background-image: url('https://www.publicdomainpictures.net/pictures/320000/nahled/background-image.png');
            background-size: cover;
            background-position: center;
        }

        /* Custom font and colors */
        .css-18e3th9 {
            font-family: 'Arial', sans-serif;
            color: #1f4e79;
        }

        .css-1d391kg, .css-18e3th9 {
            color: #f5f5f5 !important;
        }

        /* Sidebar styling */
        .css-1d391kg {
            background-color: #1f4e79;
        }

        /* Main title styling */
        .css-12ttj6m {
            color: #f5f5f5;
        }

        /* Custom button styling */
        button {
            background-color: #008CBA !important;
            color: white !important;
        }

        </style>
    """, unsafe_allow_html=True)


add_custom_css()  # Apply the custom CSS for the app

# Poll options and vote storage
poll_options = {'Option 1': 0, 'Option 2': 0, 'Option 3': 0, 'Option 4': 0}
poll = poll_options.items()


# Function to save poll results to a file
def save_results():
    try:
        with open("poll_results.txt", "w") as obj1:
            for option, votes in poll:  # unpack
                obj1.write(f"{option}: {votes} votes\n")
    except Exception as e:
        st.error(f"Error saving results: {e}")


# Function to load poll results from a file
def load_results():
    try:
        with open("poll_results.txt", "r") as obj2:
            lines = obj2.readlines()  # ["Option 1: 0 votes\n", "Option 2: 0 votes\n", "Option 3: 0 votes\n", "Option 4: 0\n"]
            for i in lines:
                options, votes = i.strip().split(': ')
                poll_options[options] = int(votes.split()[0])
    except FileNotFoundError:
        pass  # If file doesn't exist, continue with default values
    except Exception as e:
        st.error(f"Error loading results: {e}")


# Function to reset poll results
def reset_results():
    for i in poll_options.keys():
        poll_options[i] = 0
    save_results()  # Save reset results to file


# Main function for the Polling App
def main():
    st.title("🗳️ Polling App")
    st.markdown("### 🎉 *Vote for Your Favorite Option*")

    # Load results if available
    load_results()

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page", ("📩 Vote", "📊 Results"))

    # Buttons for refresh and reset
    st.sidebar.button("🔄 Refresh Results", on_click=load_results)
    if st.sidebar.button("❌ Reset Poll"):
        reset_results()
        st.success("Poll has been reset.")

    # Voting Page
    if page == "📩 Vote":
        st.subheader("Make Your Choice:")

        # Radio button to choose the poll option
        vote = st.radio("Choose an option:", list(poll_options.keys()))

        # Button to submit the vote
        if st.button("✅ Submit Your Vote"):
            poll_options[vote] += 1
            st.success(f"🎉 You voted for: *{vote}*")
            save_results()  # Save results after voting

    # Results Page
    elif page == "📊 Results":
        st.subheader("📊 Current Poll Results")

        # Display the current poll results with a progress bar
        total_votes = sum(poll_options.values()) or 1  # Prevent division by zero
        for option, votes in poll_options.items():
            st.write(f"*{option}*: {votes} votes")
            st.progress(votes / total_votes)  # Show progress bar for each option

        # Display the results as a bar chart
        st.bar_chart(poll_options)

    # Additional information
    st.markdown("### 🙏 *Thank you for participating!*")


if __name__ == "__main__":
    main()
