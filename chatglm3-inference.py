from modelscope import AutoTokenizer, AutoModel, snapshot_download
import time
model_dir = snapshot_download("ZhipuAI/chatglm3-6b", revision = "v1.0.0")
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModel.from_pretrained(model_dir, trust_remote_code=True).float()
model = model.eval()

st = time.time()
response, history = model.chat(tokenizer, "What is Intel?", history=[])
end = time.time()
print(f'Inference time: {end-st} s')
print(response)
