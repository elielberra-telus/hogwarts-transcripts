old_prompt="""
- garbage: random characters, dummy text, meaningless content, or clearly non-sensical spam
- courtesies: greetings or polite phrases (hi/hello/hey/thanks/thank you/bye/etc.)
- knowledge_questions: any real question or request with meaningful content (including “do X”, “explain Y”, “help with Z”, etc.)
- Use EXACTLY these keys: "garbage", "courtesies", "knowledge_questions"

JSON FORMAT (copy exactly):
{"garbage": SUM, "courtesies": SUM, "knowledge_questions": SUM}
"""


def _parse_counts(assistant_text: str) -> dict:
    # try to extract the first JSON object from the assistant text
    match = re.search(r"\{.*\}", assistant_text, flags=re.DOTALL)
    if not match:
        raise ValueError(f"Could not find JSON in assistant response:\n{assistant_text}")

    json_str = match.group(0).strip()
    data = json.loads(json_str)

    # normalize keys + ints
    return {
        "garbage": int(data.get("garbage", 0)),
        "courtesies": int(data.get("courtesies", 0)),
        "knowledge_questions": int(data.get("knowledge_questions", 0)),
    }