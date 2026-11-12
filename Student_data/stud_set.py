import pandas as pd


# Creating a fictional student dataset
data = {
    "Student ID": [
        "ST001", "ST002", "ST003", "ST004", "ST005",
        "ST006", "ST007", "ST008", "ST009", "ST010"
    ],

    "Department": [
        "Computer Science", "Mathematics", "Physics",
        "Computer Science", "Statistics", "Biology",
        "Physics", "Computer Science", "Statistics",
        "Mathematics"
    ],

    "Level": [
        100, 200, 300, 400, 100,
        200, 300, 400, 200, 100
    ],

    "Attendance Percentage": [
        85, 90, 78, 95, 82,
        88, 70, 92, 80, 96
    ],

    "Average Examination Score": [
        75, 82, 68, 90, 73,
        85, 60, 88, 70, 94
    ]
}

# Convert the dataset into a DataFrame
df = pd.DataFrame(data)

# Display the dataset
print(df)