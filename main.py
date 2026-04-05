from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import requests
import base64

app = FastAPI()
from fastapi.responses import FileResponse

@app.get("/")
def serve_ui():
    return FileResponse("index.html")
# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "m3IH7yas1XxWJ6jPuHzAb0ImUwfUtm3RJC39nc5PRZZO24DF99"

@app.post("/identify/")
async def identify_plant(file: UploadFile = File(...)):
    image_bytes = await file.read()
    encoded_image = base64.b64encode(image_bytes).decode("utf-8")

    response = requests.post(
        "https://api.plant.id/v2/identify",
        json={
            "images": [encoded_image],
            "plant_details": ["common_names"]
        },
        headers={"Api-Key": API_KEY}
    )

    result = response.json()

    suggestions = result.get("suggestions", [])[:3]

    plants = []

    for s in suggestions:
        scientific = s["plant_name"]
        common = s.get("plant_details", {}).get("common_names", [])

        plants.append({
            "common": common[0] if common else scientific,
            "scientific": scientific,
            "confidence": s.get("probability", 0)
        })

    return {"results": plants}
