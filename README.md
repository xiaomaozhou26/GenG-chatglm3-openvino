针对AI技术变革及各类业务应用对高质量数据资源的需求，探索面向多模态数据高质量可控生成方法，建立通用数据生成大模型，解决数据稀缺、样本不平衡等问题。

技术架构
<img width="960" alt="image" src="https://github.com/xiaomaozhou26/GenG-chatglm3-openvino/assets/31319967/bcfe9494-a337-43d9-8ae9-9e54ea339cb7">


核心模块1:Chatglm3-6B
<img width="935" alt="image" src="https://github.com/xiaomaozhou26/GenG-chatglm3-openvino/assets/31319967/32414a0a-d7f4-42f1-bf72-b1026e75fed3">

核心模块2:主流生成模型
<img width="942" alt="image" src="https://github.com/xiaomaozhou26/GenG-chatglm3-openvino/assets/31319967/cb95da00-89d0-49ad-bd47-68dad40cb9e3">


特色创新：
将预训练语言大模型作为逻辑处理中心来对任务进行解析和对数据生成流程进行管控，实现具备任意属性的多模态数据的高质量生成

利用现有的生成模型自动构建数据生成流程，不需要模型构建或再训练，能够根据任务自动构建面向不同任务的数据生成流程，支持自定义设置和能力任意拓展。

使用Openvino对模型进行优化加速，显著降低对硬件资源的要求，提升模型的运行效率。

