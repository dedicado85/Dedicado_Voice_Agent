import config

response = self.client.models.generate_content(
    model=config.LLM_MODEL,
    contents=prompt,
)