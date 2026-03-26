from abc import ABC, abstractmethod
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from config import TOKEN_HF, LLM_MODEL_NAME_HF, LLM_MODEL_NAME_GEMINI, LLM_MODEL_NAME_OPENAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI
class LlmService(ABC):
    
    @abstractmethod
    def get_message(self, response):
        pass
    
    @abstractmethod
    def get_llm(self)-> BaseChatModel:
        pass

class HuggingFaceService(LlmService):
    def __init__(self, model_name: str):
        self.model_name = model_name
        # Aquí podrías cargar el modelo de Hugging Face si es necesario

    def get_message(self, response):
        last_message = response["messages"][-1]
        messages = response["messages"]
        text_output = ""
        tools_used = []
        text_output = last_message.content if isinstance(last_message.content, str) else ""
        tools_used = []
        for msg in messages:
            tool_calls = getattr(msg, "tool_calls", None)
            if tool_calls:
                tools_used.extend(tool_calls)
        return {
            "content": text_output, 
            "tool_calls": tools_used
        }

    def get_llm(self)-> BaseChatModel:
        llm_endpoint = HuggingFaceEndpoint(
            model=self.model_name,
            huggingfacehub_api_token=TOKEN_HF,
            temperature=0,
            max_new_tokens=500,
        )
        hf_llm = ChatHuggingFace(llm=llm_endpoint)
        return hf_llm

    
class GeminiService(LlmService):
    def __init__(self, model_name: str):
        self.model_name = model_name
        # Aquí podrías cargar el modelo de Gemini si es necesario

    def get_message(self, response):
        last_message = response["messages"][-1]
        messages = response["messages"]
        text_output = ""
        tools_used = []
        text_output = ""
        if isinstance(last_message.content, list):
            text_output = " ".join([c['text'] for c in last_message.content if c['type'] == 'text'])
        else:
            text_output = str(last_message.content)

        tools_used = []
        if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
            tools_used = [call.name for call in last_message.tool_calls]
        return {
            "content": text_output, 
            "tool_calls": tools_used
        }
    def get_llm(self)-> BaseChatModel:
        gemini_llm = ChatGoogleGenerativeAI(
            model=self.model_name,
            temperature=0.2,
            max_tokens=500
            )
        return gemini_llm
    
class OpenAiService(LlmService):
    def __init__(self, model_name: str):
        self.model_name = model_name

    def get_message(self, response):
        return response

    def get_llm(self)-> BaseChatModel:
        openai_llm = ChatOpenAI(model=self.model_name, temperature=0.2, max_completion_tokens=500)
        return openai_llm
    
class LLMFactory:
    @staticmethod
    def create_llm_service(llm_type: str, model_name: str = "") -> LlmService:
        if llm_type == "hg_llm":
            if model_name == "":
                model_name = str(LLM_MODEL_NAME_HF)
            return HuggingFaceService(model_name)
        
        elif llm_type == "gemini_llm":
            if model_name == "":
                model_name = str(LLM_MODEL_NAME_GEMINI)
            return GeminiService(model_name)
        elif llm_type == "openai_llm":
            if model_name == "":
                model_name = str(LLM_MODEL_NAME_OPENAI)
            return OpenAiService(model_name)
        raise ValueError(f"Tipo de LLM no soportado: {llm_type}")