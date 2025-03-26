cd opencompass

pip install --upgrade pip
pip install -e .
pip install -r requirements.txt
pip install pythainlp langid
pip install datasets huggingface_hub
pip install https://github.com/vllm-project/vllm/releases/download/v0.8.1/vllm-0.8.1+cu118-cp38-abi3-manylinux1_x86_64.whl --extra-index-url https://download.pytorch.org/whl/cu118
pip install gptqmodel==2.1.0 --no-build-isolation
pip uninstall flash-attn -y

cd ..

cd rouge
python setup.py install
cd ..