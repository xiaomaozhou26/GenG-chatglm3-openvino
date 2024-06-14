import abc
from typing import Type
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from diffusers import AutoPipelineForText2Image
import torch
from modelscope import snapshot_download

model_dir = snapshot_download("AI-ModelScope/sdxl-turbo")
"""
pipe = AutoPipelineForText2Image.from_pretrained(model_dir, torch_dtype=torch.float16, variant="fp16")
pipe.to("cuda")

#prompt = "A cinematic shot of a baby racoon wearing an intricate italian priest robe."

prompt =  "A sequence of time series data with periodic changes"
image = pipe(prompt=prompt, num_inference_steps=1, guidance_scale=0.0).images[0]
image.save("image.png")
"""

class GenImageInput(BaseModel):
    instruction: str = Field(description="instruction")

class GenImage(BaseTool, abc.ABC):
    name = "GenImage"
    description = "generate an image based on the instruction"
    args_schema: Type[BaseModel] = GenImageInput

    def __init__(self):
        super().__init__()

    def _run(self, date: str, unit: str, to_unit: str) -> dict[str, Any]:
        flight_number = {
            "北京":{
                "上海" : "1234",
                "广州" : "8321",
            },
            "上海":{
                "北京" : "1233",
                "广州" : "8123",
            }
        }
        return { "date":date,"flight_number":flight_number[departure][destination] }
        
