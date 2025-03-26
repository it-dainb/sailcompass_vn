# ----- Stage 1: Build package-----
FROM pytorch/pytorch:2.6.0-cuda11.8-cudnn9-devel AS package

ENV PYTHONUSERBASE=/opt/eval \
    PATH="/opt/eval/bin:${PATH}" \
    PIP_USER=yes\
    PIP_NO_CACHE_DIR=1

RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/* &&\
    pip install huggingface_hub[cli] gdown

COPY opencompass/ ./opencompass
WORKDIR /workspace/opencompass
RUN pip install -r requirements.txt
RUN pip install -e .
RUN pip install pythainlp langid datasets huggingface_hub \
&& pip install https://github.com/vllm-project/vllm/releases/download/v0.8.1/vllm-0.8.1+cu118-cp38-abi3-manylinux1_x86_64.whl --extra-index-url https://download.pytorch.org/whl/cu118 \
&& pip install https://github.com/flashinfer-ai/flashinfer/releases/download/v0.2.2.post1/flashinfer_python-0.2.2.post1+cu118torch2.6-cp38-abi3-linux_x86_64.whl --extra-index-url https://download.pytorch.org/whl/cu118 \
&& pip install gptqmodel==2.1.0 --no-build-isolation \
&& pip install numpy==1.23.4 sentence-transformers==3.4.1 \
&& pip uninstall flash-attn -y

WORKDIR /workspace
COPY rouge/ ./rouge
WORKDIR /workspace/rouge
RUN pip install .

WORKDIR /workspace
COPY configs/ ./configs
COPY datasets/ ./datasets
COPY eval_sailcompass.py eval_sailcompass_vllm.py icl_sailor_evaluator.py sailor_text_postprocessors.py setup_sailcompass.sh fix_mmengine.py multi_registry.py ppl_vllm.py .
RUN bash setup_sailcompass.sh

# ----- Stage 2: Runtime -----
FROM pytorch/pytorch:2.6.0-cuda11.8-cudnn9-devel AS runtime

# Copy the installed Python packages and executables from the build stage.
COPY --from=package /opt/eval /opt/eval
COPY --from=package /workspace/opencompass/ ./opencompass

COPY data/ ./data
COPY setup_data.sh .
RUN bash setup_data.sh

ENV PYTHONUSERBASE=/opt/eval \
    PATH="/opt/eval/bin:${PATH}" \
    CUDA_HOME=/usr/local/cuda \
    VLLM_WORKER_MULTIPROC_METHOD=spawn \
    TORCH_CUDA_ARCH_LIST="8.0;8.6;8.9;9.0"

# Test if opencompass is installed correctly
RUN python -c "import opencompass, rouge, vllm, gptqmodel"