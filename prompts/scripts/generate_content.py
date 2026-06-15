import os
import json
import random
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

TOPICS = {
    "morning": [
        "People Analytics",
        "HR Analytics",
        "Workforce Analytics",
        "Recruitment Analytics",
        "Employee Retention Analytics"
    ],
    "afternoon": [
        "AI in HR",
        "Future of Work",
        "HR Technology",
        "Digital Transformation",
        "Generative AI in HR"
    ],
    "evening": [
        "MBA Insights",
        "Career Growth",
        "Leadership",
        "Workplace Psychology",
        "Productivity"
    ]
}

def generate_post(slot):
    topic = random.choice(TOPICS[slot])

    prompt = f"""
You are a top LinkedIn creator.

Create:

1. Title
2. LinkedIn Post (250-400 words)
3. Instagram Caption
4. 10 Hashtags
5. AI Image Prompt

Audience:
HR Professionals
MBA Students
Recruiters
People Analytics Professionals

Style:
Professional
Emotional
Insightful
High Engagement

Topic:
{topic}

Return JSON only:

{{
"title":"",
"linkedin_post":"",
"instagram_caption":"",
"hashtags":[],
"image_prompt":""
}}
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "qwen/qwen3-32b:free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    data = response.json()

    content = data["choices"][0]["message"]["content"]

    return json.loads(content)
