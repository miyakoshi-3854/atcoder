# atcoder

<a href="https://atcoder.jp/users/miyakoshi_">
    <img src="https://atcoder-readme-stats.vercel.app/stats/miyakoshi_?show_icons=true&width=435&height=200" />
</a>

## Overview

Python environment for AtCoder practice.

## Setup

### 1. Install [`mise`](https://mise.jdx.dev/getting-started.html)

### 2. Run

```bash
mise run setup
```

## Usage

### 1. Set the contest

```bash
mise run sc
```

Enter the contest name (e.g. `abc123`) when prompted. This will be saved to the `contest` file.

### 2. Solve a problem

Edit `main.py` and run:

```bash
mise run p
```

### 3. Save your answer

```bash
mise run sv
```

Enter the problem letter (e.g. `a`) when prompted. This will:

- Save to `_result/{contest}/{problem}/main.py`
- Commit automatically with git
- Reset `main.py` to the template

## Directory Structure

```
.
├── main.py                  # Working file
├── contest                  # Current contest name
├── .mise.toml               # Dev tool config (mise)
├── .pre-commit-config.yaml  # Pre-commit hooks
├── shell/
│   ├── setc.sh              # Contest setup script
│   └── solve.sh             # Save script
├── _template/               # Template files
└── _result/                 # Saved answers
    └── {contest}/
        └── {problem}/
            └── main.py
```
