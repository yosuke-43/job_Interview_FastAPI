import streamlit as st # Streamlitというpython用のUIを編集できるフレームワーク
import datetime
import random
import requests
import json

st.title('APIテスト画面')

with st.form(key='interview'):
  interview_id: int = random.randint(0, 10)
  company_name: str = st.text_input('企業名', max_chars=50)
  date = st.date_input('日付: ', min_value=datetime.date.today())
  # streamlitに日時型がないので、日付型と時間型を分けて作って後でマージする
  start_time = st.time_input('開始時刻: ', value=datetime.time(hour=10, minute=0))
  location: str = st.text_input('面接場所', value='オンライン')
  data = {
    'interview_id': interview_id,
    'company_name': company_name,
    'interview_datetime': datetime.datetime(
      year=date.year,
      month=date.month,
      day=date.day,
      hour=start_time.hour,
      minute=start_time.minute
    ).isoformat(),
    'location': location
  }
  submit_button = st.form_submit_button(label='リクエスト送信')

if submit_button:
  st.write('## 送信データ')
  st.json(data)
  st.write('## レスポンス結果')
  url = 'http://127.0.0.1:8000/interviews'
  res = requests.post(
    url,
    data=json.dumps(data)
  )
  st.write(res.status_code)
  st.json(res.json())