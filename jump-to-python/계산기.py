import tkinter as tk  # tkinter: 파이썬으로 화면(GUI)을 만드는 라이브러리
import math  # math: 삼각함수, 로그 등 수학 기능을 제공하는 라이브러리

class ScientificCalculator:  # 과학 계산기 클래스 정의
    def __init__(self, root):
        self.root = root  # Tk 윈도우 창 연결
        self.root.title("Scientific Calculator")  # 창 제목 설정
        self.ans = None  # 마지막 계산 결과를 저장할 변수

        # 숫자 입력 칸 생성 (오른쪽 정렬, 연한 파랑 배경)
        self.entry = tk.Entry(root, width=30, font=('Arial', 16), justify='right', bg='#f0f8ff')
        self.entry.grid(row=0, column=0, columnspan=5, pady=10)  # 첫 번째 줄에 위치

        self.create_buttons()  # 버튼 생성 함수 호출

    def create_buttons(self):  # 버튼을 배열로 만들어 배치하는 함수
        btns = [  # 버튼 글자 배열
            ["sin", "cos", "tan", "log", "ln"],
            ["(", ")", "x!", "√", "%"],
            ["7", "8", "9", "÷", "AC"],
            ["4", "5", "6", "×", "x^y"],
            ["1", "2", "3", "-", "Ans"],
            ["0", ".", "EXP", "+", "="]
        ]

        colors = {  # 버튼별 색상 설정
            'function': '#add8e6',  # 함수 버튼(삼각함수 등) - 연한 파랑
            'number': '#ffffff',    # 숫자 버튼 - 흰색
            'operator': '#87ceeb',  # 연산자 버튼(+, -, ×, ÷) - 하늘색
            'special': '#ffa07a'    # 특별 버튼(AC, =) - 주황색
        }

        for r, row in enumerate(btns):  # 각 행마다 반복
            for c, btn in enumerate(row):  # 각 버튼마다 반복
                # 버튼 종류에 따라 색상을 정함
                if btn in ["sin", "cos", "tan", "log", "ln", "√", "x!", "%", "x^y", "EXP", "Ans"]:
                    bg_color = colors['function']
                elif btn in ["+", "-", "×", "÷"]:
                    bg_color = colors['operator']
                elif btn in ["AC", "="]:
                    bg_color = colors['special']
                else:
                    bg_color = colors['number']

                # 버튼 생성 및 배치
                tk.Button(self.root, text=btn, width=5, height=2, font=('Arial', 12),
                          bg=bg_color, activebackground='#d3d3d3',  # 클릭 시 색상 변경
                          command=lambda b=btn: self.on_click(b)).grid(row=r+1, column=c, padx=3, pady=3)

    def update_entry(self, result):  # 결과를 입력칸에 표시하는 함수
        self.entry.delete(0, tk.END)  # 기존 입력 삭제
        self.entry.insert(tk.END, str(result))  # 결과 입력

    def handle_math_function(self, func, deg=False):  # 수학 함수 처리 (sin, cos 등)
        try:
            value = float(self.entry.get())  # 입력된 값을 숫자로 변환
            if deg:
                value = math.radians(value)  # 각도(degree)를 라디안으로 변환
            result = func(value)  # 함수 적용
            self.update_entry(result)  # 결과 표시
        except Exception as e:
            self.update_entry("Error")  # 에러 발생 시 "Error" 표시
            print(f"Error: {e}")  # 콘솔에 에러 출력

    def handle_factorial(self):  # 팩토리얼 처리 함수
        try:
            value = int(float(self.entry.get()))  # 입력값을 정수로 변환
            result = math.factorial(value)  # 팩토리얼 계산
            self.update_entry(result)
        except Exception as e:
            self.update_entry("Error")
            print(f"Error: {e}")

    def handle_basic_operation(self, operator):  # 단순 입력 추가 함수
        self.entry.insert(tk.END, operator)  # 입력칸 맨 끝에 글자 추가

    def on_click(self, btn):  # 버튼 클릭 시 실행되는 함수
        current = self.entry.get()  # 현재 입력된 값 가져오기

        try:
            if btn == "AC":  # AC 버튼 -> 전체 지우기
                self.entry.delete(0, tk.END)
            elif btn == "=":  # = 버튼 -> 계산 실행
                expression = current.replace("×", "*").replace("÷", "/")  # 기호 치환
                result = eval(expression)  # 문자열을 실제 계산식 처럼 계산
                self.ans = result  # 결과 저장
                self.update_entry(result)
            elif btn in ["sin", "cos", "tan"]:  # 삼각함수 처리
                self.handle_math_function(getattr(math, btn), deg=True)
            elif btn == "log":  # log(10) 계산
                self.handle_math_function(math.log10)
            elif btn == "ln":  # 자연로그 계산
                self.handle_math_function(math.log)
            elif btn == "√":  # 제곱근 계산
                self.handle_math_function(math.sqrt)
            elif btn == "x!":  # 팩토리얼 계산
                self.handle_factorial()
            elif btn == "x^y":  # 거듭제곱 연산자 입력
                self.handle_basic_operation("**")
            elif btn == "EXP":  # e 추가
                self.handle_basic_operation("e")
            elif btn == "Ans":  # 마지막 결과 불러오기
                if self.ans is not None:
                    self.handle_basic_operation(str(self.ans))
            else:  # 나머지 숫자/기호 입력
                self.handle_basic_operation(btn)

        except Exception as e:
            self.update_entry("Error")  # 에러 발생 시 "Error" 표시
            print(f"Error: {e}")

# 프로그램 실행 (Tk 창 띄우기)
if __name__ == '__main__':
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()