import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    
    race_count = (df["race"].value_counts())

    # What is the average age of men?

    average_age_men = round(df["age"].loc[df["sex"]=="Male"].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(((df.loc[df["education"]=="Bachelors"].shape[0])/df.shape[0])*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    # percentage with salary >50K
    higher_education_rich = round(
        len(higher_education[higher_education["salary"] == ">50K"]) / len(higher_education) * 100, 1)
    lower_education_rich = round(
        len(lower_education[lower_education["salary"] == ">50K"]) / len(lower_education) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = round(((df.loc[(df['salary'] == '>50K') & (df['hours-per-week'] ==  min_work_hours)].shape[0])/(df.loc[(df['hours-per-week'] ==  min_work_hours)].shape[0]))*100, 1)

    rich_percentage = num_min_workers

    # What country has the highest percentage of people that earn >50K?
    percent=[]

    for i in df['native-country'].unique():
      a = round((df.loc[(df['salary'] == '>50K') & (df['native-country'] == i)].shape[0]/df.loc[df['native-country'] == i].shape[0])*100, 1)
      percent.append(a)
    #print(percent, df['native-country'].unique())
    highest_earning_country = pd.Series(percent, index = df['native-country'].unique()).idxmax()
    highest_earning_country_percentage = max(percent)

    # Identify the most popular occupation for those who earn >50K in India.
    df_1= df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    occupation_in=pd.DataFrame(df_1, columns=['native-country','occupation']).mode()
    top_IN_occupation = occupation_in.values[0][1]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
