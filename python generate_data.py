import pandas as pd
import numpy as np

# Setting seed for unique but consistent data to meet variation requirements
np.random.seed(99)

# 1. Faculty Names (Updated to match your Dashboard names)
teachers = ["Elena Rodriguez", "Marcus Chen", "Sarah Jenkins", "David Okafor", "Priya Sharma"]
sections = ['Elite-A', 'Mainstream-B', 'Foundational-C']

data = []

# 2. Generating 300 rows of robust data
for i in range(1001, 1301):
    t = np.random.choice(teachers)
    s = np.random.choice(sections)
    
    # Performance Score (Normal distribution around 72)
    # This creates a realistic bell curve of scores
    score = int(np.random.normal(72, 15))
    score = max(0, min(100, score)) # Keep between 0-100
    
    # Late Count (Poisson distribution for realism)
    late = np.random.poisson(3)
    
    # Attendance Rate
    attendance = round(np.random.uniform(60, 99), 2)
    
    # Attrition Risk Logic (Crucial for the 3rd Dashboard Page)
    # A teacher is 'at risk' if scores are low OR lateness is high
    risk = 1 if (score < 55 or late > 7) else 0
    
    # Satisfaction Feedback (1 to 5 scale)
    feedback = np.random.randint(2, 6) if score > 60 else np.random.randint(1, 4)

    data.append([i, t, s, score, late, attendance, risk, feedback])

# 3. Create the DataFrame
df = pd.DataFrame(data, columns=[
    'Student_ID', 'Teacher_Name', 'Section', 'Performance_Score', 
    'Late_Count', 'Attendance_Rate', 'Risk_Status', 'Feedback_Rating'
])

# 4. Export to CSV (This powers your dashboard)
df.to_csv('academic_data.csv', index=False)

print("✅ Success! 'academic_data.csv' generated with 300 unique records.")