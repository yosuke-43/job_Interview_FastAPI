# 【面接スケジュール管理API】

このアプリでは、面接スケジュールの管理を行うためのAPIを提供しています。以下の機能が利用できます。

- **Create**: 面接の予定を作成します。
- **Read**: 登録されている面接の予定一覧を確認します。
- **Update**: 登録されている面接の予定を編集・更新します。
- **Delete**: 登録されている面接の予定を削除します。

# セットアップ

## 1. リポジトリのクローン

```
git clone https://github.com/yosuke-43/job_Interview_FastAPI.git
```

## 2. 必要なパッケージのインストール
以下のコマンドを使用して、必要なパッケージをインストールします。
```
pip install fastapi uvicorn pydantic sqlalchemy sqlite streamlit
```

## 3. APIサーバーの起動
```
uvicorn sql_app.main:app --reload
```

## 4. アプリの起動
```
streamlit run app.py
```
以上で、アプリのセットアップが完了しました。