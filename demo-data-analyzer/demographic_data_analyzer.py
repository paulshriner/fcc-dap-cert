import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    # Thanks https://note.nkmk.me/en/python-pandas-value-counts/ for value_counts()
    race_count = df.race.value_counts()

    # What is the average age of men?
    # Thanks https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.round.html for round()
    average_age_men = df.loc[df['sex'] == 'Male', 'age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    # Thanks https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.size.html for size
    percentage_bachelors = (df.loc[df['education'] == 'Bachelors'].size / df.size * 100).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate
    # Thanks https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html for boolean operations
    higher_education = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    lower_education = df.loc[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]

    # percentage with salary >50K
    higher_education_rich = (higher_education.loc[higher_education['salary'] == '>50K'].size / higher_education.size * 100).round(1)
    lower_education_rich = (lower_education.loc[lower_education['salary'] == '>50K'].size / lower_education.size * 100).round(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    # Thanks https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.values.html for values
    # Thanks https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.min.html for min
    min_work_hours = df['hours-per-week'].values.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours]

    rich_percentage = (num_min_workers.loc[num_min_workers['salary'] == '>50K'].size / num_min_workers.size * 100).round(1)

    # What country has the highest percentage of people that earn >50K?
    # Thanks https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.idxmax.html for idxmax
    people_over_50k = df.loc[df['salary'] == '>50K'].value_counts('native-country')
    total_people = df.value_counts('native-country')
    highest_earning_country = (people_over_50k / total_people).idxmax()
    highest_earning_country_percentage = ((people_over_50k / total_people).max() * 100).round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')].value_counts('occupation').idxmax()

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
