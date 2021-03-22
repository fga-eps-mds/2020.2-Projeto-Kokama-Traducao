from os import system


print('Essa operação pode sobrescrever os dados da base.')
print('Você deseja carregar os dados? (Y/n)')

user_input = input()

if user_input.lower() == 'y':
    system('python manage.py loaddata word_portuguese')
    system('python manage.py loaddata phrase_portuguese')
    system('python manage.py loaddata pronunciation_type')
    system('python manage.py loaddata word_kokama')
    system('python manage.py loaddata phrase_kokama')
