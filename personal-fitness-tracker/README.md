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
   ->    git clone https://github.com/Aakash315/python-learning.git
   ->    cd  python-learning/personal-fitness-tracker
2. **Run the program**
   ->    project.py

## 📂 File Structure

.
├── project.py       # Main Python script

├── fitness_data.json        # Auto-generated file to store user data

└── README.md                # Project documentation

## 🧰 How to Use

When you run the program, you'll see a menu with the following options:

=== FITNESS TRACKER MENU ===

1. Add New Workout
2. View Recent Workouts
3. Weekly Summary
4. Monthly Report
5. Set Goals
6. View Progress
7. Exit

Choose an option:


### 1. Add New Workout

=== Add New Workout ===
Exercise Types:

1. Running
2. Swimming
3. Cycling
   Choose exercise type: 1

=== Running Workout ===
Date (dd-mm-yyyy): 09-06-2025
Distance (km): 5.2
Duration (minutes): 28
Route (optional): Park Loop

✅ Running workout saved successfully!
Date: 09-06-2025 | Duration: 28 mins | Distance: 5.2 km
Estimated calories burned: 312

### 2. View Recent Workouts

=== RECENT WORKOUTS (Last 7 days) ===

🏃 Monday, 09-06-2025 - Running
   Distance: 5.2 km | Duration: 28 mins | Calories: 312
   Pace: 5:23 min/km | Route: Park Loop

🏊 Sunday, 08-06-2025 - Swimming
   Laps: 40 | Duration: 45 mins | Calories: 398
   Stroke: Freestyle | Pool: 25m

🚴 Friday, 06-06-2025 - Cycling
   Distance: 15.8 km | Duration: 52 mins | Calories: 445
   Speed: 18.2 km/h | Terrain: Mixed

Total: 3 workouts | 125 minutes | 1,155 calories

### 3. Weekly Summary

=== WEEKLY SUMMARY  ===

📊 Overview:
Total Workouts: 5
Total Duration: 183 minutes (3.05 hours)
Total Calories: 1,847
Average per workout: 37 mins, 369 calories

📈 Breakdown by Exercise:
Running: 2 workouts (50 mins, 590 calories)
Swimming: 2 workouts (83 mins, 812 calories)
Cycling: 1 workout (52 mins, 445 calories)

🔥 Best Day: Friday, 06-06-2025 (445 calories)
📅 Workout Days: Mon, Wed, Fri, Sun, Mon
⚡ Current Streak: 2 days

### 4. Monthly Report

=== MONTHLY REPORT (June 2025) ===

📊 Statistics:
Total Workouts: 12
Total Duration: 8.2 hours
Total Calories: 4,234
Average per workout: 41 mins, 353 calories

📈 Weekly Breakdown:
Week 1 (01-07 June): 3 workouts, 1,245 calories
Week 2 (08-14 June): 5 workouts, 1,847 calories
Week 3 (15-21 June): 4 workouts, 1,142 calories

🏆 Personal Records:
Longest run: 8.5 km (15-06-2025)
Most laps: 50 laps (12-06-2025)
Longest workout: 65 minutes (18-06-2025)

📅 Most Active Day: Monday (4 workouts)
🔥 Best Week: Week 2 (5 workouts)

### 5. Set Goals

=== GOAL SETTING ===

Current Goals:
Weekly Calorie Goal: 2,000 calories
Weekly Workout Goal: 4 workouts
Monthly Distance Goal: 100 km

1. Update Weekly Calorie Goal
2. Update Weekly Workout Goal
3. Update Monthly Distance Goal
4. Back to Main Menu

Choose option: 1

Current weekly calorie goal: 2,000
Enter new weekly calorie goal: 2,500

✅ Weekly calorie goal updated to 2,500 calories!

### 6. View Progress

=== PROGRESS TRACKING ===

🎯 Current Week Goals (03-06-2025 to 09-06-2025):
┌─────────────────────────────────────────────┐
│ Weekly Calories: 1,847/2,500 (74%) 🔄      │
│ ████████████████░░░░░░               74%    │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ Weekly Workouts: 5/4 (125%) ✅             │
│ ████████████████████████████████   125%     │
└─────────────────────────────────────────────┘

🏆 Achievements This Week:
✅ "Consistency King" - 5 workouts completed
🔄 "Calorie Crusher" - Need 153 more calories

📈 Trends:

- Workout frequency: Up 25% from last week
- Average calories per workout: 369 (↑12%)
- Longest streak this month: 5 days

### 7: Exit

=== FITNESS TRACKER ===

Data saved to fitness_data.json
Thanks for using Personal Fitness Tracker!
Keep up the great work! 💪

Program terminated.

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
