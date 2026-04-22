import pandas as pd
import random
from datetime import datetime, timedelta

# Number of providers
n = 3000

regions = ["Northeast", "Midwest", "South", "West"]
network_statuses = ["In-Network", "Out-of-Network"]
contract_types = ["Value-Based", "Fee-for-Service", "Capitated", "Shared Savings"]
risk_tiers = ["Low", "Medium", "High"]
provider_groups = ["Group A", "Group B", "Group C", "Independent", "Academic"]

first_names = [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael",
    "Linda", "William", "Elizabeth", "David", "Barbara", "Richard", "Susan"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
    "Miller", "Davis", "Wilson", "Taylor", "Anderson", "Thomas"
]

start_date = datetime(2015, 1, 1)
end_date = datetime(2026, 3, 25)

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

data = []

for i in range(1000, 1000 + n):
    provider_id = f"P{i}"
    provider_name = f"Dr. {random.choice(first_names)} {random.choice(last_names)}"
    provider_region = random.choice(regions)
    provider_network_status = random.choice(network_statuses)
    provider_contract_type = random.choice(contract_types)
    provider_risk_tier = random.choice(risk_tiers)
    provider_group = random.choice(provider_groups)
    provider_start_date = random_date(start_date, end_date).date()

    data.append([
        provider_id,
        provider_name,
        provider_region,
        provider_network_status,
        provider_contract_type,
        provider_risk_tier,
        provider_group,
        provider_start_date
    ])

columns = [
    "provider_id",
    "provider_name",
    "provider_region",
    "provider_network_status",
    "provider_contract_type",
    "provider_risk_tier",
    "provider_group",
    "provider_start_date"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("data/provider_reference.csv", index=False)

print("provider_reference.csv generated successfully")
print(df.head())
print("\nColumns:")
print(df.columns.tolist())