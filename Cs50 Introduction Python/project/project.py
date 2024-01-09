# FINAL PROJECT CS50 PANDAS

# python project.py

import pandas as pd
#import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
import pyfiglet
plt.style.use("ggplot")

import sys
import csv


# python project.py

statictics_s_sn = {}

def main():
    ti = gain()
    title = "Analysis of Titanic Disaster"
    ascii_title = pyfiglet.figlet_format(title,font = 'slant')
    print(ascii_title)
    login = input("Log in: ").strip().capitalize()
    if not login.isalpha():
        sys.exit("Invalid Username of login")
    t = rez(login)
    print(t)
    answer = input(f"Hi {login}, are you ready to analyze Titanic dataframe?(Y/N) ").lower()
    if answer == "y":
        # I want to open csv via pandas
        df = pd.read_csv('titanic_dataset.csv')
        #Ask if user want to clean ataframe
        choice_clean = input(f"{login} Do you want to clean dataframe?(Y/N)").strip().lower()
        if choice_clean == "y":
            # I want to know the shape of dataframe before and after the cleaning
            print(f"Before cleaning ={df.shape}")
            if df.duplicated().any():
                print("Handle dupplicates")
            else:
                print("There are not duplicate in df")
            #print(f"duplicated = {df.duplicated()}")
            print(df.isnull().sum())
            df.dropna(inplace=True)
            print(df.isnull().sum())
            print(f"After cleaning ={df.shape}")
        # I ask if he or she want to see or analize dataframe
        answer_1 = input(f"Perfect {login}, what do you want to know about the tragedy of Titanic?(R/A) ").lower()
        if answer_1 == "r":
            n = int(read(login))
            # I want to see the first 5 rows
            print(df.head(n))
        elif answer_1 == "a":
            result = analyze(login,df)
            # I want to check if result is a new_dataframe or a string of end
            if isinstance(result,pd.DataFrame):
                input(f"{login}, do you want to work with new DataFrame?(Y/N) ").lower().strip()
                print("Write code with pandas to analyze data in your own way")
                sys.exit()
            # If I finished the analysis print defoult finish string
            else:
                print(result)




def read (login):
    # This function is useful beacause I want to know in read mode, how many rows I users want to see
    n = input(f"READING SECTION = {login} How many rows do you want to see?")
    return n


def analyze(login,df):
    # In this function I want to handle the possibility of analize
    choice = input("What kind of analisis do you want to have?\n"
                    "A1) See the general statistc parameters\n"
                    "A2) Reduce the data frame\n"
                    "A3) Survived and not survived analysis\n"
                    "A4) Interesting plots\n"
                    "A5) Query about the Embarked "
                    "CHOISE(A1/A2/A3/A4/A5): ").lower().strip()
    if choice == "a1":
        # I want to know if the user want to see the type = 'object' statistics
        choice_1 = input(f"{login} do you want to include 'object' in generals statistics?(Y/N)").strip().lower()
        if choice_1 == "y":
            # I'm define general statistics usig 'object type'
            print(df.describe(include = "object"))
        elif choice_1 == "n":
            print(df.describe())
        else:
            sys.exit("Invalid option choose")
        return f"{login} , read command succesful done"
    elif choice == "a2":
        try:
            # I want to grab a cert columns numbers
            choice_3 = input(f"{login} Which columns do you want to consider [{df.columns}]. WRITE AS ARRAY Age, Name, ecc.... INPUT= ")
            # I want to formmat the input into a list that is the right argument for the new_df = df[column_to_select]
            column_to_select = [co.strip().capitalize() for co in choice_3.split(",")]
            print(f"column{column_to_select}")
            # I'm define a new data frame via array of columns as input
            new_df = df[column_to_select]
            # if new data_frame exist and is not empty then return
            if not new_df.empty:
                return new_df
            else:
                return f"{login} analisys done correctly"
            #print(new_df)
        except KeyError as k:
            sys.exit(f"KEY ERROR is {k}")
    elif choice == "a3":
        result_survived = survived(login,df)
        print(f"result_survived = {result_survived}")
        return f"{login}, analys of survived and not survived people done"
    elif choice == "a4":
        plot_choosen = plot(login)
        #print(plot_choosen)
    elif choice == "a5":
        query = que(login)
    else:
        print(f"ATTENTION {login} invalid choice. MUST DIGIT (a1,a2,a3,a4,a5)")

    return 'analyze done'












def survived(login,df):
    try:
        # I want to know if user want to work with survived analysis or not
        choice_3 = input("Do you want to analyze survived or not survived (S/SN)? ").lower().strip()
        if choice_3 == "s":
            survived_df = df[df["Survived"]== 1]
            # the functionvalue_counts count all data in the columns of df in these SEX column, get count the number of female in these case in proporcion of all value_count, if there'is' not value I have 0
            number_female_s = str(round(survived_df['Sex'].value_counts(normalize = True).get('female',0)*100,0))+"%"
            number_male_s = str(round(survived_df['Sex'].value_counts(normalize = True).get('male',0)*100,0))+"%"
            # definition of a data frame of survived female
            df_female_s = df[(df['Sex']=='female') & (df['Survived']== 1)]
            year_female_s = round(df_female_s['Age'].mean(),2)
            # definition of a data frame of survived female
            df_male_s = df[(df['Sex']=='male') & (df['Survived']== 1)]
            year_male_s = round(df_male_s['Age'].mean(),2)
            # I want to save results in a dict
            statictics_s_sn["number_female_s"] = number_female_s
            statictics_s_sn["number_male_s"] = number_male_s
            statictics_s_sn["year_female_s"] = year_female_s
            statictics_s_sn["year_male_s"] = year_male_s

            #return statictics_s_sn
            #print(f"survived_df = {survived_df}")
        elif choice_3 == "sn":
            not_survived_df = df[df["Survived"]== 0]
            # the functionvalue_counts count all data in the columns of df in these SEX column, get count the number of female in these case in proporcion of all value_count, if there'is' not value I have 0
            number_female_ns = str(round(not_survived_df['Sex'].value_counts(normalize = True).get('female',0)*100,0))+"%"
            number_male_ns = str(round(not_survived_df['Sex'].value_counts(normalize = True).get('male',0)*100,0)) + "%"
            # creaction of dataFrame that has only Survived or not and age and Sex
            df_female_ns = df[(df['Sex']=='female') & (df['Survived']== 0)]
            year_female_ns = round(df_female_ns['Age'].mean(),2)
             # definition of a data frame of survived female
            df_male_ns = df[(df['Sex']=='male') & (df['Survived']== 0)]
            year_male_ns = round(df_male_ns['Age'].mean(),2)

            # I want to save results in a dict
            statictics_s_sn["number_female_ns"] = number_female_ns
            statictics_s_sn["number_male_ns"] = number_male_ns
            statictics_s_sn["year_female_ns"] = year_female_ns
            statictics_s_sn["year_male_ns"] = year_male_ns

    except ValueError as d:
        sys.exit(f"[VALUE ERROR] in survived function {d}")

    return statictics_s_sn




def plot(login):
     try:
         df1 = pd.read_csv('titanic_dataset.csv')
         #selection of plot
         plots_answer = input(f"{login} which plots do you want to see?\n"
            "A1) Plot describes the distribution of Survived, Age\n"
            "A2) General plots\n"
            "A3) Correlations\n"
            "Input(A1/A2/A3): ").strip().lower()
         if plots_answer =="a1":
            #print(df1.dtypes)
            #print(f"df in plots is {df1}")
            df1['Survived'] = pd.to_numeric(df1['Survived'], errors='coerce')
            df_plot1 = df1[(df1['Survived'] == 1) &(df1['Age'].notna())]
            df_plot1.plot(kind= 'hist',y='Age', bins=40 , title = "Age of survived distribution")
            plt.xlabel('Age')
            plt.ylabel('Frequency')
            plt.savefig('age_distribution_plot.png')  # Salva il grafico come un file PNG
            df1.plot(kind ='scatter', y='Age', x ='Parch', title = 'Numbers of family people on Titanic for age')
            plt.xlabel('Parch')
            plt.ylabel('Age')
            plt.savefig('age_parch_scatter_plot.png')
         elif plots_answer == "a2":
             # this code is generate generals graph using the three columns
             sns.pairplot( df1,
                          vars = ['Survived','Age','Parch'],
                          hue = 'Sex'
                        )
             plt.savefig('general_plots.png')
         elif plots_answer == "a3":
             # this plot analize the correlations of differents columns. Linear correlation if colors is near to blanck, no correlations if colors is near to black
             df_corr = df1[['Age','Parch','Survived']].dropna().corr()
             sns.heatmap(df_corr,annot = True, fmt = '.2f', cmap = 'coolwarm')
             plt.savefig("correlations_plots.png")
         else:
            sys.exit("Invalid answr")
     except FileNotFoundError as y:
        print(f"Errore nell'apertura del file: {y}")

     return 'plot done'



def que(login):
    try:
        # Open the csv
        df2 = pd.read_csv('titanic_dataset.csv')

        # Sobstitute 'Embarked'
        df2.replace({'Embarked': {'C': 'Cherbourg', 'Q': 'Queenstown', 'S': 'Southampton'}}, inplace=True)

        # Creation of countplot Seaborn
        plt.figure(figsize=(8, 6))
        sns.countplot(x='Embarked', data=df2)
        plt.title('Number of passengers embarked')
        plt.xlabel('City')
        plt.ylabel('Number of passenger')
        plt.savefig('count_embarked.png')
        plt.show()

    except ValueError as g:
        print(f"ValueError is {g}")

        return 'Query done'

def gain():
    return True


def rez(login):
            return f"Welcome {login}"


'''

         print(data_query.groupby('Embarked').agg({'mean', 'count'}).sort_values("mean").dropna())

''








# cd project
# python project.py

            #print(f"not_survived_df = {not_survived_df}")



    #return f"{login} Survived Analysis done"

'''
'''
    if survived_df:
        if not survived_df.empty:
            return survived_df
        elif not_survived_df:
            if not not_survived_df.empty:
                return not_survived_df
'''





if __name__ == "__main__":
    main()
