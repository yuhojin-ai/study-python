# 라이브러리 임포트
import tkinter as tk              # tkinter: GUI를 만들기 위한 기본 라이브러리
from tkinter import ttk, messagebox  # ttk: 고급 위젯, messagebox: 팝업 메시지 창
import requests                   # requests: 웹사이트 요청용 라이브러리
from bs4 import BeautifulSoup     # BeautifulSoup: HTML 파싱 라이브러리

# 상수 정의
URL = 'https://finance.naver.com/marketindex/'  # 환율 정보를 가져올 네이버 금융 URL
HEADERS = {"User-Agent": "Mozilla/5.0"}         # 요청할 때 사용할 헤더 설정 (브라우저처럼 요청하기 위해)
TARGET_CURRENCIES = {                           # 가져올 목표 통화 (한글명 -> 약어 매칭)
    "미국 USD": "USD",
    "일본 JPY(100엔)": "JPY",
    "유럽연합 EUR": "EUR",
    "중국 CNY": "CNY"
}

# 1. 환율 정보 가져오기 함수
def get_exchange_rates():
    """
    네이버 금융 페이지에서 환율 정보를 크롤링해오는 함수
    """
    try:
        response = requests.get(URL, headers=HEADERS)  # 네이버에 요청
        response.raise_for_status()                   # HTTP 오류 발생시 예외 발생
        soup = BeautifulSoup(response.text, 'html.parser')  # HTML 파싱

        exchange_rates = {}                            # 환율 저장할 딕셔너리
        exchange_list = soup.select('div.market1 li')  # 주요 통화 리스트 가져오기

        for item in exchange_list:                     # 각각의 통화 항목에 대해
            name_tag = item.select_one('h3')            # 통화명 추출
            value_tag = item.select_one('span.value')   # 환율값 추출

            if name_tag and value_tag:                  # 둘 다 존재할 경우에만
                currency_name = name_tag.text.strip()   # 통화명 텍스트 추출 및 양쪽 공백 제거
                if currency_name in TARGET_CURRENCIES:  # 우리가 찾는 통화면
                    krw_value = float(value_tag.text.replace(',', ''))  # 쉼표 제거 후 실수 변환
                    exchange_rates[TARGET_CURRENCIES[currency_name]] = krw_value  # 딕셔너리에 저장

        if not exchange_rates:                         # 만약 환율 정보가 하나도 없다면
            raise ValueError("환율 정보를 찾을 수 없습니다.")  # 에러 발생

        return exchange_rates                          # 정상적으로 환율 딕셔너리 반환

    except Exception as e:
        messagebox.showerror("환율 가져오기 실패", f"에러: {e}")  # 팝업창으로 에러 메시지 출력
        return None

# 2. 환전 계산 함수
def convert_currency():
    """
    입력한 원화를 선택한 통화로 환산하여 결과를 출력하는 함수
    """
    try:
        krw_amount = float(entry_krw.get())             # 입력된 원화 금액 가져오기
        selected_currency = currency_var.get()          # 선택한 통화 가져오기

        if selected_currency not in exchange_rates:     # 통화가 없으면 에러 처리
            messagebox.showerror("선택 오류", "통화를 선택해주세요.")
            return

        rate = exchange_rates[selected_currency]        # 선택한 통화의 환율
        converted_amount = krw_amount / rate            # 원화 금액을 환율로 나눠서 변환

        result_label.config(text=f"환전 결과: {converted_amount:.2f} {selected_currency}")  # 결과 출력

    except ValueError:
        messagebox.showerror("입력 오류", "유효한 숫자를 입력해주세요.")  # 숫자 변환 실패시 에러 출력

# --- 프로그램 시작 (메인 흐름) ---
exchange_rates = get_exchange_rates()                  # 프로그램 실행 시 환율 데이터 가져오기
print(exchange_rates)
if not exchange_rates:                                 # 환율 정보 없으면 프로그램 종료
    exit()

# --- tkinter 윈도우 생성 ---
root = tk.Tk()                                          # 메인 창 생성
root.title("KRW 환율 계산기")                            # 창 제목 설정

# --- 대한민국 원 입력 부분 ---
tk.Label(root, text="대한민국 원 (KRW)").grid(row=0, column=0, padx=10, pady=10)  # 입력창 라벨
entry_krw = tk.Entry(root)                              # 금액 입력창 생성
entry_krw.grid(row=0, column=1, padx=10, pady=10)

# --- 변환 통화 선택 부분 ---
tk.Label(root, text="변환할 통화 선택").grid(row=1, column=0, padx=10, pady=10)    # 통화 선택 라벨
currency_var = tk.StringVar()                          # 선택 통화 저장할 변수
currency_combo = ttk.Combobox(root, textvariable=currency_var, values=list(exchange_rates.keys()), state="readonly")  # 콤보박스 생성
currency_combo.grid(row=1, column=1, padx=10, pady=10)
currency_combo.set('USD')                              # 기본 선택 통화는 USD

# --- 환전 버튼 ---
tk.Button(root, text="환전하기", command=convert_currency).grid(row=2, column=0, columnspan=2, pady=10)  # 환전 버튼

# --- 환전 결과 표시 부분 ---
result_label = tk.Label(root, text="환전 결과: ")       # 결과 표시 레이블
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# --- 메인 루프 실행 ---
root.mainloop()                                         # tkinter 이벤트 루프 실행
