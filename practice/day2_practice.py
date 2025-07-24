#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!------------------------------------------------------------------------------
#!                            简单的if语句
#!------------------------------------------------------------------------------
temperature = 32  # 当前温度
print(f"当前温度：{temperature}°C") # 根据温度给出建议

if temperature > 30:
    print("The weather is very hot, it is recommended to drink more water")  # 如果温度>30，输出"天气很热，建议多喝水"
elif temperature < 10:
    print("The weather is very cold, please keep warm")  # 如果温度<10，输出"天气很冷，注意保暖"
else:
    print("The weather is good")  # 否则输出"天气还不错"


#!------------------------------------------------------------------------------
#!                           if-elif-else语句
#!------------------------------------------------------------------------------
score = 92  # 分数成绩
print(f"Test_scores:{score}")  # 根据分数确定等级

if score >= 90:
    grade = "A"
    comment = "excellent"  # 90-100: A等级，"优秀"
elif score >= 80:
    grade = "B"
    comment = "good"  # 80-89: B等级，"良好"
elif score >= 70:
    grade = "C"
    comment = "medium"  # 70-79: C等级，"中等"
elif score >= 60:
    grade = "D"
    comment = "Pass"  # 60-69: D等级，"及格"
else:
    grade = "F"
    comment = "Fail"  # 0-59: F等级，"不及格"

print(f"grade:{grade} - {comment}")


#!------------------------------------------------------------------------------
#!                           用户年龄分类
#!------------------------------------------------------------------------------
age = 80  # 请填入一个年龄
print(f"age:{age}")

if age >= 0 and age <= 2:
    category = "baby"  # 0-2岁：婴儿
elif age >= 3 and age <= 12:
    category = "child"  # 3-12岁：儿童
elif age >= 13 and age <= 19:
    category = "teenager"  # 13-19岁：青少年
elif age >= 20 and age <= 59:  
    category = "Adults"  # 20-59岁：成年人
elif age >= 60:
    category = "Elderly"  # 60岁以上：老年人
else:
    category = "Unknown_age"
    
print(f"Age_classification:{category}")  # 输出年龄分类


#!------------------------------------------------------------------------------
#!                          逻辑运算符:驾驶资格判断
#!------------------------------------------------------------------------------
age = 22  # 年龄
has_license = True  # 是否有驾照
has_violations = False  # 是否有违章记录
is_drunk = False  # 是否饮酒

print(f"age:{age}")
print(f"Have a driver's license:{has_license}")
print(f"Have a violation record:{has_violations}")
print(f"Drinking status:{is_drunk}")

can_drive = (age >= 18) and has_license and (not has_violations) and (not is_drunk)  # 使用逻辑运算符完成判断

if can_drive:
    print("Can drive!")  # 如果满足所有条件，输出"可以驾驶"
else:
    print("Not allowed to drive!")  # 否则输出"不允许驾驶"


#!------------------------------------------------------------------------------
#!                          会员等级判定
#!------------------------------------------------------------------------------
total_spent = 5100  # 总消费金额
member_years = 3  # 会员年限

print(f"Total_consumption_amount:¥{total_spent}")
print(f"Membership_Period:{member_years}年")

if total_spent >= 10000 and member_years >= 5:  # 钻石会员：消费>=10000 AND 年限>=5
    member_level = "Diamond Member"
elif total_spent >= 5000 and member_years >= 2:  # 黄金会员：消费>=5000 AND 年限>=2
    member_level = "Gold Member"
elif total_spent >= 2000 or member_years >= 1:  # 银牌会员：消费>=2000 OR 年限>=1
    member_level = "Silver Member"
else:
    member_level = "Ordinary Member"  # 普通会员：其他情况

print(f"Membership Level:{member_level}")


#!------------------------------------------------------------------------------
#!                          嵌套条件:电影票价计算
#!------------------------------------------------------------------------------
age = 20  # 年龄
is_student = True  # 是否学生
is_weekday = True  # 是否工作日
is_morning = False  # 是否上午场

print(f"age：{age}")
print(f"student：{is_student}")
print(f"Working_Day：{is_weekday}")
print(f"Morning_Session：{is_morning}")

base_price = 50  # 基础票价
final_price = base_price  # 初始票价

if age < 18 or age >= 65:
    final_price *= 0.8  # 18岁以下或65岁以上8折
elif is_student:
    final_price *= 0.9  # 学生9折（与年龄折扣不叠加，取最优）
if is_weekday:
    final_price *= 0.9  # 工作日9折
if is_morning:
    final_price *= 0.8  # 上午场8折

print(f"Final_fare：¥{final_price:.2f}")  # 最终票价


#!------------------------------------------------------------------------------
#!                          综合应用:贷款审批系统
#!------------------------------------------------------------------------------
applicant_age = 30  # 申请人年龄
monthly_income = 10000  # 月收入
credit_score = 720  # 信用分
has_job = True  # 是否有工作
existing_loans = 100000  # 现有贷款
loan_amount = 300000  # 申请贷款金额

print(f"Applicant's age：{applicant_age}")
print(f"Monthly income：¥{monthly_income}")
print(f"Trust Points：{credit_score}")
print(f"Have a job：{has_job}")
print(f"Existing loans：¥{existing_loans}")
print(f"Application amount：¥{loan_amount}")

if not (22 <= applicant_age <= 60):
    loan_approved = False
    rejection_reason = "Age requirement not met"  # 年龄不符合要求
else:
    monthly_playment = loan_amount / 120  # 贷款月供（假设分120个月还清）
    if monthly_income < monthly_playment:
        loan_approved = False
        rejection_reason = "Insufficient monthly income"  # 贷款月供大于月收入
    else:
        total_debt = existing_loans + loan_amount
        debt_ratio = total_debt / (monthly_income * 12)  # 负债比例
        if debt_ratio > 0.5:
            loan_approved = False  
            rejection_reason = "Too high debt ratio"  # 负债比例过高
        else:
            if credit_score >= 750:
                approval_ratio = 1.2  # 信用分>=750，额度120%
            elif credit_score >= 700:
                approval_ratio = 1.0  # 信用分700-749，正常额度
            else:
                approval_ratio = 0.8  # 信用分650-699，额度80%
            loan_approved = True
            approval_amount = loan_amount * approval_ratio  # 批准金额

if loan_approved:
    print(f"approve:¥{approval_amount}")
else:
    print(f"reject:{rejection_reason}")

#!------------------------------------------------------------------------------
#!                          音乐智能推荐系统
#!------------------------------------------------------------------------------
# User Information
user_age = 25
mood = "happy"  # Mood: happy, sad, calm, excited, stressed, romantic
time_of_day = "night"  # Time: morning, afternoon, evening, night
is_working = False
likes_classic = True
energy_level = "high"  # Energy: high, medium, low

print(f"User Age: {user_age}")
print(f"Current Mood: {mood}")
print(f"Time of Day: {time_of_day}")
print(f"Working Status: {'Working' if is_working else 'Leisure Time'}")
print(f"Likes Classic: {'Yes' if likes_classic else 'No'}")
print(f"Energy Level: {energy_level}")

# Recommend based on mood categories
if mood == "happy":
    if energy_level == "high":
        if time_of_day == "morning":
            recommended_music = "Upbeat Pop" if not likes_classic else "Classical March"
            reason = "Happy and energetic morning calls for vibrant music to start a wonderful day"
        elif time_of_day == "night" and not is_working:
            recommended_music = "Classic Rock" if likes_classic else "Electronic Dance"
            reason = "Happy relaxing night with high energy suits rhythmic music to release vitality"
        else:
            recommended_music = "Light Jazz" if likes_classic else "Pop Hits"
            reason = "Happy mood with upbeat rhythm keeps the good vibes going"
    elif energy_level == "medium":
        recommended_music = "Easy Folk" if not likes_classic else "Chamber Music"
        reason = "Happy but not overly excited, gentle music maintains pleasant mood"
    else:  # low energy
        recommended_music = "Soft Instrumental" if not likes_classic else "Classical Miniatures"
        reason = "Happy but quiet, soft music keeps good mood without causing fatigue"

elif mood == "sad":
    if energy_level == "high":
        recommended_music = "Motivational Rock" if not likes_classic else "Triumphant Classical"
        reason = "Sad but energetic, need uplifting music to reignite fighting spirit"
    elif energy_level == "medium":
        recommended_music = "Healing Folk" if not likes_classic else "Lyrical Classical"
        reason = "Sadness needs warmth and healing to slowly restore inner peace"
    else:  # low energy
        recommended_music = "Gentle Piano" if not likes_classic else "Nocturnes"
        reason = "When sad and low, gentle music accompanies and slowly soothes the soul"

elif mood == "calm":
    if time_of_day == "morning":
        recommended_music = "Morning Songs" if likes_classic else "Light Instrumental"
        reason = "Peaceful morning, gentle music welcomes a new day"
    elif time_of_day == "night":
        recommended_music = "Nocturnes" if likes_classic else "Ambient Music"
        reason = "Quiet night time needs serene and profound music"
    else:
        recommended_music = "New Age Music" if not likes_classic else "Pastoral Symphony"
        reason = "Calm state suits ethereal music, letting thoughts flow freely"
        
elif mood == "excited":
    if is_working:
        recommended_music = "Light Background Music" if likes_classic else "Rhythmic Instrumentals"
        reason = "Excited while working needs rhythmic but non-distracting music for focus"
    else:
        recommended_music = "Dynamic Rock" if not likes_classic else "Marches"
        reason = "Excited state needs strong beats to match inner passion"

elif mood == "stressed":
    recommended_music = "Relaxation Music" if not likes_classic else "Baroque Music"
    reason = "High stress requires music that can relieve tension and calm the mind"

elif mood == "romantic":
    if time_of_day == "evening" or time_of_day == "night":
        recommended_music = "Romantic Piano" if likes_classic else "Love Duets"
        reason = "Romantic evening time, tender music creates beautiful atmosphere"
    else:
        recommended_music = "Smooth Jazz" if likes_classic else "Sweet Love Songs"
        reason = "Romantic mood needs warm and sweet melodies to express inner feelings"

else:
    # Default recommendation
    if user_age < 25:
        recommended_music = "Pop Music" if not likes_classic else "Modern Classical"
        reason = "Young people suit trendy and contemporary music styles"
    elif user_age >= 30:
        recommended_music = "Classic Oldies" if not likes_classic else "Classical Masterpieces"
        reason = "Mature age suits deep and nostalgic classic music"
    else:
        recommended_music = "Light Music" if not likes_classic else "Chamber Music"
        reason = "Based on your preferences, recommending this gentle and comfortable music type"

# Output recommendation results
print(f"Recommended Music Type: {recommended_music}")
print(f"Recommendation Reason: {reason}")

# Additional suggestions
print("Additional Suggestions:")
if is_working:
    print("For work time, suggest instrumental music to avoid lyrical distraction")
if time_of_day == "night":
    print("For nighttime, suggest moderate volume to avoid disturbing others")
if energy_level == "low":
    print("With low energy, avoid overly intense music to prevent fatigue")

print("Today's recommendation complete! Enjoy your music!")


#!------------------------------------------------------------------------------
#!                          检查
#!------------------------------------------------------------------------------
print("done!")
