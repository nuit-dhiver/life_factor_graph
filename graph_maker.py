import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

    
year = input("Enter the year:")
df = pd.read_csv(year + ".csv")
df.reset_index(inplace = True)

country = input("Enter country name:").capitalize()
country_index = df.loc[df["Country or region"] == country, "index"].astype(int)


df_columns = ["Social support", "Healthy life expectancy", "Freedom to make life choices", "Generosity", "Perceptions of corruption"]

mean_social_support, mean_healthy_life, mean_life_choices, mean_generosity, mean_poc = np.mean(df[df_columns])

mean_social_support_top, mean_healthy_life_top, mean_life_choices_top, mean_generosity_top, mean_poc_top = np.mean(df[df_columns].head(15))

country_social_support, country_healthy_life, country_life_choices, country_generosity, country_poc = df.loc[country_index, df_columns].squeeze()

#ploting
labels = ['Social support', 'Healthy life expectancy', 'freedom to make life choices', 'Generosity', 'Perceptions of coroption']
x = np.arange(len(labels))

mean_values = [mean_social_support, mean_healthy_life, mean_life_choices, mean_generosity, mean_poc]
top_mean_values = [mean_social_support_top, mean_healthy_life_top, mean_life_choices_top, mean_generosity_top, mean_poc_top]
country_values = [country_social_support, country_healthy_life, country_life_choices, country_generosity, country_poc]

width = 0.25
fig, ax = plt.subplots(figsize=(15,7))

a1 = ax.bar(x - width*1.5, top_mean_values, width, label = "Top 15 Countries")
a2 = ax.bar(x - width/2, mean_values, width, label = "World Mean")
a3 = ax.bar(x + width/2, country_values, width, label = country)

ax.set_ylabel("score")
ax.set_title("Life factors of " +country + " vs World vs Top 15 Countries")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.savefig('vs_world_vs_top.svg')

plt.show()