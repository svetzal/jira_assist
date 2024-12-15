from typing import List

from pydantic import BaseModel, Field


class LLMMessage(BaseModel):
    role: str = Field(..., title="The role of the message sender.")
    content: str = Field(..., title="The message content.")

def llm_messages_adapter(messages: List[LLMMessage]) -> List[dict]:
    return [message.model_dump() for message in messages]
