# 【面接スケジュール管理API】
このアプリではCRUD機能として以下のことが実現できます。
- create 面接の予定を作成できる
- read 面接の予定一覧を確認できる
- update 登録している面接の予定を編集、更新できる
- delete 登録している面接の予定を削除できる


# セットアップ
#### 必要なパッケージのインストール
```zsh
pip install fastapi uvicorn pydantic sqlalchemy sqlite streamlit
```
ターミナルを2つ準備する。
#### APIサーバーの立ち上げ
ターミナルの1つを使いローカルでAPIサーバーを立ち上げる
```zsh
uvicorn sql_app.main:app --reload
```
#### アプリの立ち上げ
ターミナルのもう1つを使いローカルでアプリを立ち上げる
```zsh
streamlit run app.py
```