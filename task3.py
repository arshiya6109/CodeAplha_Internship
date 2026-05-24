import re

print("=" * 50)
print("      EMAIL ADDRESS EXTRACTOR")
print("=" * 50)

try:
    with open(r"C:\Users\AAR\codealpha\input.txt", "r") as file:
        text = file.read()

    emails = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    with open(r"C:\Users\AAR\codealpha\emails.txt", "w") as file:
        for email in emails:
            file.write(email + "\n")

    print("\nExtracted Emails:")
    print("-" * 30)

    for email in emails:
        print(email)

    print("\nResults saved in emails.txt")

except FileNotFoundError:
    print("input.txt file not found.")