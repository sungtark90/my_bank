import streamlit as st
import sqlite3
import pandas as pd
import os

# DB연결(파일경로)
db_path = "my_bank.db"

# DB파일에서 데이터 추출
file_data = os.path.exists(db_path)

if file_data:
  # DB연결
  conn = sqlite3.connect(db_path)
  # query 작성
  #query = "select * from virtual_loan where credit_score = '1등급'"
  query = "select borrower_name, loan_type, credit_score from virtual_loan" 
  # 쿼리문을 이용해서 데이터 불러오기
  df_a_grade = pd.read_sql(query, conn)

  # Frontend 데이터 웹페이지에 출력
  st.subheader("신용등급이 1등급인 고객 리스트")
  st.dataframe(df_a_grade)

  grade_optin = st.selectbox("확인할 등급을 선택하세요.", df['credit_score'].unique())

  selected_df = df[df['credit_score'] == grade_optin
  st.write(f"{grade_optin}등급 고객 데이터 : ")
  st.dataframe(selected_df)
  
  # DB 연결 종료
  conn.close()
  
else:
  st.error("파일 경로를 확인해 주세요.")

""" 멀티라인 주석처리
st.write("안녕하세요")
print("안녕하세요")

for text in range(2):
  st.write("반갑습니다")
"""
