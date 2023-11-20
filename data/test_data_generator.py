from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
faker = Faker()

# Function to generate a random timestamp within a range
def random_timestamp(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

# Define the start and end dates for created_at and updated_at fields
start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 4, 30)

# Generate 30 rows of data for the 'plans' table

plans_data = []
for _ in range(30):
    id = _ + 1  # Assuming id starts from 1

    description = faker.sentence(nb_words=6)
    price = round(random.uniform(10.00, 1000.00), 2)
    currency = faker.currency_code()
    country_restrictions = faker.country() if random.choice([True, False]) else None
    expiry_date = random_timestamp(start_date, end_date) if random.choice([True, False]) else None
    created_at = random_timestamp(start_date, end_date)
    updated_at = random_timestamp(created_at, end_date)  # updated_at should be after created_at

    plans_data.append(
        (id, description, price, currency, country_restrictions, expiry_date, created_at, updated_at)
    )

# Adjusting the descriptions to match a music streaming service context
plan_descriptions = [
    "Basic Plan", "Premium Plan", "Student Plan", "Family Plan",
    "Annual Basic Plan", "Annual Premium Plan", "Group Plan",
    "Artist Support Plan", "Hi-Fi Plan", "Mobile Only Plan",
    "Web Streaming Plan", "Offline Plan", "Podcast Plan",
    "Video Streaming Plan", "Premium Family Plan", "Premium Duo Plan",
    "Exclusive Content Plan", "Early Access Plan", "Unlimited Skips Plan",
    "No Ads Plan", "Hi-Res Audio Plan", "Live Concert Plan",
    "Music Video Plan", "DJ Mix Plan", "Soundtrack Plan",
    "Radio Plan", "Single Device Plan", "Multi-Device Plan",
    "Weekly Plan", "Daily Plan"
]

# Updating the description field in the generated data
for i, plan in enumerate(plans_data):
    # Replace the description with one from the new list
    plans_data[i] = (plan[0], plan_descriptions[i], *plan[2:])


# Updating the country_restrictions to be an array of countries
for i, plan in enumerate(plans_data):
    # Randomly decide how many countries to include in the restrictions, up to 3
    num_countries = random.randint(0, 3)
    country_restrictions = [faker.country() for _ in range(num_countries)]

    # Replace the country_restrictions with the new list
    plans_data[i] = (*plan[:4], country_restrictions, *plan[5:])


# Displaying a few sample rows
plans_data[:5]  # Displaying the first 5 rows as a sample



# Generate 30 rows of data for the 'users' table
users_data = []
plan_ids = list(range(1, 31))  # Assuming plan IDs are from 1 to 30

for i in range(30):
    id = i + 1  # Assuming id starts from 1
    country = faker.country_code(representation="alpha-2")
    mobileoperator = faker.company()
    email = faker.email()

    # Randomly decide if the user should have an Arabic name
    if random.choice([True, False]):
        firstname = faker.first_name_male() if random.choice([True, False]) else faker.first_name_female()
        lastname = faker.last_name()
    else:
        firstname = faker.first_name_nonbinary()
        lastname = faker.last_name_nonbinary()
    mobile_country_code = '+' + str(faker.random_int(min=1, max=999))
    mobile_number = faker.random_number(digits=8, fix_len=True)
    registration_date = random_timestamp(start_date, end_date)
    device_id = faker.uuid4()
    language = random.choice(['en', 'ar'])
    plan_id = random.choice(plan_ids)
    last_login_date = random_timestamp(registration_date, end_date) if random.choice([True, False]) else None
    last_played_date = random_timestamp(registration_date, end_date) if random.choice([True, False]) else None
    created_on = registration_date  # Using registration date as created_on
    updated_on = random_timestamp(created_on, end_date)

    users_data.append(
        (id, country, mobileoperator, email, firstname, lastname, mobile_country_code, mobile_number,
         registration_date, device_id, language, plan_id, last_login_date, last_played_date, created_on, updated_on)
    )

# Displaying a few sample rows
users_data[:5]  # Displaying the first 5 rows as a sample

import csv
import os

# Path for the CSV file
csv_file_path = '/mnt/data/users_data.csv'

# Adjusting the data generation to include only 'en' or 'ar' languages and Arabic names for some users
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Writing the header
    writer.writerow(['id', 'country', 'mobileoperator', 'email', 'firstname', 'lastname',
                     'mobile_country_code', 'mobile_number', 'registration_date', 'device_id',
                     'language', 'plan_id', 'last_login_date', 'last_played_date', 'created_on', 'updated_on'])

    for i in range(1000):
        id = i + 1  # Assuming id starts from 1
        country = faker.country_code(representation="alpha-2")
        mobileoperator = faker.company()
        email = faker.email()
        
        # Randomly decide if the user should have an Arabic name
        if random.choice([True, False]):
            firstname = faker.first_name_male() if random.choice([True, False]) else faker.first_name_female()
            lastname = faker.last_name()
        else:
            firstname = faker.first_name_nonbinary()
            lastname = faker.last_name_nonbinary()

        writer.writerow([id, country, mobileoperator, email, firstname, lastname,
                         mobile_country_code, mobile_number, registration_date, device_id,
                         language, plan_id, last_login_date, last_played_date, created_on, updated_on])



