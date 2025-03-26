from mmengine.config import read_base

with read_base():
    #------------------------------------------------------
    from .models.sailor2_1b import models as sailor2_1b
    from .models.sailor2_8b import models as sailor2_8b

    from .models.sailor2_1b_4bit import models as sailor2_1b_4bit
    from .models.sailor2_8b_4bit import models as sailor2_8b_4bit

    #------------------------------------------------------
    # QA
    from .datasets.xquad.xquad_vi_34e7ab import xquad_datasets as xquad_vi
    #------------------------------------------------------
    # MT
    from .datasets.flores200.flores_en_vi_ei3232 import flores_datasets as flores_en_vi
    from .datasets.flores200.flores_vi_en_ei3232 import flores_datasets as flores_vi_en
    #------------------------------------------------------
    # TS
    from .datasets.xlsum_vi.xlsum_vi_48d2e3 import xlsum_datasets as xlsum_vi  
    #------------------------------------------------------
    # EXAM - GEN
    from .datasets.m3exam.m3exam_vi_172ds2 import m3exam_datasets as m3exam_vi
    #------------------------------------------------------
    # MRC
    from .datasets.belebele.belebele_vi_ppl_23f2d2 import belebele_datasets as belebele_vi_ppl
    #------------------------------------------------------
    # NLI
    from .datasets.xnli.xnli_vi_ppl_121b02 import xnli_datasets as xnli_vi_ppl
    #------------------------------------------------------
    # CR
    from .datasets.xcopa.xcopa_vi_ppl_49je23 import xcopa_datasets as xcopa_vi_ppl  
    #------------------------------------------------------
    # SA
    from .datasets.vsmec.vsmec_vi_3i7d12 import vsmec_datasets as vsmec_vi_ppl
    #------------------------------------------------------

datasets = [
    *xquad_vi,
    *flores_en_vi,
    *flores_vi_en,
    *xlsum_vi,
    *m3exam_vi,
    *belebele_vi_ppl,
    *xnli_vi_ppl,
    *xcopa_vi_ppl,
    *vsmec_vi_ppl
]

models = sailor2_1b + sailor2_1b_4bit + sailor2_8b  + sailor2_8b_4bit
