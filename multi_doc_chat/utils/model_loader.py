import os
import sys
import json
from dotenv import load_dotenv
from multi_doc_chat.utils.config_loader import load_config
from langchain_nebius import ChatNebius, NebiusEmbeddings
from multi_doc_chat.logger import log
from multi_doc_chat.exception import MyException

class ApiKeyManager:
    REQUIRED_KEYS=["NEBIUS_API_KEY"]

    def __init__(self):
        self.api_keys={}

        for key in self.REQUIRED_KEYS:
            if not self.api_keys.get(key):
                env_val=os.getenv(key)
                if env_val:
                    self.api_keys[key] = env_val
                    log.info(f"Loaded {key} from individual env var")

        missing= [k for k in self.REQUIRED_KEYS if not self.api_keys.get(k)]
        if missing:
            log.error("Missing required api keys",missing_keys=missing) 
            raise MyException(f"Missing API keys", sys)

    
    def get(self,key:str)->str:
        val=self.api_keys.get(key)
        if not val:
            raise KeyError(f"API key for {key} is missing")
        return val
    
class ModelLoader:
    """
    Loads embedding models and LLMs based on config and environment
    """

    def __init__(self):
        if os.getenv("ENV", "local").lower() != "production":
            load_dotenv()
            log.info("Running in local mode: env loaded")
        else:
            log.info("Running in production mode")
        
        self.api_key_mngr=ApiKeyManager()
        self.config=load_config()
        log.info("YAML config loaded",config_keys=list(self.config.keys()))

    def load_embeddings(self):
        """
        Load and return the embeddings model
        """
        try:
            model_name=self.config["embedding_model"]["model"]
            log.info("Embedding Model Loaded", model=model_name)
            return NebiusEmbeddings(model=model_name, api_key=self.api_key_mngr.get("NEBIUS_API_KEY"))

        except Exception as e:
            raise MyException(f"Failed to load model",sys) from e
        
    def load_llm(self):
        """
        Load and return the configured llm
        """
        llm_block=self.config["llm"]
        provider_key=os.getenv("LLM_PROVIDER","nebius")

        if provider_key not in llm_block:
            log.error("LLM PRovider not found in config", provider=provider_key)
            raise MyException(f"LLm Provider :{provider_key} not found",sys)
    
        llm_config=llm_block[provider_key]
        provider=llm_config.get("provider")
        model_name=llm_config.get("model_name")
        temperature=llm_config.get("temperature",0.2)
        max_tokens=llm_config.get("max_output_tokens",2048)

        log.info("Loading LLM",provider=provider,model=model_name)

        if provider =="nebius":
            return ChatNebius(
                model=model_name,
                temperature=temperature,
                max_tokens=max_tokens
            )
        else:
            log.error("Unsupported LLM provider", provider=provider)
            raise MyException(f"Unsupported LLM provider: {provider}", sys)

if __name__=="__main__":
    loader=ModelLoader()

        # Test Embedding
    embeddings = loader.load_embeddings()
    print(f"Embedding Model Loaded: {embeddings}")
    result = embeddings.embed_query("Hello, how are you?")
    print(f"Embedding Result: {result}")

    # Test LLM
    llm = loader.load_llm()
    print(f"LLM Loaded: {llm}")
    result = llm.invoke("Hello, how are you?")
    print(f"LLM Result: {result.content}")

 
