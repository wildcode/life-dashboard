import os
import json
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

prompt = """
Analyze progress and return updated dashboard data.
Output strict JSON matching:
{
  "last_updated": "YYYY-MM-DD",
  "status": "on_track | attention_needed | off_track",
  "priorities": ["string"]
}
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt,
    config={"response_mime_type": "application/json"}
)

with open("data.json", "w", encoding="utf-8") as f:
    f.write(response.text)
