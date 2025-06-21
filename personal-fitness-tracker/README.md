# 🏋️ Personal Fitness Tracker

A command-line based Personal Fitness Tracker written in Python. This application helps users log their workouts, track calories, monitor their weekly and monthly progress, and set personalized fitness goals.

## 🚀 Features

* ✅ Add  **Running** ,  **Swimming** , or **Cycling** workouts
* 📅 Track  **daily** ,  **weekly** , and **monthly** activity
* 🔥 Automatic **calorie estimation** based on METs
* 🎯 Set and monitor **fitness goals**
* 📊 Detailed summaries with trends and personal records
* 💾 Automatically saves data to a JSON file

## 🛠️ Installation

1. **Clone the repository**
   ->    git clone https://github.com/Aakash315/python-learning/personal-fitness-tracker.git
   ->    cd personal-fitness-tracker
2. **Run the program**
   ->    project.py

## 📂 File Structure

.
├── project.py       # Main Python script
├── fitness_data.json        # Auto-generated file to store user data
└── README.md                # Project documentation


## 🧰 How to Use

When you run the program, you'll see a menu with the following options:

1. Add New Workout
2. View Recent Workouts
3. Weekly Summary
4. Monthly Report
5. Set Goals
6. View Progress
7. Exit

### 1. Add New Workout

Log running, swimming, or cycling sessions, including details like distance, duration, laps, stroke type, etc. Calories are calculated automatically.

### 2. View Recent Workouts

Shows today's workouts with key stats like distance, pace, and calories burned.

### 3. Weekly Summary

Summarizes your past 7 days, including:

* Number of workouts
* Total duration and calories
* Best workout day and streaks

### 4. Monthly Report

Provides a breakdown of workouts by week, personal records, and activity trends for the current month.

### 5. Set Goals

Set or update:

* Weekly calorie goal
* Weekly workout goal
* Monthly distance goal

### 6. View Progress

Visual progress bars and icons show how you're doing compared to your goals with week-to-week comparisons and trend analysis.


## 🧠 Technologies Used

* Python 3
* `datetime` for time-based operations
* `json` for saving and loading workout data
* Command-line interface (no external libraries needed)


## 📌 Notes

* All data is saved to a local file: `fitness_data.json`
* Pace, speed, and calorie calculations are based on simplified MET formulas
* Lightweight and runs entirely offline


## 🙌 Acknowledgements

Inspired by the need for a simple, lightweight, and private fitness tracker without relying on online accounts or apps.
