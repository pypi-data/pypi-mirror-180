# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['inseq',
 'inseq.attr',
 'inseq.attr.feat',
 'inseq.attr.feat.ops',
 'inseq.commands',
 'inseq.data',
 'inseq.models',
 'inseq.utils']

package_data = \
{'': ['*']}

install_requires = \
['captum>=0.5.0,<0.6.0',
 'json-tricks>=3.15.5,<4.0.0',
 'matplotlib>=3.5.2,<4.0.0',
 'numpy>=1.22.4,<2.0.0',
 'poethepoet>=0.13.1,<0.14.0',
 'protobuf>=3.20.2,<4.0.0',
 'rich>=10.13.0,<11.0.0',
 'scipy>=1.8.1,<2.0.0',
 'torch>=1.13.0,<2.0.0',
 'torchtyping>=0.1.4,<0.2.0',
 'tqdm>=4.64.0,<5.0.0',
 'transformers[sentencepiece,tokenizers,torch]>=4.22.0,<5.0.0']

extras_require = \
{'datasets': ['datasets[torch]>=2.3.2,<3.0.0'],
 'notebook': ['ipykernel>=6.15.0,<7.0.0', 'ipywidgets>=8.0.0rc2,<9.0.0'],
 'sklearn': ['joblib>=1.2.0,<2.0.0', 'scikit-learn>=1.1.1,<2.0.0']}

entry_points = \
{'console_scripts': ['inseq = inseq.commands.cli:main']}

setup_kwargs = {
    'name': 'inseq',
    'version': '0.3.1',
    'description': 'Interpretability for Sequence Generation Models 🔍',
    'long_description': '<div align="center">\n  <img src="/docs/source/images/inseq_logo.png" width="300"/>\n  <h4>Intepretability for Sequence Generation Models 🔍</h4>\n</div>\n<br/>\n<div align="center">\n\n[![Build status](https://github.com/inseq-team/inseq/workflows/build/badge.svg?branch=master&event=push)](https://github.com/inseq-team/inseq/actions?query=workflow%3Abuild)\n[![Python Version](https://img.shields.io/pypi/pyversions/inseq.svg)](https://pypi.org/project/inseq/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![License](https://img.shields.io/github/license/inseq-team/inseq)](https://github.com/inseq-team/inseq/blob/main/LICENSE)\n\n</div>\n\nInseq is a Pytorch-based hackable toolkit to democratize the access to common post-hoc **in**terpretability analyses of **seq**uence generation models.\n\n## Installation\n\nInseq is available on PyPI and can be installed with `pip`:\n\n```bash\npip install inseq\n```\n\n<details>\n  <summary>Dev Installation</summary>\nTo install the package, clone the repository and run the following commands:\n\n```bash\ncd inseq\nmake poetry-download # Download and install the Poetry package manager\nmake install # Installs the package and all dependencies\n```\n\nIf you have a GPU available, use `make install-gpu` to install the latest `torch` version with GPU support.\n\nFor library developers, you can use the `make install-dev` command to install and its GPU-friendly counterpart `make install-dev-gpu` to install all development dependencies (quality, docs, extras).\n\nAfter installation, you should be able to run `make fast-test` and `make lint` without errors.\n</details>\n\n<details>\n  <summary>FAQ Installation</summary>\n\n  - Installing the `tokenizers` package requires a Rust compiler installation. You can install Rust from [https://rustup.rs](https://rustup.rs) and add `$HOME/.cargo/env` to your PATH.\n\n  - Installing `sentencepiece` requires various packages, install with `sudo apt-get install cmake build-essential pkg-config` or `brew install cmake gperftools pkg-config`.\n</details>\n\n## Example usage in Python\n\nThis example uses the Integrated Gradients attribution method to attribute the English-French translation of a sentence taken from the WinoMT corpus:\n\n```python\nimport inseq\n\nmodel = inseq.load_model("Helsinki-NLP/opus-mt-en-fr", "integrated_gradients")\nout = model.attribute(\n  "The developer argued with the designer because her idea cannot be implemented.",\n  n_steps=100\n)\nout.show()\n```\n\nThis produces a visualization of the attribution scores for each token in the input sentence (token-level aggregation is handled automatically). Here is what the visualization looks like inside a Jupyter Notebook:\n\n![WinoMT Attribution Map](docs/source/images/heatmap_winomt.png)\n\nInseq also supports decoder-only models such as [GPT-2](https://huggingface.co/transformers/model_doc/gpt2.html), enabling usage of a variety of attribution methods and customizable settings directly from the console:\n\n```python\nimport inseq\n\nmodel = inseq.load_model("gpt2", "integrated_gradients")\nmodel.attribute(\n    "Hello ladies and",\n    generation_args={"max_new_tokens": 9},\n    n_steps=500,\n    internal_batch_size=50\n).show()\n```\n\n![GPT-2 Attribution in the console](docs/source/images/inseq_python_console.gif)\n\n## What does Inseq support?\n\n- Feature attribution of sequence generation for most `ForConditionalGeneration` (encoder-decoder) and `ForCausalLM` (decoder-only) models from 🤗 Transformers\n\n- Support for single and batched attribution using multiple gradient-based feature attribution methods from Captum\n\n- Post-hoc aggregation of feature attribution maps via `Aggregator` classes.\n\n- Attribution visualization in notebooks, browser and command line.\n\n- Command line interface for attributing single examples or entire 🤗 datasets.\n\n- Custom attribution of target functions, supporting advanced usage for cases such as contrastive and uncertainty-weighted feature attributions.\n\n- Extract and visualize custom scores for every generation step alongsides attribution maps.\n\n## What we plan to support in the future?\n\n- Attention-based and occlusion-based feature attribution methods\n\n- Interoperability with other interpretability libraries\n\n- Rich and interactive visualizations in a tabbed interface\n\n## Using the Inseq client\n\nThe Inseq library also provides useful client commands to enable repeated attribution of individual examples and even entire 🤗 datasets directly from the console. See the available options by typing `inseq -h` in the terminal after installing the package.\n\nFor now, two commands are supported:\n\n- `ìnseq attribute`: Wraps the `attribute` method shown above, requires explicit inputs to be attributed.\n\n- `inseq attribute-dataset`: Enables attribution for a full dataset using Hugging Face `datasets.load_dataset`.\n\nBoth commands support the full range of parameters available for `attribute`, attribution visualization in the console and saving outputs to disk.\n\n**Example:** The following command can be used to perform attribution (both source and target-side) of Italian translations for a dummy sample of 20 English sentences taken from the FLORES-101 parallel corpus, using a MarianNMT translation model from Hugging Face `transformers`. We save the visualizations in HTML format in the file `attributions.html`. See the `--help` flag for more options.\n\n```bash\ninseq attribute-dataset \\\n  --model_name_or_path Helsinki-NLP/opus-mt-en-it \\\n  --attribution_method saliency \\\n  --do_prefix_attribution \\\n  --dataset_name inseq/dummy_enit \\\n  --input_text_field en \\\n  --dataset_split "train[:20]" \\\n  --viz_path attributions.html \\\n  --batch_size 8 \\\n  --hide\n```',
    'author': 'The Inseq Team',
    'author_email': 'None',
    'maintainer': 'gsarti',
    'maintainer_email': 'gabriele.sarti996@gmail.com',
    'url': 'https://github.com/inseq-team/inseq',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<3.12',
}


setup(**setup_kwargs)
