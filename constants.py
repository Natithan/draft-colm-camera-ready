from os.path import join as jn
import getpass
USER = getpass.getuser()
on_VSC = USER.startswith("vsc")
VSC_USER_ID = USER if USER.startswith("vsc") else "vsc33642"
LIIR_DATA_ROOT_DIR = '/cw/liir_data/NoCsBack'
VSC_DATA_ROOT_DIR = f"/scratch/leuven/{VSC_USER_ID[3:6]}/{VSC_USER_ID}"

DATA_ROOT_DIR = LIIR_DATA_ROOT_DIR if not on_VSC else VSC_DATA_ROOT_DIR

NATHAN_CODE_ROOT_DIR = '/cw/liir_code/NoCsBack/nathan'
FLORIAN_CODE_ROOT_DIR = '/cw/liir_code/NoCsBack/florian'
VSC_CODE_ROOT_DIR = f"/data/leuven/{VSC_USER_ID[3:6]}/{VSC_USER_ID}"

# match USER:
#     case 'nathan':
#         CODE_ROOT_DIR = NATHAN_CODE_ROOT_DIR
#     case 'florianm':
#         CODE_ROOT_DIR = FLORIAN_CODE_ROOT_DIR
#     case VSC_USER_ID:
#         CODE_ROOT_DIR = VSC_CODE_ROOT_DIR
#     case _:
#         raise ValueError(f"Unknown user: {USER}")
CODE_ROOT_DIR = NATHAN_CODE_ROOT_DIR if USER == 'nathan' else FLORIAN_CODE_ROOT_DIR if USER == 'florianm' else VSC_CODE_ROOT_DIR if on_VSC else None

CODE_DIR = jn(CODE_ROOT_DIR,"muLM")
SF_CACHE_DIR = jn(CODE_ROOT_DIR, 'hf-cache' if USER == 'florianm' else 'huggingface_cache_nathan')
WIKI_DIR = jn(DATA_ROOT_DIR, 'wikipedia')
EN_WIKI_FILE = jn(WIKI_DIR, 'enwiki-latest.json.gz') # /cw/liir_data/NoCsBack/wikipedia/enwiki-latest.json.gz
EN_WIKI_ARTICLE_COUNT = 5866389 # Takes a few minutes to compute. To compute: sum(1 for _ in open(EN_WIKI_FILE, 'r'))
NEW_EN_WIKI_ARTICLE_COUNT = 6458670 # load_dataset("wikipedia", "20220301.en").shape['train'][0]
DOLMA_ARTICLE_COUNT = 13095416 # load_dataset("allenai/dolma", "v1_6-sample").shape['train'][0]
DEFAULT_PICKLE_DIR =jn(CODE_DIR if not on_VSC else jn(DATA_ROOT_DIR,'muLM')
                       , 'pickles') # /cw/liir_code/NoCsBack/nathan/muLM/pickles
DEFAULT_LLM = "meta-llama/Llama-2-7b-hf"
DEFAULT_CKPT_DIR = jn(CODE_DIR if not on_VSC else jn(DATA_ROOT_DIR,'muLM')
                      , 'checkpoints') # /cw/liir_code/NoCsBack/nathan/muLM/checkpoints
OTHER_CKPT_DIR = jn(FLORIAN_CODE_ROOT_DIR, 'muLM', 'checkpoints') # /cw/liir_code/NoCsBack/florian/muLM/checkpoints

SHORT2FULL_EMBEDDER_NAME = { # See https://huggingface.co/spaces/mteb/leaderboard
    'mpnet': 'sentence-transformers/all-mpnet-base-v2',
    'bge_base': 'BAAI/bge-base-en-v1.5'
}
FULL2SHORT_EMBEDDER_NAME = {v: k for k, v in SHORT2FULL_EMBEDDER_NAME.items()}
DEFAULT_EMBEDDER = 'sentence-transformers/all-mpnet-base-v2'
FIXED_CODE = 0
EOT_STRING = "<|endoftext|>"