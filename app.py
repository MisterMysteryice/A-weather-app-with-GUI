import requests
import tkinter

window = tkinter.Tk()
window.title("Weather App")
window.geometry("400x200")
window.configure(bg="#0276AB")

frame = tkinter.Frame(bg="#0276AB")

def weather():
    city_name = website_entry.get()
    API_KEY = "dccf47c42397245dae4c99e1ba8be90e"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    request_url = f"{BASE_URL}?appid={API_KEY}&q={city_name}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]["description"]
        temperature = round(data["main"]["temp"] - 273, 2)

        sky_condition_label = tkinter.Label(frame, text=weather, bg="#0276AB")
        sky_condition_label.grid(row=8, column=1)

        weather_label = tkinter.Label(frame, text=str(temperature) + str(" Degrees Celsius"), bg="#0276AB")
        weather_label.grid(row=9, column=1)

    elif city_name == "":
        print("You haven't typed anything - type a city name")

    else:
        print("That's either not a city or a city I have information on at this moment. Try a different city")


app_title = tkinter.Label(frame, text="Yussuf's secure password storage tool", bg="#0276AB", font=("Calibri", 10))
website_label = tkinter.Label(frame, text="Weather city request? ", bg="#0276AB")
website_entry = tkinter.Entry(frame)
generate_button = tkinter.Button(frame, text="Generate weather forecast", command=weather)

app_title.grid(row=2, column=1, pady=20)
website_entry.grid(row=3, column=1, padx=10, pady=10)
website_label.grid(row=3, column=0)
generate_button.grid(row=7, column=1)

frame.pack()

window.mainloop()
