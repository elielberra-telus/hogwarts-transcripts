prompt="""
- courtesies: basic greetings, courtesies and polite phrases (hi/hello/hey/thanks/pleasantries/etc.)
- garbage: random characters, dummy text, meaningless content, or nonsensical input
- image_requests: image analysis requests and image generation requests
- technical_development: coding, debugging, programming, React, JavaScript, Firebase, etc.
- information_lookup: search or lookup requests (find, look up, internet searches)
- meta_system: questions about the AI system, capabilities, tools, files, or model behavior
- business_professional: email drafts, business tasks, planning, or professional requests
- testing: explicit test messages
- telus_product: TELUS-specific queries, product questions, or customer service scenarios
- weather: weather-related queries
- single_word_tests: prompts that require responding with one specific word only
- creative_entertainment: jokes, stories, poems, or other creative writing
- Use EXACTLY these keys:
  "courtesies", "garbage", "image_requests", "technical_development",
  "information_lookup", "meta_system", "business_professional",
  "testing", "telus_product", "weather", "single_word_tests",
  "creative_entertainment"

JSON FORMAT (copy exactly):
{
  "courtesies": SUM,
  "garbage": SUM,
  "image_requests": SUM,
  "technical_development": SUM,
  "information_lookup": SUM,
  "meta_system": SUM,
  "business_professional": SUM,
  "testing": SUM,
  "telus_product": SUM,
  "weather": SUM,
  "single_word_tests": SUM,
  "creative_entertainment": SUM
}

"""
