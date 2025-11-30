# Hello, Tinker 👋

Welcome to a tiny, beginner-friendly playground for the [Tinker](https://github.com/thinkingmachines/tinker) API. This repo is meant for workshops, demos, and "Hello World" experiments—clone it whenever you need a clean starting point.

## What's inside?

- `notebooks/00_check_env.ipynb` — sanity checks for your Python/Jupyter environment and SDK versions.
- `notebooks/01_tinker_hello_LoRA_world.ipynb` — a minimal LoRA fine-tuning walkthrough that keeps all of the original demo logic intact.
- `test_env.py` — quick CLI script to confirm your `.env` file is wired up.

> **Community note:** this is an independent community project and is **not** affiliated with or endorsed by Thinking Machines Lab.

## Quickstart

1. **Clone the template**
   ```bash
   git clone https://github.com/<your-org>/Tinker-hello-world-notebooks.git
   cd Tinker-hello-world-notebooks
   ```
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Open .env and paste your Tinker API key
   ```
5. **Verify your setup**
   ```bash
   python test_env.py
   ```
   You should see `TINKER_API_KEY present: True` before launching any notebooks.

## Running the notebooks

1. Start Jupyter (Lab or Notebook):
   ```bash
   jupyter lab  # or: jupyter notebook
   ```
2. Open `notebooks/00_check_env.ipynb` and run all cells from top to bottom. This confirms your interpreter, file paths, and SDK versions.
3. Move on to `notebooks/01_tinker_hello_LoRA_world.ipynb`. The first markdown cell acts as a mini tutorial—follow it step-by-step to configure a service client, choose a base model, and kick off a LoRA run.
4. Keep everything in order: run cells sequentially so credentials are loaded before you interact with the service.

## Notebooks

- `00_check_env.ipynb` – Verify environment, install deps.
- `01_tinker_hello_LoRA_world.ipynb` – Original Tinker LoRA hello world.
- `02_basketball_prompt_distill.ipynb` – Basketball prompt distillation example.
- `03_tinker_hello_LoRA_piglatin_wandb.ipynb` – Pig Latin LoRA fine-tune with W&B logging.

### How to run the Pig Latin + W&B demo

1. Create and activate the virtualenv.
2. Install requirements: `pip install -r requirements.txt`.
3. Start JupyterLab in the repo.
4. Run `00_check_env.ipynb`.
5. Open `03_tinker_hello_LoRA_piglatin_wandb.ipynb` and:
   - Run all cells top to bottom.
   - Make sure `USE_WANDB = True` and you’re logged into W&B.
6. Watch the run under the `tinker-hello-world` project in your W&B workspace.

## Troubleshooting tips

- **Missing API key?** Double-check `.env` and re-run `python test_env.py`.
- **Module import errors?** Re-install requirements inside the same interpreter used by Jupyter.
- **Notebook can't find `.env`?** Ensure you're launching Jupyter from the repo root so relative paths resolve correctly.

Have fun tinkering! Feel free to fork this template and adapt it for your own workshops.
