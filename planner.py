from datetime import datetime

def calculate_priority(deadline, difficulty):
    today = datetime.today()
    deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
    days_left = (deadline_date - today).days

    if days_left <= 0:
        days_left = 1

    difficulty_map = {
        "Easy": 1,
        "Medium": 2,
        "Hard": 3
    }

    return (1 / days_left) + difficulty_map[difficulty]


def generate_plan(subjects):
    plan = []

    for sub in subjects:
        score = calculate_priority(sub["deadline"], sub["difficulty"])
        hours = round(score * 2, 1)

        plan.append({
            "subject": sub["name"],
            "hours": hours
        })

    plan = sorted(plan, key=lambda x: x["hours"], reverse=True)
    return plan