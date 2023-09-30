from time import localtime 
name, age, city, country = input(), int(input()), input(), input()
born_year = localtime().tm_year - age
print(f"Уважаемый {name}!\nНа сегодняшний день Вы проживаете в стране {country}, в городе {city}, и вы родились в {born_year} году.")
