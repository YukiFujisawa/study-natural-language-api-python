# study-natural-language-api-python

## Install

- Anaconda
    - https://www.anaconda.com/products/individual

## Setup

- Natural Language API の設定
    - https://cloud.google.com/natural-language/docs/setup

## サービス アカウント キーが含まれる JSON ファイルのパスに設定する

zshの場合
```
$ vi ~/.zshrc

# GoogleAPI用
export GOOGLE_APPLICATION_CREDENTIALS="$HOME/Downloads/StudyNaturalLanguageAPI.json"
```

## Natural Language Api勉強用の仮想環境作成

```bash
$ conda create -n google-natural-language-api python=3.8
```

## Start

```bash
# conda activate google-natural-language-api
```

## End

```bash
# conda deactivate google-natural-language-api
```