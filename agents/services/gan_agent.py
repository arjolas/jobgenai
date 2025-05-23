from PIL import Image
import torch
from torchvision.utils import save_image
import os
import uuid

class GANGenerator:
    def __init__(self, model_path: str):
        self.model = torch.load(model_path)
        self.model.eval()

    def generate(self, latent_dim: int = 100, output_dir: str = "media/generated") -> str:
        z = torch.randn(1, latent_dim)
        with torch.no_grad():
            generated = self.model(z)
        filename = f"{uuid.uuid4().hex}.png"
        path = os.path.join(output_dir, filename)
        save_image(generated, path)
        return path
