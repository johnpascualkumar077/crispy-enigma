# 簡単な計算機プログラム

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "エラー: 0で割ることはできません"

# メイン処理
print("簡単な計算機")
num1 = float(input("1つ目の数字を入力してください: "))
num2 = float(input("2つ目の数字を入力してください: "))
operation = input("演算子を入力してください (+, -, *, /): ")

if operation == '+':
    print(f"結果: {add(num1, num2)}")
elif operation == '-':
    print(f"結果: {subtract(num1, num2)}")
elif operation == '*':
    print(f"結果: {multiply(num1, num2)}")
elif operation == '/':
    print(f"結果: {divide(num1, num2)}")
else:
    print("無効な演算子です")
S