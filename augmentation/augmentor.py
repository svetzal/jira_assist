from llm.llm_gateway import LLMGateway


class Augmentor:
    def __init__(self, llm: LLMGateway):
        self.llm = llm
