

def laundry_exponent(temp:str, humidity:str):
    calc = round((0.81 * float(temp) + 0.01 * float(humidity) * (0.99 * float(temp) - 14.3) + 46.3), 3)
    return calc

def wind_condition(wind: str):
    convert_wind = float(wind)
    condition_text = ""
    if convert_wind >= 7.0:
        condition_text = "風が強いです。室内干しを検討しましょう。"
    elif convert_wind >= 4.0:
        condition_text = "少し風が強いです。洗濯物が飛ばないように気を付けましょう。"
    elif convert_wind >= 1.6:
        condition_text = "心地いい風です。"
    elif convert_wind < 1.6:
        condition_text = "風は殆どありません。"

    return condition_text

def weather_condition(weather: str):
    condition_text = ""
    if weather == "Clear":
        condition_text = "洗濯日和です。"
    elif weather == "Clouds":
        condition_text = "洗濯物が乾くのに少し時間がかかるかも知れません。"
    elif weather == "Snow":
        condition_text = "室内干しを検討しましょう。"
    elif weather == "Rain":
        condition_text = "室内干しにしましょう。"
    elif weather == "Drizzle":
        condition_text = "室内干しにしましょう。"
    elif weather == "Thunderstorm":
        condition_text = "室内干しにしましょう。"
    else:
        condition_text = "室内干しを検討しましょう。"

    return condition_text

def laundry_recommendation(weather: str,exponent: float):
    num = int(exponent)
    recommendation_text = ""
    recommendation_value = ""
    if num >= 70:
        if weather == "Clear":
            recommendation_text = "最高の洗濯日和です!!!"
            recommendation_value = "5"
        elif weather == "Cloud":
            recommendation_text = "天気の割に、洗濯物は乾きやすいです"
            recommendation_value = "4"
        else: 
            recommendation_text = "室内干しをするなら..."
            recommendation_value = "2"
    elif num >= 50:
        if weather == "Clear":
            recommendation_text = "洗濯日和です!!!"
            recommendation_value = "4"
        elif weather == "Cloud":
            recommendation_text = "天気の割に、洗濯物は乾きやすいです"
            recommendation_value = "3"
        else: 
            recommendation_text = "室内干しをするなら..."
            recommendation_value = "2"
    elif num < 50:
        if weather == "Clear":
            recommendation_text = "洗濯日和です"
            recommendation_value = "4"
        elif weather == "Cloud":
            recommendation_text = "洗濯物は乾きにくいです。室内干しの検討も..."
            recommendation_value = "2"
        else: 
            recommendation_text = "今日は休みましょう"
            recommendation_value = "1"
    
    return {"おすすめ度": recommendation_value, "コメント": recommendation_text}
