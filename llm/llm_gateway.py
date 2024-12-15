from typing import List

from openai import OpenAI
import instructor
from pydantic import Field, BaseModel


class LLMGateway:
    def complete(self, messages: list, response_model):
        raise NotImplementedError("Subclasses should implement this method")


class ChatGPTGateway(LLMGateway):
    def __init__(self, api_key: str):
        self.adapter = OpenAI(api_key=api_key)
        self.client = instructor.from_openai(
            self.adapter,
            mode=instructor.Mode.JSON
        )

    def complete(self, messages: list, response_model):
        response = self.client.Completion.create(
            model="gpt-4o",
            messages=messages
        )
        return response_model(**response)


class OLlamaGateway(LLMGateway):
    def __init__(self, model="llama3.3-instruct"):
        self.model = model
        self.adapter = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
        self.client = instructor.from_openai(
            self.adapter,
            mode=instructor.Mode.JSON
        )

    def create_messages(self, message):
        return [
            {
                "role": "user",
                "content": message.strip()
            }
        ]

    def complete(self, messages: List, response_model):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            response_model=response_model
        )
        return response

    def query(self, message):
        # messages = self.create_messages(message)
        return self.adapter.completions.create(
            model=self.model,
            prompt=message
        ).choices[0].text.strip()
