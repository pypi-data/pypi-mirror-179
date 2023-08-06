import os
from transformers import pipeline


def hf_provider(model_path, model_name, task_name, mii_config):
    if mii_config.load_with_sys_mem:
        local_rank = -1
    else:
        local_rank = int(os.getenv('LOCAL_RANK', '0'))
    inference_pipeline = pipeline(
        task_name,
        model=model_name,
        device=local_rank,
        framework="pt",
        use_auth_token=mii_config.hf_auth_token,
        torch_dtype=mii_config.dtype,
    )
    return inference_pipeline
