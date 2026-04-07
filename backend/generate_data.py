import pandas as pd
import random

data = []

for _ in range(300):  # generate 300 rows

    hours = random.randint(1, 8)
    focus = random.randint(1, 10)
    sleep = random.randint(4, 8)
    difficulty = random.randint(1, 5)
    distractions = random.randint(0, 10)
    revision = random.randint(0, 1)

    # realistic formula (THIS IS IMPORTANT)
    study_time_needed = (
        hours * 0.4 +
        difficulty * 1.5 +
        distractions * 0.3 -
        focus * 0.5 -
        sleep * 0.3 -
        revision * 1.0 +
        random.uniform(-0.5, 0.5)
    )

    # ensure no negative values
    study_time_needed = max(1, round(study_time_needed, 2))

    data.append([
        hours, focus, sleep, difficulty,
        distractions, revision, study_time_needed
    ])

df = pd.DataFrame(data, columns=[
    "hours_studied",
    "focus_level",
    "sleep_hours",
    "difficulty",
    "distractions",
    "revision_done",
    "study_time_needed"
])

df.to_csv("data.csv", index=False)

print("✅ dataset created successfully")