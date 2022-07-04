str1 = "murphy"
str2 = "pumrhy"


# convert both the strings into lowercase
str1 = str1.lower()
str2 = str2.lower()

msg = "{} and {} are not anagram".format(str1, str2)

# check if length is same
if len(str1) == len(str2):

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if sorted_str1 == sorted_str2:
        msg = "{} and {} are anagram".format(str1, str2)

    print(msg)
