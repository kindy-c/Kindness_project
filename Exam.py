# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta
# import us
# import os

# # Removing the 'Tags' column
# df= pd.read_csv(r'C:\Users\surface\Desktop\KINDNESS\RewardsData.csv')
# df = df.drop('Tags', axis=1)

# # Removing the 'Joined on' column
# df = df.drop('Joined On', axis=1)

# # Removing the 'Last seen' column
# df = df.drop('Last Seen', axis=1)

# # Locating the empty cell in the Zip column on row number 438
# if pd.isnull(df.loc[437, 'Zip']):
#     df.loc[437, 'Zip'] = 11011 

# # Limiting to 5 digits in the Zip column
# df['Zip'] = pd.to_numeric(df['Zip'], errors='coerce')
# df['Zip'] = df['Zip'].apply(lambda x: x % 100000 if x >= 100000 else x)
# df['Zip'] = df['Zip'].apply(lambda x: int(x) % 100000 if isinstance(x, int) or (isinstance(x, str) and x.isdigit()) else x)

# # Populating the empty cells in the Zip column with the mean value
# mean_zip = round(df['Zip'].mean(skipna=True))
# df['Zip'] = df['Zip'].fillna(mean_zip)
# df['Zip'] = df['Zip'].astype(int)

# # Capitalizing instances in the City column
# df['City'] = df['City'].str.replace('winston-salem', 'Winston-Salem', case=False)

# # Removing abbreviations in the City column
# df['City'] = df['City'].fillna('')
# df.loc[df['City'].str.isupper(), 'City'] = ''

# # Replacing abbreviations in State column with full State's name
# state_map = {state.abbr: state.name for state in us.states.STATES}
# df['State'] = df['State'].apply(lambda x: state_map.get(x, x))
# state_names = [state.name for state in us.states.STATES]
# empty_state_cells = df[df['State'].isnull() | (df['State'] == '')].index.tolist()

# state_index = 0
# for index in empty_state_cells:
#     df.loc[index, 'State'] = state_names[state_index]
#     state_index += 1
#     if state_index >= len(state_names):
#         state_index = 0

# # Setting the dates in the Birthdate column to the proper format
# df['Birthdate'] = pd.to_datetime(df['Birthdate']).dt.date

# # Replacing empty cells in the Birthdate column with any birthdate of choice
# def generate_random_dates(n):
#     start_date = datetime(1990, 1, 1)
#     end_date = datetime(2010, 12, 31)
#     time_between_dates = end_date - start_date
#     days_between_dates = time_between_dates.days
#     random_number_of_days = np.random.randint(0, days_between_dates, n)
#     return [start_date + timedelta(days=int(days)) for days in random_number_of_days]

# mask = (df['Birthdate'].isnull()) | (df['Birthdate'] == '')
# null_count = mask.sum()
# random_dates = generate_random_dates(null_count)
# df.loc[mask, 'Birthdate'] = [d.date() for d in random_dates]

# # Removing any row in the Zip column not up to 5 digits
# df = df[(df['Zip'] >= 10000) & (df['Zip'] <= 99999)]

# # Populating all empty cells in the City column with 'Thomasville'
# df['City'] = df['City'].apply(lambda x: 'Thomasville' if pd.isnull(x) or str(x).strip() == '' else str(x))


# df.to_csv('New_RewardsData.csv', index=False)


# Uploading the CSV file to database
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='CSV_File',
    user='postgres',
    password='Kindyx@7',
    port='5432'
)

cur = conn.cursor()

# Set the datestyle parameter
cur.execute("SET datestyle TO 'DMY';")

cur.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        "User ID" VARCHAR(255),
        "Birthdate" DATE,
        "City" VARCHAR(255),
        "State" VARCHAR(255),
        "Zip" VARCHAR(10),
        "Available Points" INTEGER,
        "Total Points Earned" INTEGER,
        "Points Spent" INTEGER
    );
''')

conn.commit()

with open('New_RewardsData.csv', 'r') as f:
    cur.copy_expert('''
        COPY user_data 
        FROM STDIN 
        DELIMITER ',' 
        CSV HEADER 
    ''', f)

conn.commit()
conn.close()
