import time
from bigdl.llm.transformers import AutoModel
from transformers import AutoTokenizer

CHATGLM_V3_PROMPT_FORMAT = "<|user|>\n{prompt}\n<|assistant|>"
# 请指定chatglm3-6b的本地路径
model_path = "d:/chatglm3-6b"
# 载入ChatGLM3-6B模型并实现INT4量化
model = AutoModel.from_pretrained(model_path,
                                  load_in_4bit=True,
                                  trust_remote_code=True)
# 载入tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path,
                                          trust_remote_code=True)
# 制作ChatGLM3格式提示词    
prompt = CHATGLM_V3_PROMPT_FORMAT.format(prompt="What is Intel?")
# 对提示词编码
input_ids = tokenizer.encode(prompt, return_tensors="pt")
st = time.time()
# 执行推理计算，生成Tokens
output = model.generate(input_ids,max_new_tokens=32)
end = time.time()
# 对生成Tokens解码并显示
output_str = tokenizer.decode(output[0], skip_special_tokens=True)
print(f'Inference time: {end-st} s')
print('-'*20, 'Prompt', '-'*20)
print(prompt)
print('-'*20, 'Output', '-'*20)
print(output_str)
