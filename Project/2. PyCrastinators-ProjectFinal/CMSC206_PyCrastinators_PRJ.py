#Authors: PyCrastinators- Kane, Jose, and Raymond

import pandas as pd
import plotly.express as px

steam = pd.read_csv('steam.csv')
allGames=pd.read_csv('video_game.csv')

steam_dataframe = pd.read_csv("steam.csv")
video_game_dataframe = pd.read_csv("video_game.csv")
video_game_dataframe['Count'] = 1

def genreByYear(year):
    df = allGames[allGames['Year_of_Release'] == year].head(100).groupby(
        ['Genre']
    )['Global_players'].sum()

    df.to_csv('allgames.csv')

    df2 = pd.read_csv('allgames.csv')

    print(df2)

    fig=px.bar(df2,x='Genre',y='Global_players',title='Genre sales from year '+str(year))
    fig.show()


def genreNAandEU():
    dataset = allGames[allGames['Year_of_Release']>1994].groupby(
        ['Genre', 'Year_of_Release']
    )['NA_players','EU_players'].sum()

    dataset.to_csv('naeu.csv')
    dataset = pd.read_csv('naeu.csv')
    dataset = dataset[dataset['Year_of_Release']<2016]
    print(dataset)

    fig = px.bar(dataset, x="Year_of_Release", y='NA_players', color='Genre',barmode='group',title='Genre sales from NA players')
    fig.show()

    fig = px.bar(dataset, x="Year_of_Release", y='EU_players', color='Genre',barmode='group',title='Genre sales from EU players')
    fig.show()

def gameGenYear():
    # Crate a new dataframe, sum all 'Count' column , Groupy by 'Year_of_Release' and 'Genre'
    dataset = video_game_dataframe.groupby(['Genre', 'Year_of_Release'])['Count'].sum()

    # Save this dataset to a csv file because 'dataset' doesnt have headers. Saving as csvfile, automatically creates the headers
    dataset.to_csv('temp.csv')

    # Read the csv file created
    dataset = pd.read_csv('temp.csv')

    # Code to plot line chart
    fig = px.line(dataset, x="Year_of_Release", y="Count", color='Genre', title='Number of games released each year by Genre', markers=True)
    fig.show()

def gameRateYear():
    # Crate a new dataframe, sum all 'Count' column , Groupy by 'Year_of_Release' and 'Platform'
    dataset = video_game_dataframe.groupby(['Platform', 'Year_of_Release'])['Count'].sum()

    # Save this dataset to a csv file because 'dataset' doesnt have headers. Saving as csvfile, automatically creates the headers
    dataset.to_csv('temp.csv')

    # Read the csv file created
    dataset = pd.read_csv('temp.csv')

    # Code to plot line chart
    fig = px.line(dataset, x="Year_of_Release", y="Count", color='Platform', title='Number of games released each year by Platform', markers=True)
    fig.show()


def gamePlatYear():
    # Crate a new dataframe, sum all 'Count' column , Groupy by 'Year_of_Release' and 'Rating'
    dataset = video_game_dataframe.groupby(['Rating', 'Year_of_Release'])['Count'].sum()

    # Save this dataset to a csv file because 'dataset' doesnt have headers. Saving as csvfile, automatically creates the headers
    dataset.to_csv('temp.csv')

    # Read the csv file created
    dataset = pd.read_csv('temp.csv')

    # Code to plot line chart
    fig = px.line(dataset, x="Year_of_Release", y="Count", color='Rating', title='Number of games released each year by ESRB Rating', markers=True)
    fig.show()

def gamesReleased():
    # Crate a new dataframe, sum all 'Count' column , Groupy by 'Year_of_Release' and 'Rating'
    dataset = video_game_dataframe.groupby(['Year_of_Release'])['Count'].sum()

    # Save this dataset to a csv file because 'dataset' doesnt have headers. Saving as csvfile, automatically creates the headers
    dataset.to_csv('temp.csv')

    # Read the csv file created
    dataset = pd.read_csv('temp.csv')

    # Code to plot line chart
    fig = px.pie(dataset, values='Count', names='Year_of_Release', title='Number of games released each year')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    fig.show()

def totalPlayers():
    dataset = allGames[allGames['Year_of_Release']>1994].groupby(
        ['Year_of_Release']
    )['Global_players'].sum()

    dataset.to_csv('players.csv')
    dataset = pd.read_csv('players.csv')
    dataset = dataset[dataset['Year_of_Release']<2016]

    fig = px.line(dataset, x="Year_of_Release", y='Global_players',title="Total players from 1995 to 2015")
    fig.show()

def played_platform_by_year():
    colors = ['#1E90FF', '#B22222', '#3CB371', '#4682B4', '#CD853F', '#00BFFF', '#FF69B4', '#FA8072', '#90EE90', '#EE82EE', '#F4A460' , '#5F9EA0' , '#B0E0E6' , '#EEE8AA' , '#BA55D3' , '#7B68EE' , '#8B4513' , '#B0C4DE']

    video_game_dataframe=pd.read_csv('video_game.csv')

    dataset = video_game_dataframe.groupby(
        ['Platform', 'Year_of_Release']
    )['Global_players'].sum()

    # Save this dataset to a csv file
    dataset.to_csv('category_year.csv')

    # Read the csv file created
    df2 = pd.read_csv('category_year.csv')


    #df2.loc[df2['Global_players'] < 5, 'Platform'] = 'Other Platform with less than 5 millions players'
    fig=px.bar(df2,x='Year_of_Release',y='Global_players', color="Platform", color_discrete_sequence=colors, title='The most played platform per year' )
    fig.write_html('played_platform_by_year.html', auto_open=True) 

def common_words_videogames_title():
    # Function to get a list of words
    def process_words(text : str):
        import re
        text = text.lower()           # Convert the whole text to lower case
        text = re.sub(u"[-()\"#$/@;:<>{}`+=~|!?,\â€“”\*]|\[.*\]|\d{1,}th|\d{1,}s|\d{1,}'s|\d{1,}", " ", text)
        list_words = re.split('[-\s—]', text)  # Split string with multiple delimiters: - , \s, — 

        list_words = [ (eachWord.strip('.,“”!;()-[]?,):\n"')) for eachWord in list_words]     # Cleaning the words from . , ! ; () [] “ ” ? ' 
        list_words = [ (eachWord.replace("’s" , '')) for eachWord in list_words]    # Replace 's from words with ''
        list_words = [ (eachWord.replace("’ll" , '')) for eachWord in list_words]    # Replace 'll from words ''
        list_words = [ (eachWord.replace("’t" , '')) for eachWord in list_words]    # Replace 't from words ''
        list_words = [ (eachWord.replace("'s" , '')) for eachWord in list_words]    # Replace 's from words with ''
        list_words = [ (eachWord.replace("'ll" , '')) for eachWord in list_words]    # Replace 'll from words ''
        list_words = [ (eachWord.replace("'t" , '')) for eachWord in list_words]    # Replace 't from words ''
        list_words = list(filter(None, list_words))         # Filter Null values or empty strings from the List  
        return list_words

    # Function to get frequent words
    def freq_words(list_words : list):
        from collections import Counter
        # Filter out values: the, a, an
        unwanted = ('the', 'no', 'a', 'world', '&','ds','an','ni','ii','to','x','jp','vol','nfl','de','and','iii','of','we','that','in','our','is','it','for','i','or','do','this','on','who','not','but','us','as','are','their','so','be','if','by')
        list_words = [ words for words in list_words if words not in unwanted]

        # Counter module to count freq words        
        Counter = Counter(list_words)
        most_occur = Counter.most_common(300)
        words = ""
        for (word,repetition) in most_occur:
            words += word + " "
        return words


    # Plot wordCloud
    def wordCloud(text : str):
        # Import packages
        from wordcloud import WordCloud, STOPWORDS
        import numpy as np
        from PIL import Image
        import matplotlib.pyplot as plt

        mask = np.array(Image.open('starwars.png'))

        wordcloud = WordCloud(width = 1500, height = 1000, random_state=1, background_color='Black', colormap='autumn', collocations=False, stopwords = STOPWORDS, mask=mask).generate(text)
        
        # Set figure size
        plt.figure(figsize=(20, 15))
        # Display image
        plt.imshow(wordcloud) 
        # No axis details
        plt.axis("off")
        plt.show()
        


    video_game_dataframe = pd.read_csv("video_game.csv")
    games_name_string = ""
    for index, row in video_game_dataframe.iterrows():
        string = str(row["Name"])
        games_name_string += string + " "

    games_name_list = process_words(games_name_string)
    most_freq_words = freq_words(games_name_list)

    wordCloud(most_freq_words)

def companies_with_mostplayer():
    video_game_dataframe=pd.read_csv('video_game.csv')

    dataset = video_game_dataframe[video_game_dataframe['Rating'] == 'E'].groupby(
        ['Publisher']
    )['Global_players'].sum()

    # Save this dataset to a csv file
    dataset.to_csv('publisher_globalPlayers.csv')

    # Read the csv file created
    df2 = pd.read_csv('publisher_globalPlayers.csv')

    df2.loc[df2['Global_players'] < 5, 'Publisher'] = 'Other games with less than 5 millions players'
    fig=px.bar(df2,x='Publisher',y='Global_players',title='Companies with the most players')
    fig.write_html('Companies_with_most_players.html', auto_open=True) 

def top_15_positive_ratings_free_games():
    import plotly.express as px

    steam_dataframe = pd.read_csv("steam.csv")
    df = steam_dataframe[steam_dataframe['price'] == 0].head(100).groupby(
        ['name']
    )['positive_ratings'].sum()

    # Save this dataset to a csv file
    df.to_csv('name_positiveRatings.csv')

    # Read the csv file created
    df2 = pd.read_csv('name_positiveRatings.csv')

    df2.loc[df2['positive_ratings'] < 10000, 'name'] = 'Other games with less 0.2%' # Represent only large countries
    fig = px.pie(df2, values='positive_ratings', names='name', title='Top 100 free-to-play games with better positive ratings')
    fig.write_html('Top_100_positive_ratings_free_games.html', auto_open=True)

    
    
while(True):
    print('------------------------Video Game Trend Analysis-------------------------------')
    print('1. What are the most popular genres by year?')
    print('2. What genres did better in the American market than the European market from 1995-2015?')
    print('3. How have the total players changed over the years?')
    print('4. What are the number of games by genre released each year?')
    print('5. What are the number of games by rating released each year?')
    print('6. What are the number of games by platform released each year?')
    print('7. What are the number of games released each year?')
    print('8. What is the most played platform by year?')
    print('9. Which video games companies have the most players of all time?')
    print('10. What are the top 100 free to play games with the most positive ratings on steam?')
    print('11. What are the common words for videogame titles?')
    print('Type any other number to terminate')

    ans=input('What question would you like to see answered?: ')

    if not ans.isdigit():
        break
    
    #if/else tree instead of switch implemented as python 3.9 is being utilized instead of 3.10
    ans=int(ans)

    if ans==1:
        num=input('What year would you like to see? Has to be between 1995 and 2015: ')
        num=int(num)
        if num > 1994 and num <2016:
            genreByYear(num)
        else:
            print('Nonvalid year')
    elif ans==2:
        genreNAandEU()
    elif ans==3:
        totalPlayers()
    elif ans==4:
        gameGenYear()
    elif ans==5:
        gameRateYear()
    elif ans==6:
        gamePlatYear()
    elif ans==7:
        gamesReleased()
    elif ans==8:
        played_platform_by_year()
    elif ans==9:
        companies_with_mostplayer()
    elif ans==10:
        top_15_positive_ratings_free_games()
    elif ans==11:
        common_words_videogames_title()
    else:
        break



