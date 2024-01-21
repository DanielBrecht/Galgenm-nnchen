""" VERSION 2.2 LATEST """


from random import randint
# import random as r

# valid_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',\
#                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

current_language = 'deutsch'

def generate_storage():
    global entered_letters, false_letters, easy_words, current_language,\
           medium_words, hard_words, final_word, choose_words
########################## DEUTSCH ###########################
    d_easy = open('Wortspeicher/Deutsch/[deutsch] wortspeicher - leicht.txt', 'r')
    d_medium = open('Wortspeicher/Deutsch/[deutsch] wortspeicher - mittel.txt', 'r')
    d_hard = open('Wortspeicher/Deutsch/[deutsch] wortspeicher - schwer.txt', 'r')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
######################### ENGLISCH ############################
    e_easy = open('Wortspeicher/Englisch/[englisch] wortspeicher - leicht.txt', 'r')
    e_medium = open('Wortspeicher/Englisch/[englisch] wortspeicher - mittel.txt', 'r')
    e_hard = open('Wortspeicher/Englisch/[englisch] wortspeicher - schwer.txt', 'r')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
######################### FRANZÖSISCH #########################
    f_easy = open('Wortspeicher/Französisch/[französisch] wortspeicher - leicht.txt', 'r')
    f_medium = open('Wortspeicher/Französisch/[französisch] wortspeicher - mittel.txt', 'r')
    f_hard = open('Wortspeicher/Französisch/[französisch] wortspeicher - schwer.txt', 'r')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
######################### ITALIENISCH ##########################
    i_easy = open('Wortspeicher/Italienisch/[italienisch] wortspeicher - leicht.txt', 'r')
    i_medium = open('Wortspeicher/Italienisch/[italienisch] wortspeicher - mittel.txt', 'r')
    i_hard = open('Wortspeicher/Italienisch/[italienisch] wortspeicher - schwer.txt', 'r')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

########################### LATEIN #############################
    l_easy = open('Wortspeicher/Latein/[latein] wortspeicher - leicht.txt', 'r')
    l_medium = open('Wortspeicher/Latein/[latein] wortspeicher - mittel.txt', 'r')
    l_hard = open('Wortspeicher/Latein/[latein] wortspeicher - schwer.txt', 'r')
    


    easy_word = ''
    medium_word = ''
    hard_word = ''

    if current_language == 'deutsch':
        easy = d_easy 
        medium = d_medium
        hard = d_hard
    elif current_language == 'english':
        easy = e_easy 
        medium = e_medium
        hard = e_hard
    elif current_language == 'français':
        easy = f_easy 
        medium = f_medium
        hard = f_hard
    elif current_language == 'italiano':
        easy = i_easy 
        medium = i_medium
        hard = i_hard
    elif current_language == 'latein':
        easy = l_easy 
        medium = l_medium
        hard = l_hard        
    #>>>>>>>>>>>>>>>>>>LISTEN<<<<<<<<<<<<<<<<<<<<<<
    entered_letters = []
    false_letters = ['']


    final_word = []
    # print(len(final_word))
    choose_words = ['']

    easy_words = []
    for i in easy:
        easy_word = i.upper()
#         print(i)
        easy_words.append(easy_word.replace(' ','').replace('\n',''))
        

    medium_words = []
    for e in medium:
        medium_word = e.upper()
        medium_words.append(medium_word.replace(' ','').replace('\n',''))


    hard_words = []
    for u in hard:
        hard_word = u.upper()
        hard_words.append(hard_word.replace(' ','').replace('\n',''))
#     print(easy_words)
#     print()
#     print(medium_words)
#     print()
#     print(hard_words)

    easy_word = ''
    medium_word = ''
    hard_word = ''

generate_storage()


own_word = ['']
#----------------------------------------------

#>>>>>>>>>>>>>>>>>VARIABLEN<<<<<<<<<<<<<<<<<<<<<<<<<<<
option = 0
difficulty = 0
word = ''
bedingung = True
retry = 0
value = 0
letter = ''
double_input = False
pos_counter = 0
win_counter = 0
check_win_counter = 0
check_loose_lttr_visual = False  #nur zum tracken von richtigen lttr  wenn als Modul benutzt
loose_counter = 0
tries = 11
more_tries = False # 14 tries
victory = 0
game_over = 0
#-----------------------------------------------------

#>>>>>>>>>>>>>>>>>>>>>>>>>ANLEITUNG<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def guide():
    global value
    
    while value != 1 and value != 2:
        print('Wollen Sie die Spielregeln anzeigen lassen')
        value = int(input('Ja(1), Nein(2): '))
        print()
    
    if value == 2:
        value += 0
    else:
        print('''Sie bekommen ein zufälliges, oder von jemand anderem ausgesuchtes Wort.
Jeder Buchstabe dieses Wortes wird Ihnen als _ dargestellt (z.B. Baum → _ _ _ _).
Von diesem Wort müssen Sie Stück für Stück die Buchstaben erraten, welche im Wort enthalten sind.
Wenn Sie einen Buchstaben richtigen Buchstaben gefunden haben,
wird dieser an der passenden Stelle eingesetzt(z.B. Baum: a →  _ a _ _).
Um zu gewinnen, müssen Sie alle richtigen Buchstaben erraten.
Dafür haben Sie jedoch bloß elf Versuche.
Ist ein erratener Buchstabe aber korrekt, wird Ihnen kein Versuch abgezogen.
Viel Glück 🍀''')
        print()
        print()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>RETRY<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def retry_game():
    global retry, value, letter, double_input, pos_counter, game_over,\
           win_counter, check_win_counter, loose_counter, tries, victory, more_tries,\
           option, difficulty, final_word, entered_letters, own_word, choose_words, false_letters
    
    if __name__ == '__main__':
        while retry != 1 and retry != 2:
            print('Wollen Sie nochaml spielen')
            retry = int(input('Ja(1), Nein(2): '))
            print()
            if retry != 2:
                print('Neues Wort wurde generiert')
            print()
        
    if retry == 1:
        entered_letters = []
        false_letters = ['']
        final_word = []
        
        option = 0
        difficulty = 0
        retry = 0
        value = 0
        letter = ''
        double_input = False
        pos_counter = 0
        win_counter = 0
        check_win_counter = 0
        check_loose_lttr_visual = False
        loose_counter = 0
        tries = 11
        game_over = 0
        own_word = [''] # retry: neues Wort aus derselben Liste
                         # in own_word wird aber immer nur ein einziges Wort sein
        choose_words = ['']
        
        if more_tries == True:
            tries = 14
        else:
            tries = 11
 
#>>>>>>>>>>>>>>>>>>>>>>>>WÖRTER_AUSWAHLMÖGLICHKEIT<<<<<<<<<<<<<<<<<<<<<<<
def word_option():
    global option, difficulty, choose_words, easy_words, medium_words, hard_words
    
#     print(choose_words)
    while option != 1 and option != 2:
        option = int(input('''Wollen Sie ein Wort für jemanden eingeben (1),
oder wollen Sie ein Wort aus dem Wortspeicher (2): '''))
    if option == 1:   
        own_word[0] = input('Geben Sie bitte ein Wort ein: ')
        choose_words[0] = own_word[0]
            
    else:
        print()
        print('Welchen Schwierigkeitsgrad wollen Sie auswählen: ')
        while difficulty != 1 and difficulty != 2 and difficulty != 3:
            difficulty = int(input('Leicht (1), Mittel (2), Schwer (3): '))
        
        if difficulty == 1:
            choose_words = easy_words
        elif difficulty == 2:
            choose_words = medium_words
        elif difficulty == 3:
            choose_words = hard_words
#     print(choose_words)
    print()

#>>>>>>>>>>>>>>>>>>>>>>EINGABE_VON_BUCHSTABEN<<<<<<<<<<<<<<<<<<<<<<<<<<<
def guess_letter():
    global letter, double_input, pos_counter, \
    win_counter, check_win_counter, loose_counter
    
    letter = '' # default
    while len(letter) == 0 or len(letter) > 1: # genau ein Buchstabe
        if double_input == True: 
            letter = input('Bitte geben Sie jeden Buchstaben nur einmal ein: ')
        else:
            letter = input('Bitte geben Sie einen Buchstaben ein: ')
        print()
        letter = letter.upper()
        
        check_multiple_letters()
        check_right_letter()
        
#>>>>>>>>>>>>>>>>>>PRÜFT,_OB_BUCHSTABEN_MEHRMALS_VORKOMMEN<<<<<<<<<<<<<<<<<<<        
def check_multiple_letters():
    global double_input, entered_letters, letter, false_letters, false_letters, bedingung
    
    for double_letter in entered_letters[0:len(entered_letters)]: # alle eingegebenen Buchstaben
        if double_letter == letter:
            double_input = True 
    
    if double_input != True:
        entered_letters.append(letter)
        sorted(entered_letters)
        
        
#         for x in false_letters:
#             if x == letter:
#                 bedingung = False
#             elif x != letter and bedingung: # and x == false_letters[-1]
#                 if false_letters[0] == '':
#                     false_letters.remove('')
#                 false_letters.append(letter)
#                 sorted(false_letters)
#                 bedingung = True
#                 print(f'false_letters = {false_letters}')
#     else:
#         return False
#>>>>>>>>>>>>>>>>>>PRÜFT,_OB_BUCHSTABE_IM_WORT_VORKOMMT<<<<<<<<<<<<<<<<<<
def check_right_letter():
    global choose_words, pos_counter, double_input, win_counter, false_letters,\
           final_counter, check_win_counter, loose_counter, check_loose_lttr_visual, letter
    
    for check_element in choose_words[r_value]: # DURCH RANDOM ERSTEZEN
        pos_counter += 1
        if letter == check_element:
            if double_input == True: # verhindert, dass man richtige Buchstaben mehrmals benutzen kann um win_counter zu erhöhen
                win_counter += 0    
            else:
                final_word[pos_counter -1] = letter
                win_counter += 1
                check_win_counter = 1
        if pos_counter == len(choose_words[r_value]): # DURCH RANDOM ERSETZEN
            pos_counter = 0
            
    if check_win_counter == 0:
        if double_input == True: # bei doppelten Input keinen Versuch abziehen
            loose_counter = 0
        else:
            loose_counter = 1
            check_loose_lttr_visual = True
    else:
        loose_counter = 0
        check_win_counter = 0

def set_double_input():
    global double_input
    double_input = False

def set_check_loose_lttr_visual():
    global check_loose_lttr_visual
    check_loose_lttr_visual = False
    false_letters.append(letter)
# #>>>>>>>>>>>>>>>>>>>>>>>AUSGABE_ERRATENES_WORT<<<<<<<<<<<<<<<<<<<<<<<<<<<
def underscore_letters():
    for letter_print in final_word[0:len(choose_words[r_value])]: # DURCH RANDOM ERSETZEN
        print(letter_print + ' ', end = '')
    print()
    print()
    #print(final_word)


#>>>>>>>>>>>>>>>>>>ANZEIGE_BEREITS_GERATENE_BUCHSTABEN<<<<<<<<<<<<<<<<<<<<<
def show_guessed_letters():
    global entered_letters
    
    if len(entered_letters) > 1:
        entered_letters = sorted(entered_letters)
        print('Diese Buchstaben haben Sie bereits erraten: ')
        for show_letters in entered_letters[1:]:
            print(show_letters, end = ', ')
        print()
        
#>>>>>>>>>>>>>>>>>>>>>>ANZEIGE_WIN_ODER_LOOSE<<<<<<<<<<<<<<<<<<<<<<
def win_or_loose():
    global victory, game_over
    
    print()
    if win_counter == len(choose_words[r_value]): # DURCH RANDOM ERSETZEN
        print('Gratulation, Sie haben gewonnen!')
        victory = 1
        
    else:
        print('Schade, Sie haben verloren.')
        print(f'Das gesuchte Wort war {choose_words[r_value]}.') # DURCH RANDOM ERSTZEN
        game_over = 1
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def play_game():
    
#>>>>>>>>>>>>>>>>>>>>>>>> LSITEN <<<<<<<<<<<<<<<<<<<<<<<<<<<<
    global entered_letters, final_word, choose_words, easy_words,\
           medium_words, hard_words, own_word, false_letters    
#>>>>>>>>>>>>>>>>>VARIABLEN<<<<<<<<<<<<<<<<<<<<<<<<<<<
    global option, difficulty, word, retry, value, letter, double_input, retry,\
           pos_counter, win_counter, check_win_counter, loose_counter, tries, r_value
#----------------------------------------------------- 
    
    guide()
    global r_value
    
    while retry != 2:
        word_option()
        r_value = randint(0,(len(choose_words) -1))
        for create_ in choose_words[r_value]:
            final_word.append('_')
    #     print(f'{choose_words[r_value]}   {final_word}')
    #     print(r_value)
#         print(choose_words[r_value])
        
        choose_words[r_value] = choose_words[r_value].upper()
        while win_counter != len(choose_words[r_value]) and tries >= 1: # DURCH RANDOM ERSETZEN
            print('Versuche: ' + str(tries))
            print()
            underscore_letters()
            guess_letter()
            print(more_tries)
#             print(f'false_letters = {false_letters}')
            set_double_input()
            underscore_letters()
#             print(false_letters)
            if win_counter != len(choose_words[r_value]) and tries >= 1:
                show_guessed_letters()
            #     print('Erratene Buchstaben: ' + str(win_counter))
                tries -= loose_counter
                #print('Versuche: ' + str(tries))
                print()

        win_or_loose()
        retry_game()

if __name__ == '__main__':
    play_game()


# To Do Liste:
#
# - wiederholte Eingabe verhindern ✔
#
# - bei doppelter Eingabe Versuch nicht abziehen ✔
#
# - bei doppelter Eingabe win_counter nicht erhöhen ✔
#
# - eigenes Wort eingeben können ✔
#   if Wort eingegeben liste = Wort ✔
#   else liste = word_list ✔
#
# - Auswahlmöglichkeit zwischen leicht und schwer ✔
#
# - bei eigener Worteingabe: Anzahl der Buchstaben begrenzen
#
# - (ausgewähltes Wort zufällig auswählen lassen) ✔
#
# - Wort aus Wortspeicher löschen nachdem es dran war 
#
# - Eingabe von Leerzeile/ä/ö/ü/ß verhindern
#
# - mit command "!" ganzes Wort eingeben können
#  (for Schleife checkt 1. Buchstabe; wenn ! ... ; ansonsten normal weiter machen)