import streamlit as st
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

# DataFrameが空の場合
if df_interviews.empty:
    st.write("予定している面接はありません。")
else:
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


st.write('#### 面接編集')
# 面接編集フォーム
with st.form(key='edit_interview'):
    interview_id_to_edit = st.number_input('編集する面接のidを入力してください:', min_value=1)
    edit_button = st.form_submit_button(label='編集')

# 編集ページの表示部分
if edit_button:
    # 指定された面接IDが存在するか確認
    if interview_id_to_edit not in df_interviews['面接id'].values:
        st.error('指定された面接が見つかりませんでした')
    else:
        # 編集ページに遷移する
        st.session_state.interview_id_to_edit = interview_id_to_edit

# 編集ページでの処理
if 'interview_id_to_edit' in st.session_state:
    interview_id_to_edit = st.session_state.interview_id_to_edit
    selected_interview = df_interviews[df_interviews['面接id'] == int(interview_id_to_edit)].iloc[0]

    # 編集フォームを表示
    form_key = f'edit_interview_{interview_id_to_edit}'  # ユニークなキーを生成する
    with st.form(key=form_key):
        company_name = st.text_input('企業名', value=selected_interview['企業名'], max_chars=50)
        # 日付入力のデフォルト値が現在の日付以上になるようにする
        interview_date = datetime.datetime.strptime(selected_interview['面接開始日時'], '%Y/%m/%d %H:%M').date()
        default_date = max(interview_date, datetime.date.today())
        date = st.date_input('日付: ', value=default_date, min_value=datetime.date.today())
        start_time = st.time_input('開始時刻: ', value=datetime.datetime.strptime(selected_interview['面接開始日時'], '%Y/%m/%d %H:%M').time())
        location = st.text_input('面接場所', value=selected_interview['面接場所'])
        submit_button = st.form_submit_button(label='保存')

    if submit_button:
        data = {
            'company_name': company_name,
            'interview_datetime': datetime.datetime(year=date.year, month=date.month, day=date.day, hour=start_time.hour, minute=start_time.minute).isoformat(),
            'location': location
        }
        url_edit = f'http://127.0.0.1:8000/interviews/{interview_id_to_edit}'
        headers = {"Content-Type": "application/json"}
        res_edit = requests.patch(url_edit, data=json.dumps(data), headers=headers)

        if res_edit.status_code == 200:
            st.success('面接が編集されました')
        else:
            st.error('面接の編集中にエラーが発生しました')


st.write('#### 面接削除')
# 面接削除フォーム
with st.form(key='delete_interview'):
    interview_id_to_delete = st.number_input('削除する面接のidを入力してください:', min_value=1)
    delete_button = st.form_submit_button(label='削除')

if delete_button:
    # 指定された面接IDが存在するか確認
    if interview_id_to_delete not in df_interviews['面接id'].values:
        st.error('指定された面接が見つかりませんでした')
    else:
        url_delete = f'http://127.0.0.1:8000/interviews/{interview_id_to_delete}'
        res_delete = requests.delete(url_delete)
        if res_delete.status_code == 200:
            st.success('面接が削除されました')
        else:
            st.error('面接の削除中にエラーが発生しました')



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