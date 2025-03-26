from opencompass.models import HuggingFaceCausalLM
import torch

models = [
    dict(
        type=HuggingFaceCausalLM,
        abbr='sailor2_1B',
        path='sail/Sailor2-1B',
        tokenizer_path="sail/Sailor2-1B",
        model_kwargs=dict(
            device_map='auto',
            trust_remote_code=True,
            torch_dtype=torch.bfloat16,
        ),
        tokenizer_kwargs=dict(
            padding_side='left',
            truncation_side='left',
            trust_remote_code=True,
            use_fast=True,
        ),
        max_out_len=100,
        max_seq_len=4096,
        batch_size=16,
        run_cfg=dict(num_gpus=1, num_procs=1),
    )
]
