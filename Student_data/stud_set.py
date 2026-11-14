import pandas as pd


# Creating a fictional student dataset
data = {
    "Student ID": [
        "26/3459", "23/9865", "22/2958", "24/3455", "23/3467",
        "23/3075", "21/5674", "20/3789", "23/0094", "21/4329"
    ],

    "Department": [
        "Cocis", "CASMASS", "COHEALTHS",
        "COCIS", "COMED", "COCOM",
        "COCOM", "COPAS", "CASMAS",
        "COLENSMA"
    ],

    "Level": [
        100, 200, 300, 400, 100,
        200, 300, 400, 200, 100
    ],

    "Attendance Percentage": [
        85, 90, 78, 95, 82,
        88, 70, 92, 80, 96
    ],

    "Cumulative Grade Point Average": [
        5.0, 2.0, 4.0, 3.50, 4.84,
        5.0, 3.94, 2.45, 4.76, 4.23
    ]
}

# Convert the dataset into a DataFrame
df = pd.DataFrame(data)

# Display the dataset
print(df)
print(df)
