import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Row count
n = 121484

# Helper functions
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

start_date = datetime(2022, 1, 1)
end_date = datetime(2026, 3, 25)

# Categorical values
genders = ["M", "F"]
states = ["MD", "VA", "DC", "PA", "NY", "CA"]
specialties = ["Oncology", "Cardiology", "Primary Care", "Orthopedics", "Neurology"]
provider_types = ["Hospital", "Clinic", "Specialty Center"]
claim_types = ["Professional", "Facility", "Pharmacy"]
pos = ["Inpatient", "Outpatient", "Office"]
diagnosis_codes = ["E11.9", "I10", "C50.9", "J45.909", "M54.5"]
procedure_codes = ["99213", "J3490", "93000", "71020", "80050"]
drug_codes = ["J9312", "J2357", "J9035", "J0897", "J1745"]
claim_statuses = ["Paid", "Denied", "Pending"]

# Generate data
data = []

for i in range(n):
    service_date = random_date(start_date, end_date)
    paid_date = service_date + timedelta(days=random.randint(5, 60))
    received_date = service_date - timedelta(days=random.randint(1, 10))

    billed = round(random.uniform(100, 10000), 2)
    allowed = round(billed * random.uniform(0.6, 0.9), 2)
    paid = round(allowed * random.uniform(0.7, 1.0), 2)
    member_resp = round(allowed - paid, 2)

    status = random.choice(claim_statuses)
    is_denied = status == "Denied"
    is_pending = status == "Pending"
    is_reversed = random.choice([True, False]) if status == "Paid" else False

    data.append([
        f"M{random.randint(10000,99999)}",  # member_id
        f"P{random.randint(1000,9999)}",    # provider_id
        f"C{100000+i}",                     # claim_id
        random.randint(1,5),                # claim_line_number
        service_date,
        paid_date,
        received_date,
        random.randint(18, 90),             # age
        random.choice(genders),
        random.choice(states),
        random.choice(specialties),
        random.choice(provider_types),
        random.choice(claim_types),
        random.choice(pos),
        random.choice(diagnosis_codes),
        random.choice(procedure_codes),
        billed,
        allowed,
        paid,
        member_resp,
        random.choice(drug_codes),
        random.randint(1, 10),
        status,
	is_reversed,
	is_denied,
	is_pending
    ])

# Create DataFrame
columns = [
    "member_id", "provider_id", "claim_id", "claim_line_number",
    "service_date", "paid_date", "claim_received_date",
    "member_age", "gender", "member_state",
    "provider_specialty", "provider_type",
    "claim_type", "place_of_service",
    "diagnosis_code", "procedure_code",
    "billed_amount", "allowed_amount", "paid_amount", "member_responsibility",
    "drug_code", "units_administered",
    "claim_status",
    "is_reversed",
    "is_denied",
    "is_pending"
]

df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv("data/healthcare_claims_100k.csv", index=False)

print("Dataset generated successfully!")