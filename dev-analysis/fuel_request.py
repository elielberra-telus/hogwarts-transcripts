import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

url = "https://api.fuelix.ai/v1/chat/completions"

def fuel_request(content: str):
    payload = {
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ],
        "model": "claude-sonnet-4-5"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=60)

        if response.status_code != 200:
            raise RuntimeError(
                f"Fuel API request failed: status_code={response.status_code}, body={response.text}"
            )

        data = response.json()

        assistant_content = (
            data.get("choices", [{}])[0]
                .get("message", {})
                .get("content")
        )

        if not isinstance(assistant_content, str) or not assistant_content.strip():
            raise RuntimeError(
                f"Fuel API response missing choices[0].message.content. Full response: {data}"
            )

        return assistant_content

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Fuel API request error: {e}") from e
    except ValueError as e:
        raise RuntimeError(f"Fuel API returned invalid JSON: {response.text}") from e
