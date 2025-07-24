#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!------------------------------------------------------------------------------
#!                         函数基础定义和调用
#!------------------------------------------------------------------------------
def greet(name):  # 定义一个简单的问候函数
    return f"Hello, {name}!"

def add_numbers(a, b):  # 定义加法函数
    return a + b

result1 = greet("Python")  # 调用函数
result2 = add_numbers(5, 3)  # 调用加法函数

print(f"问候结果: {result1}")
print(f"加法结果: {result2}")

#!------------------------------------------------------------------------------
#!                         练习1: 创建个人函数
#!------------------------------------------------------------------------------
def introduce_myself(name, age, city):  # 创建自我介绍函数
    return f"我是{name}，今年{age}岁，来自{city}"

def calculate_bmi(weight, height):  # 计算BMI指数
    bmi = weight / (height ** 2)
    return round(bmi, 2)

my_intro = introduce_myself("小明", 25, "北京")  # 调用介绍函数
my_bmi = calculate_bmi(70, 1.75)  # 计算BMI

print(f"自我介绍: {my_intro}")
print(f"BMI指数: {my_bmi}")

#!------------------------------------------------------------------------------
#!                         练习2: 参数类型详解
#!------------------------------------------------------------------------------
def order_coffee(size, coffee_type="拿铁", sugar=True):  # 默认参数函数
    order = f"一杯{size}杯{coffee_type}"
    if sugar:
        order += "，加糖"
    else:
        order += "，不加糖" 
    return order

def calculate_total(*prices):  # 可变位置参数
    return sum(prices)

def create_profile(**info):  # 可变关键字参数
    profile = "用户档案:\n"
    for key, value in info.items():
        profile += f"  {key}: {value}\n"
    return profile

coffee1 = order_coffee("大")  # 使用默认参数
coffee2 = order_coffee("中", "美式", False)  # 指定所有参数
total = calculate_total(12.5, 15.0, 8.5, 20.0)  # 可变参数
profile = create_profile(name="Alice", age=28, city="上海", job="工程师")  # 可变关键字参数

print(f"咖啡1: {coffee1}")
print(f"咖啡2: {coffee2}")
print(f"总价: ¥{total}")
print(profile)

#!------------------------------------------------------------------------------
#!                         练习3: 函数返回多个值
#!------------------------------------------------------------------------------
def analyze_scores(scores):  # 分析成绩，返回多个值
    avg = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    return avg, max_score, min_score

def divide_with_remainder(a, b):  # 计算商和余数
    quotient = a // b
    remainder = a % b
    return quotient, remainder

test_scores = [85, 92, 78, 96, 88]
avg, max_val, min_val = analyze_scores(test_scores)  # 解包多个返回值
q, r = divide_with_remainder(17, 5)

print(f"成绩分析: 平均{avg:.1f}, 最高{max_val}, 最低{min_val}")
print(f"17÷5 = {q}余{r}")

#!------------------------------------------------------------------------------
#!                         练习4: 作用域和全局变量
#!------------------------------------------------------------------------------
global_counter = 0  # 全局变量

def increment_counter():  # 修改全局变量
    global global_counter
    global_counter += 1
    return global_counter

def local_scope_demo(x):  # 局部作用域演示
    local_var = x * 2  # 局部变量
    print(f"局部变量: {local_var}")
    return local_var

count1 = increment_counter()  # 第一次调用
count2 = increment_counter()  # 第二次调用
local_result = local_scope_demo(10)

print(f"全局计数器: {count1}, {count2}")
print(f"局部作用域结果: {local_result}")

#!------------------------------------------------------------------------------
#!                         练习5: Lambda表达式
#!------------------------------------------------------------------------------
square = lambda x: x ** 2  # 平方函数
add = lambda a, b: a + b  # 加法函数
is_even = lambda n: n % 2 == 0  # 判断偶数

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(square, numbers))  # 使用map和lambda
even_nums = list(filter(is_even, numbers))  # 使用filter和lambda

print(f"原数字: {numbers}")
print(f"平方: {squares}")
print(f"偶数: {even_nums}")

#!------------------------------------------------------------------------------
#!                         练习6: 高阶函数应用
#!------------------------------------------------------------------------------
def apply_operation(numbers, operation):  # 高阶函数：接受函数作为参数
    return [operation(x) for x in numbers]

def create_multiplier(factor):  # 高阶函数：返回函数
    return lambda x: x * factor

def retry_function(func, max_attempts=3):  # 重试装饰器函数
    def wrapper(*args, **kwargs):
        for attempt in range(max_attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == max_attempts - 1:
                    raise e
                print(f"尝试 {attempt + 1} 失败，重试中...")
    return wrapper

double = create_multiplier(2)  # 创建乘2函数
triple = create_multiplier(3)  # 创建乘3函数

test_nums = [1, 2, 3, 4, 5]
doubled = apply_operation(test_nums, double)
tripled = apply_operation(test_nums, triple)

print(f"原数字: {test_nums}")
print(f"乘以2: {doubled}")
print(f"乘以3: {tripled}")

#!------------------------------------------------------------------------------
#!                         练习7: 递归函数
#!------------------------------------------------------------------------------
def factorial(n):  # 计算阶乘的递归函数
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):  # 斐波那契数列递归
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def count_down(n):  # 倒计时递归
    if n <= 0:
        print("发射!")
        return
    print(f"倒计时: {n}")
    count_down(n - 1)

fact_5 = factorial(5)  # 5的阶乘
fib_8 = fibonacci(8)  # 第8个斐波那契数

print(f"5的阶乘: {fact_5}")
print(f"第8个斐波那契数: {fib_8}")
print("火箭发射倒计时:")
count_down(3)

#!------------------------------------------------------------------------------
#!                         练习8: 内置函数综合应用
#!------------------------------------------------------------------------------
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["alice", "bob", "charlie", "diana"]
scores = [85, 92, 78, 96, 88]

total = sum(data)  # 求和
length = len(data)  # 长度
maximum = max(scores)  # 最大值
minimum = min(scores)  # 最小值
sorted_names = sorted(names)  # 排序
capitalized = list(map(str.capitalize, names))  # 首字母大写
high_scores = list(filter(lambda x: x >= 90, scores))  # 筛选高分

print(f"数据总和: {total}")
print(f"数据长度: {length}")
print(f"最高分: {maximum}, 最低分: {minimum}")
print(f"原姓名: {names}")
print(f"排序后: {sorted_names}")
print(f"首字母大写: {capitalized}")
print(f"高分(>=90): {high_scores}")

#!------------------------------------------------------------------------------
#!                         练习9: 错误处理和异常
#!------------------------------------------------------------------------------
def safe_divide(a, b):  # 安全除法函数
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "错误: 不能除以零"
    except TypeError:
        return "错误: 参数类型不正确"

def validate_age(age):  # 年龄验证函数
    if not isinstance(age, int):
        raise TypeError("年龄必须是整数")
    if age < 0:
        raise ValueError("年龄不能为负数")
    if age > 150:
        raise ValueError("年龄不能超过150")
    return f"有效年龄: {age}"

result1 = safe_divide(10, 2)  # 正常除法
result2 = safe_divide(10, 0)  # 除零错误
result3 = safe_divide("10", 2)  # 类型错误

try:
    age_check = validate_age(25)  # 有效年龄
    print(age_check)
except (TypeError, ValueError) as e:
    print(f"年龄验证错误: {e}")

print(f"除法结果: {result1}")
print(f"除零结果: {result2}")
print(f"类型错误结果: {result3}")

#!------------------------------------------------------------------------------
#!                         练习10: 文件操作函数
#!------------------------------------------------------------------------------
def write_to_file(filename, content):  # 写入文件
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"成功写入文件: {filename}"
    except Exception as e:
        return f"写入失败: {e}"

def read_from_file(filename):  # 读取文件
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"文件不存在: {filename}"
    except Exception as e:
        return f"读取失败: {e}"

def count_words_in_text(text):  # 统计单词数量
    words = text.split()
    return len(words)

sample_text = "Python是一门优秀的编程语言，适合初学者学习。"
write_result = write_to_file("sample.txt", sample_text)  # 写入文件
read_result = read_from_file("sample.txt")  # 读取文件
word_count = count_words_in_text(sample_text)

print(write_result)
print(f"文件内容: {read_result}")
print(f"单词数量: {word_count}")

#!------------------------------------------------------------------------------
#!                         练习11: 装饰器入门
#!------------------------------------------------------------------------------
def timer_decorator(func):  # 计时装饰器
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 执行时间: {end_time - start_time:.4f}秒")
        return result
    return wrapper

def log_decorator(func):  # 日志装饰器
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"函数执行完成: {func.__name__}")
        return result
    return wrapper

@timer_decorator  # 使用装饰器
def slow_function():
    import time
    time.sleep(0.1)  # 模拟耗时操作
    return "任务完成"

@log_decorator  # 使用装饰器
def calculate_sum(n):
    return sum(range(1, n + 1))

slow_result = slow_function()
sum_result = calculate_sum(100)

print(f"慢函数结果: {slow_result}")
print(f"求和结果: {sum_result}")

#!------------------------------------------------------------------------------
#!                         练习12: 闭包应用
#!------------------------------------------------------------------------------
def create_counter(initial=0):  # 创建计数器闭包
    count = initial
    def increment(step=1):
        nonlocal count
        count += step
        return count
    return increment

def create_calculator():  # 创建计算器闭包
    history = []
    def calculate(operation, a, b):
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            result = a / b if b != 0 else "除数不能为零"
        else:
            result = "未知操作"
        
        history.append(f"{operation}({a}, {b}) = {result}")
        return result
    
    def get_history():
        return history.copy()
    
    return calculate, get_history

counter1 = create_counter(10)  # 创建计数器1
counter2 = create_counter()  # 创建计数器2

calc, get_hist = create_calculator()  # 创建计算器

print(f"计数器1: {counter1()}, {counter1(5)}, {counter1()}")
print(f"计数器2: {counter2()}, {counter2(3)}")

print(f"计算: {calc('add', 10, 5)}")
print(f"计算: {calc('multiply', 3, 4)}")
print(f"历史记录: {get_hist()}")

#!------------------------------------------------------------------------------
#!                         练习13: 生成器函数
#!------------------------------------------------------------------------------
def number_generator(start, end):  # 数字生成器
    current = start
    while current <= end:
        yield current
        current += 1

def fibonacci_generator():  # 斐波那契生成器
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def even_squares_generator(limit):  # 偶数平方生成器
    n = 0
    while n * n <= limit:
        if n % 2 == 0:
            yield n * n
        n += 1

numbers = list(number_generator(1, 10))  # 生成1到10
fib_gen = fibonacci_generator()
fib_list = [next(fib_gen) for _ in range(10)]  # 前10个斐波那契数
even_squares = list(even_squares_generator(50))

print(f"数字生成器: {numbers}")
print(f"斐波那契前10个: {fib_list}")
print(f"小于50的偶数平方: {even_squares}")

#!------------------------------------------------------------------------------
#!                         练习14: 函数式编程工具
#!------------------------------------------------------------------------------
from functools import reduce
import operator

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["python", "java", "javascript", "go", "rust"]

# 使用map、filter、reduce
squares = list(map(lambda x: x ** 2, numbers))  # 映射
evens = list(filter(lambda x: x % 2 == 0, numbers))  # 过滤
product = reduce(operator.mul, numbers[:5])  # 累积（前5个数的乘积）

# 字符串操作
lengths = list(map(len, words))  # 字符串长度
long_words = list(filter(lambda w: len(w) > 4, words))  # 长单词
combined = reduce(lambda a, b: a + " " + b, words)  # 连接字符串

print(f"平方: {squares}")
print(f"偶数: {evens}")
print(f"前5个数乘积: {product}")
print(f"单词长度: {lengths}")
print(f"长单词: {long_words}")
print(f"连接结果: {combined}")

#!------------------------------------------------------------------------------
#!                         练习15: 模块和导入基础
#!------------------------------------------------------------------------------
import math
import random
import datetime
from collections import Counter

# 数学模块应用
angle = 45
radians = math.radians(angle)  # 角度转弧度
sin_value = math.sin(radians)  # 正弦值
sqrt_value = math.sqrt(16)  # 平方根
pi_value = math.pi  # 圆周率

# 随机模块应用
random_int = random.randint(1, 100)  # 随机整数
random_choice = random.choice(["苹果", "香蕉", "橘子"])  # 随机选择
random_sample = random.sample(numbers, 3)  # 随机抽样

# 日期时间模块
now = datetime.datetime.now()  # 当前时间
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")  # 格式化时间

# 计数器应用
text = "hello world hello python"
word_count = Counter(text.split())  # 单词计数

print(f"数学计算: sin({angle}°) = {sin_value:.3f}")
print(f"平方根16 = {sqrt_value}, π = {pi_value:.3f}")
print(f"随机数: {random_int}")
print(f"随机选择: {random_choice}")
print(f"随机抽样: {random_sample}")
print(f"当前时间: {formatted_time}")
print(f"单词计数: {dict(word_count)}")

#!------------------------------------------------------------------------------
#!                         练习16: 面向对象函数设计
#!------------------------------------------------------------------------------
class MathUtils:  # 数学工具类
    @staticmethod
    def is_prime(n):  # 静态方法：判断质数
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    @classmethod
    def gcd(cls, a, b):  # 类方法：最大公约数
        while b:
            a, b = b, a % b
        return a
    
    def lcm(self, a, b):  # 实例方法：最小公倍数
        return abs(a * b) // self.gcd(a, b)

class StringProcessor:  # 字符串处理器
    def __init__(self):
        self.processed_count = 0
    
    def reverse_words(self, text):  # 反转单词
        self.processed_count += 1
        words = text.split()
        return " ".join(word[::-1] for word in words)
    
    def count_vowels(self, text):  # 统计元音
        self.processed_count += 1
        vowels = "aeiouAEIOU"
        return sum(1 for char in text if char in vowels)

math_util = MathUtils()
str_proc = StringProcessor()

prime_check = MathUtils.is_prime(17)  # 静态方法调用
gcd_result = MathUtils.gcd(48, 18)  # 类方法调用
lcm_result = math_util.lcm(12, 8)  # 实例方法调用

text_sample = "Hello Python World"
reversed_text = str_proc.reverse_words(text_sample)
vowel_count = str_proc.count_vowels(text_sample)

print(f"17是质数: {prime_check}")
print(f"48和18的最大公约数: {gcd_result}")
print(f"12和8的最小公倍数: {lcm_result}")
print(f"原文: {text_sample}")
print(f"反转单词: {reversed_text}")
print(f"元音数量: {vowel_count}")
print(f"处理次数: {str_proc.processed_count}")

#!------------------------------------------------------------------------------
#!                         练习17: 算法函数实现
#!------------------------------------------------------------------------------
def bubble_sort(arr):  # 冒泡排序
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, target):  # 二分搜索
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def quick_sort(arr):  # 快速排序
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

unsorted_data = [64, 34, 25, 12, 22, 11, 90]
sorted_data = [11, 12, 22, 25, 34, 64, 90]

bubble_result = bubble_sort(unsorted_data.copy())  # 冒泡排序
search_result = binary_search(sorted_data, 25)  # 二分搜索
quick_result = quick_sort([3, 1, 4, 1, 5, 9, 2, 6])  # 快速排序

print(f"原数据: {unsorted_data}")
print(f"冒泡排序: {bubble_result}")
print(f"搜索25的位置: {search_result}")
print(f"快速排序: {quick_result}")

#!------------------------------------------------------------------------------
#!                         练习18: 数据处理函数
#!------------------------------------------------------------------------------
def analyze_sales_data(sales):  # 销售数据分析
    total_sales = sum(sales)
    avg_sales = total_sales / len(sales)
    max_sales = max(sales)
    min_sales = min(sales)
    
    growth_rate = []
    for i in range(1, len(sales)):
        rate = ((sales[i] - sales[i-1]) / sales[i-1]) * 100
        growth_rate.append(rate)
    
    return {
        "total": total_sales,
        "average": avg_sales,
        "max": max_sales,
        "min": min_sales,
        "growth_rates": growth_rate
    }

def process_student_grades(students_data):  # 学生成绩处理
    processed = {}
    for name, grades in students_data.items():
        avg_grade = sum(grades) / len(grades)
        status = "优秀" if avg_grade >= 90 else "良好" if avg_grade >= 80 else "及格" if avg_grade >= 60 else "不及格"
        processed[name] = {
            "grades": grades,
            "average": avg_grade,
            "status": status
        }
    return processed

def find_patterns_in_numbers(numbers):  # 数字模式查找
    patterns = {}
    patterns["arithmetic"] = all(numbers[i+1] - numbers[i] == numbers[1] - numbers[0] 
                            for i in range(len(numbers)-1))
    patterns["geometric"] = all(numbers[i+1] / numbers[i] == numbers[1] / numbers[0] 
                            for i in range(len(numbers)-1) if numbers[i] != 0)
    patterns["fibonacci"] = all(numbers[i] == numbers[i-1] + numbers[i-2] 
                            for i in range(2, len(numbers))) if len(numbers) >= 3 else False
    return patterns

monthly_sales = [10000, 12000, 15000, 18000, 16000, 20000]
student_data = {
    "张三": [85, 92, 78, 88],
    "李四": [90, 95, 87, 93],
    "王五": [70, 75, 68, 72]
}
test_sequence = [2, 4, 6, 8, 10]

sales_analysis = analyze_sales_data(monthly_sales)
grade_analysis = process_student_grades(student_data)
pattern_analysis = find_patterns_in_numbers(test_sequence)

print(f"销售分析: {sales_analysis}")
print(f"成绩分析: {grade_analysis}")
print(f"数列模式: {pattern_analysis}")

#!------------------------------------------------------------------------------
#!                         练习19: 游戏逻辑函数
#!------------------------------------------------------------------------------
def create_game_character(name, char_class="战士"):  # 创建游戏角色
    stats = {
        "战士": {"hp": 100, "attack": 15, "defense": 10},
        "法师": {"hp": 70, "attack": 20, "defense": 5},
        "射手": {"hp": 80, "attack": 18, "defense": 7}
    }
    
    character = {
        "name": name,
        "class": char_class,
        "level": 1,
        "experience": 0,
        **stats.get(char_class, stats["战士"])
    }
    return character

def battle_simulation(char1, char2):  # 战斗模拟
    print(f"战斗开始: {char1['name']} VS {char2['name']}")
    
    while char1["hp"] > 0 and char2["hp"] > 0:
        # char1攻击char2
        damage = max(1, char1["attack"] - char2["defense"])
        char2["hp"] -= damage
        print(f"{char1['name']} 对 {char2['name']} 造成 {damage} 点伤害")
        
        if char2["hp"] <= 0:
            print(f"{char2['name']} 被击败了!")
            return char1["name"]
        
        # char2攻击char1
        damage = max(1, char2["attack"] - char1["defense"])
        char1["hp"] -= damage
        print(f"{char2['name']} 对 {char1['name']} 造成 {damage} 点伤害")
        
        if char1["hp"] <= 0:
            print(f"{char1['name']} 被击败了!")
            return char2["name"]
    
    return "平局"

def level_up_character(character, exp_gained):  # 角色升级
    character["experience"] += exp_gained
    while character["experience"] >= character["level"] * 100:
        character["experience"] -= character["level"] * 100
        character["level"] += 1
        character["hp"] += 10
        character["attack"] += 2
        character["defense"] += 1
        print(f"{character['name']} 升级了! 等级: {character['level']}")
    
    return character

hero = create_game_character("勇者小明", "战士")  # 创建英雄
villain = create_game_character("邪恶法师", "法师")  # 创建反派

print(f"英雄: {hero}")
print(f"反派: {villain}")

# 战斗前备份血量
hero_backup = hero.copy()
villain_backup = villain.copy()

winner = battle_simulation(hero_backup, villain_backup)
print(f"获胜者: {winner}")

# 角色升级
hero_upgraded = level_up_character(hero, 250)
print(f"升级后的英雄: {hero_upgraded}")

#!------------------------------------------------------------------------------
#!                         练习20: 综合项目 - 个人理财管理器
#!------------------------------------------------------------------------------
class FinanceManager:  # 理财管理器类
    def __init__(self):
        self.transactions = []  # 交易记录
        self.categories = {
            "收入": ["工资", "奖金", "投资收益", "其他收入"],
            "支出": ["餐饮", "交通", "购物", "娱乐", "房租", "其他支出"]
        }
    
    def add_transaction(self, amount, category, description="", trans_type="支出"):  # 添加交易
        transaction = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "amount": amount,
            "type": trans_type,
            "category": category,
            "description": description
        }
        self.transactions.append(transaction)
        print(f"记录{trans_type}: ¥{amount} ({category})")
        return transaction
    
    def get_balance(self):  # 计算余额
        income = sum(t["amount"] for t in self.transactions if t["type"] == "收入")
        expense = sum(t["amount"] for t in self.transactions if t["type"] == "支出")
        return income - expense
    
    def get_monthly_summary(self, year, month):  # 月度总结
        monthly_trans = [t for t in self.transactions 
                        if t["date"].startswith(f"{year}-{month:02d}")]
        
        income = sum(t["amount"] for t in monthly_trans if t["type"] == "收入")
        expense = sum(t["amount"] for t in monthly_trans if t["type"] == "支出")
        
        category_summary = {}
        for trans in monthly_trans:
            cat = trans["category"]
            category_summary[cat] = category_summary.get(cat, 0) + trans["amount"]
        
        return {
            "income": income,
            "expense": expense,
            "balance": income - expense,
            "categories": category_summary
        }
    
    def budget_analysis(self, budget_limits):  # 预算分析
        current_month = datetime.datetime.now().month
        current_year = datetime.datetime.now().year
        monthly_data = self.get_monthly_summary(current_year, current_month)
        
        analysis = {}
        for category, limit in budget_limits.items():
            spent = monthly_data["categories"].get(category, 0)
            remaining = limit - spent
            percentage = (spent / limit * 100) if limit > 0 else 0
            
            analysis[category] = {
                "budget": limit,
                "spent": spent,
                "remaining": remaining,
                "percentage": percentage,
                "status": "超支" if spent > limit else "正常"
            }
        
        return analysis

fm = FinanceManager()  # 创建理财管理器并测试

# 添加一些交易记录
fm.add_transaction(5000, "工资", "月薪", "收入")
fm.add_transaction(1200, "房租", "月租金")
fm.add_transaction(300, "餐饮", "日常用餐")
fm.add_transaction(200, "交通", "地铁公交费")
fm.add_transaction(500, "购物", "买衣服")
fm.add_transaction(100, "娱乐", "看电影")

# 获取当前余额
current_balance = fm.get_balance()
print(f"\n当前余额: ¥{current_balance}")

# 获取本月总结
current_date = datetime.datetime.now()
monthly_summary = fm.get_monthly_summary(current_date.year, current_date.month)
print(f"本月总结: {monthly_summary}")

# 预算分析
budget_limits = {"餐饮": 400, "交通": 250, "购物": 800, "娱乐": 200}
budget_report = fm.budget_analysis(budget_limits)
print(f"预算分析: {budget_report}")

#!------------------------------------------------------------------------------
#!                         学习完成总结
#!------------------------------------------------------------------------------
print("done!")