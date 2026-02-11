import json, glob, sys

total = 0

for file in glob.glob("**/*.json", recursive=True):
    try:
        with open(file) as f:
            data = json.load(f)
            if "severity" in str(data):
                total += 10
    except:
        pass

print("TOTAL_RISK:", total)

if total > 20:
    print("BLOCK RELEASE")
    sys.exit(1)
