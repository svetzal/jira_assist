from openai import OpenAI
import instructor

class LLMGateway:
    def create_completion(self, messages: list, response_model):
        raise NotImplementedError("Subclasses should implement this method")

class ChatGPTGateway(LLMGateway):
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def create_completion(self, messages: list, response_model):
        response = self.client.Completion.create(
            model="gpt-4o",
            messages=messages
        )
        return response_model(**response)

class OLlamaGateway(LLMGateway):
    def __init__(self):
        self.client = instructor.from_openai(
            OpenAI(
                base_url="http://localhost:11434/v1",
                api_key="ollama"
            ),
            mode=instructor.Mode.JSON
        )

    def create_completion(self, messages: list, response_model):
        response = self.client.chat.completions.create(
            model="llama3.3-instruct",
            messages=messages,
            response_model=response_model
        )
        return response