from llama_index import SimpleDirectoryReader, VectorStoreIndex
from llama_index.prompts import PromptTemplate
from typing import List, Dict
import logging

class MultiplexCoTReasoner:
    def __init__(self):
        # 定义第一次思考的提示词模板
        self.first_think_template = PromptTemplate(
            """
            # Role
            You are an expert AI assistant capable of gradually explaining the reasoning process.

            # Task
            Please help analyze the following question:
            {question}

            # First Think step
            For each step, provide a title that describes what you did in that step, along with the corresponding content.
            Decide whether another step is needed or if you are ready to give the final answer.

            Remember:
            1. Use as many **reasoning steps** as possible. At least 3 steps.
            2. Be aware of your limitations as an AI and what you can and cannot do.
            3. Include exploration of alternative answers.
            4. When you say you are rechecking, actually recheck and use another method.
            5. Use at least 3 methods to arrive at the answer.
            6. Use best practices.

            Please provide your step-by-step analysis:
            """
        )

        # 定义第二次思考的提示词模板
        self.second_think_template = PromptTemplate(
            """
            # Review and Verification

            Based on the previous analysis:
            {first_analysis}

            # Second Think step
            For each step mentioned above, please:
            1. Verify its correctness with sub-steps
            2. Review from different perspectives
            3. Consider potential errors or alternative approaches

            Remember:
            1. Use as many **reasoning steps** as possible
            2. Be aware of AI limitations
            3. Explore alternative answers and potential errors

            Please provide your detailed review:
            """
        )

    async def process_question(self, question: str, llm_service) -> Dict:
        """
        处理问题并返回两阶段的思考结果
        """
        try:
            # 第一阶段思考
            first_response = await llm_service.complete(
                self.first_think_template.format(question=question)
            )
            
            # 第二阶段思考
            second_response = await llm_service.complete(
                self.second_think_template.format(first_analysis=first_response)
            )

            return {
                "question": question,
                "first_think": first_response,
                "second_think": second_response
            }
        except Exception as e:
            logging.error(f"Error in processing question: {str(e)}")
            raise

    def format_response(self, response: Dict) -> str:
        """
        格式化响应结果
        """
        formatted_response = f"""
        # Question
        {response['question']}

        # First Analysis
        {response['first_think']}

        # Review and Verification
        {response['second_think']}
        """
        return formatted_response

# 使用示例
async def main():
    from llama_index.llms import OpenAI
    llm = OpenAI(temperature=0.7, model="gpt-4")

    # 创建 MultiplexCoT 实例
    reasoner = MultiplexCoTReasoner()

    # 示例问题
    question = "What would happen if the moon suddenly disappeared?"

    # 处理问题
    result = await reasoner.process_question(question, llm)
    
    # 格式化并打印结果
    formatted_output = reasoner.format_response(result)
    print(formatted_output)

# 使用方法
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
