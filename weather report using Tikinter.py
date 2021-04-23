import tkinter as tk
import requests

Height =700
Width = 800


##def text_function(entry):
##    print('This is the entry:', entry)

root = tk.Tk()                                                          #~~~~ assigning the Tkinter to root
root.title('Getting an weather')

canvas =tk.Canvas(root, height=Height, width=Width)                     #~~~~ Creating an window frame
canvas.pack()                                                           #~~~~ every identifire need to be packed to run the output

frame = tk.Frame(root, bg = '#80c1ff')                                  #~~~~ setting Frame back ground colour by hexadecimal
frame.place(relx=0.1, rely=0.1, relwidth =0.8, relheight=0.8)           #~~~~ declaring the frame size by place keyword

button = tk.Button(root, text ='Test Button', bg = 'Gray', fg ='Red')   #~~~~ creating an button and adding baground by bg and foreground by fg
button.pack()                                                           #~~~~ packing the button

button = tk.Button(frame, text ='Test Button', bg = 'Gray', fg ='Red')  #~~~~ moving the buttom inside the frame
button.pack()

label =tk.Label(frame, text ='This is an label', bg='yellow')           #~~~~ adding an label to the frame 
label.pack()


button = tk.Button(frame, text ='Test Button', bg = 'Gray', fg ='Red')  
button.pack(side = 'left')                                              #~~~~ re-arranging the button position
##
label =tk.Label(frame, text ='This is an label', bg='yellow')           
label.pack(side='right')                                                #~~~~ re-arranging the button position

##entery = tk.Entry(frame, bg='green').pack(side='left')                  #~~~~ adding an empty text boxk to enter


##button = tk.Button(frame, text ='Test Button', bg = 'Gray', fg ='Red')  
##button.pack(side = 'left', fill='x', expand =True)                      #~~~~ here we fill/extend the left out portion of the button through out the frame
                                                                          #~~~~ if we give expand keyword as true it will take 50% of the frame and we can fill the button in x and y direction

##label =tk.Label(frame, text ='This is an label', bg='yellow')           
##label.pack(side='left', fill='both')                                    #~~~~ here we fill/extend the left out portion of the label through out the fram


##entery = tk.Entry(frame, bg='green').pack(side='left', fill ='both')    #~~~~ here we fill/extend the left out portion of the entery key through out the fram

## Note
    # we can set same side for all the button and label and enter key it will
    # but it will not ovelap it will give output next to one by one

##button = tk.Button(frame, text ='Test Button', bg = 'Gray', fg ='Red')  
##button.grid(row=0,column=0)                                             #~~~~ can advise the button position by rows and column by passing Grid function

##label =tk.Label(frame, text ='This is an label', bg='yellow')           #~~~~ can advise the button position by rows and column by passing Grid function
##label.grid(row=1,column=1)

##entery = tk.Entry(frame, bg='green').grid(row=2,column=2)               #~~~~ #~~~~ can advise the button position by rows and column by passing Grid function


## Note:
    # here if we give the row and column same value for allthe buttons , labels nd entery
    # the output will be overlapped




    ##def test_function(entry):
    ##    print('This is the entry:', entry)

# api.openweathermap.org/data/2.5/forecast/hourly?q={city name},{country code}
# 58b65139d1c4b88257e365818ea76927
# 77411d4442910b840dd2aa90a01df205

    ##def format_response(weather):
    ##    name = weather['name']
    ##    desc = weather['weather'][0]['description']
    ##    temp = weather['main']['temp']
    ##
    ##    return str(name) +'\n '+ str(desc) +'\n '+ str(temp)

    ##def get_weather(city):
    ##    weather_key = '58b65139d1c4b88257e365818ea76927'
    ##    url = 'http://api.openweathermap.org/data/2.5/weather'
    ##    params ={'APPID':weather_key,'q':city,'units':'Imperial'}
    ##    response = requests.get(url, params=params)
    ##    weather = response.json()
    ##    print(response.json())
    ##
    ##    label['text'] = format_response(weather)

##    print(weather['name'])
##    print(weather['weather'][0]['description'])
##    print(weather['main']['temp'])
    

    ##root = tk.Tk()                                                          #~~~~ assigning the Tkinter to root
    ##root.title('Getting an weather')
    ##
    ##canvas =tk.Canvas(root, height=Height, width=Width)                     #~~~~ Creating an window frame
    ##canvas.pack() 
    ##
    ##
    ##background_image = tk.PhotoImage(file=r'C:\Users\DManiX092238\Downloads\pngquant-logo.png')
    ##background_label = tk.Label(root, image=background_image)
    ##background_label.place(relwidth=1, relheight=1)
    ##
    ##
    ##frame = tk.Frame(root, bg = '#80c1ff', bd=5)                                  
    ##frame.place(relx=0.5, rely=0.1, relwidth =0.75, relheight=0.1, anchor ='n')           
    ##
    ##entry = tk.Entry(frame, font=40)
    ##entry.place(relwidth =0.65, relheight=1)
    ##
    ##button = tk.Button(frame, text ='Get Weather', font =40, command = lambda : get_weather(entry.get())) # lambda : get_weather(entry.get())  
    ##button.place(relx=0.7, relheight=1, relwidth =0.3)                                             
    ##
    ##lower_frame = tk.Frame(root, bg = '#80c1ff', bd=10)                                  
    ##lower_frame.place(relx=0.5, rely=0.25, relwidth =0.75, relheight=0.6, anchor ='n')
    ##
    ##label =tk.Label(lower_frame, bg ='white')           
    ##label.place(relwidth=1, relheight=1)

               


root.mainloop()                                                         #~~~~ it will excute the window untill we close it
