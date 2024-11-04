import bentoml


MAX_TOKENS = 1024
SYSTEM_PROMPT = """You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""

PROMPT_TEMPLATE = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{user_prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

"""

MODEL_ID = "meta-llama/Meta-Llama-3.1-8B-Instruct"


@bentoml.service(
    name="llama3.1-8b-insruct-service-sp-nomodel",
    traffic={
        "timeout": 300,
        "concurrency": 256,  # Matches the default max_num_seqs in the VLLM engine
    },
    resources={
        "gpu": 1,
        "gpu_type": "nvidia-l4",
    },
)
class VLLM:
    model_id = bentoml.models.HuggingFaceModel(MODEL_ID)

    @bentoml.on_deployment
    @staticmethod
    def on_deployment():
        import subprocess
        import sys
        import pathlib

        cwd = pathlib.Path(__file__).parent

        subprocess.run(
            [
                sys.executable,
                "-m",
                "uv",
                "pip",
                "install",
                "--prefix",
                "/home/bentoml/.local",
                "-r",
                cwd / "requirements.txt",
            ],
        )

    def __init__(self) -> None:
        from transformers import AutoTokenizer
        from vllm import AsyncEngineArgs, AsyncLLMEngine
