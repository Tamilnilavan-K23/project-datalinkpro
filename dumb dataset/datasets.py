import json
import random
from datetime import datetime, timedelta

def generate_random_name(gender):
    male_names = ["John", "James", "Robert", "Michael", "William"]
    female_names = ["Mary", "Patricia", "Jennifer", "Linda", "Elizabeth"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones"]

    first_name = random.choice(male_names if gender == "Male" else female_names)
    last_name = random.choice(last_names)
    
    return f"{first_name} {last_name}"

def generate_random_dob():
    start_date = datetime(1970, 1, 1)
    end_date = datetime(2000, 12, 31)
    dob = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return dob.strftime("%Y-%m-%d")

def generate_employee_data(employee_id):
    genders = ["Male", "Female"]
    months = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]
    
    reasons = ["Sick Leave", "Vacation", "Personal Leave", "Family Emergency", "Unpaid Leave"]
    departments = ["HR", "Finance", "Engineering", "Marketing", "Sales"]
    job_titles = ["Manager", "Senior Developer", "Junior Developer", "Analyst", "Intern"]
    employment_types = ["Full-time", "Part-time", "Contract", "Intern"]
    work_locations = ["Office A", "Office B", "Remote"]
    legal_status = ["Authorized", "Pending", "Denied"]
    qualifications = ["Bachelor's Degree", "Master's Degree", "PhD", "Associate's Degree", "Diploma"]
    certifications = ["Certified Project Manager", "Certified Developer", "Certified Analyst", "Certified HR Professional"]
    previous_companies = ["Company A", "Company B", "Company C", "Company D"]
    
    gender = random.choice(genders)
    name = generate_random_name(gender)
    dob = generate_random_dob()
    marital_status = random.choice(["Single", "Married"])
    nationality = random.choice(["American", "Canadian", "British", "Australian"])
    address = f"{random.randint(100, 999)} Main St, City, Country"
    contact_number = f"+1-{random.randint(100,999)}-{random.randint(1000,9999)}"
    email = f"{name.replace(' ', '.').lower()}@example.com"
    
    in_time = random.choice(["09:00", "09:30", "10:00", "08:00"])
    out_time = random.choice(["17:00", "17:30", "18:00", "16:00"])
    
    department = random.choice(departments)
    job_title = random.choice(job_titles)
    date_of_hire = (datetime.now() - timedelta(days=random.randint(0, 3650))).strftime("%Y-%m-%d")
    employment_type = random.choice(employment_types)
    work_location = random.choice(work_locations)
    supervisor = f"Supervisor {random.randint(1, 50)}"  # Randomly assigning a supervisor ID

    # Legal and Compliance Information
    work_authorization = random.choice(["Valid Visa", "Work Permit", "No Authorization"])
    background_check = random.choice(["Clear", "Pending", "Not Cleared"])
    employment_agreement = random.choice(["Signed", "Pending", "Not Signed"])

    # Education and Work History
    education = random.choice(qualifications)
    certifications = random.sample(certifications, k=random.randint(0, 2))  # Random number of certifications
    previous_experience = [f"Previous Experience at {random.choice(previous_companies)}" for _ in range(random.randint(1, 3))]
    references = [f"Reference {random.randint(1, 50)}"]

    # Compensation and Benefits
    salary = round(random.uniform(30000, 120000), 2)  # Random salary between $30,000 and $120,000
    bonus = round(random.uniform(0, 10000), 2)  # Random bonus between $0 and $10,000
    commission = round(random.uniform(0, 5000), 2)  # Random commission between $0 and $5,000
    
    leaves_taken = {}
    for month in months:
        leave_days = random.randint(0, 2)  # Randomly decide the number of leave days in the month
        leaves_taken[month] = []
        for _ in range(leave_days):
            day = random.randint(1, 28)  # Assume all months have up to 28 days for simplicity
            reason = random.choice(reasons)
            leaves_taken[month].append({"day": day, "reason": reason})
    
    total_working_days = 252
    total_leaves = sum(len(leaves) for leaves in leaves_taken.values())
    total_worked_days = total_working_days - total_leaves
    
    return {
        "employee_id": employee_id,
        "name": name,
        "gender": gender,
        "date_of_birth": dob,
        "marital_status": marital_status,
        "nationality": nationality,
        "address": address,
        "contact_number": contact_number,
        "email": email,
        "in_time": in_time,
        "out_time": out_time,
        "department": department,
        "job_title": job_title,
        "date_of_hire": date_of_hire,
        "employment_type": employment_type,
        "work_location": work_location,
        "supervisor": supervisor,
        "work_authorization": work_authorization,
        "background_check": background_check,
        "employment_agreement": employment_agreement,
        "education": education,
        "certifications": certifications,
        "previous_experience": previous_experience,
        "references": references,
        "salary": salary,
        "bonus": bonus,
        "commission": commission,
        "leaves_taken": leaves_taken,
        "total_working_days": total_working_days,
        "total_worked_days": total_worked_days
    }

employees = [generate_employee_data(f"E{str(i).zfill(3)}") for i in range(1, 201)]

with open("employee_data.json", "w") as f:
    json.dump(employees, f, indent=4)

print("Employee dataset generated successfully!")
