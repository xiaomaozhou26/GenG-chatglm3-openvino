https://github.com/OpenVINO-dev-contest/chatglm3.openvino
https://modelscope.cn/models/ZhipuAI/chatglm3-6b/summary

git clone https://github.com/OpenVINO-dev-contest/chatglm3.openvino.git
cd chatglm3.openvino

git lfs install
git clone https://www.modelscope.cn/ZhipuAI/chatglm3-6b.git
#######################################################################################

1. Environment configuration
python3 -m venv openvino_env

source openvino_env/bin/activate

python3 -m pip install --upgrade pip

pip install wheel setuptools

pip install -r requirements.txt

#######################################################################################
2. Convert model
python3 convert.py --model_id THUDM/chatglm3-6b --precision int4 --output {your_path}/chatglm3-6b-ov

Parameters that can be selected
--model_id - path (absolute path) to be used from Huggngface_hub (https://huggingface.co/models) or the directory where the model is located.
--precision - model precision: fp16, int8 or int4.
--output - the path where the converted model is saved

#######################################################################################
3. Run the streaming chatbot
python3 chat.py --model_path {your_path}/chatglm3-6b-ov --max_sequence_length 4096 --device CPU

Parameters that can be selected
--model_path - The path to the directory where the OpenVINO IR model is located.
--max_sequence_length - Maximum size of output tokens.
--device - The device to run inference on. e.g "CPU","GPU".
