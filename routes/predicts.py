from fastapi import APIRouter,File,UploadFile
from model.classify_model import predict_image
from PIL import Image
import torchvision.transforms as transforms
from io import BytesIO
router = APIRouter()

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert("RGB")

    transforms_pipeline = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    image_tensor = transforms_pipeline(image).unsqueeze(0)

    prediction = predict_image(image_tensor)
    return {"class_id": prediction}