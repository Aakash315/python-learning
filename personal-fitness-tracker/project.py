
# === 1. IMPORTS ===
import json
from datetime import datetime
from datetime import timedelta
from itertools import groupby
import calendar


# === 2. BASE EXERCISE CLASS ===

class Exercise:
    def __init__(self, date, duration, exercise_type, notes=""):
        self.date = date  # dd-mm-yyyy format
        self.duration = duration  # in minutes
        self.exercise_type = exercise_type
        self.weight = 70
        self.notes = notes
        self.calories = 0

    def estimate_calories(self, mets):
        self.calories = mets * self.weight * (self.duration / 60)
        return self.calories


# Inherited Classes
class Running(Exercise):
    def __init__(self, date, duration, distance, route=""):
        super().__init__(date, duration, "Running")
        self.distance = distance    # in km
        self.route = route
        self.pace = self.calculate_pace()
        self.calories = self.running_calories()

    def calculate_pace(self):
        return self.duration / self.distance

    def running_calories(self):
        if self.pace < 4:
            mets = 12
        elif self.pace < 5:
            mets = 10
        elif self.pace < 6:
            mets = 8
        else:
            mets = 6

        return self.estimate_calories(mets)


class Swimming(Exercise):
    def __init__(self, date, duration, laps, stroke_type, pool_length=25):
        super().__init__(date, duration, "Swimming")
        self.laps = laps
        self.stroke_type = stroke_type
        self.pool_length = pool_length
        self.calories = self.swimming_calories()

    def swimming_calories(self):
        if self.stroke_type == "freestyle":
            mets = 8
        elif self.stroke_type == "backstroke":
            mets = 7
        elif self.stroke_type == "breaststroke":
            mets = 10
        elif self.stroke_type == "butterfly":
            mets = 12
        else:
            mets = 8

        return self.estimate_calories(mets)


class Cycling(Exercise):
    def __init__(self, date, duration, distance, terrain="Road"):
        super().__init__(date, duration, "Cycling")
        self.distance = distance
        self.terrain = terrain
        self.speed = self.calculate_speed()
        self.calories = self.cycling_calories()

    def calculate_speed(self):
        return round((self.distance * 60) / self.duration)

    def speed_mets(self):
        if self.speed >= 25:
            return 12
        elif self.speed >= 20:
            return 10
        elif self.speed >= 15:
            return 8
        else:
            return 6

    def terrain_multiplier(self):
        if self.terrain == "road":
            return 1.0
        elif self.terrain == "hills":
            return 1.3
        elif self.terrain == "mountain":
            return 1.5
        else:
            return 1.2

    def cycling_calories(self):
        mets = (self.speed_mets() * self.terrain_multiplier())
        return self.estimate_calories(mets)


# === 3. FILE HANDLING ===

def save_to_json(workouts, goals, filename="fitness_data.json"):
    data = {
        "goals": goals,
        "workouts": workouts
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    # print("✅ Data saved successfully.")


def load_from_json(filename="fitness_data.json"):
    default_goals = {
        "weekly_calories": 2000,
        "weekly_workouts": 4,
        "monthly_distance": 50
    }
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            workouts = data.get("workouts", [])
            goals = data.get("goals", {})

             # Ensure all required keys are present in goals
            for key, default in default_goals.items():
                goals.setdefault(key, default)

            return workouts, goals 
    except FileNotFoundError:
        return [], default_goals


# === 4. MAIN FUNCTIONALITY MODULES ===

# == ADD NEW WORKOUT ==
def new_workouts(workouts, goals):
    print("===== Add New Workout =====\n")
    print("1. Running\n2. Swimming\n3. Cycling\n")
    add_new1 = int(input("Choose exercise type: "))
    date = input("Date (dd-mm-yyyy): ")

    if add_new1 == 1:
        print("=== Running Workout ===")
        distance = float(input("Distance (km): "))
        duration = int(input("Duration (minutes): "))
        route = input("Route (optional): ")
        run = Running(date, duration, distance, route)
        workouts.append({
            "id": 1,
            "type": "Running",
            "date": date,
            "duration": duration,
            "calories": run.calories,
            "distance": distance,
            "pace": run.pace,
            "route": route
        })
        save_to_json(workouts, goals)
        print("\n✅ Running workout saved successfully!")
        print(
            f"Date: {run.date} | Duration: {run.duration} mins | Distance: {run.distance} km")
        print(f"Estimated calories burned: {run.calories}")

    elif add_new1 == 2:
        print("=== Swimming Workout ===")
        laps = int(input("Number of Laps: "))
        duration = int(input("Duration (minutes): "))
        print("    - Freestyle")
        print("    - Backstroke")
        print("    - Breaststroke")
        print("    - Butterfly")
        print("    - Mixed strokes")
        stroke_type = input("Stroke Type: ").lower()
        swim = Swimming(date, duration, laps, stroke_type)
        workouts.append({
            "id": 2,
            "type": "Swimming",
            "date": date,
            "duration": duration,
            "calories": swim.calories,
            "laps": laps,
            "stroke_type": stroke_type,
            "pool_length": 25
        })
        save_to_json(workouts, goals)
        print("\n✅ Swimming workout saved successfully!")
        print(
            f"Date: {swim.date} | Duration: {swim.duration} mins | Laps: {swim.laps}")
        print(f"Estimated calories burned: {swim.calories}")

    elif add_new1 == 3:
        print("=== Cycling Workout ===")
        distance = float(input("Distance (km): "))
        duration = int(input("Duration (minutes): "))
        print("    - Road")
        print("    - Hills")
        print("    - Mountain")
        print("    - Mixed")
        terrain = input("Terrain: ").lower()
        cycle = Cycling(date, duration, distance, terrain)
        workouts.append({
            "id": 3,
            "type": "Cycling",
            "date": date,
            "duration": duration,
            "calories": cycle.calories,
            "distance": distance,
            "speed": cycle.speed,
            "terrain": terrain
        })
        save_to_json(workouts, goals)
        print("\n✅ Cycling workout saved successfully!")
        print(
            f"Date: {cycle.date} | Duration: {cycle.duration} mins | Distance: {cycle.distance} km")
        print(f"Estimated calories burned: {cycle.calories}")

    else:
        print("Invalid Workout Type")


# == View Recent Workouts ==
def recent_workouts(workouts):
    print("===== RECENT WORKOUTS =====\n")
    today = datetime.today()
    ftoday = today.strftime("%d-%m-%Y")
    weekday = today.strftime("%A")

    todaysworkout = list(
        filter(lambda x: x["date"] == ftoday, workouts))

    total = len(todaysworkout)
    totalDuration = sum([a["duration"] for a in todaysworkout])
    totalCalories = sum([b["calories"] for b in todaysworkout])

    for z in todaysworkout:
        if z["type"] == "Running":
            print(f"🏃 {weekday}, {z["date"]} - {z["type"]}")
            print(
                f"   Distance: {z["distance"]} km | Duration: {z["duration"]} mins | Calories: {z["calories"]}")
            print(
                f"   Pace: {z["pace"]:.2f} min/km | Route: {z["route"]}")
            print("")

        elif z["type"] == "Swimming":
            print(f"🏊 {weekday}, {z["date"]} - {z["type"]}")
            print(
                f"   Laps: {z["laps"]} | Duration: {z["duration"]} mins | Calories: {z["calories"]:.2f}")
            print(
                f"   Stroke: {z["stroke_type"]} | Pool: {z["pool_length"]}")
            print("")

        else:
            print(f"🚴 {weekday}, {z["date"]} - {z["type"]}")
            print(
                f"   Distance: {z["distance"]} km | Duration: {z["duration"]} mins | Calories: {z["calories"]}")
            print(
                f"   Speed: {z["speed"]} | Terrain: {z["terrain"]}")

    print("")
    print(
        f"Total: {total} workouts | {totalDuration} minutes | {totalCalories:.2f} calories")


# == Weekly Summary ==
def weekly_summary(workouts):
    weekly_data = []
    today = datetime.today()
    ftoday = today.strftime("%d-%m-%Y")

    for i in range(7):
        weekDate = today - timedelta(days=i)
        diff_days = weekDate.strftime("%d-%m-%Y")
        weekly_workouts = filter(lambda x: x['date'] == diff_days, workouts)
        weekly_data.extend(list(weekly_workouts))

    firstDate = today-timedelta(days=6)
    fdate = firstDate.strftime("%d-%m-%Y")

    total = len(weekly_data)
    totalDuration = sum([a["duration"] for a in weekly_data])
    totalCalories = sum([b["calories"] for b in weekly_data])
    min_to_hour = totalDuration / 60

    average_duration = round(totalDuration / total)
    average_calories = round(totalCalories / total)

    print(f"===== WEEKLY SUMMARY  ({fdate} to {ftoday})  =====\n")

    print("📊 Overview:")
    print(f"Total Workouts: {total}")
    print(f"Total Duration: {totalDuration} minutes ({min_to_hour:.2f} hours)")
    print(f"Total Calories: {totalCalories:.2f}")
    print(
        f"Average per workout: {average_duration} mins, {average_calories} calories\n")

    def breakDown(exercise):
        weeklyExercise = list(
            filter(lambda x: x['id'] == exercise, weekly_data))
        exerciseTotal = len(weeklyExercise)
        exerciseDuration = sum([t["duration"] for t in weeklyExercise])
        exerciseCalories = sum([s["calories"] for s in weeklyExercise])
        if exercise == 1:
            exerciseType = "Running"
        elif exercise == 2:
            exerciseType = "Swimming"
        else:
            exerciseType = "Cycling"

        print(f" {exerciseType}: {exerciseTotal} workouts ({exerciseDuration} mins, {exerciseCalories:.2f} calories)")

    print(f"📈 Breakdown by Exercise:")
    breakDown(1)
    breakDown(2)
    breakDown(3)

    weekCalories = {}
    for item in weekly_data:
        x = item['date']
        calories = item['calories']
        if x in weekCalories:
            weekCalories[x] += calories
        else:
            weekCalories[x] = calories

    best_day = max(weekCalories, key=weekCalories.get)
    bestCalories = weekCalories[best_day]
    best_day_str = f"{datetime.strptime(best_day, '%d-%m-%Y').strftime('%A, %d-%m-%Y')} ({bestCalories:.2f} calories)"

    workout_days = sorted(set(datetime.strptime(
        w["date"], "%d-%m-%Y").strftime("%a") for w in weekly_data))

    workout_dates = sorted(datetime.strptime(
        w["date"], "%d-%m-%Y") for w in weekly_data)

    def currentStreak(dates):
        if not dates:
            return 0

        max_streak = 1
        current_streak = 1

        for i in range(1, len(dates)):
            delta = (dates[i] - dates[i - 1]).days
            if delta == 1:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            elif delta > 1:
                current_streak = 1

        return max_streak

    print(f"\n🔥 Best Day: {best_day_str}")
    print(f"📅 Workout Days: {', '.join(workout_days)}")
    print("⚡ Current Streak:", currentStreak(workout_dates), "days")


# == Monthly Report ==
def monthly_report(workouts):
    today = datetime.today()
    current_month = today.month
    current_year = today.year
    current_month_name = today.strftime("%b")

    monthly_data = []
    for w in workouts:
        workout_date = datetime.strptime(w["date"], "%d-%m-%Y")
        if workout_date.month == current_month and workout_date.year == current_year:
            w["datetime"] = workout_date
            monthly_data.append(w)

    fdate = today.replace(day=1).strftime("%d-%m-%Y")
    ftoday = today.strftime("%d-%m-%Y")

    total = len(monthly_data)
    totalDuration = sum([a["duration"] for a in monthly_data])
    totalCalories = sum([b["calories"] for b in monthly_data])
    min_to_hour = totalDuration / 60

    if total > 0:
        average_duration = round(totalDuration / total)
        average_calories = round(totalCalories / total)
    else:
        average_duration = 0
        average_calories = 0

    print(
        f"===== MONTHLY SUMMARY ({current_month_name} {current_year}) =====\n")

    print("📊 Statistics:")
    print(f"Total Workouts: {total}")
    print(f"Total Duration: {min_to_hour:.2f} hours")
    print(f"Total Calories: {totalCalories:.2f}")
    print(
        f"Average per workout: {average_duration} mins, {average_calories} calories\n")

    def weekRange(year, month):
        first_day = datetime(year, month, 1)
        week_ranges = []
        while first_day.month == month:
            week_start = first_day
            week_end = week_start + timedelta(days=6)
            if week_end.month != month:
                week_end = datetime(year, month + 1, 1) - timedelta(
                    days=1) if month < 12 else datetime(year + 1, 1, 1) - timedelta(days=1)
            week_ranges.append((week_start, week_end))
            first_day = week_end + timedelta(days=1)
        return week_ranges

    print("📈 Weekly Breakdown:")

    week_ranges = weekRange(current_year, current_month)
    best_week_index = None
    max_week_workouts = 0

    for i, (start, end) in enumerate(week_ranges, 1):
        week_workouts = list(
            filter(lambda w: start <= w["datetime"] <= end, monthly_data))
        week_count = len(week_workouts)
        week_calories = sum(w["calories"] for w in week_workouts)
        print(f"Week {i} ({start.strftime('%d')} - {end.strftime('%d %B')}): {len(week_workouts)} workouts, {week_calories:.2f} calories")

        if week_count > max_week_workouts:
            max_week_workouts = week_count
            best_week_index = i

    maxRunningdist = [x for x in monthly_data if x["type"] == "Running"]
    longestRun = max(maxRunningdist, key=lambda x: x['distance'], default=None)

    maxSwimmingLaps = [x for x in monthly_data if x["type"] == "Swimming"]
    mostLaps = max(maxSwimmingLaps, key=lambda x: x['laps'], default=None)

    longestWorkout = max(
        monthly_data, key=lambda x: x["duration"], default=None)

    print("\n🏆 Personal Records:")
    print(f"Longest run: {longestRun["distance"]} km ({longestRun["date"]})")
    print(f"Most laps: {mostLaps["laps"]} laps ({mostLaps["date"]})")
    print(
        f"Longest workout: {longestWorkout["duration"]} minutes ({longestWorkout["date"]})")
    print("")

    dateCounts = [{keys: len(list(value))} for keys, value in groupby(
        monthly_data, lambda index: index["date"])]
    merged = {k: v for d in dateCounts for k, v in d.items()}
    max_value = max(merged.values())
    most_active_days = [k for k, v in merged.items() if v == max_value]

    activeday = most_active_days[-1]
    fmostActiveDay = datetime.strptime(activeday, "%d-%m-%Y").date()
    activeweekDay = fmostActiveDay .strftime('%A')

    print(f"📅 Most Active Day: {activeweekDay} ({max_value} workouts)")
    print(
        f"🔥 Best Week: Week {best_week_index} ({max_week_workouts} workouts)")


# == Set Goals ==
def set_goals(workouts, goals):
    print("===== GOAL SETTING =====\n")

    print("Current Goals:")
    print(
        f"Weekly Calorie Goal: {goals["weekly_calories"]} calories")
    print(
        f"Weekly Workout Goal: {goals["weekly_workouts"]} workouts")
    print(f"Monthly Distance Goal: {goals["monthly_distance"]} km\n")
    print("   1. Update Weekly Calorie Goal")
    print("   2. Update Weekly Workout Goal")
    print("   3. Update Monthly Distance Goal")
    print("   4. Back to Main Menu\n")
    entry = int(input("Choose option:"))
    match entry:
        case 1:
            print(
                f"Current weekly calorie goal: {goals["weekly_calories"]}")
            new_goal = int(input("Enter new weekly calorie goal:\n"))
            goals["weekly_calories"] = new_goal
            save_to_json(workouts, goals)
            print(
                f"\n✅ Weekly calorie goal updated to {new_goal} calories!")

        case 2:
            print(
                f"Current weekly workout goal: {goals["weekly_workouts"]}")
            new_goal = int(input("Enter new weekly workout goal:\n"))
            goals["weekly_workouts"] = new_goal
            save_to_json(workouts, goals)
            print(
                f"\n✅ Weekly workout goal updated to {new_goal} workouts!")

        case 3:
            print(
                f"Current monthly distance goal: {goals["monthly_distance"]}")
            new_goal = int(
                input("Enter new monthly distance goal:\n"))
            goals["monthly_distance"] = new_goal
            save_to_json(workouts, goals)
            print(
                f"\n✅ Monthly distance goal updated to {new_goal} km!")

        case 4:
            print("Back to Main Menu")

        case _:
            print("Invalid input")


# == View Progress ==
def view_progress():
    def get_week_number(date_str):
        day = datetime.strptime(date_str, '%d-%m-%Y').day
        if 1 <= day <= 7:
            return 1
        elif 8 <= day <= 14:
            return 2
        elif 15 <= day <= 21:
            return 3
        elif 22 <= day <= 28:
            return 4
        elif 29 <= day <= 31:
            return 5
        return None

    def icon(percentage):
        return "✅" if percentage >= 100 else "🔄"

    def build_progress_bar(percentage):
        bar_length = 20
        filled = int(bar_length * min(percentage / 100, 1.0))
        return '█' * filled + '░' * (bar_length - filled)

    def main():
        workouts, goals = load_from_json()

        today = datetime.today()
        month = today.month
        year = today.year
        num_days = calendar.monthrange(year, month)[1]
        first_day = datetime(year, month, 1)

        all_dates = []
        month_data = []
        for i in range(num_days):
            curr_date = first_day + timedelta(days=i)
            date_str = curr_date.strftime('%d-%m-%Y')
            daily_workouts = list(
                filter(lambda w: w['date'] == date_str, workouts))
            all_dates.append(date_str)
            if daily_workouts:
                month_data.extend(daily_workouts)

        week_data = {w: {'totalWorkouts': 0, 'totalCalories': 0,
                         'entries': []} for w in range(1, 6)}
        for entry in month_data:
            week = get_week_number(entry['date'])
            if week:
                week_data[week]['totalWorkouts'] += 1
                week_data[week]['totalCalories'] += entry.get('calories', 0)
                week_data[week]['entries'].append(entry)

        weekday = today.weekday()
        start_of_week = today - timedelta(days=weekday + 1)
        end_of_week = start_of_week + timedelta(days=6)
        formatted_start = start_of_week.strftime('%d-%m-%Y')
        formatted_end = end_of_week.strftime('%d-%m-%Y')

        current_week = get_week_number(today.strftime('%d-%m-%Y'))
        current = week_data.get(
            current_week, {'totalWorkouts': 0, 'totalCalories': 0, 'entries': []})
        previous = week_data.get(
            current_week - 1, {'totalWorkouts': 0, 'totalCalories': 0, 'entries': []})

        calorie_goal = goals.get('weekly_calories', 1)
        workout_goal = goals.get('weekly_workouts', 1)

        calorie_percentage = current['totalCalories'] / calorie_goal * 100
        workout_percentage = current['totalWorkouts'] / workout_goal * 100

        print("\n=== PROGRESS TRACKING ===")
        print(f"\n🎯 Current Week Goals ({formatted_start} to {formatted_end})")

        print(
            f"\nWeekly Calories: {current['totalCalories']:.2f}/{calorie_goal} ({calorie_percentage:.2f}%) {icon(calorie_percentage)}")
        print(build_progress_bar(calorie_percentage),
              f"{calorie_percentage:.2f}%")

        print(
            f"\nWeekly Workouts: {current['totalWorkouts']}/{workout_goal} ({workout_percentage:.2f}%) {icon(workout_percentage)}")
        print(build_progress_bar(workout_percentage),
              f"{workout_percentage:.2f}%")

        print("\n🏆 Achievements This Week:")

        if current['totalWorkouts'] >= 5:
            print("✅ \"Consistency King\" - 5 workouts completed")
        else:
            print(
                f"🔄 \"Consistency King\" - Need {5 - current['totalWorkouts']} more workouts")

        calories_left = max(0, calorie_goal - current['totalCalories'])
        if calories_left == 0:
            print("✅ \"Calorie Crusher\" - Goal reached")
        else:
            print(
                f"🔄 \"Calorie Crusher\" - Need {calories_left:.2f} more calories")

        print("\n📈 Trends:")
        if previous['totalWorkouts'] > 0:
            freq_change = (
                (current['totalWorkouts'] - previous['totalWorkouts']) / previous['totalWorkouts']) * 100
            print(
                f"- Workout frequency: {'Up' if freq_change > 0 else 'Down'} {abs(freq_change):.0f}% from last week")
        else:
            print("- Workout frequency: No data for last week")

        current_avg_cal = (
            current['totalCalories'] / current['totalWorkouts']) if current['totalWorkouts'] else 0
        prev_avg_cal = (previous['totalCalories'] /
                        previous['totalWorkouts']) if previous['totalWorkouts'] else 0
        if prev_avg_cal > 0:
            cal_change = ((current_avg_cal - prev_avg_cal) /
                          prev_avg_cal) * 100
            print(
                f"- Average calories per workout: {int(current_avg_cal)} ({'↑' if cal_change > 0 else '↓'}{abs(cal_change):.0f}%)")
        else:
            print(
                f"- Average calories per workout: {int(current_avg_cal)} (no data for last week)")

        streak = longest = 0
        for i in range(num_days):
            day_str = (first_day + timedelta(days=i)).strftime('%d-%m-%Y')
            if any(w['date'] == day_str for w in workouts):
                streak += 1
                longest = max(longest, streak)
            else:
                streak = 0
        print(f"- Longest streak this month: {longest} days")

    if __name__ == "__main__":
        main()


# === 5. MAIN APPLICATION ===
def start_program():
    workouts, goals = load_from_json()

    while True:
        print("\n======== FITNESS TRACKER MENU ========\n")
        print("1. Add New Workout")
        print("2. View recent Workouts")
        print("3. Weekly Summary")
        print("4. Monthly Report")
        print("5. Set Goals")
        print("6. View Progress")
        print("7. Exit\n")

        menu = int(input("Choose an option:"))

        match menu:
            case 1:
                # ===== Add New Workout =====
                new_workouts(workouts, goals)

            case 2:
                # ===== RECENT WORKOUTS =====
                recent_workouts(workouts)

            case 3:
                # ===== WEEKLY SUMMARY  =====
                weekly_summary(workouts)

            case 4:
                # ===== MONTHLY REPORT =====
                monthly_report(workouts)

            case 5:
                # ===== GOAL SETTING =====
                set_goals(workouts, goals)

            case 6:
                # ===== PROGRESS TRACKING =====
                view_progress()

            case 7:
                print("===== FITNESS TRACKER =====\n")
                print(f"Data saved to fitness_data.json")
                print(f"Thanks for using Personal Fitness Tracker!")
                print(f"Keep up the great work! 💪\n")
                print(f"Program terminated.")
                break

            case _:
                print("Invalid Selection")

# === 6. ENTRY POINT ===
start_program()
