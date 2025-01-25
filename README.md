# Multiplex CoT: A way for the LLM to review its own thinking while reasoning by initiating double CoT thinking

[![Open Auto-CoT in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1rB3Re3D7alu28JgChFUy6BKmvmNADsdk?usp=sharing)[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/mygo-multiplex-cot-a-method-for-self/gsm8k-on-gsm8k)](https://paperswithcode.com/sota/gsm8k-on-gsm8k?p=mygo-multiplex-cot-a-method-for-self)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/mygo-multiplex-cot-a-method-for-self/humaneval-on-humaneval-1)](https://paperswithcode.com/sota/humaneval-on-humaneval-1?p=mygo-multiplex-cot-a-method-for-self)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/mygo-multiplex-cot-a-method-for-self/llm-real-life-tasks-on-llm-real-life-tasks)](https://paperswithcode.com/sota/llm-real-life-tasks-on-llm-real-life-tasks?p=mygo-multiplex-cot-a-method-for-self)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/mygo-multiplex-cot-a-method-for-self/mmlu-on-mmlu-pro)](https://paperswithcode.com/sota/mmlu-on-mmlu-pro?p=mygo-multiplex-cot-a-method-for-self)


By employing the Prompt method, the LLM can attain an effect that closely resembles that of the LRM without necessitating additional training.

In the context of reasoning and decision-making, Multiplex CoT (Chain of Thought) enables the model to simulate a form of self-reflection, improving its ability to generate coherent, logical answers. This method works by prompting the LLM to first generate a chain of reasoning (CoT), then iteratively reviewing and refining it by initiating a second round of reasoning, which acts as a critique or review of the first.

![Figure 1](Figure_1.png)

## Quickly start

Run `Multiplex_CoT.ipynb`.

## How to use

See `example.py`.
