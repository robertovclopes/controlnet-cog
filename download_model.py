import os
import shutil
from huggingface_hub import hf_hub_download

downloaded_model_path = hf_hub_download(
 repo_id="robertovclopes/controlnet",
 # subfolder="models",
 filename="control_interioria_mlsd.pth",
)

print(downloaded_model_path)
shutil.move(os.readlink(downloaded_model_path), "./models/control_interioria_mlsd.pth")