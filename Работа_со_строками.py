favour_word = "Чурчхелла"
print(favour_word)


#Another task
first_name = "Виталий"
last_name = "Красилов"
new_account = last_name[:5]
temp_password = last_name[3:7]
print(new_account, temp_password)


#Another task
first_name = "Виталий"
last_name = "Красилов"
def account_generator(f_name, l_name):
    return f_name[:3] + l_name[:3]
new_account = account_generator(first_name, last_name)
print(new_account)


#Another task
first_name = "Виталий"
last_name = "Красилов"
def password_generator(first_name, last_name):
    return first_name[-3:] + last_name[-3:]
temp_password = password_generator(first_name, last_name)
print(temp_password)


#Another task
company_motto = "Мечты сбываются"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]


#Another task
first_name = "Боб"
fixed_first_name = "Р" + first_name[1:]
print(fixed_first_name)


#Another task
password = "theycallme\"crazy\"91"


#Another task
poem_title = "spring storm"
poem_title_fixed = poem_title.title()
print(poem_title_fixed)
print(poem_title) 
