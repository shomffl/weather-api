

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

