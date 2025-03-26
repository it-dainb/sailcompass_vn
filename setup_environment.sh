cd opencompass

pip install --upgrade pip
pip install -e .
pip install -r requirements.txt
pip install pythainlp langid
pip install datasets huggingface_hub
pip install https://github.com/vllm-project/vllm/releases/download/v0.8.1/vllm-0.8.1+cu118-cp38-abi3-manylinux1_x86_64.whl --extra-index-url https://download.pytorch.org/whl/cu118 \
pip install https://github.com/flashinfer-ai/flashinfer/releases/download/v0.2.2.post1/flashinfer_python-0.2.2.post1+cu118torch2.6-cp38-abi3-linux_x86_64.whl --extra-index-url https://download.pytorch.org/whl/cu118 \
pip install gptqmodel==2.1.0 --no-build-isolation \
pip install numpy==1.23.4 sentence-transformers==3.4.1 \
pip uninstall flash-attn -y

cd ..
cd rouge
python setup.py install
cd ..