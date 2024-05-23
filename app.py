import streamlit as st # Streamlitというpython用のUIを編集できるフレームワーク
import datetime
import requests
import json
import pandas as pd

st.title('面接予約画面')

st.write('#### 面接一覧')
# 面接一覧取得
url_interviews = 'http://127.0.0.1:8000/interviews'
res = requests.get(url_interviews)
interviews = res.json()
df_interviews = pd.DataFrame(interviews)

# 日時のフォーマットを見やすい形に変換
to_datetime = lambda x: datetime.datetime.fromisoformat(x).strftime('%Y/%m/%d %H:%M')

# 面接開始日時の列に適用
df_interviews['interview_datetime'] = df_interviews['interview_datetime'].map(to_datetime)

df_interviews = df_interviews.rename(columns={
  'company_name': '企業名',
  'interview_datetime': '面接開始日時',
  'location': '面接場所',
  'interview_id': '面接id'
}) 
st.table(df_interviews)

st.write('#### 面接登録')
# 面接一覧取得
with st.form(key='interview'):
  # interview_id: int = random.randint(0, 10)
  company_name: str = st.text_input('企業名', max_chars=50)
  date = st.date_input('日付: ', min_value=datetime.date.today())
  # streamlitに日時型がないので、日付型と時間型を分けて作って後でマージする
  start_time = st.time_input('開始時刻: ', value=datetime.time(hour=10, minute=0))
  location: str = st.text_input('面接場所', value='オンライン')
  data = {
    # 'interview_id': interview_id,
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
  submit_button = st.form_submit_button(label='面接登録')

if submit_button:
  url = 'http://127.0.0.1:8000/interviews'
  res = requests.post(
    url,
    data=json.dumps(data)
  )
  if res.status_code == 200:
    st.success('面接登録完了')
  st.write(res.status_code)
  st.json(res.json())