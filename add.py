import os
import json

# 📂 Your folder path
folder_path = "C:\\Users\\Vinay\\Kawaiininja\\assets\\Kawaiininja-AnimeArchive\\animes"

# 💫 Loop through all JSON files in folder
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"⚠️ Skipping invalid JSON file: {filename}")
                continue

        # 🌟 Check for episode structure and apply tracker
        try:
            seasons = data["type"]["tv"]["seasons"]
            for season in seasons:
                for ep in season.get("episodes", []):
                    if "tracker" not in ep:
                        ep["tracker"] = {"status": "Not Watched"}
        except KeyError:
            print(f"📛 Skipping: {filename} - missing expected keys.")
            continue

        # 💾 Save updated JSON
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"✅ Updated: {filename}")

print("🌸 All anime JSONs updated with missing trackers!~ 🩵")
