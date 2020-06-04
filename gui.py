from tkinter import *
from tkinter import messagebox
import re, pymysql,  random
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from sklearn.linear_model import LinearRegression

def SplashScreen(Frame):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    w = 600
    h = 600
    x = (ws/2) - (w/2) 
    y = (hs/2) - (h/2)
    Frame.geometry('%dx%d+%d+%d' % (w, h, x, y))
    Frame.overrideredirect(True)
    Frame.lift()

def adjustWindow(window):
    w=600
    h=600
    ws = screen.winfo_screenwidth()
    hs = screen.winfo_screenheight()
    x = (ws/2)-(w/2)
    y = (hs/2)-(h/2)
    window.geometry('%dx%d+%d+%d'%(w,h,x,y))
    window.resizable(False, False)
  
def one():
    global screen6
    
    screen6 = Toplevel()
    screen6.title("Percentage download in each category on the playstore")
    adjustWindow(screen6)
    screen6.configure(background = 'black')
    screen6.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen6, text="CATEGORY WISE DOWNLOAD", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').pack() 
    
    Label(screen6, text = "", bg = 'black').pack()
    
#ploting
    copy = data.copy()
    category = StringVar()
    
    copy.drop(['App', 'Size', 'Reviews', 'Current Ver', 'Type', 'Price', 'Content Rating', 'Genres', 'Android Ver'], axis = 1, inplace = True)
    
    copy['Installs'] = copy.Installs.str.replace(",","")
    copy['Installs'] = copy.Installs.str.replace("+","")
    copy['Installs'] = copy.Installs.replace("Free", 0) 
    copy['Installs'] = copy['Installs'].astype(float)
    copy['Installs'].dtype
    
    category_list = list(copy['Category'].unique())
    
    category_install = []
    install_count = a = 0
    
    for i in category_list:
        x = copy[copy['Category'] == i]
        
        if(len(x) != 0):
            install = sum(x.Installs)/len(x)
            install_count = install_count + install
            category_install.append(install)
        else:
            install = sum(x.Installs) 
            install_count = install_count + install
            category_install.append(install)
                
    for i in category_install:
        i = float((category_install[a]/install_count)*100)
        category_install[a] = i
        a = a + 1
        
#sorting
    data_category_install = pd.DataFrame({'category': category_list, 'install':category_install})
    new_index = (data_category_install['install'].sort_values(ascending = False)).index.values
    sorted_data = data_category_install.reindex(new_index)

# visualization
    fig = plt.figure()
    sns.barplot(x = sorted_data['category'], y = sorted_data['install'])
    plt.xticks(rotation = 90)
    plt.xlabel("Category")
    plt.ylabel("Installs (in %)")
    plt.title("Category and Install")
    plt.savefig('C:\\Google-play-store-prediction\\images\\a.png', bbox_inches='tight')
    plt.close()
    
    img = PhotoImage(file='C:\\Google-play-store-prediction\\images\\a.png')
    label = Label(screen6, image=img, anchor = 'w')
    label.image = img
    label.pack()
    
    Label(screen6, text='Choose Category:', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 520)    
    
    droplist = OptionMenu(screen6, category, *category_list)
    category.set("Category List")
    droplist.configure(width = 15)
    droplist.place(x = 160, y = 520)
    
    Button(screen6, text='GO', font=('calibri', 12, 'bold'), bg='brown', fg='white', command= lambda: messagebox.showinfo('Percentage', 'The percentage download in ' + category.get() + ' is ' + sorted_data[sorted_data['category'] == category.get()].install.to_string(index = False) + '%', parent = screen6)).place(x = 350, y = 520)
    
    Button(screen6, text = '<<<', bg='brown', fg = 'white', command = screen6.destroy).place(x = 10, y = 560)
    Label(screen6, text = 'Back to Previous Screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)    
    
def two():
    global screen7
    
    screen7 = Toplevel()
    screen7.title("Downloads Range wise")
    adjustWindow(screen7)
    screen7.configure(background = 'black')
    screen7.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen7, text="DOWNLOADS IN RANGE", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').pack() 
    
    Label(screen7, text = "", bg = 'black').pack()
#ploting
    copy = data.copy()
    copy.drop(['App', 'Size', 'Reviews', 'Current Ver', 'Type', 'Price', 'Content Rating', 'Genres', 'Android Ver'], axis = 1, inplace = True)
    
    copy['Installs'] = copy.Installs.str.replace(",","")
    copy['Installs'] = copy.Installs.str.replace("+","")
    copy['Installs'] = copy.Installs.replace("Free", 0) 
    copy['Installs'] = copy['Installs'].astype(float)
    copy['Installs'].dtype
    
    first = second = third = four = five = 0
    percent_list = []
    installs = list(copy['Installs'])
    
    for i in installs:
        
        if (i >= 10000) and (i <= 50000):
            first = first + 1
            
        if (i >= 50000) and (i <= 150000):
            second = second + 1        
        
        if (i >= 150000) and (i <= 500000):
            third = third + 1

        if (i >= 500000) and (i <= 5000000):
            four = four + 1
            
        if (i >= 5000000):
            five = five + 1
    
    counted_data = [first, second, third, four, five]
    total = first + second + third + four + five
    range_data = ['Btwn 10k & 50k', 'Btwn 50k & 150k', 'Btwn 150k & 500k', 'Btwn 500k & 5000k','More than 5000k']
    
    for i in counted_data:
        percent = (i / total)*100
        percent_list.append(percent)
    
    plt.figure(figsize=(5, 3))
    sns.barplot(x = range_data, y = counted_data)
    plt.xticks(rotation = 90)
    plt.xlabel("Range")
    plt.ylabel("Download count")
    plt.title("Range of Downloads")
    plt.savefig('C:\\Google-play-store-prediction\\images\\b.png', bbox_inches='tight')
    plt.close()
# visualization
    img = PhotoImage(file='C:\\Google-play-store-prediction\\images\\b.png')
    im = Image.open('C:\\Google-play-store-prediction\\images\\b.png')
    ph = ImageTk.PhotoImage(im)
    label = Label(screen7, text='', image=img, anchor='w')
    label.image = img
    label.pack()
    
    Label(screen7, text='Download in Range:', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 225, y = 420)
    Label(screen7, text='>>  10k to 50k:  ' + str(round(percent_list[0], 2)) + '%', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 450)
    Label(screen7, text='>>  50k to 150k:  ' + str(round(percent_list[1], 2)) + '%', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 300, y = 450)
    Label(screen7, text='>>  150k to 500k:  ' + str(round(percent_list[2], 2)) + '%', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 480)
    Label(screen7, text='>>  500k to 5000k:  ' + str(round(percent_list[3], 2)) + '%', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 300, y = 480)
    Label(screen7, text='>>  More then 5000k:  ' + str(round(percent_list[4], 2)) + '%', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 510)

    Button(screen7, text = '<<<', bg='brown', fg = 'white', command = screen7.destroy).place(x = 10, y = 560)
    Label(screen7, text = 'Back to Previous Screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
      
def three():
    global screen8
    
    screen8 = Tk()
    screen8.title("Category of apps that have managed to get most, least and average installs")
    adjustWindow(screen8)
    screen8.configure(background = 'black')
    screen8.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen8, text="Most, Least and Average Installs (Category wise)", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').pack() 
    
    Label(screen8, text = "", bg = 'black').pack()
    
    copy = data.copy()
    copy.drop(['App', 'Size', 'Reviews', 'Current Ver', 'Type', 'Price', 'Content Rating', 'Genres', 'Android Ver'], axis = 1, inplace = True)
    
    copy['Installs'] = copy.Installs.str.replace(",","")
    copy['Installs'] = copy.Installs.str.replace("+","")
    copy['Installs'] = copy.Installs.replace("Free", 0) 
    copy['Installs'] = copy['Installs'].astype(float)
    copy['Installs'].dtype
    
    category_list = list(copy['Category'].unique())
    
    category_copy = []
    
    for i in category_list:
        x = copy[copy['Category'] == i]
        
        if(len(x) != 0):
            install = sum(x.Installs)/len(x)
            category_copy.append(install)
        else:
            install = sum(x.Installs) 
            category_copy.append(install)
                
    min = max = category_copy[0]
    avg = []
    
    for i in category_copy:
        if i < min:
            min = i
        if i > max:
            max = i
        if i >= 250000:
            avg.append(i)
            
    Label(screen8, text='>> Category of apps which has received Most Download is:  ' + category_list[category_copy.index(max)], bg='black', fg='white', font=("calibri", 11, 'bold')).pack(anchor = 'w')
    Label(screen8, bg='black').pack()
    Label(screen8, text='>> Category of apps which has received Least Download is:  ' + category_list[category_copy.index(min)], bg='black', fg='white', font=("calibri", 11, 'bold')).pack(anchor = 'w')
    Label(screen8, bg='black').pack()
    Label(screen8, text='>> Category of apps which has received Average Download of 2,50,000 are :  ' , bg='black', fg='white', font=("calibri", 11, 'bold')).pack(anchor = 'w')
    y_lm = 190
    x_lm = 20
    for i in avg:
        if y_lm == 510:
            y_lm = 210
            x_lm = 300
        else:
            y_lm = y_lm + 20
        Label(screen8, text=category_list[avg.index(i)], bg='black', fg='white', font=("calibri", 11, 'bold')).place(x  = x_lm, y = y_lm)
    
    Button(screen8, text = '<<<', bg='brown', fg = 'white', command = screen8.destroy).place(x = 10, y = 560)
    Label(screen8, text = 'Back to Previous Screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
    
def four():
    global screen9
    
    screen9 = Toplevel()
    screen9.title("Category of apps managed to get highest maximum rating")
    adjustWindow(screen9)
    screen9.configure(background = 'black')
    screen9.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen9, text="Category of apps Rating", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').pack() 
    
    Label(screen9, text = "", bg = 'black').pack()
    
#ploting
    copy = data.copy()
    copy.drop(['App', 'Size', 'Reviews', 'Current Ver', 'Type', 'Price', 'Content Rating', 'Genres', 'Android Ver'], axis = 1, inplace = True)
    
    copy['Installs'] = copy.Installs.str.replace(",","")
    copy['Installs'] = copy.Installs.str.replace("+","")
    copy['Installs'] = copy.Installs.replace("Free", 0) 
    copy['Installs'] = copy['Installs'].astype(float)
    copy['Installs'].dtype
    
    category_list = list(copy['Category'].unique())
    
    ratings = []
    
    for i in category_list:
        x = copy[copy['Category'] == i]
        
        if(len(x) != 0):
            rating = sum(x.Rating)/len(x)
            ratings.append(rating)
        else:
            rating = sum(x.Rating) 
            ratings.append(rating)
#sorting
    data_category_ratings = pd.DataFrame({'category': category_list, 'ratings': ratings})
    new_index = (data_category_ratings['ratings'].sort_values(ascending = False)).index.values
    sorted_data = data_category_ratings.reindex(new_index)
    
    max_rat = ratings[0]
    for i in ratings:
        if i > max_rat:
            max_rat = i        
#plotting    
    fig = plt.figure()
    sns.barplot(x = sorted_data['category'], y = sorted_data['ratings'])
    plt.xticks(rotation = 90)
    plt.xlabel("Category")
    plt.ylabel("Ratings")
    plt.title("Category wise Ratings")
    plt.savefig('C:\\Google-play-store-prediction\\images\\d.png', bbox_inches='tight')
    plt.close()
    
    img = PhotoImage(file='C:\\Google-play-store-prediction\\images\\d.png')
    label = Label(screen9, image=img, anchor = 'w')
    label.image=img 
    label.pack()
    
    Label(screen9, text='', bg='black').pack()
    Label(screen9, text='The category of app that has managed to get max rating is '+ category_list[ratings.index(max_rat)] + ' with avg rating of '+ str(round(max_rat, 2)), bg='black', fg='white', font=("calibri", 11, 'bold')).pack()
    
    Button(screen9, text = '<<<', bg='brown', fg = 'white', command = screen9.destroy).place(x = 10, y = 560)
    Label(screen9, text = 'Back to Previous Screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
        
def five():
    global screen10
    
    screen10 = Toplevel()
    screen10.title("Download trend category wise")
    adjustWindow(screen10)
    screen10.configure(background = 'black')
    screen10.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen10, text="Download trend Category wise", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').pack() 
    
    Label(screen10, text = "", bg = 'black').pack()
#Data Wrangling
    copy = data.copy()
    copy.drop(['App', 'Size', 'Reviews', 'Current Ver', 'Type', 'Price', 'Content Rating', 'Genres', 'Android Ver'], axis = 1, inplace = True)
    
    copy['Installs'] = copy.Installs.str.replace(",","")
    copy['Installs'] = copy.Installs.str.replace("+","")
    copy['Installs'] = copy.Installs.replace("Free", 0) 
    copy['Installs'] = copy['Installs'].astype(float)
    copy['Installs'].dtype
        
    copy['Last Updated'] = pd.to_datetime(copy['Last Updated'])
    copy['year'] = copy['Last Updated'].dt.year
    
    copy['Installs']= copy['Installs']/1000000000
# plot data
    fig, ax= plt.subplots(figsize=(10, 11))
# use unstack()
    plt.ylabel("Install(in billions)")
    plt.xlabel('Year')
    copy.groupby(['year','Category']).sum()['Installs'].unstack().plot(ax=ax)
    plt.savefig('C:\\Google-play-store-prediction\\images\\e.png', bbox_inches='tight')
    plt.close()
    
    img = PhotoImage(file='C:\\Google-play-store-prediction\\images\\e_.png')
    label = Label(screen10, image=img, anchor = 'w')
    label.image=img 
    label.pack()
    
    Button(screen10, text = '<<<', bg='brown', fg = 'white', command = screen10.destroy).place(x = 10, y = 560)
    Label(screen10, text = 'Back to Previous Screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
      
def six():
    global screen14
    
    screen14 = Toplevel()
    screen14.title("All apps whose version is not an issue, % increase and decrease in download")
    adjustWindow(screen14)
    screen14.configure(background = 'black')
    screen14.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen14, text="Apps whose version is not an issue, change in download", width='50', height="2", font=("Calibri", 18, 'bold'), fg='white', bg='#00e750').pack() 
    Label(screen14, text = "", bg = 'black').pack()
    
    copy = data.copy()
    
    copy.drop(['App', 'Size', 'Reviews', 'Current Ver', 'Type', 'Price', 'Content Rating', 'Genres'], axis = 1, inplace = True)
        
    copy['Installs'] = copy.Installs.str.replace(",","")
    copy['Installs'] = copy.Installs.str.replace("+","")
    copy['Installs'] = copy.Installs.replace("Free", 0) 
    copy['Installs'] = copy['Installs'].astype(float)
    copy['Installs'].dtype
    
    copy['Last Updated'] = pd.to_datetime(copy['Last Updated'])
    copy['month'] = copy['Last Updated'].dt.month
    copy['year'] = copy['Last Updated'].dt.year
    copy['android'] = copy['Android Ver']
    value=copy.groupby(['android', 'year'], as_index = False)['Installs'].sum()    
    value['Installs'] = value['Installs']/10000000
    
    ver=value[value.android == 'Varies with device'].sort_values(by = 'year', ascending = True)
    
    fig = plt.figure()
    sns.barplot(x = ver['year'], y = ver['Installs'])
    plt.xticks(rotation = 90)
    plt.xlabel("Years")
    plt.ylabel("Downloads(in crore)")
    plt.title("Apps with compatible versions")
    plt.savefig('C:\\Google-play-store-prediction\\images\\g.png', bbox_inches='tight')
    plt.close()
    
    img = PhotoImage(file='C:\\Google-play-store-prediction\\images\\g.png')
    label = Label(screen14, image=img, anchor = 'w')
    label.image=img 
    label.pack()

    Button(screen14, text = '<<<', bg='brown', fg = 'white', command=screen14.destroy).place(x = 10, y = 560)
    Label(screen14, text = 'Back to Previous Screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
        
def seven():
    global screen15
    
    screen15 = Toplevel()
    screen15.title("Apps which have managed rating of 4.1 and above and downloads of 100k+")
    adjustWindow(screen15)
    screen15.configure(background = 'black')
    screen15.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen15, text="Apps with rating 4.1 and above and dwnlds of 1,00,000+", width='50', height="2", font=("Calibri", 18, 'bold'), fg='white', bg='#00e750').pack() 
    Label(screen15, text = "", bg = 'black').pack()
    
    copy = data.copy()
    
    copy.drop(['App', 'Size', 'Reviews', 'Type', 'Price', 'Content Rating', 'Genres', 'Android Ver', 'Current Ver'], axis = 1, inplace = True)
        
    copy['Installs'] = copy.Installs.str.replace(",","")
    copy['Installs'] = copy.Installs.str.replace("+","")
    copy['Installs'] = copy.Installs.replace("Free", 0) 
    copy['Installs'] = copy['Installs'].astype(float)
    copy['Installs'].dtype
    
    installs = copy[copy.Installs >= 100000]
    value=len(installs)
    
    ratings = copy[copy.Rating >= 4.1]
    inst = ratings[copy.Installs >= 100000]
        
    plt.figure(figsize=(2,2))
    size=[len(inst), (value-len(inst))]
    sentiment = ['Yes', 'No']
    plt.pie(size, labels=sentiment, startangle=90, autopct='%.1f%%')
    plt.title('% Apps having rating 4.1+ and 100000+ downloads')
    plt.savefig('C:\\Google-play-store-prediction\\images\\h1.png', bbox_inches='tight')
    plt.close()
    
    plt.figure(figsize=(6,3))
    sns.barplot(y = copy['Installs'], x= copy['Rating'], ci = None)
    plt.ylabel("Install (in millions)")
    plt.xticks(rotation=80)
    plt.title("Apps Installed and ratings ")
    plt.savefig('C:\\Google-play-store-prediction\\images\\h2.png', bbox_inches='tight')
    plt.close()
    
    img = PhotoImage(file='C:\\Google-play-store-prediction\\images\\h1.png')
    label = Label(screen15, image=img, anchor = 'w')
    label.image=img 
    label.pack()
    
    Label(screen15, text='', bg='black').pack()
    
    img1 = PhotoImage(file='C:\\Google-play-store-prediction\\images\\h2.png')
    label = Label(screen15, image=img1, anchor = 'w')
    label.image=img1
    label.pack()
    
    Label(screen15, text = '>>  The apps that have managed to get rating 4.1 and more and downlads of 100k+ is ' + str((len(inst))), bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 20, y = 520)
    
    Button(screen15, text = '<<<', bg='brown', fg = 'white', command=screen15.destroy).place(x = 10, y = 560)
    Label(screen15, text = 'Back to Previous Screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
          
def eight():
    global screen25, val1, val2, pol
    
    screen25 = Tk()
    screen25.title("Which quarter of which year has generated maximum install for each category")
    adjustWindow(screen25)
    screen25.configure(background = 'black')
    screen25.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen25, text="Max Download in Years", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').pack() 
        
    copy = data

    copy['Installs'] = data.Installs.str.replace(",","")
    copy['Installs'] = data.Installs.str.replace("+","")
    copy['Installs'] = data.Installs.replace("Free", 0) 
    copy['Installs'] = data['Installs'].astype(float)
    copy['Installs'].dtype
    
    copy['Last Updated'] = pd.to_datetime(copy['Last Updated'])
    copy['year'] = copy['Last Updated'].dt.year
    
    copy['qtr'] = pd.to_datetime(copy['Last Updated']).dt.quarter
    
    value = copy.groupby(['year', 'qtr'], as_index = False)['Installs'].sum()
    
    value['Installs'] = value['Installs']/1000000
    
    new_index = (value['Installs'].sort_values(ascending = False)).index.values
    sorted_data = value.reindex(new_index)
         
    stat = "The" + str(sorted_data['qtr'].head(1).to_string(index=False))+ "rd quarter of the year" +str(sorted_data['year'].head(1).to_string(index=False))+ " has the maximum install of "+str(round(float(sorted_data['Installs'].head(1).to_string(index=False)), 2)) + " millions"
    Label(screen25, text=stat, bg = 'black', fg='white', font=('calibri', 12, 'bold')).place(x = 10, y = 100)     
    
    Button(screen25, text = '<<<', bg='brown', fg = 'white', command=screen25.destroy).place(x = 10, y = 560)
    Label(screen25, text = 'Back to Previous Screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
    

    copy['Installs'] = data.Installs.str.replace(",","")
    copy['Installs'] = data.Installs.str.replace("+","")
    copy['Installs'] = data.Installs.replace("Free", 0) 
    copy['Installs'] = data['Installs'].astype(float)
    copy['Installs'].dtype
    
    copy['Last Updated'] = pd.to_datetime(copy['Last Updated'])
    copy['year'] = copy['Last Updated'].dt.year
    
    copy['qtr'] = pd.to_datetime(copy['Last Updated']).dt.quarter
    
    value = copy.groupby(['year', 'qtr'], as_index = False)['Installs'].sum()
    
    value['Installs'] = value['Installs']/1000000
    
    new_index = (value['Installs'].sort_values(ascending = False)).index.values
    sorted_data = value.reindex(new_index)
         
    stat = "The" + str(sorted_data['qtr'].head(1).to_string(index=False))+ "rd quarter of the year" +str(sorted_data['year'].head(1).to_string(index=False))+ " has the maximum install of "+str(round(float(sorted_data['Installs'].head(1).to_string(index=False)), 2)) + " millions"
    Label(screen25, text=stat, bg = 'black', fg='white', font=('calibri', 12, 'bold')).place(x = 10, y = 100)     
    
    Button(screen25, text = '<<<', bg='brown', fg = 'white', command=screen25.destroy).place(x = 10, y = 560)
    Label(screen25, text = 'Back to Previous Screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
  
def nine():
    global screen11, choice, pos, neg, same
    
    screen11 = Tk()
    screen11.title("Apps that have generate most positive and negative sentiments and same ratio of Positive and negative sentiments")
    adjustWindow(screen11)
    screen11.configure(background = 'black')
    screen11.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    choice = StringVar()
    pos = []
    neg = []
    same = []
    positive = negative = neutral = 0
    pos_senti = []
    neg_senti = []
    neutral_senti = []
    total_senti = []
    per_pos = []
    per_neg = []
    per_neutral = []
    
    Label(screen11, text="Apps with most positive, negative and same number of Sentiments", width='70', height="3", font=("Calibri", 15, 'bold'), fg='white', bg='#00e750').pack() 
    
    Label(screen11, text = "", bg = 'black').pack()
    
    copy = data1.copy()
    copy.drop(['Translated_Review', 'Sentiment_Polarity', 'Sentiment_Subjectivity'], axis = 1, inplace = True)
    copy = copy.dropna()
    
    app_list = list(copy['App'].unique())
    
    for i in app_list:
        x = copy[copy['App'] == i]
        
        if(len(x) != 0):
            for i in x.Sentiment:
                if i == 'Positive':
                    positive = positive + 1
                if i == 'Negative':
                    negative = negative + 1
                if i == 'Neutral':
                    neutral = neutral + 1
                    
            pos_senti.append(positive)
            neg_senti.append(negative)
            neutral_senti.append(neutral)
            total_senti.append(positive + negative + neutral)
            positive = negative = neutral = 0

        else:
            for i in x.Sentiment:
                if i == 'Positive':
                    positive = positive + 1
                if i == 'Negative':
                    negative = negative + 1
                if i == 'Neutral':
                    neutral = neutral + 1
                    
            pos_senti.append(positive)
            neg_senti.append(negative)
            neutral_senti.append(neutral)
            total_senti.append(positive + negative + neutral)
            positive = negative = neutral = 0
        
    count = len(pos_senti)
    
    for i in range(count):
        temp = round((pos_senti[i]/total_senti[i])*100, 2)
        per_pos.append(temp)
        
        temp1 = round((neg_senti[i]/total_senti[i])*100, 2)
        per_neg.append(temp1)
        
        temp2 = round((neutral_senti[i]/total_senti[i])*100, 2)
        per_neutral.append(temp2)
        
    data_pos = pd.DataFrame({'App': app_list, 'Positive': per_pos})
    new_index = (data_pos['Positive'].sort_values(ascending = False)).index.values
    sorted_pos = data_pos.reindex(new_index)
    
    data_neg = pd.DataFrame({'App': app_list, 'Negative': per_neg})
    new_index = (data_neg['Negative'].sort_values(ascending = False)).index.values
    sorted_neg = data_neg.reindex(new_index)
    
    count = data_pos['Positive'].count()
        
    for i in range(count):
        if(data_pos['Positive'][i] == data_neg['Negative'][i]):
            same.append(data_pos['App'][i])
    
    Label(screen11, text='>>  APP WITH HIGHEST NUMBER OF POSITIVE SENTIMENTS:  '+ sorted_pos['App'].head(1).to_string(index=False), bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 15, y = 90)
    
    Label(screen11, text='>>  APP WITH HIGHEST NUMBER OF NEGATIVE SENTIMENTS:  '+ sorted_neg['App'].head(1).to_string(index=False), bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 15, y = 120)
    
    Label(screen11, text='>>  APPS WITH SAME NUMBER OF POSITIVE AND NEGATIVE SENTIMENTS:', bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 15, y = 150)
    y_lm = 160
    x_lm = 25
    for i in same:
        if y_lm == 500:
            y_lm = 180
            x_lm = 250
        else:
            y_lm = y_lm + 20
        Label(screen11, text=i, bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = x_lm, y = y_lm)

    Button(screen11, text = '<<<', bg='brown', fg = 'white', command=screen11.destroy).place(x = 10, y = 560)
    Label(screen11, text = 'Back to Previous Screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
  
def go_bttn():
    try:
        rate = float(pol.get())
    except ValueError:
        messagebox.showerror('ERROR', 'ENTER ONLY NUMBERS')
        screen22.destroy()
        return(ten())
        
    if (round(rate, 2) < -1.0) or (round(rate, 2) > 1.0):
        messagebox.showerror('ERROR', 'ENTER NUMBER BETWEEN -1 TO 1')
        screen22.destroy()
        return(ten())
    else:
        ans = round(rate * val1 + val2, 2)
        Label(screen22, text = 'Sentiment Subjectivity is: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 420)
        Label(screen22, text= ans, fg = 'white', bg = 'black', font=('calibri', 12, 'bold')).place(x = 200, y =  420)
    
def ten():
    global screen22, val1, val2, pol, go
    
    screen22 = Toplevel()
    screen22.title("Relation between sentiment polarity and sentiment subjectivity")
    adjustWindow(screen22)
    screen22.configure(background = 'black')
    screen22.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen22, text="Sentiment Polarity vs. Sentiment Subjectivity", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').pack() 
        
    copy = data1.copy()
    copy = copy.dropna()
    
    X=copy['Sentiment_Polarity'].values.reshape(-1,1)
    y=copy['Sentiment_Subjectivity'].values.reshape(-1,1)

    reg=LinearRegression()
    reg.fit(X,y)
    predictions=reg.predict(X)
    
    val1 = reg.coef_[0][0]
    val2 = reg.intercept_[0]

    plt.figure()
    plt.scatter(copy['Sentiment_Polarity'], copy['Sentiment_Subjectivity'],c='green')
    plt.plot(copy['Sentiment_Polarity'], predictions,c='red',linewidth=2)
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Sentiment Subjectivity')
    plt.savefig('C:\\Google-play-store-prediction\\images\\l.png', bbox_inches='tight')
    plt.close()
    
    Label(screen22, bg='black').pack()
    
    img = PhotoImage(file='C:\\Google-play-store-prediction\\images\\l.png')
    label = Label(screen22, image=img, anchor = 'w')
    label.image=img 
    label.pack()
    
    Label(screen22, text='Enter Sentiment Polarity: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 390)
    
    pol = Entry(screen22, width = 10)
    pol.place(x = 210, y = 395)
    
    go = Button(screen22, text='GO', bg='brown', fg='white', command= go_bttn)
    go.place(x = 300, y = 390)

    Button(screen22, text = '<<<', bg='brown', fg = 'white', command=screen22.destroy).place(x = 10, y = 560)
    Label(screen22, text = 'Back to Previous Screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
      
def twelve():
    global screen12
    
    screen12 = Toplevel()
    screen12.title("Is it advisable to launch an app like 10 Best foods for you?")
    adjustWindow(screen12)
    screen12.configure(background = 'black')
    screen12.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen12, text="10 Best food for you?", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').pack() 
    Label(screen12, text = "", bg = 'black').pack()
    
    copy1 = data1.copy()
    copy1.drop(['Translated_Review'], axis = 1, inplace = True)
    copy1 = copy1.dropna()
    
    app = copy1[copy1['App'] == '10 Best Foods for You'].copy()
    
    app = app.dropna()
    
    app['Sentiment_Polarity'] = app['Sentiment_Polarity'].astype(float)
    app['Sentiment_Polarity'].dtype
    
    positive = negative = neutral = 0
    
    sentiment = list(app['Sentiment'])
    
    for i in sentiment:
        
        if i == 'Positive':
            positive = positive + 1
        if i == 'Negative':
            negative = negative + 1
        if i == 'Neutral':
            neutral = neutral + 1
            
    total = positive + negative + neutral
    
    fig = plt.figure(figsize=(3, 3))
    size = [positive, negative, neutral]
    sentiment = ['Positive', 'Negative', 'Neutral']
    plt.pie(size, labels = sentiment, startangle = 90, autopct = '%.1f%%')
    plt.title('Sentiment Analysis for "10 best food for you"')
    plt.savefig('C:\\Google-play-store-prediction\\images\\c.png', bbox_inches='tight')
    plt.close()
    
    img = PhotoImage(file='C:\\Google-play-store-prediction\\images\\c.png')
    label = Label(screen12, image=img, anchor = 'w')
    label.image=img 
    label.pack()
    
    # Each word in the lexicon has scores for:
    #1)    polarity: negative vs. positive    (-1.0 => +1.0)
    #2)    subjectivity: objective vs. subjective (+0.0 => +1.0)
    pos_pol = []
    pos_sub = []
    neg_pol = []
    neg_sub = []
    
    x = app[app['Sentiment'] == 'Positive']
    pos_pol.append(x.Sentiment_Polarity)
    pos_sub.append(x.Sentiment_Subjectivity)
    
    x = app[app['Sentiment'] == 'Negative']
    neg_pol.append(x.Sentiment_Polarity)
    neg_sub.append(x.Sentiment_Subjectivity)
    
    #x = app[app['Sentiment'] == 'Neutral']
    #neutral_pol.append(x.Sentiment_Polarity)
    #neutral_sub.append(x.Sentiment_Subjectivity)

    pos_pol_sum = sum(pos_pol[0])
    pos_sub_sum = sum(pos_sub[0])
    
    neg_pol_sum = sum(neg_pol[0])
    neg_sub_sum = sum(neg_sub[0])
    
        
    avg_pos_pol = round(pos_pol_sum/positive, 2)
    avg_pos_sub = round(pos_sub_sum/positive, 2)
    
    avg_neg_pol = round(neg_pol_sum/negative, 2)
    avg_neg_sub = round(neg_sub_sum/negative, 2)
    
    Label(screen12, text='>>  The average Sentiment polarity for Positive review is ' + str(avg_pos_pol) + ' and Average', bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 20, y = 320)
    Label(screen12, text='Sentiment Subjectivity is ' + str(avg_pos_sub), bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 45, y = 340)
    
    Label(screen12, text='>>  The average Sentiment polarity for Negative review is ' + str(avg_neg_pol) + ' and  average', bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 20, y = 370)
    Label(screen12, text='Sentiment Subjectivity is ' + str(avg_neg_sub), bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 45, y = 390)
    
    Label(screen12, text='>>  There are ' + str(neutral) + ' Neutral Sentiments out of ' + str(total) + ' user reviews', bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 20, y = 420)
    
    Label(screen12, text='>>  We have ' + str(positive) + ' Positive Sentiments out of ' + str(total) + ' user reviews', bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 20, y = 450)
    
    Label(screen12, text='>>  The Sentiment Subjectivity for Positive Sentiment is ' + str(avg_pos_sub) + ' which is Fairly Subjective', bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 20, y = 480)
    
    Label(screen12, text='>>  Hence, from the reviews we can conclude that the app is fairly not so convincing', bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 20, y = 510)
    Label(screen12, text='to the users with an average Positive review', bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 45, y = 530)
    
    Button(screen12, text = '<<<', bg='brown', fg = 'white', command=screen12.destroy).place(x = 10, y = 560)
    Label(screen12, text = 'Back to Previous Screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
   
def size_refining(num):
    if len(num) > 10:
        num = num
    elif 'M' in num:
        num = num.replace("M","")
        num = float(num)
    elif 'k' in num:
        num = num.replace('k',"")
        num = float(num)/1000
    return num

def size_categorical(num):
    if type(num) != float:
        num = num
    elif num < 1:
        num = "Less than 1M"
    elif (num >= 1 and num < 10):
        num = "Small Size (1M to 10M)"
    elif (num >=10 and num <30):
        num = "Medium Size (10M to 30M)"
    elif (num >=30 and num <60):
        num = "Large Size(30M to 60M)"
    else:
        num = "Very Large(Greater than 60M)"
    return num

def thirteen():
    global screen13
    
    screen13 = Toplevel()
    screen13.title("Does the size of the App influence the number of installs that it gets?")
    adjustWindow(screen13)
    screen13.configure(background = 'black')
    screen13.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen13, text="Size vs. Number of Installs", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').pack() 
    Label(screen13, text = "", bg = 'black').pack()
    
    copy = data.copy()
    
    copy.drop(['App', 'Rating', 'Current Ver', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Android Ver', 'Reviews'],axis=1,inplace=True)
    
    copy['Installs'] = copy.Installs.str.replace(",","")
    copy['Installs'] = copy.Installs.str.replace("+","")
    copy['Installs'] = copy['Installs'].astype(float)
    copy['Installs'].dtype
    
    copy['Size'] = copy['Size'].apply(size_refining)
     
    size_not = copy[copy['Size'] != 'Varies with device']
    size = copy[copy['Size'] == 'Varies with device']
    size_not['Size'] = size_not['Size'].apply(size_categorical)
    
    size_of = pd.concat([size_not, size])
    
    total_download = []
    for i in size_of['Size'].value_counts().index:
        total_download.append(sum(size_of[size_of['Size'] == i]['Installs'])/1000000000)
    
    fig = plt.figure()
    sns.barplot(x = size_of['Size'].value_counts().index, y = total_download)
    plt.xticks(rotation = 90)
    plt.xlabel("Index")
    plt.ylabel("Downloads (in billion)")
    plt.title("Downloads as per Size of Apps")
    plt.savefig('C:\\Google-play-store-prediction\\images\\f.png', bbox_inches='tight')
    plt.close()
    
    img = PhotoImage(file='C:\\Google-play-store-prediction\\images\\f.png')
    label = Label(screen13, image=img, anchor = 'w')
    label.image=img 
    label.pack()
    
    Button(screen13, text = '<<<', bg='brown', fg = 'white', command=screen13.destroy).place(x = 10, y = 560)
    Label(screen13, text = 'Back to Previous Screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
       

def fifteen_3(yr_17, yr_18):
    global screen18
    
    screen18 = Toplevel()
    screen18.title("For 2016, 17 & 18 most & least dwnld(category wise)")
    adjustWindow(screen18)
    screen18.configure(background = 'black')
    screen18.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen18, text="Download trend in year 2018", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').pack() 
    Label(screen18, text = "", bg = 'black').pack()
    
    plt.figure()
    sns.barplot(x = yr_18['Category'], y = yr_18['Installs'])
    plt.xticks(rotation = 90)
    plt.xlabel("Category")
    plt.ylabel("Downloads(in ten millions)")
    plt.title("Downloads in 2018")
    plt.savefig('C:\\Google-play-store-prediction\\images\\i3.png', bbox_inches='tight')
    plt.close()

    img = PhotoImage(file='C:\\Google-play-store-prediction\\images\\i3.png')
    label = Label(screen18, image=img, anchor = 'w')
    label.image=img 
    label.pack()
    
    Button(screen18, text = '2017', bg='brown', fg = 'white', command=lambda: [fifteen_2(yr_17, yr_18), screen18.destroy()]).place(x = 10, y = 560)

def fifteen_2(yr_17, yr_18):
    
    global screen17
    
    screen17 = Toplevel()
    screen17.title("For 2016, 17 & 18 most & least dwnld(category wise)")
    adjustWindow(screen17)
    screen17.configure(background = 'black')
    screen17.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen17, text="Download trend in year 2017", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').pack() 
    Label(screen17, text = "", bg = 'black').pack()
    
    plt.figure()
    sns.barplot(x = yr_17['Category'], y = yr_17['Installs'])
    plt.xticks(rotation = 90)
    plt.xlabel("Category")
    plt.ylabel("Downloads(in ten millions)")
    plt.title("Downloads in 2017")
    plt.savefig('C:\\Google-play-store-prediction\\images\\i2.png', bbox_inches='tight')
    plt.close()
    
    img = PhotoImage(file='C:\\Google-play-store-prediction\\images\\i2.png')
    label = Label(screen17, image=img, anchor = 'w')
    label.image=img 
    label.pack()
    
    Button(screen17, text = '2016', bg='brown', fg = 'white', command=lambda:[fifteen(), screen17.destroy()]).place(x = 10, y = 560)
    
    Button(screen17, text = '2018', bg='brown', fg = 'white', command= lambda: [fifteen_3(yr_17, yr_18)]).place(x = 550, y = 560)

def fifteen():
    global screen16
    
    screen16 = Toplevel()
    screen16.title("For 2016, 17 & 18 most & least dwnld(category wise)")
    adjustWindow(screen16)
    screen16.configure(background = 'black')
    screen16.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen16, text="Download trend in year 2016", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').pack() 
    Label(screen16, text = "", bg = 'black').pack()
    
    copy = data.copy()
    
    copy.drop(['App', 'Size', 'Reviews', 'Type', 'Price', 'Content Rating', 'Genres', 'Android Ver', 'Current Ver'], axis = 1, inplace = True)
        
    copy['Installs'] = copy.Installs.str.replace(",","")
    copy['Installs'] = copy.Installs.str.replace("+","")
    copy['Installs'] = copy.Installs.replace("Free", 0) 
    copy['Installs'] = copy['Installs'].astype(float)
    copy['Installs'].dtype
    
    copy['Last Updated'] = pd.to_datetime(copy['Last Updated'])
    copy['year'] = copy['Last Updated'].dt.year
    
    value=copy.groupby(['year', 'Category'], as_index = False)['Installs'].sum()
    value['Installs'] = value['Installs']/10000000
    yr_16 = value[value.year == 2016].sort_values(by='Installs',ascending = False)
    
    plt.figure()
    sns.barplot(x = yr_16['Category'], y = yr_16['Installs'])
    plt.xticks(rotation = 90)
    plt.xlabel("Category")
    plt.ylabel("Downloads(in ten millions)")
    plt.title("Downloads in 2016")
    plt.savefig('C:\\Google-play-store-prediction\\images\\i1.png', bbox_inches='tight')
    plt.close()
        
    img = PhotoImage(file='C:\\Google-play-store-prediction\\images\\i1.png')
    label = Label(screen16, image=img, anchor = 'w')
    label.image=img 
    label.pack()
    
    yr_17 = value[value.year == 2017].sort_values(by='Installs',ascending = False)
    
    yr_18 = value[value.year == 2018].sort_values(by='Installs',ascending = False)
    
    Button(screen16, text = '<<<', bg='brown', fg = 'white', command=lambda:[screen16.destroy(), screen17.destroy(), screen18.destroy()]).place(x = 10, y = 560)
    Label(screen16, text = 'Back to Previous Screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
    
    Button(screen16, text = '2017', bg='brown', fg = 'white', command= lambda: [fifteen_2(yr_17, yr_18)]).place(x = 550, y = 560)
    
def sixteen():
    global screen19
    
    screen19 = Toplevel()
    screen19.title("Predict Download of apps (Category wise)")
    adjustWindow(screen19)
    screen19.configure(background = 'black')
    screen19.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen19, text="Predict Download of apps (Category wise)", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').pack() 
    Label(screen19, text = "", bg = 'black').pack()
    
    copy = data.copy()
    
    copy.drop(['App', 'Size', 'Reviews', 'Type', 'Price', 'Content Rating', 'Genres', 'Android Ver', 'Current Ver'], axis = 1, inplace = True)
        
    copy['Installs'] = copy.Installs.str.replace(",","")
    copy['Installs'] = copy.Installs.str.replace("+","")
    copy['Installs'] = copy.Installs.replace("Free", 0) 
    copy['Installs'] = copy['Installs'].astype(float)
    copy['Installs'].dtype
    
    category_list = ['ART_AND_DESIGN', 'AUTO_AND_VEHICLES', 'BEAUTY', 'FI0CE', 'BOOKS_AND_REFERENCE', 'BUSINESS', 'COMICS', 'COMMUNICATION', 'DATING', 'EDUCATION', 'FINANCE', 'FOOD_AND_DRINK', 'HEALTH_AND_FITNESS', 'HOUSE_AND_HOME', 'LIBRARIES_AND_DEMO', 'LIFESTYLE', 'FAMILY', 'MEDICAL', 'SHOPPING', 'PHOTOGRAPHY', 'TOOLS', 'PERSONALIZATION', 'PRODUCTIVITY', 'PARENTING', 'WEATHER', 'VIDEO_PLAYERS', 'MAPS_AND_NAVIGATION', 'lIFESTYLE']

    n = len(category_list)

    for i in range (n):
        indexNames = copy[ copy['Category'] == category_list[i] ].index
        copy.drop(indexNames , inplace=True)
    
    copy['Last Updated'] = pd.to_datetime(copy['Last Updated'])
    copy['year'] = copy['Last Updated'].dt.year
    
    copy['Installs']= copy['Installs']/1000000000
    # plot data
    fig, ax = plt.subplots()
    # use unstack()
    plt.ylabel("Install(in billions)")
    plt.xlabel('Year')
    copy.groupby(['year','Category']).sum()['Installs'].unstack().plot(ax=ax)
    plt.savefig('C:\\Google-play-store-prediction\\images\\j.png', bbox_inches='tight')
    plt.close()
    
    img = PhotoImage(file='C:\\Google-play-store-prediction\\images\\j.png')
    label = Label(screen19, image=img, anchor = 'w')
    label.image=img 
    label.pack()
    
    Label(screen19, text = '>>  From above graph we can see that the Number of downloads of Apps that belongs to', bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 10, y = 380)
    Label(screen19, text = 'GAME category has increased drastically in past some years.', bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 30, y = 400)
    
    Label(screen19, text = '>>  And also the number of Downloads of Apps belongs to SOCIAL MEDIA and NEWS category', bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 10, y = 430)
    Label(screen19, text = 'has increased from 2017 to 2018.', bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 30, y = 450)
    
    Label(screen19, text = '>>  Hence, the Category of apps that will be downloaded in upcoming years are GAME,', bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 10, y = 480)
    Label(screen19, text = 'SOCIAL MEDIA and NEWS', bg='black', fg='white', font=("calibri", 11, 'bold')).place(x = 30, y = 500)

    Button(screen19, text = '<<<', bg='brown', fg = 'white', command = screen19.destroy).place(x = 10, y = 560)
    Label(screen19, text = 'Back to Previous Screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
            
def seventeen_2():
    global screen21
    
    screen21 = Toplevel()
    screen21.title("Ratio download of app for teen versus mature 17+")
    adjustWindow(screen21)
    screen21.configure(background = 'black')
    screen21.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen21, text="Teen vs. Mature 17+", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').pack() 
    
    Label(screen21, text='', bg='black').pack()
          
    copy = data.copy()

    mature=copy[copy['Content Rating']=='Mature 17+']
    teen=copy[copy['Content Rating']=='Teen']
    
    size=[len(mature), len(teen)]
    content = ['MATURE 17+', 'TEEN']
    plt.pie(size, labels=content, startangle=0, autopct='%.1f%%') 
    plt.title('Ratio download of app for teen versus mature 17+')
    plt.savefig('C:\\Google-play-store-prediction\\images\\k.png', bbox_inches='tight')
    plt.close()
    
    img = PhotoImage(file='C:\\Google-play-store-prediction\\images\\k.png')
    label = Label(screen21, image=img, anchor = 'w')
    label.image=img 
    label.pack()
         
    Button(screen21, text = '<<<', bg='brown', fg = 'white', command=screen21.destroy).place(x = 10, y = 560)
    Label(screen21, text = 'Back to Previous Screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
    
def seventeen():
    global screen20
    
    screen20 = Tk()
    screen20.title("Across all yrs which month has max dwnld (catgry wise)")
    adjustWindow(screen20)
    screen20.configure(background = 'black')
    screen20.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen20, text="Category wise maximum Downloads in months", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').pack() 
    
    scrollbar = Scrollbar(screen20)
    scrollbar.pack( side = RIGHT, fill = Y )
        
    copy = data.copy()
    
    copy.drop(['App', 'Size', 'Reviews', 'Type', 'Price', 'Content Rating', 'Genres', 'Android Ver', 'Current Ver'], axis = 1, inplace = True)

    copy['Installs'] = copy.Installs.str.replace(",","")
    copy['Installs'] = copy.Installs.str.replace("+","")
    copy['Installs'] = copy.Installs.replace("Free", 0) 
    copy['Installs'] = copy['Installs'].astype(float)
    copy['Installs'].dtype
    
    copy['Last Updated'] = pd.to_datetime(copy['Last Updated'])
    copy['month'] = copy['Last Updated'].dt.month
    
    value = copy.groupby(['Category', 'month'], as_index = False)['Installs'].sum()
    value['Installs'] = value['Installs'].astype(int)
    cat = list(value['Category'].unique())
    
    output = []
    clr = []
    lr =[]
    cat_list = []
    mon_list = []
    install_list = []
    n = 0
    
    for i in cat:
       output.append(value[value.Category == i].sort_values(by = 'Installs', ascending = False).head(1).to_string(index = False))
       
    for i in output:
        x = i.split('\n')
        clr.append(x[1])
    
    for i in clr:
        x = i.split(' ')
        lr.append(x)
        
    count = len(lr)
    for i in range(count):
        lr[i] = [y for y in lr[i] if y != '']
    
    for i in range(count):
        
        cat_list.append(lr[i][0])
        mon_list.append(lr[i][1])
        install_list.append(lr[i][2])
        
    for i in (mon_list):
        if i == str(2):
            mon_list[n] = 'February'
        if i == str(3):
            mon_list[n] = 'March'
        if i == str(6):
            mon_list[n] = 'June'
        if i == str(7):
            mon_list[n] = 'July'
        if i == str(8):
            mon_list[n] = 'August'
        if i == str(5):
            mon_list[n] = 'May'
        n = n + 1
            
    mylist = Listbox(screen20, yscrollcommand = scrollbar.set, width = 80, height = 23, bg='black', fg='white', highlightbackground='black', selectbackground="black", font=('calibri', 12, 'bold'))
    
    for i in range(count):
        mylist.insert(END, '>>  For category ' + cat_list[i] + ' the Maximum Downloads are in Month ' )
        mylist.insert(END, str(mon_list[i]) + ' with Download Count ' + install_list[i])
        mylist.insert(END, '')

    mylist.pack( anchor='w' )
    scrollbar.config( command = mylist.yview )
    
    Button(screen20, text = '<<<', bg='brown', fg = 'white', command=screen20.destroy).place(x = 10, y = 560)
    Label(screen20, text = 'Back to Previous Screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
    
    Button(screen20, text = '>>>', bg='brown', fg = 'white', command=lambda:[seventeen_2()]).place(x = 540, y = 560)
    Label(screen20, text = 'Go to Next screen', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 380, y = 560)
         
def enter_app_data():
    df = pd.DataFrame()
    data_dict = {'App': [app.get()], 'Category': [category.get()], 'Rating': [rating.get()], 'Reviews': [reviews.get()], 'Size': [size.get()], 'Installs': [installs.get()], 'Type': [types.get()], 'Price': [price.get()], 'Content Rating': [con_rating.get()], 'Genres': [genres.get()], 'Last Updated': [updated.get()], 'Current Ver': [cur_ver.get()], 'Android Ver': [and_ver.get()]}
    app_dataset = pd.DataFrame(data_dict)
    
    app_dataset.to_csv('C:\\Google-play-store-prediction\\Database\\app.csv')
    for f in ['C:\\Google-play-store-prediction\\Database\\googleplaystore-App-data.csv', 'C:\\Google-play-store-prediction\\Database\\app.csv']:
        data = pd.read_csv(f, 'Sheet1') 
        df = df.append(data)
    
    df.to_csv("C:\\Google-play-store-prediction\\Database\\googleplaystore-App-data.csv")
    messagebox.showinfo('Successfull', 'Data added Successfully!')
    
def enter_review_data():
    df = pd.DataFrame()
    data_dict = {'App': [app_name.get()], 'Translated_Review': [reviews.get()], 'Sentiment': [sentiment.get()], 'Sentiment_Polarity': [polarity.get()], 'Sentiment_Subjectivity': [subjectivity.get()]}
    review_dataset = pd.DataFrame(data_dict)
    
    review_dataset.to_csv('C:\\Google-play-store-prediction\\Database\\reviews.csv')
    for f in ['C:\\Google-play-store-prediction\\Database\\googleplaystore_user_reviews.csv', 'C:\\Google-play-store-prediction\\Database\\reviews.csv']:
        data = pd.read_csv(f, 'Sheet1') 
        df = df.append(data)
    
    df.to_csv("C:\\Google-play-store-prediction\\Database\\googleplaystore_user_reviews.csv")
    messagebox.showinfo('Successfull', 'Data added Successfully!')

def app_new():
    app.delete(0, 'end')
    category.delete(0, 'end')
    rating.delete(0, 'end')
    reviews.delete(0, 'end') 
    size.delete(0, 'end') 
    installs.delete(0, 'end') 
    types.delete(0, 'end') 
    price.delete(0, 'end') 
    con_rating.delete(0, 'end') 
    genres.delete(0, 'end') 
    updated.delete(0, 'end') 
    cur_ver.delete(0, 'end') 
    and_ver.delete(0, 'end') 
    return

def review_new():
    app_name.delete(0, 'end') 
    reviews.delete(0, 'end') 
    sentiment.delete(0, 'end') 
    polarity.delete(0, 'end') 
    subjectivity.delete(0, 'end') 
    return

def review_record():
    global screen24, app_name, polarity, subjectivity, sentiment, reviews
    
    screen24 = Tk()
    screen24.title("Enter New Records to Datasets")
    adjustWindow(screen24)
    screen24.configure(background = 'black')
    screen24.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen24, text="Enter New Record", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').pack()
    Label(screen24, text='DATASET NAME: Google playstore User Reviews', bg='black', fg='#CCCC00', font=('calibri', 12, 'bold')).place(x = 10, y = 100)
    
    Label(screen24, text='App Name: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 150)
    app_name = Entry(screen24)
    app_name.place(x = 200, y = 155)
    
    Label(screen24, text='Reviews: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 200)
    reviews = Entry(screen24)
    reviews.place(x = 200, y = 205)

    Label(screen24, text='Sentiment: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 250)
    sentiment = Entry(screen24)
    sentiment.place(x = 200, y = 255)
    
    Label(screen24, text='Sentimemt Polarity: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 300)
    polarity = Entry(screen24)
    polarity.place(x = 200, y = 305)

    Label(screen24, text='Sentiments Subjectivity: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 350)
    subjectivity = Entry(screen24)
    subjectivity.place(x = 200, y = 355)
    
    Button(screen24, text='Save', bg='brown', fg='white', font=('calibri', 11, 'bold'), command = enter_review_data).place(x = 330, y = 560)
    Label(screen24, text='or Add one more Row >>', bg='black', fg='brown', font=('calibri', 12, 'bold')).place(x = 375, y = 565)
    Button(screen24, text='GO', bg='brown', fg='white', font=('calibri', 11, 'bold'), command = review_new).place(x = 555, y = 560)
    
    Button(screen24, text='BACK', bg='brown', fg='white', font=('calibri', 12, 'bold'), command = screen24.destroy).place(x = 10, y = 560)
    
    screen24.mainloop()
    
def app_record():
    global screen23, app, category, rating, reviews, size, installs, types, price, con_rating, genres, updated, cur_ver, and_ver
    
    screen23 = Tk()
    screen23.title("Enter New Records to Datasets")
    adjustWindow(screen23)
    screen23.configure(background = 'black')
    screen23.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
        
    Label(screen23, text="Enter New Record", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').pack()
    Label(screen23, text='DATASET NAME: Google playstore App data', bg='black', fg='#CCCC00', font=('calibri', 12, 'bold')).place(x = 10, y = 100)
    
    Label(screen23, text='App Name: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 150)
    app = Entry(screen23)
    app.place(x = 160, y = 155)
    
    Label(screen23, text='Category: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 325, y = 150)
    category = Entry(screen23)
    category.place(x = 450, y = 155)

    Label(screen23, text='Rating: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 200)
    rating = Entry(screen23)
    rating.place(x = 160, y = 205)
    
    Label(screen23, text='Reviews: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 325, y = 200)
    reviews = Entry(screen23)
    reviews.place(x = 450, y = 205)

    Label(screen23, text='Size: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 250)
    size = Entry(screen23)
    size.place(x = 160, y = 255)
    
    Label(screen23, text='Installs: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 325, y = 250)
    installs = Entry(screen23)
    installs.place(x = 450, y = 255)
    
    Label(screen23, text='Type: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 300)
    types = Entry(screen23)
    types.place(x = 160, y = 305)
    
    Label(screen23, text='Price: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 325, y = 300)
    price = Entry(screen23)
    price.place(x = 450, y = 305)
    
    Label(screen23, text='Content Ratings: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 350)
    con_rating = Entry(screen23)
    con_rating.place(x = 160, y = 355)
    
    Label(screen23, text='Genres: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 325, y = 350)
    genres = Entry(screen23)
    genres.place(x = 450, y = 355)
    
    Label(screen23, text='Last Updated: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 400)
    updated = Entry(screen23)
    updated.place(x = 160, y = 405)
    
    Label(screen23, text='Cureent Version: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 325, y = 400)
    cur_ver = Entry(screen23)
    cur_ver.place(x = 450, y = 405)
    
    Label(screen23, text='Android Version: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 20, y = 450)
    and_ver = Entry(screen23)
    and_ver.place(x = 160, y = 455)
    
    Button(screen23, text='Save', bg='brown', fg='white', font=('calibri', 11, 'bold'), command = enter_app_data).place(x = 330, y = 560)
    Label(screen23, text='or Add one more Row >>', bg='black', fg='brown', font=('calibri', 12, 'bold')).place(x = 375, y = 565)
    Button(screen23, text='GO', bg='brown', fg='white', font=('calibri', 11, 'bold'), command = lambda: [app_new(), enter_app_data()]).place(x = 555, y = 560)
     
    Button(screen23, text='BACK', bg='brown', fg='white', font=('calibri', 12, 'bold'), command = screen23.destroy).place(x = 10, y = 560)
        
def logout():
    screen5.destroy()
    screen4.destroy()
    screen3.destroy()
    pass_btn.delete(0, 'end')
    user_btn.delete(0, 'end')
    
def third_screen():
    global screen5
    
    screen5 = Tk()
    screen5.title("SELECT YOUR CHOICE (Page 3)")
    adjustWindow(screen5)
    screen5.configure(background = 'black')
    screen5.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen5, text="SELECT YOUR CHOICE", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').place(x=0, y=0) 
    
    Label(screen5, text = '(15)  For 2016, 17 & 18 most & least dwnld(category wise)', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 100) 
    Label(screen5, text = 'Percent increase or decrease in downloads in this three year', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 45, y = 120)     
    Button(screen5, text = 'GO', bg='brown', fg='white', command = fifteen).place(x = 450, y = 100)  
    
    Label(screen5, text = '(16)  Amongst sports, entertainment, social media, news,', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 160) 
    Label(screen5, text = 'events, travel and games,which is the category of app', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 45, y = 180)     
    Label(screen5, text = 'that is most likely to be downloaded in the coming years', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 45, y = 200)         
    Button(screen5, text = 'GO', bg='brown', fg='white', command = sixteen).place(x = 450, y = 160) 
    
    Label(screen5, text = '(17)  Across all yrs which month has max dwnld(catgry wise)', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 230) 
    Label(screen5, text = 'Ratio download of app for teen versus mature 17+', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 45, y = 250)     
    Button(screen5, text = 'GO', bg='brown', fg='white', command = seventeen).place(x = 450, y = 230) 
    
    Label(screen5, text = '(18)  An interface to add new data to both the datasets.', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 280) 
    Label(screen5, text='Select Dataset: ', bg='black', fg='white', font=('calibri', 12, 'bold')).place(x = 45, y = 310)
    Button(screen5, text='Google playstore App data', bg='brown', fg='white', command = app_record).place(x = 50, y = 340)
    Button(screen5, text='Google playstore User Reviews', bg='brown', fg='white', command = review_record).place(x = 250, y = 340)   
    #Label(screen5, text = '(19)  ', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 340) 
    #Button(screen5, text = 'GO', bg='brown', fg='white').place(x = 450, y = 340) 
    
    #Label(screen5, text = '(20)  ', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 400) 
    #Label(screen5, text = '', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 45, y = 420)     
    #Button(screen5, text = 'GO', bg='brown', fg='white').place(x = 450, y = 400) 
    
    Button(screen5, text = '<<<', bg='brown', fg = 'white', command = second_screen).place(x = 10, y = 560)
    Label(screen5, text = 'Previous Page', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
    
    Button(screen5, text = 'LOGOUT', bg='brown', fg = 'white', command = logout).place(x = 525, y = 560)
    
def second_screen():
    global screen4
    
    screen4 = Tk()
    screen4.title("SELECT YOUR CHOICE (Page 2)")
    adjustWindow(screen4)
    screen4.configure(background = 'black')
    screen4.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen4, text="SELECT YOUR CHOICE", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').place(x=0, y=0) 
    
    Label(screen4, text = '(8)  Which quarter of which year has generated maximum', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 100) 
    Label(screen4, text = 'install for each category', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 35, y = 120)     
    Button(screen4, text = 'GO', bg='brown', fg='white', command = eight).place(x = 450, y = 100)  
    
    Label(screen4, text = '(9)  Apps that have generate most positive and negative senti-', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 160) 
    Label(screen4, text = 'ments and same ratio of Positive and negative sentiments', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 35, y = 180)     
    Button(screen4, text = 'GO', bg='brown', fg='white', command=nine).place(x = 450, y = 160) 
    
    Label(screen4, text = '(10)  Relation between sentiment polarity and sentiment', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 220) 
    Label(screen4, text = 'subjectivity', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 45, y = 240)     
    Button(screen4, text = 'GO', bg='brown', fg='white', command = ten).place(x = 450, y = 220) 
    
    Label(screen4, text = '(11)  An interface where the client can see reviews categorized', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 280) 
    Label(screen4, text = 'as positive, negative & neutral', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 45, y = 300)     
    Button(screen4, text = 'GO', bg='brown', fg='white').place(x = 450, y = 280)
    
    Label(screen4, text = '(12)  Is it advisable to launch an app like 10 Best foods for you?', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 340) 
    Button(screen4, text = 'GO', bg='brown', fg='white', command=twelve).place(x = 450, y = 340) 
    
    Label(screen4, text = '(13)  Does the size of the App influence the number of installs', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 400) 
    Label(screen4, text = 'that it gets ?', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 45, y = 420)     
    Button(screen4, text = 'GO', bg='brown', fg='white', command= thirteen).place(x = 450, y = 400) 
    
    Label(screen4, text = '(14)  Which month of the year  is best indicator to the average', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 460) 
    Label(screen4, text = 'downloads that an app will generate over the entire year?', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 45, y = 480)     
    Button(screen4, text = 'GO', bg='brown', fg='white').place(x = 450, y = 460) 
    
    Label(screen4, text = 'Next Page', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 480, y = 560)
    Button(screen4, text = '>>>', bg='brown', fg = 'white', command = third_screen).place(x = 555, y = 560)
    
    Button(screen4, text = '<<<', bg='brown', fg = 'white', command = first_screen).place(x = 10, y = 560)
    Label(screen4, text = 'Previous Page', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 50, y = 560)
    
def first_screen():
    global screen3
    
    screen3 = Tk()
    screen3.title("SELECT YOUR CHOICE (Page 1)")
    adjustWindow(screen3)
    screen3.configure(background = 'black')
    screen3.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
        
    Label(screen3, text="SELECT YOUR CHOICE", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').place(x=0, y=0) 
    
    Label(screen3, text = '(1)  Percentage download in each category on the playstore', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 100) 
    Button(screen3, text = 'GO', bg='brown', fg='white', command = one).place(x = 450, y = 100)  
    
    Label(screen3, text = '(2)  Apps that have manged to get download in range', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 160) 
    Label(screen3, text = '10k to 5ok, 50k to 150k and so on...', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 35, y = 180)     
    Button(screen3, text = 'GO', bg='brown', fg='white', command = two).place(x = 450, y = 160) 
    
    Label(screen3, text = '(3)  Category of apps that have managed to get most, least', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 220) 
    Label(screen3, text = 'and average istall of 250k', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 35, y = 240)     
    Button(screen3, text = 'GO', bg='brown', fg='white', command = three).place(x = 450, y = 220) 
    
    Label(screen3, text = '(4)  Category of app managed to get highest maximum rating', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 280) 
    Button(screen3, text = 'GO', bg='brown', fg='white', command = four).place(x = 450, y = 280)
    
    Label(screen3, text = '(5)  Download trend category wise', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 340) 
    Button(screen3, text = 'GO', bg='brown', fg='white', command = five).place(x = 450, y = 340) 
    
    Label(screen3, text = '(6)  All apps whose version is not an issue, % increase and', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 400) 
    Label(screen3, text = 'decrease in download', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 35, y = 420)     
    Button(screen3, text = 'GO', bg='brown', fg='white', command = six).place(x = 450, y = 400) 
    
    Label(screen3, text = '(7)  Apps which have managed rating of 4.1 and above and', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 10, y = 460) 
    Label(screen3, text = 'downloads of 100k+', bg='black', fg='white', font=("calibri", 12, 'bold')).place(x = 35, y = 480)     
    Button(screen3, text = 'GO', bg='brown', fg='white', command = seven).place(x = 450, y = 460) 
    
    Label(screen3, text = 'Next Page', bg='black', fg='brown', font=("calibri", 11, 'bold')).place(x = 480, y = 560)
    Button(screen3, text = '>>>', bg='brown', fg = 'white', command = second_screen).place(x = 555, y = 560)     
                     
def login_verify():
    global studentID 
    
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="anonymous")
    cursor = connection.cursor() 
    select_query =  "SELECT * FROM login_details where email = '" + username_verify.get() + "' AND password = '" + password_verify.get() + "';" 
    cursor.execute(select_query)  
    student_info = cursor.fetchall() 
    connection.commit() 
    connection.close() 
                     
    if student_info: 
        messagebox.showinfo("Congratulation", "Login Successful")
        first_screen() 
    else: 
        messagebox.showerror("Error", "Invalid Username or Password") 
                   
def register_user():
    if fullname.get() and email.get() and password.get() and repassword.get() and gender.get():
        
        found = 0
        mail = email.get()
        connection = pymysql.connect(host = "localhost", user = "root", passwd="", database="anonymous")
        cursor = connection.cursor()
        mquery = "SELECT email FROM login_details"
        idq = 'SELECT id FROM login_details'
        cursor.execute(mquery) 
        a = cursor.fetchall()
        cursor.execute(idq)
        b = cursor.fetchall()
        connection.commit() 
        connection.close() 
        
        idn = random.randint(0, 999)
        if idn in b[0]:
            idn = random.randint(0, 999)
                
        for i in a:
         
            if i[0] == mail:
                found = 1
                break
      
        if found == 1:
            Label(screen1, text="Email already registered", fg="red", font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
            Button(screen1, text='Proceed to Login ->', width=20, font=("Constantia", 9,'bold'), bg='brown', fg='white',command=screen1.destroy).place(x=170, y=570)
            return
        elif company.get() == "if Not make it Blank": 
                Label(screen1, text="Please enter your Company Name", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                return
        else:
            if tnc.get():
                if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email.get()):
                    if password.get() == repassword.get(): 
                        gender_value = 'male'
                        if gender.get() == 2:
                            gender_value = 'female'
                        if found == 0:
                            
                            connection = pymysql.connect(host="localhost", user="root", passwd="", database="anonymous")
                            cursor = connection.cursor()
                            insert_query = "INSERT INTO login_details (id, fullname, email, password, gender, company) VALUES('" + str(idn) + "', '"+ fullname.get() + "', '"+ email.get() + "', '"+ password.get() +"', '"+ gender_value + "', '"+ company.get() + "' );" 
                            cursor.execute(insert_query) 
                            connection.commit() 
                            connection.close() 
                            
                            Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11), width='30', anchor=W, bg='black').place(x=0, y=570) 
                            Button(screen1, text='Proceed to Login ->', width=20, font=("Constantia", 9,'bold'), bg='brown', fg='white',command=screen1.destroy).place(x=170, y=570)
                    else:
                        Label(screen1, text="Password does not match", fg="red", font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                        return
                else:
                    Label(screen1, text="Please enter valid email id", fg="red", font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                    return
            else:
                Label(screen1, text="Please accept the agreement", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
                return
    else:
        Label(screen1, text="Please fill all the details", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
        return

def register():                   
    global screen1, fullname, email, password, repassword, company, gender, tnc 
    
    fullname = StringVar() 
    email = StringVar() 
    password = StringVar() 
    repassword = StringVar() 
    company = StringVar() 
    gender = IntVar() 
    tnc = IntVar() 
    
    screen1 = Toplevel(screen) 
    screen1.title("Registration Form") 
    adjustWindow(screen1) 
    screen1.configure(background = 'black')
    screen1.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    Label(screen1, text="Registration Form", width='40', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#00e750').place(x=0, y=0) 
          
    Label(screen1, text="Full Name:", font=("Constantia", 11, 'bold'), fg='white', bg='black', anchor=W).place(x=150, y=160) 
    Entry(screen1, textvar=fullname).place(x=300, y=160) 
    
    Label(screen1, text="Email ID:", font=("Constantia", 11, 'bold'), fg='white', bg='black', anchor=W).place(x=150, y=210) 
    Entry(screen1, textvar=email).place(x=300, y=210) 
    
    Label(screen1, text="Gender:", font=("Constantia", 11, 'bold'), fg='white', bg='black', anchor=W).place(x=150, y=260) 
    Radiobutton(screen1, text="Male", variable=gender, value=1, selectcolor='black', fg = 'white', bg = 'black').place(x=300, y=260) 
    Radiobutton(screen1, text="Female", variable=gender, value=2, selectcolor='black', fg = 'white', bg = 'black' ).place(x=370, y=260) 
    
    Label(screen1, text="Company:", font=("Constantia", 11, 'bold'), fg='white', bg='black', anchor=W).place(x=150, y=310) 
    Entry(screen1, textvar = company).place(x = 300, y = 310)
    company.set('if Not make it Blank') 
    
    Label(screen1, text="Password:", font=("Constantia", 11, 'bold'), fg='white', bg = 'black', anchor=W).place(x=150, y=360) 
    Entry(screen1, textvar=password, show="*").place(x=300, y=360) 
    
    Label(screen1, text="Re-Password:", font=("Constantia", 11, 'bold'), fg='white', bg = 'black', anchor=W).place(x=150, y=410) 
    entry_4 = Entry(screen1, textvar=repassword, show="*") 
    entry_4.place(x=300, y=410) 
    
    Checkbutton(screen1, text="I accept all terms and conditions", variable=tnc, bg='black', font=("Constantia", 9, 'bold'), fg='brown').place(x=175, y=450) 
    Button(screen1, text='Submit', width=20, font=("Constantia", 13, 'bold'), bg='brown', fg='white', command=register_user).place(x=170, y=490)         

def main_screen():
    global screen, username_verify, password_verify, pass_btn, user_btn
    
    screen=Tk()
    screen.title("THE ANONYMOUS")
    adjustWindow(screen)
    screen.configure(background = 'black')
    screen.wm_iconbitmap('C:\\Google-play-store-prediction\\images\\try.ico')
    
    username_verify = StringVar()
    password_verify = StringVar()
    
    image = PhotoImage(file = 'C:\\Google-play-store-prediction\\images\\grp.png')
    
    Label(screen, text = "THE ANONYMOUS", width = 500, height = 2, font = ("Calibri", "22", 'bold'), fg = 'white', bg = '#00e750').pack()
          
    Label(screen, image = image, bg = '#00e750').place(x = 0, y = 0)

    Label(text = "", bg = 'black').pack()
    Label(text = "", bg = 'black').pack()
    Label(text = "", bg = 'black').pack()
    Label(text = "", bg = 'black').pack()
    
    Label(screen, text="Please enter details below to login", bg='black', fg='white', font=("Constantia", 15, 'bold')).pack() 
    Label(screen, text="", bg='black').pack()
    
    Label(screen, text="Enter your ID * ", font=("Constantia", 10, 'bold'), bg='black', fg='white').pack()
    user_btn = Entry(screen,textvar=username_verify)
    user_btn.pack()
    Label(screen, text="", bg='black').pack()  
    
    Label(screen, text="Password * ", font=("Constantia", 10, 'bold'), bg='black', fg='white').pack() 
    pass_btn = Entry(screen, textvar=password_verify, show="*")
    pass_btn.pack()
    Label(screen, text="", bg='black').pack() 
    
    Button(screen, text="LOGIN", bg="brown", width=15, height=1, font=("Constantia", 13, 'bold'), fg='white', command=login_verify).pack() 
    Label(screen, text="", bg='black').pack() 
    
    Button(screen, text="New User? Register Here", height="2", width="30", bg='brown', font=("Constantia", 10, 'bold'), fg='white', command=register).pack() 
          
    screen.mainloop()
    
def splash():
    global root
    
    root = Tk()
    root.configure(background = 'black')
    sp = SplashScreen(root)
    img = PhotoImage(file='C:\\Google-play-store-prediction\\images\\splash.gif')
    
    Label(root, bg='black').pack()
    Label(root, bg='black').pack()
    Label(root, bg='black').pack()
    Label(root, bg='black').pack()
    Label(root, bg='black').pack()
    Label(root, bg='black').pack()
    
    m = Label(sp, text="", image = img, bg = 'black')
    m.pack()
    Label(root, text='Created By:', bg='black', fg='brown', font=('calibri', 12, 'bold')).place(x = 450, y = 500)
    Label(root, text='Bhavesh Singh', bg='black', fg='brown', font=('calibri', 12, 'bold')).place(x = 470, y = 520)
    Label(root, text='Asmita Singh', bg='black', fg='brown', font=('calibri', 12, 'bold')).place(x = 470, y = 540)
    Button(sp, text="Press this button to Start the Application", bg='red', command=lambda:[root.destroy(), main_screen()]).pack(side=BOTTOM, fill=X)
    
    root.mainloop()    

global data, data1
data = pd.read_csv("C:\\Google-play-store-prediction\\Database\\googleplaystore-App-data.csv")
data1 = pd.read_csv("C:\\Google-play-store-prediction\\Database\\googleplaystore_user_reviews.csv")

splash()