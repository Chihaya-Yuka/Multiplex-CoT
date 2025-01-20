from llama_index.llms import OpenAI

# 设置你的 OpenAI API key
import os
os.environ["OPENAI_API_KEY"] = "your-api-key"

# 创建 LLM 实例
llm = OpenAI(temperature=0.7, model="gpt-4")

# 创建推理器实例
reasoner = MultiplexCoTReasoner()

# 处理问题
question = "Why is the sky blue?"
result = await reasoner.process_question(question, llm)

# 打印结果
print(reasoner.format_response(result))
