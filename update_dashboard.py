import os
import json
from datetime import datetime, timezone
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

prompt = """
Analyze progress and return updated dashboard data.
Output strict JSON matching:
{
  "status": "on_track | attention_needed | off_track",
  "priorities": ["string"]
}
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt,
    config={"response_mime_type": "application/json"}
)

data = json.loads(response.text)
data["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
