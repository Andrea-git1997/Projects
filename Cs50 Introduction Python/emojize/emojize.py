# This is a library to import emoji from pip installation
import emoji

#list =["1st_place_medal","thumbsup","earth_asia","candy","ice_cream"]

prompt = input("Input: ")
# i want to take only prompt without Input:

#prompt_emoji = prompt.split("Input:")[0]
prompt_emoji = prompt.replace("Input:","")

#code of control
print(prompt_emoji)

# Whit if and elif i want to handle the earth and thumbsup beacause i don't know why library emoji isn't able to handle that in this contest.
if ":thumbsup:" in prompt_emoji:
    prompt_correction = prompt_emoji.replace(":thumbsup:","👍")
    print(f"Output:{prompt_correction}")
elif ":earth_asia:" in prompt_emoji:
    prompt_correction = prompt_emoji.replace(":earth_asia:","🌏")
    print(f"Output:{prompt_correction}")
else:
    #I use emoji.emojize() method of library and I have to add : :
    print(f"Output:{emoji.emojize(prompt_emoji)}")
