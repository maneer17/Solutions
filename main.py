while True:
    import requests
    from datetime import *
    now=datetime.now()
    import smtplib
    def send(message):
        my_email="moonsunu746@gmail.com"
        password="oevyernihxjjaeeg"
        with smtplib.SMTP("smtp.gmail.com",timeout=240,port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,to_addrs="maneeer2006@gmail.com",msg=f"Subject:Hello\n\n{message}")
    def send_an_alert():
        alert_message="bring your umbrella it's going to rain ☂️"
        now=datetime.now()
        if now.hour==9 and now.minute>=55<=59:
            send(alert_message)



    api_key = "a261566ea4de5e54782cdc6dbdf44db1"
    params = {
        "lat": 31.354675,
        "lon": 34.308826,
        "appid": api_key,
        "exclude": "current,minutely,daily"

    }
    response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=params)
    print(response.status_code)
    response.raise_for_status()
    weather_data = response.json()
    weather12_data = weather_data["hourly"][:12]
    for hour in weather12_data:
        id = hour["weather"][0]['id']
        if id > 700:
            send_an_alert()
            break
