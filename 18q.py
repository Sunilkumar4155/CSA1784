db = {
    "john": "2000-05-15",
    "alex": "1998-11-23",
    "mary": "2002-01-08"
}

def get_dob(name):
    return db.get(name.lower(), "Name not found")

print(get_dob("alex"))
