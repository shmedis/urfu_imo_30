from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFacePipeline

# template for an instrution with no input
prompt = PromptTemplate(
    input_variables=["instruction"],
    template="{instruction}")

# template for an instruction with input
prompt_with_context = PromptTemplate(
    input_variables=["instruction", "context"],
    template="{instruction}\n\nInput:\n{context}")

hf_pipeline = HuggingFacePipeline(pipeline=generate_text)

llm_chain = LLMChain(llm=hf_pipeline, prompt=prompt)
llm_context_chain = LLMChain(llm=hf_pipeline, prompt=prompt_with_context)
