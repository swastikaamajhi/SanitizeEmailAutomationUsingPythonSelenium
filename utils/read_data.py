import csv

def read_emails():
    """Read emails from CSV and return as a list"""
    emails = []
    with open("testdata/emails.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            emails.append(row["email"])
    return emails