# atcoder

## 📝概要

atcoder用 python環境

## 🛠️環境構築

### 1. [`mise`](https://mise.jdx.dev/getting-started.html)をインストールする

### 2. 下記コマンドを実行

```bash
mise run setup
```

## 🚀使い方

### 1. コンテストを設定

```bash
mise run sc
```

コンテスト名を (例: `abc123`) を入力すると `contest` ファイルに保存される

### 2. 問題を解く

./main.pyを編集して問題を解く。

```bash
mise run p
```

### 3. 回答を保存

```bash
mise run sv
```

問題番号 (例: `a`) を入力すると:
- `_result/{contest}/{problem}/main.py` に保存
- 自動で `git commit`
- `main.py`がテンプレートにリセット

## 📂ディレクトリ構成

```bash
.
├── main.py                # 作業用メインファイル
├── contest                # 現在のコンテスト名
├── .mise.toml             # 開発ツール管理 (mise)
├── .pre-commit-config.yaml # コードチェック自動化設定
├── shell/
│   ├── setc.sh            # コンテスト設定用スクリプト
│   └── solve.sh           # 解答保存用スクリプト
├── _template/             # テンプレートファイル格納
└── _result/               # 解答保存先
    └── {contest}/
        └── {problem}/
            └── main.py
```
