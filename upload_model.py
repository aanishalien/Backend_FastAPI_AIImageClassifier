from huggingface_hub import HfApi

api = HfApi()

api.upload_file(
    path_or_fileobj="./model",
    path_in_repo="",
    repo_id="aanish28/fastapi_image_classifier",
    repo_type="model"
)