import os
from langchain import LLMChain, OpenAI, Cohere, HuggingFaceHub, PromptTemplate
from langchain.model_laboratory import ModelLaboratory

os.environ["OPENAI_API_KEY"]

llms = [
    OpenAI(temperature=0),
    OpenAI(temperature=0, model_name="text-davinci-002"),
    OpenAI(temperature=0, model_name="text-davinci-002", max_tokens=20),
    OpenAI(temperature=0, model_name="text-davinci-003", max_tokens=20),
    # OpenAI(temperature=0, model_name="davinci:ft-personal-2022-12-16-13-41-18"), # politics
    # OpenAI(temperature=0, model_name="davinci:ft-personal-2022-12-16-13-44-16"), # apple
    OpenAI(temperature=0, model_name="text-curie-001", max_tokens=20),
]


model_lab = ModelLaboratory.from_llms(llms)

# History removed.
template = """
Classifier's job is to categorize the input. What topic is being asked about?

Input: {human_input}
Classifier:"""


prompt = PromptTemplate(
    input_variables=["human_input"],
    template=template
)

model_lab_with_prompt = ModelLaboratory.from_llms(llms, prompt=prompt)



if __name__ == "__main__":
  while(True):
    request = input('Input:\n') 

    output = model_lab_with_prompt.compare(request)
    print(output)


