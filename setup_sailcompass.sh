
cp -r configs/* opencompass/configs/
cp -r datasets/* opencompass/opencompass/datasets/
cp icl_sailor_evaluator.py opencompass/opencompass/openicl/icl_evaluator/
cp sailor_text_postprocessors.py opencompass/opencompass/utils/
echo "from .icl_sailor_evaluator import AnsEvaluator, TextGenEvaluator  # noqa" >> "opencompass/opencompass/openicl/icl_evaluator/__init__.py"
echo "from .sailor_text_postprocessors import *  # noqa" >> "opencompass/opencompass/utils/__init__.py"

###=====generation tasks======
###question answering
echo "from .xquad import *  # noqa: F401, F403" >> "opencompass/opencompass/datasets/__init__.py"
###machine translation
echo "from .flores200 import *  # noqa: F401, F403" >> "opencompass/opencompass/datasets/__init__.py"
###text summarization
echo "from .xlsum_vi import *  # noqa: F401, F403" >> "opencompass/opencompass/datasets/__init__.py"
###=====mcq tasks======
###examination
echo "from .m3exam import *  # noqa: F401, F403" >> "opencompass/opencompass/datasets/__init__.py"
###commonsense reasoning
echo "from .xcopa_sea import *  # noqa: F401, F403" >> "opencompass/opencompass/datasets/__init__.py"
###machine reading conprehension
echo "from .belebele import *  # noqa: F401, F403" >> "opencompass/opencompass/datasets/__init__.py"
###=====classification tasks======
###natural language inference
echo "from .xnli import *  # noqa: F401, F403" >> "opencompass/opencompass/datasets/__init__.py"
###sentiment analysis
echo "from .vsmec import *  # noqa: F401, F403" >> "opencompass/opencompass/datasets/__init__.py"

cp eval_sailcompass.py opencompass/configs/
cp eval_sailcompass_vllm.py opencompass/configs/

cp ppl_vllm.py opencompass/opencompass/models/vllm.py
python fix_mmengine.py