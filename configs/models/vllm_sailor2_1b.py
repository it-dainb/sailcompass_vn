from opencompass.models import VLLM

models = [
    dict(
        type=VLLM,
        abbr='sailor2_1B',
        path='sail/Sailor2-1B',
        model_kwargs=dict(
            dtype="bfloat16",
            trust_remote_code=True,
            seed=42
        ),
        max_out_len=100,
        max_seq_len=4096,
        batch_size=16,
        generation_kwargs=dict(
            temperature=0,
            seed=42
        ),
        run_cfg=dict(num_gpus=1, num_procs=1),
    )
]
