Here’s the complete README formatted for GitHub, based on your input:

---

# Polling App 🗳️

A Python-based polling application built using Streamlit. The app allows users to vote, view real-time results, and reset polls. It also features custom CSS for an enhanced visual experience.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Customization](#customization)
- [Conclusion](#conclusion)

## Introduction

This polling application provides a user-friendly platform for voting on options with real-time result tracking. It includes functionality for resetting polls and uses custom CSS to enhance the user interface.

## Features

- **Custom CSS Styling**: Unique background, font colors, and button designs.
- **Real-time Voting**: Instantly updates results as users vote.
- **Data Persistence**: Poll results are saved in a text file and reloaded upon restarting the app.
- **Reset Functionality**: Easily reset poll results to start a new voting session.
- **Progress Bars**: Visualize voting results with progress bars and a bar chart.
- **Streamlit Sidebar Navigation**: Switch between the voting and results pages.

## Technologies Used

- **Programming Language**: Python
- **Framework**: Streamlit
- **Storage Solution**: Text files for saving poll results

## Usage

- **Vote**: Select an option and submit your vote.
- **View Results**: View real-time results in both text format and progress bars.
- **Reset Poll**: Reset the poll results to start a fresh voting session.
- **Navigate**: Use the sidebar to navigate between the voting and results pages.

## Code Overview

- **Custom CSS**: The app uses custom CSS to add a background image and apply a color theme to the interface.
- **Saving and Loading Poll Results**: The app saves poll results to a text file (`poll_results.txt`) and reloads them when the app is restarted.
- **Voting Mechanism**: The app allows users to select an option and submit their vote. Votes are updated and saved in real-time.
- **Poll Reset**: The poll can be reset, clearing all previous votes and starting fresh.

## Customization

To change the background or colors, modify the CSS section in the `add_custom_css()` function. For example, you can replace the background image URL with your preferred image:

```css
body {
    background-image: url('your-background-image-url');
}
```

## Conclusion

The Polling App is a simple yet powerful tool for collecting votes and displaying results in real-time. With its intuitive interface, real-time updates, and flexible reset options, it provides an efficient way to manage polls. The use of Streamlit allows for rapid development, while the custom CSS adds a personal touch to the user experience. This project can be easily customized for various applications, from casual opinion gathering to decision-making in more formal settings.

Thank you for using the Polling App! Your feedback and contributions are highly appreciated.

---

