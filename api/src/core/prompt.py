DELIVERY_PROMPT = """You are provided with an image of a delivery summary screen from a mobile application.

Extract the following structured information from the image and return it as a JSON object:

{
  "date": string (format: "YYYY-MM-DD"),
  "distance_km": float,
  "deliveries": integer,
  "tips_kd": float | null,
  "collected_kd": float | null,
  "delivery_items": [
    {
      "delivery_id": string,
      "code": string,
      "finished_at": string (format: "HH:MM")
    },
    ...
  ]
}

Rules:
- Use only the data that is clearly visible in the image.
- If a value is missing or unclear, return it as null.
- Return only the JSON — no comments, no explanations, no markdown.
"""