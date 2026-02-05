import os
import json
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

today = datetime.now(timezone.utc).strftime("%d %b %Y")


def extract_tasks(transcript: str):

    json_prompt = {
        "objective": "Extract actionable tasks from a meeting transcript",
        "context": {
            "today_date": today,
            "source_material": transcript
        },
        "rules": {
            "only_real_commitments": True,
            "infer_owner_from": "speaker labels like 'Name: or context in sentences'",
            "rewrite_into": "clean task phrases"
        },
        "output_schema": {
            "description": "string",
            "owner": "string",
            "deadline": "string or null",
            "priority": "Low | Medium | High"
        }
    }

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": "Return ONLY a JSON array. No text."
                },
                {
                    "role": "user",
                    "content": json.dumps(json_prompt, indent=2)
                }
            ],
        )

        content = response.choices[0].message.content

        tasks = json.loads(content)
        return tasks

    except Exception as e:
        with open("groq_error.txt", "w") as f:
            f.write(str(e))
        print("GROQ ERROR:", e)
        return []
