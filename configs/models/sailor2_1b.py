from opencompass.models import VLLM

models = [
    dict(
        type=VLLM,
        abbr='sailor2_1B',
        path='sail/Sailor2-1B',
        tokenizer_path='sail/Sailor2-1B',
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
