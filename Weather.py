# pip install geopy

from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
import pytz


from tkinter import *
from tkinter import ttk
import requests
import datetime





def convert_to_ampm(timestamp):
    # Convert Unix timestamp to datetime object
    time = datetime.datetime.fromtimestamp(timestamp)
    # Convert time to 12-hour format with AM/PM indicator
    return time.strftime("%I:%M %p")




def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=90b8d085446fc3313adfb6eedc8c545f").json()
    ee_label.config(text=data["weather"][0]["main"])
    er_label.config(text=data["weather"][0]["description"])
    gg_label.config(text=str(int(data["main"]["temp"]-273.15)))
    id_label.config(text=str(int(data["main"]["feels_like"]-273.15)))
    Max_label.config(text=data["visibility"])
    min_label.config(text=data["wind"]["speed"])



    dd_label.config(text=data["main"]["pressure"])
    sunrise_time = convert_to_ampm(data["sys"]["sunrise"])
    sunset_time = convert_to_ampm(data["sys"]["sunset"])
    sun_rsee.config(text=sunrise_time)
    sun_setr.config(text=sunset_time)



win = Tk()
win.title("Rain")
win.config(bg="Sky blue")
win.geometry("500x600")




name_label = Label(win, text="      Rain Weather🌦️", font=("Times New Roman", 30, "bold"), bg="teal")
name_label.place(x=97, y=40, width=320)

List_Name = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']




city_name= StringVar()
com = ttk.Combobox(win, text="City_name", values=List_Name, font=("Times New Roman",15, "bold"),textvariable=city_name)
com.place(x=64, y=120,height=30, width=375)






w_label = Label(win, text="Weather Climate", font=("Times New Roman", 13, "bold"), bg="gray")
w_label.place(x=50, y=250,width=200)



wb_label = Label(win, text="Weather Description", font=("Times New Roman", 13, "bold"), bg="gray")
wb_label.place(x=50, y=280,width=200)



wr_label = Label(win, text="Temperature", font=("Times New Roman", 13, "bold"), bg="gray")
wr_label.place(x=50, y=310,width=200)



wr_labelMax = Label(win, text="Visibility", font=("Times New Roman", 13, "bold"), bg="gray")
wr_labelMax.place(x=50, y=340,width=200)



wr_labelMin = Label(win, text="Wind Speed", font=("Times New Roman", 13, "bold"), bg="gray")
wr_labelMin.place(x=50, y=370,width=200)



id_label = Label(win, text="Feels Like", font=("Times New Roman", 13, "bold"), bg="gray")
id_label.place(x=50, y=400,width=200)



wj_label = Label(win, text="Pressure", font=("Times New Roman", 13, "bold"), bg="gray")
wj_label.place(x=50, y=430,width=200)



sun_rise = Label(win, text="Sun Rise", font=("Times New Roman", 13, "bold"), bg="gray")
sun_rise.place(x=50, y=460,width=200)



sun_set = Label(win, text="Sun Set", font=("Times New Roman", 13, "bold"), bg="gray")
sun_set.place(x=50, y=490,width=200)




ee_label = Label(win, text="", font=("Times New Roman", 13, "bold"), bg="gray")
ee_label.place(x=255, y=250,width=200)



er_label = Label(win, text="", font=("Times New Roman", 13, "bold"), bg="gray")
er_label.place(x=255, y=280,width=200)



gg_label = Label(win, text="", font=("Times New Roman", 13, "bold"), bg="gray")
gg_label.place(x=255, y=310,width=200)



Max_label = Label(win, text="", font=("Times New Roman", 13, "bold"), bg="gray")
Max_label.place(x=255, y=340,width=200)



min_label = Label(win, text="", font=("Times New Roman", 13, "bold"), bg="gray")
min_label.place(x=255, y=370,width=200)



id_label = Label(win, text="", font=("Times New Roman", 13, "bold"), bg="gray")
id_label.place(x=255, y=400,width=200)



dd_label = Label(win, text="", font=("Times New Roman", 13, "bold"), bg="gray")
dd_label.place(x=255, y=430,width=200)



sun_rsee = Label(win, text="", font=("Times New Roman", 13, "bold"), bg="gray")
sun_rsee.place(x=255, y=460,width=200)



sun_setr = Label(win, text="", font=("Times New Roman", 13, "bold"), bg="gray")
sun_setr.place(x=255, y=490,width=200)


button = Button(win, text="Done", font=("Times New Roman", 15, "bold"), command=data_get, bg="teal", fg="black")


com.place(x=64, y=120,height=30, width=375)
button.place(x=200, y=165,height=30, width=100)


win.mainloop()






