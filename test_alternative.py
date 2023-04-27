import torch
from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    
    torch_dtype=torch.float16,
)
pipe = pipe.to("cuda")

prompt = "a photo of an horse riding a elephant on mars"
image = pipe(prompt).images[0]