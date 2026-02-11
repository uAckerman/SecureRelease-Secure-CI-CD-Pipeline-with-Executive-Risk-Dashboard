import json, glob, sys

total = 0

print("Scanning JSON security reports...\n")

for file in glob.glob("Reports/**/*.json", recursive=True):
    print("Reading:", file)
    try:
        with open(file) as f:
            data = json.load(f)
            content = json.dumps(data)

            # simple demo logic
            if "CRITICAL" in content:
                total += 10
            if "HIGH" in content:
                total += 5
            if "secret" in content.lower():
                total += 10
            if "sql" in content.lower():
                total += 5
    except Exception as e:
        print("Skipping:", file, e)

print("\nTOTAL_RISK:", total)

if total > 20:
    print("BLOCK RELEASE")
    sys.exit(1)
else:
    print("ALLOW RELEASE")
