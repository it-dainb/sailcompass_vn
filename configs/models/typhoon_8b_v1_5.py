from opencompass.models import HuggingFaceCausalLM



models = [
    dict(
        type=HuggingFaceCausalLM,
        abbr='typhoon_8b_v1_5',
        path="scb10x/llama-3-typhoon-v1.5-8b",
        tokenizer_path="scb10x/llama-3-typhoon-v1.5-8b",
        model_kwargs=dict(
            device_map='auto',
            trust_remote_code=True
        ),
        tokenizer_kwargs=dict(
            padding_side='left',
            truncation_side='left',
            trust_remote_code=True,
            use_fast=False,
        ),
        max_out_len=100,
        max_seq_len=4096,
        batch_size=8,
        batch_padding=True,
        run_cfg=dict(num_gpus=1, num_procs=1),
    )
]


