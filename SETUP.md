# Environment Setup — Step by Step

This guide takes you from a fresh computer to a running lab notebook. It assumes **no prior experience** with Python tooling. Follow it top to bottom; the whole process takes about 15 minutes.

**Contents**

1. [What we are installing and why](#1-what-we-are-installing-and-why)
2. [Step 1 — Open a terminal](#2-step-1--open-a-terminal)
3. [Step 2 — Install Git](#3-step-2--install-git)
4. [Step 3 — Install uv](#4-step-3--install-uv)
5. [Step 4 — Download the course repository](#5-step-4--download-the-course-repository)
6. [Step 5 — Create the environment](#6-step-5--create-the-environment)
7. [Step 6 — Run the notebooks](#7-step-6--run-the-notebooks)
8. [Step 7 — Verify that everything works](#8-step-7--verify-that-everything-works)
9. [Keeping your copy up to date](#9-keeping-your-copy-up-to-date)
10. [Adding your own packages (Kaggle League)](#10-adding-your-own-packages-kaggle-league)
11. [uv cheat sheet](#11-uv-cheat-sheet)
12. [Troubleshooting](#12-troubleshooting)
13. [FAQ](#13-faq)

---

## 1. What we are installing and why

### The problem

A machine learning project depends on dozens of Python packages (`numpy`, `pandas`, `scikit-learn`, ...), each in a specific version. Code that works with `pandas 3.0` may fail with `pandas 1.5`, and the other way round. If every student installs "whatever is newest today" into one global Python installation, sooner or later:

- the notebook that ran on the lecturer's laptop does not run on yours,
- installing a package for another course breaks this one,
- nobody can reproduce a result from three months ago.

### The solution: one isolated, locked environment per project

| Concept | What it is | In this repository |
|---|---|---|
| **Python interpreter** | The program that runs `.py` files and notebooks | Python 3.12 (declared in `.python-version`) |
| **Package** | A reusable library installed from [PyPI](https://pypi.org/) | `numpy`, `pandas`, `scikit-learn`, ... |
| **Virtual environment** | A private folder holding one interpreter plus the packages of **one** project, isolated from the rest of your system | the `.venv/` folder (created for you, never committed to Git) |
| **`pyproject.toml`** | The human-written list of what the project needs ("scikit-learn, version 1.9 or newer") | in the repository root |
| **Lock file** | The machine-written list of the *exact* version of every package, including dependencies of dependencies (140 packages) | `uv.lock` |

Because the lock file is part of the repository, **everyone in the course gets a byte-for-byte identical environment** — on Windows, macOS and Linux alike.

### What is uv?

[**uv**](https://docs.astral.sh/uv/) is a modern Python project manager written in Rust by [Astral](https://astral.sh/) (the authors of the `ruff` linter). It is a single small program that replaces a whole zoo of older tools:

| Task | Traditional tool | With uv |
|---|---|---|
| Install Python itself | python.org installer, `pyenv`, Anaconda | `uv python install` (automatic) |
| Create a virtual environment | `python -m venv`, `virtualenv`, `conda create` | `uv sync` (automatic) |
| Install packages | `pip install`, `conda install` | `uv add` / `uv sync` |
| Pin exact versions | `pip freeze`, `pip-tools`, `poetry lock` | `uv lock` (automatic) |
| Run a program inside the environment | `source .venv/bin/activate`, then `python ...` | `uv run ...` |

Why we use it in this course:

- **One command.** `uv sync` reads `uv.lock`, downloads the right Python if you do not have it, creates `.venv/` and installs everything.
- **Fast.** Typically 10–100× faster than `pip`; the full environment installs in well under a minute.
- **Reproducible.** The lock file guarantees identical versions for everybody.
- **No activation needed.** `uv run <command>` always uses the project's environment, so you cannot accidentally use the wrong Python.
- **You do not need Anaconda**, and you do not need to install Python beforehand. If you already have them, that is fine — uv does not interfere with them.

> **Already know `pip` or `conda`?** Think of `pyproject.toml` as `requirements.in` / `environment.yml`, of `uv.lock` as a fully pinned `requirements.txt`, and of `uv sync` as "create the venv and `pip install -r requirements.txt`" in one step.

---

## 2. Step 1 — Open a terminal

All commands in this guide are typed into a terminal (command line).

- **Windows:** press `Win`, type **PowerShell**, press `Enter`. (Use *Windows PowerShell* or *Terminal*, not the old *Command Prompt*.)
- **macOS:** press `Cmd + Space`, type **Terminal**, press `Enter`.
- **Linux:** usually `Ctrl + Alt + T`.

Type a command, press `Enter`, wait for it to finish. Lines starting with `#` in the code blocks below are comments — do not type them.

---

## 3. Step 2 — Install Git

Git downloads the repository and, later, lets you pull updates with one command.

Check whether you already have it:

```bash
git --version
```

If you see a version number (e.g. `git version 2.45.0`), skip to the next step. Otherwise:

- **Windows:** `winget install --id Git.Git -e` — or download the installer from <https://git-scm.com/download/win> and accept the default options. **Close and reopen PowerShell afterwards.**
- **macOS:** `xcode-select --install` and confirm the dialog (or `brew install git` if you use Homebrew).
- **Linux (Debian/Ubuntu):** `sudo apt update && sudo apt install git`

> **No Git, no problem (not recommended):** on the GitHub page of the repository click **Code → Download ZIP** and unpack it. You will have to download the ZIP again every time the materials are updated.

---

## 4. Step 3 — Install uv

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Alternatives: `brew install uv` (macOS), `winget install --id=astral-sh.uv -e` (Windows), `pipx install uv`. Full instructions: <https://docs.astral.sh/uv/getting-started/installation/>.

**Now close the terminal and open a new one** (so that it notices the new program), then check:

```bash
uv --version
```

You should see something like `uv 0.12.x`. If you installed uv a long time ago, update it first — old versions may not understand a current lock file:

```bash
uv self update        # if installed with the script above
brew upgrade uv       # if installed with Homebrew
```

---

## 5. Step 4 — Download the course repository

Choose a folder where you keep your university work, **preferably one whose path has no spaces or non-ASCII characters** (e.g. `C:\Users\anna\uw`, not `C:\Users\Żaneta\Moje dokumenty\Studia (mgr)`), and not a folder synchronised by OneDrive / iCloud / Dropbox (`.venv` contains tens of thousands of small files).

```bash
cd path/to/your/folder
git clone https://github.com/wne-uw-mjwozniak/wne-uw-ml1-qf-labs-materials.git
cd wne-uw-ml1-qf-labs-materials
```

All remaining commands must be run **from inside this folder** (the one containing `pyproject.toml`).

---

## 6. Step 5 — Create the environment

```bash
uv sync
```

What happens:

1. uv reads `.python-version` and, if you do not have Python 3.12, downloads it (into uv's own cache — your system is untouched).
2. It creates the virtual environment in `.venv/`.
3. It installs the exact package versions recorded in `uv.lock`.

The first run downloads a few hundred MB and takes a minute or two; later runs take a second. You should end with a line similar to `Installed 133 packages in ...`.

> You never need to "activate" the environment. Just prefix commands with `uv run`.

---

## 7. Step 6 — Run the notebooks

### Option A — JupyterLab in the browser (simplest)

```bash
uv run jupyter lab
```

Your browser opens JupyterLab. In the file panel on the left open the `notebooks/` folder and double-click a notebook. Run a cell with `Shift + Enter`; run everything with **Run → Run All Cells**.

To stop JupyterLab, go back to the terminal and press `Ctrl + C` (twice).

### Option B — VS Code (recommended for regular work)

An IDE gives you code completion, a debugger, a variable explorer and Git integration.

1. Install [VS Code](https://code.visualstudio.com/) and, inside it, the **Python** and **Jupyter** extensions (Extensions icon in the left bar → search → Install).
2. **File → Open Folder...** and choose the `wne-uw-ml1-qf-labs-materials` folder (the repository root, not `notebooks/`).
3. Open a notebook from `notebooks/`.
4. Click **Select Kernel** (top-right corner) → **Python Environments...** → choose the entry containing **`.venv`**.
   If it is not listed: `Ctrl/Cmd + Shift + P` → **Python: Select Interpreter** → **Enter interpreter path...** →
   - Windows: `.venv\Scripts\python.exe`
   - macOS / Linux: `.venv/bin/python`
5. Run cells with `Shift + Enter`.

[Cursor](https://www.cursor.com/) works identically. In [PyCharm](https://www.jetbrains.com/pycharm/): *Settings → Project → Python Interpreter → Add Interpreter → Add Local Interpreter → Existing* and point it to the same `.venv` path.

---

## 8. Step 7 — Verify that everything works

Run this one-liner from the repository root:

```bash
uv run python -c "import sys, numpy, pandas, sklearn, statsmodels, imblearn, skopt; print('Python', sys.version.split()[0]); print('numpy', numpy.__version__, '| pandas', pandas.__version__, '| scikit-learn', sklearn.__version__); print('Environment OK')"
```

Expected output (patch versions may differ after an update of the materials):

```text
Python 3.12.x
numpy 2.5.x | pandas 3.0.x | scikit-learn 1.9.x
Environment OK
```

Then open `notebooks/python_course.ipynb` and choose **Run → Run All Cells**. If it finishes without a red error box, you are ready for the labs.

---

## 9. Keeping your copy up to date

The materials are updated during the semester. Before each class:

```bash
git pull      # download the latest notebooks
uv sync       # update the environment if the lock file changed
```

**Tip — avoid merge conflicts:** do not edit the original notebooks. Make a copy first (e.g. `knn.ipynb` → `knn_my_notes.ipynb`) and work in the copy. If `git pull` still complains about local changes you do not want to keep:

```bash
git stash     # puts your local changes aside (recover them later with: git stash pop)
git pull
```

---

## 10. Adding your own packages (Kaggle League)

The Kaggle League rules require a notebook that *"runs top-to-bottom without errors in a clean environment"*. The safest way to achieve that is to build your solution on top of this very environment.

```bash
uv add polars              # adds the package to pyproject.toml, updates uv.lock, installs it
uv remove polars           # the reverse
```

Do **not** use `pip install` inside the project: packages installed that way are not recorded anywhere and will be removed by the next `uv sync`.

For your own project outside this repository:

```bash
mkdir my-kaggle-team && cd my-kaggle-team
uv init --python 3.12
uv add numpy pandas scikit-learn matplotlib jupyter ipykernel
uv run jupyter lab
```

---

## 11. uv cheat sheet

| Command | What it does |
|---|---|
| `uv sync` | Make `.venv` match `uv.lock` exactly (create it if missing) |
| `uv run jupyter lab` | Start JupyterLab inside the project environment |
| `uv run python script.py` | Run a script inside the project environment |
| `uv run python --version` | Show which Python the project uses |
| `uv add <package>` | Add a dependency |
| `uv remove <package>` | Remove a dependency |
| `uv pip list` | List installed packages and versions |
| `uv tree` | Show the dependency tree |
| `uv lock --upgrade` | Upgrade all packages to the newest allowed versions (**do not do this in the course repository** — you would no longer match the rest of the group) |
| `uv python list` | Show available / installed Python versions |
| `uv cache clean` | Delete uv's download cache (frees disk space) |
| `uv self update` | Update uv itself |

---

## 12. Troubleshooting

**`uv: command not found` / `uv is not recognized as the name of a cmdlet`**
The terminal was opened before uv was installed — close it and open a new one. If that does not help, the installer printed the folder it installed into (usually `~/.local/bin` on macOS/Linux, `%USERPROFILE%\.local\bin` on Windows); add it to your `PATH` or simply re-run the installer and follow its final instructions.

**Windows: `running scripts is disabled on this system`**
Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` in PowerShell, confirm with `Y`, and repeat the installation.

**`error: No pyproject.toml found`** (or `uv sync` creates an empty environment)
You are in the wrong folder. `cd` into `wne-uw-ml1-qf-labs-materials` — the `ls` (macOS/Linux) or `dir` (Windows) command should list `pyproject.toml`.

**`Failed to parse uv.lock` or complaints about the lock file format**
Your uv is outdated. Run `uv self update` (or `brew upgrade uv`) and try again.

**`ModuleNotFoundError: No module named 'sklearn'` inside a notebook**
The notebook is running on the wrong kernel (your global Python instead of the project's `.venv`). In VS Code pick the `.venv` kernel (Step 6, Option B). In JupyterLab make sure you started it with `uv run jupyter lab` from the repository root, not from a desktop shortcut or Anaconda Navigator.

**VS Code does not list `.venv` among the kernels**
You probably opened the `notebooks/` sub-folder or a single file. Use **File → Open Folder...** on the repository root, then **Developer: Reload Window** from the command palette. If needed, enter the interpreter path manually (Step 6, Option B, point 4).

**SSL / certificate / proxy errors during `uv sync`** (common on corporate laptops and some university networks)
Try another network (e.g. a phone hotspot) or run `uv sync --system-certs` (in older uv versions the flag is called `--native-tls`), which makes uv use the certificates of your operating system.

**`uv sync` is interrupted or the environment looks broken**
Delete the environment and start again — it is completely disposable:

```bash
# macOS / Linux
rm -rf .venv && uv sync
# Windows PowerShell
Remove-Item -Recurse -Force .venv; uv sync
```

**A dataset fails to download** (`fetch_california_housing`, `URLError`, `HTTP Error 503`)
Some notebooks download a public dataset on first use and cache it in `~/scikit_learn_data`. The first run needs internet access; if the server is temporarily unavailable, try again later. Datasets stored in the `data/` folder of this repository need no connection.

**Apple Silicon (M1–M4), Windows on ARM**
Nothing special to do — uv installs native builds automatically.

**Still stuck?**
Copy the *full* error message (text, not a photo of the screen), note your operating system and the output of `uv --version`, and ask during the lab or by e-mail.

---

## 13. FAQ

**Do I need to install Python or Anaconda first?**
No. uv downloads and manages the right Python version on its own.

**I already have Anaconda. Will there be a conflict?**
No. The project environment lives entirely in `.venv/` and ignores conda. If your prompt shows `(base)`, that is harmless — just always use `uv run ...`. (Optional: `conda config --set auto_activate_base false` stops conda from activating itself in every terminal.)

**Can I use Google Colab instead?**
The notebooks will mostly run there, but Colab ships different package versions, so outputs and even behaviour may differ, and files from `data/` have to be uploaded manually. We strongly recommend the local setup — you will need it for the Kaggle League anyway.

**How much disk space does it take?**
About 1 GB (`.venv` is roughly 600 MB; the rest is uv's download cache). `uv cache clean` frees the cache.

**What is `.venv` and may I delete it?**
It is the virtual environment. It is safe to delete at any time; `uv sync` recreates it in seconds.

**Why is there no `requirements.txt`?**
`pyproject.toml` + `uv.lock` serve the same purpose, with exact and cross-platform pinning. If another tool needs one: `uv export --format requirements-txt > requirements.txt`.
