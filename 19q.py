records = [
    {"student": "alex", "teacher": "smith", "subject": "math", "code": "mt101"},
    {"student": "john", "teacher": "jones", "subject": "physics", "code": "ph202"}
]

def get_details(student_name):
    for r in records:
        if r["student"] == student_name.lower():
            return f"Teacher: {r['teacher']}, Subject: {r['subject']}"
    return "Not found"

print(get_details("alex"))
