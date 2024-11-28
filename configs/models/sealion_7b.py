from opencompass.models import HuggingFaceCausalLM



models = [
    dict(
        type=HuggingFaceCausalLM,
        abbr='sealion_7b',
        path="aisingapore/sea-lion-7b",
        tokenizer_path="aisingapore/sea-lion-7b",
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
        max_seq_len=2048,
        batch_size=8,
        batch_padding=True,
        run_cfg=dict(num_gpus=1, num_procs=1),
    )
]


