#!/usr/bin/env python3
import os
import json

apps = os.listdir('apps')
print("Building data files...")
app_names = []
orgs = {}
for app in apps:
    app_name = os.path.splitext(app)[0]
    app_names.append(app_name)
    with open(os.path.join('apps', app), "r") as f:
        data = json.load(f)
        if('org' in data):
            if(data['org'] not in orgs):
                orgs[data['org']] = []
            orgs[data['org']].append(app_name)
os.makedirs('orgs', exist_ok=True)
for org, apps in orgs.items():
    with open(os.path.join("orgs", org + ".json"), "w") as f:
        json.dump(apps, f)

with open('index.json', "w") as f:
    json.dump({"apps": app_names, "orgs": list(orgs.keys())}, f, ensure_ascii=False, indent=4)

print("Successfully built data files.")