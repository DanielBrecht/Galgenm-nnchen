''' hangman_visual   Vers. 3.4				
											
	PROGRAMM ABSPIELEN --> CNTR + T '''		
											

from sys import exit
from random import randint
import hangman_latest as hangm
from tkinter import Tk, Canvas, Frame, Label,\
     Entry, Button, Radiobutton, StringVar, IntVar



#Ganz unten Liste elements (sonst Elemente in Liste nicht defined)

current_language = 'deutsch'
text_storage = []
zähler = 0
loop_counter = 0
alphabet_character = False
undersc_word = ''
used_letters = ''
counter = 0
running = True
draw_counter = 0
game_over_counter = 0
vict_counter = 0
versuche = hangm.tries
valid = False
valid_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',\
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



############################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TRANSLATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################

RETTUNGSSCHWIMMER = 'RETTUNGSSCHWIMMER'

deutsch =  ["Galgenmännchen", "  Auswahl des zufälligen Wortes:", "   Schwierigkeitsgrad auswählen:", "Wortspeicher", "Eigenes Wort",\
            "LEICHT", "MITTEL", "SCHWER", "ZURÜCK","           Eigenes Wort eingeben:",\
            "MIND. 3 BUCHSTABEN\n  EINGEBEN", f"MAX. {len(RETTUNGSSCHWIMMER)} BUCHSTABEN\n  EINGEBEN",\
            "Versuche:", f"{hangm.tries}", " (NUR) EINEN \n BUCHSTABEN EINGEBEN", "Jeden Buchstaben\n nur einmal benutzen!",\
            "Bereits geratene Buchstaben:", "WEITER", "Neustart", "Beenden", "Anzahl an Siegen:", f"{vict_counter}",\
            "Anzahl an Niederlagen:", f"{game_over_counter}", " Gratulation,\n Sie haben das Wort richtig erraten!",\
            "Entwickelt von:                      Daniel Brecht  (JS1)", "Programmiersprache:           Python  (Vers. 3.7.9)",\
            "Veröffentlicht:                        XX.02.2022", "Version des Spiels:               3.4",\
            "Sprache auswählen:", "Wort aufdecken".upper(), "Anzahl an Versuchen:", "latein", "Programm beenden:",\
            "Für jede Sprache eigenen\nWortspeicher benutzen:", "Ja", "Nein",\
            "  Nur Buchstaben aus\n dem Alphabet eingeben!",\
            "Übersetzungshilfen:              Marc Wolf,\n                                              Daniel Issa\n                                          Fr. Rehn"]
# print(deutsch[37])
english = ["Hangman", "          Choose a word with:", "           Choose a difficulty:", "Word storage", "Own word",\
           "EASY", "MEDIUM", "HARD", "BACK", "                 Enter own word:",\
           "   ENTER AT LEAST 3\n  LETTERS", f" ENTER A MAX. OF {len(RETTUNGSSCHWIMMER)}\n LETTERS",\
           " TRIES:",  f"{hangm.tries}", "     ENTER (ONLY)\n    ONE LETTER", "    Use each letter\n    only once",\
           "Already used letters:", "CONTINUE", "Restart", "Quit", "Number of wins:", f"{vict_counter}",\
           "Number of losses:", f"{game_over_counter}", "  Congratulations,\n    you guessed the word correctly!",\
           "Developed by:                       Daniel Brecht (JS1)", "Programming language:       Python  (Vers. 3.7.9)",\
           "Published:                             XX.02.2022", "Game Version:                      3.4",\
           "Select a language:", "Reveal word".upper(), "Number of tries:", "latin", "Quit program",\
           "Use a separate word\nstorage for each language:", "Yes", "No",\
           "   Only enter letters\n   from the alphabet",\
           "Translation aids:                   Marc Wolf,\n                                              Daniel Issa\n                                          Fr. Rehn"]

français = []

italiano = ["Impiccato", "   Seleziona della parola a caso:", "            Scegli la difficoltà:", "Memoria di parole", "Propria parola",\
            "FACILE", "MEDIO", "DIFFICILE", "INDIETRO","         Inserisci una propria parola:",\
            "   INSERISCI ALMENO\n   3 LETTERE", f"INSERISCI UN MASSISMO\nDI {len(RETTUNGSSCHWIMMER)} LETTERE",\
            "TENTATIVI:", f"{hangm.tries}", "   BASTA INSERISCI\n   UNA LETTERA", "  Inserisci ogni lettera\n  una sola volta!",\
            "Lettere già indovinate:", "CONTINUA", "Ravvio", "Uscire", "Numero di vittorie:", f"{vict_counter}",\
            "Numero di sconfitta:", f"{game_over_counter}", " Congratulazioni,\nha indovinato la parola correttamente!",\
            "Sviluppato da:                                Daniel Brecht  (JS1)", "Linguaggio di programmazione:    Python  (Vers. 3.7.9)",\
            "Publicato:                                       XX.02.2022", "Versione del videogiocho:              3.4",\
            "Scegli la lingua:", "Rivela la parola".upper(), "Numero di tentativi:", "latino", "Uscire il programma:",\
            "Usa una memoria di parole\nseparata per ogni lingua:", "Si", "No",\
            "  Usa solo lettere\n dell'alfabeto",\
            "Aiuti alla traduzione:                     Marc Wolf\n                                                       Daniel Issa\n                                                   Fr. Rehn"]

latein = ["Mortuus homo", "        Delectus verbi fortuiti:", "       Quam difficilis est lege:", "Collectio verborum", "Verbum iniungere",\
          "FACILIS", "MODICUS", "GRAVIS", "REDIRE","           Proprium verbum iniunge:",\
          " SALTEM 3 LITTERAE\n INIUNGE", f"SUMMUM {len(RETTUNGSSCHWIMMER)}\nLITTERAE INIUNGERE",\
          "Conatus:", f"{hangm.tries}", "  SOLA UNA LITTERA\n INIUNGE", "  Omne litterae\n   semel utere!",\
          "Iam quaesivisse litterae:", "PERGERE ", "Repetere", "Desinere", "Numerus ex victoriis:", f"{vict_counter}",\
          "Numerus ex cladibus:", f"{game_over_counter}", "     Gratulatio, verbum inveniebas!",\
          "Factum a:                              Daniel Brecht  (JS1)", "Programmiersprache:           Python  (Vers. 3.7.9)",\
          "Elatum:                                  XX.02.2022", "Versio ludi:                            3.4",\
          "Lingua lege:", "Verbum expone".upper(), "Numerus ex conatibus:", "latein", "Ludus finire:",\
          "Lingua collectionem\npropriam verborum utitur:", "Sic est", "Non sic est",\
          "    Litterae ex\n    indice litterae iniunge!",\
          "Auxilium cum tradendo:        Marc Wolf,\n                                              Daniel Issa\n                                          Fr. Rehn"]

#noch keine Übersetzung für französisch
if current_language == 'deutsch' or current_language == 'français':
    for i in deutsch:
        text_storage.append(i)
elif current_language == 'english':
    for i in english:
        text_storage.append(i)
elif current_language == 'italiano':
    for i in italiano:
        text_storage.append(i)
elif current_language == 'latein':
    for i in latein:
        text_storage.append(i)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


######## DEFINITIONEN UND COMMANDS #########
def mode():
    global text_storage, zähler, current_language
    
    if rdbtn_mode.get() == 'deutsch':
        current_language = 'deutsch'
        hangm.current_language = 'deutsch'
        if seperate_word_storage.get() == 'yes':
            hangm.generate_storage()
        for i in range(39):
            text_storage[zähler] = deutsch[zähler]
            zähler += 1
        zähler = 0
    
    elif rdbtn_mode.get() == 'english':
        current_language = 'english'
        hangm.current_language = 'english'
        if seperate_word_storage.get() == 'yes':
            hangm.generate_storage()
        for i in range(39):
            text_storage[zähler] = english[zähler]
            zähler += 1
        zähler = 0
            
    elif rdbtn_mode.get() == 'français':
        current_language = 'français'
        hangm.current_language = 'français'
        if seperate_word_storage.get() == 'yes':
            hangm.generate_storage()
        print("ERROR 404 - language not available")
    
    elif rdbtn_mode.get() == 'italiano':
        current_language = 'italiano'
        hangm.current_language = 'italiano'
        if seperate_word_storage.get() == 'yes':
            hangm.generate_storage()
        for i in range(39):
            text_storage[zähler] = italiano[zähler]
            zähler += 1
        zähler = 0
        

    elif rdbtn_mode.get() == 'latein':
        current_language = 'latein'
        hangm.current_language = 'latein'
        if seperate_word_storage.get() == 'yes':
            hangm.generate_storage()
        for i in range(39):
            text_storage[zähler] = latein[zähler]
            zähler += 1
        zähler = 0
        
    
############ TEXTE UPDATEN ###########    
    Galgenmännchen.title(text_storage[0])
    
    btn_choice2.configure(text = text_storage[3])
    btn_choice1.configure(text = text_storage[4])
    leicht_btn.configure(text = text_storage[5])
    mittel_btn.configure(text = text_storage[6])
    schwer_btn.configure(text = text_storage[7])
    back_btn.configure(text = text_storage[8])
    all_letters.configure(text = text_storage[16])
    continue_btn.configure(text = text_storage[17])
    restart_btn.configure(text = text_storage[18])
    quit_btn.configure(text = text_storage[19])
    quit_btn2.configure(text = text_storage[19])
    developer_label.configure(text = text_storage[25])
    language_label.configure(text = text_storage[26])
    release_label.configure(text = text_storage[27])
    version_label.configure(text = text_storage[28])
    explain_label.configure(text = text_storage[29])
    reveal_btn.configure(text = text_storage[30])
    amount_tries_label.configure(text = text_storage[31])
    radiobtn_latein.configure(text = text_storage[32])
    quit_label.configure(text = text_storage[33])
    file_word_storage_label.configure(text = text_storage[34])
    seperate_yes_rdbtn.configure(text = text_storage[35])
    seperate_no_rdbtn.configure(text = text_storage[36])
    translation_aids.configure(text = text_storage[38])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def more_tries():
    if amount_tries.get() == 11:
        hangm.tries = 11
        hangm.more_tries = False
        text_storage[13] = f'{hangm.tries}'
    
    elif amount_tries.get() == 14:
        hangm.tries = 14
        hangm.more_tries = True
        text_storage[13] = f'{hangm.tries}'
    
    tries_label.configure(text = f'{text_storage[12]} {text_storage[13]}')
#     print(f'{text_storage[12]} {text_storage[13]}')

def storage():
    if seperate_word_storage.get() == 'yes':
        hangm.current_language = current_language
        hangm.generate_storage()
    elif seperate_word_storage.get() == 'no':
        hangm.current_language = 'deutsch'
        hangm.generate_storage()
        

def reveal_word():
    reveal_btn.configure(fg = 'red',
                         font = ('Arial 14 bold'),
                         text = hangm.choose_words[hangm.r_value])


def choice1():
    hangm.option = 1
    Galgenmännchen.configure(bg = '#FFD700')
    Gallows.configure(bg = '#FFD700')
    Choice_Rahmen.configure(bg = '#FFD700')
    explain_label.configure(bg = '#FFD700', text = text_storage[9])
    explain_label.place(x=90, y=50)
    
    while len(word_entry.get()) != 0:
        word_entry.delete(0, 'end')
    
    btn_choice1.place_forget()
    btn_choice2.place_forget()
    
    word_entry.place(x=268, y= 200)
    enter_word_btn.place(x=308, y=280)
    
    settings_btn.place_forget() 
    credits.place_forget()
    back_btn.place(x=20, y=555)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    

def choice2():
    hangm.option = 2
    Galgenmännchen.configure(bg = '#FFD700')
    Gallows.configure(bg = '#FFD700')
    Choice_Rahmen.configure(bg = '#FFD700')
    explain_label.configure(bg = '#FFD700', text = text_storage[2])
    
    btn_choice1.place_forget()
    btn_choice2.place_forget()
    
    leicht_btn.place(x=290, y=130)
    mittel_btn.place(x= 290, y=250)
    schwer_btn.place(x=290, y=370)
    
    settings_btn.place_forget() 
    credits.place_forget()
    back_btn.place(x=20, y=555)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def back():
    
    Galgenmännchen.configure(bg = '#FFB90F')
    Gallows.configure(bg = '#FFB90F')
    Choice_Rahmen.configure(bg = '#FFB90F')
    explain_label.configure(bg = '#FFB90F',
                            text = text_storage[1],
                            font = ('Arial', 24))
    explain_label.place(x=127, y=0)
    btn_choice1.place(x=270, y=295)
    btn_choice1.configure(width = 11)
    btn_choice2.place(x=270, y=155)
    btn_choice2.configure(width = 11)
    
    if rdbtn_mode.get() == 'italiano' or rdbtn_mode.get() == 'latein':
        btn_choice2.configure(width = 14)
        btn_choice2.place(x=250, y=155)
        btn_choice1.configure(width = 14)
        btn_choice1.place(x=250, y=295)
    
    settings_btn.place(x=14, y=557) 
    credits.place(x=707, y=557)
    back_btn.place_forget()
    quit_btn2.place_forget()
    
    radiobtn_german.place_forget()
    radiobtn_english.place_forget()
    radiobtn_français.place_forget()
    radiobtn_italiano.place_forget()
    radiobtn_latein.place_forget()
    
    amount_tries_label.place_forget()
    amount_11_tries_rdbtn.place_forget()
    amount_14_tries_rdbtn.place_forget()
    
    quit_label.place_forget()
    quit_btn.place_forget()
    
    file_word_storage_label.place_forget()
    seperate_yes_rdbtn.place_forget()
    seperate_no_rdbtn.place_forget()
    
    if hangm.option == 1:
        word_entry.place_forget()
        enter_word_btn.place_forget()
        word_warning.place_forget()
        
    elif hangm.option == 2:
        leicht_btn.place_forget()
        mittel_btn.place_forget()
        schwer_btn.place_forget()
    
    else:
        developer_label.place_forget()
        language_label.place_forget()
        release_label.place_forget()
        version_label.place_forget()
        translation_aids.place_forget()
    
    hangm.option = 0
        

def enter_own_word():
    global word_entry, valid, loop_counter, alphabet_character
    
    word_warning.place_forget()
    if len(word_entry.get()) > 2:
        if len(word_entry.get()) < len('RETTUNGSSCHWIMMER') +1:
            hangm.choose_words[0] = word_entry.get().upper()
        #     print(hangm.own_word[0])
        
#             if word_entry.get().isalpha() == True:
#                 valid = True
#                 for s in word_entry.get():
#                     if s == 'ö' or s == 'ä' or s == 'ü':
            
            for s in word_entry.get():
                if s not in valid_letters:
                    valid = False
      
            if valid == False:    
                word_warning.configure(text = text_storage[37])
                word_warning.place(x=235, y=340)
                            
            while len(word_entry.get()) != 0:
                word_entry.delete(0, 'end')
                
            if valid == True:
                valid = False
                hangm.r_value = randint(0,(len(hangm.choose_words) -1))
                
                for i in hangm.choose_words[hangm.r_value]:
                    hangm.final_word.append('_')
            #     print(hangm.final_word)
                update_screen()
        else:
            word_warning.configure(text = text_storage[11])
            word_warning.place(x=245, y=340)
    else:
        word_warning.configure(text = text_storage[10])
        word_warning.place(x=245, y=340)
        
    while len(word_entry.get()) != 0:    
        word_entry.delete(0, 'end')

#-------------------

def leicht():
    hangm.choose_words = hangm.easy_words
    hangm.r_value = randint(0,(len(hangm.choose_words) -1))
    
    for i in hangm.choose_words[hangm.r_value]:
        hangm.final_word.append('_')
#     print(hangm.final_word)
    update_screen()

def mittel():
    hangm.choose_words = hangm.medium_words
    hangm.r_value = randint(0,(len(hangm.choose_words) -1))
    
    for i in hangm.choose_words[hangm.r_value]:
        hangm.final_word.append('_')
#     print(hangm.final_word)
    update_screen()

def schwer():
    hangm.choose_words = hangm.hard_words
    hangm.r_value = randint(0,(len(hangm.choose_words) -1))
    
    for i in hangm.choose_words[hangm.r_value]:
        hangm.final_word.append('_')
#     print(hangm.final_word)
    update_screen()
    
#---------------------
    
def update_screen(): #Spiel beginnt
    global letter_button, undersc_word, length_word

    undersc_word = ' '.join(hangm.final_word)
    print(undersc_word)
    
    
    back_btn.place_forget()
    Choice_Rahmen.place_forget()
    if hangm.option == 1:
        word_entry.place_forget()
        enter_word_btn.place_forget()
    else:
        leicht_btn.place_forget()
        mittel_btn.place_forget()
        schwer_btn.place_forget()
    explain_label.configure(bg ='#FFB90F',
                            text = text_storage[1])
    explain_label.place(x=127, y=0)
    
    Galgenmännchen.configure(bg = '#B3EE3A')
    Gallows.configure(bg = '#B3EE3A')
    while len(letter_eingabe.get()) != 0:
        letter_eingabe.delet(0, 'end')
    
    Letter_Enter_Rahmen.place(x=10, y= 2)
    letter_eingabe.place(x=30, y=25)
    letter_button.place(x=100, y=19)
    
    output_word.configure(text = undersc_word)
    output_word.place(x= 210, y=22)
    all_letters.place(x= 150, y=550)
    
    tries_label.configure(text = f'{text_storage[12]} {text_storage[13]}')
    tries_label.place(x=20, y= 80)
    
    
    print(hangm.choose_words[hangm.r_value])
    

def enter_letter():
    global counter, used_letters, undersc_word, valid,\
           running, draw_counter, elements, galgen_elements
    
    hangm.letter = letter_eingabe.get().upper()
    while len(letter_eingabe.get()) != 0:    
        letter_eingabe.delete(0, 'end')
    tries_label.configure(text = f'{text_storage[12]} {text_storage[13]}')
#     print(text_storage[12])
#     print(hangm.tries)
    tries_label.place(x=20, y= 80)
    
    warning_label.place_forget()
#     print(hangm.letter)
    
    if len(hangm.letter) != 1:  # Eingabe nicht valid (zu viele/wenige Zeichen)
        tries_label.place_forget()
        
        warning_label.configure(text = text_storage[14],
                                font = ('Arial', 10))
        warning_label.place(x=0, y=80)
    
    else:
#         for v in valid_letters:
#             if hangm.letter == v:
#                 valid = True
        if hangm.letter.isalpha() == True:
            valid = True
            print(hangm.letter)
            for d in 'ÄÖÜ':
                if d == hangm.letter:
                    valid = False
                
        if valid == False:
            tries_label.place_forget()
            warning_label.configure(text = text_storage[37],
                                    font = ('Arial', 12))
            warning_label.place(x=0, y=80)
            valid = False
            
        elif running == True:
            
            print(len(hangm.choose_words[hangm.r_value]))
#             print(f'{5 != 5}')
            print(f'{hangm.win_counter != len(hangm.choose_words[hangm.r_value])}')
            print(f'{hangm.tries >= 1}')
            print(f'{hangm.win_counter != len(hangm.choose_words[hangm.r_value]) and hangm.tries >= 1}')
            
            hangm.check_multiple_letters()
            hangm.check_right_letter()
            
            hangm.tries -= hangm.loose_counter
            text_storage[13] = hangm.tries
            print(f'hangm.win_counter = {hangm.win_counter},\nhangm.tries = {hangm.tries}') 
            
            
            print(f'hangm.double_input = {hangm.double_input}')
            if hangm.double_input == 1:
                tries_label.place_forget()
                
                warning_label.configure(text = text_storage[15],
                                        font = ('Arial', 12))
                warning_label.place(x=0, y=80)
                hangm.set_double_input()
                print(f'hangm.double_input = {hangm.double_input}')
                
            
            if hangm.tries <= 3:
                tries_label.configure(fg = 'red')
            tries_label.configure(text = f'{text_storage[12]} {text_storage[13]}') #TEXT UPDTATEN 
            
            
            undersc_word = ' '.join(hangm.final_word)
            print(undersc_word)
                
            output_word.configure(text = undersc_word) #TEXT UPDTATEN            
            
            
            if hangm.check_loose_lttr_visual == True:#überprüft: richtiger Buchst. --> zeichnet Galgen
                hangm.set_check_loose_lttr_visual()
                draw_counter += 1
                
                       
                
                used_letters = ', '.join(hangm.false_letters)
                all_letters.configure(text = used_letters[2:]) #TEXT UPDTATEN
                
                if draw_counter >= 1:
################################### GALGEN ##############################
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GERÜST<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    try1_1 = Gallows.create_oval(150+25,450, 400+25,600,
                                               width = 0,
                                               fill = '#8B5A2B')
                    galgen_elements.append(try1_1)
                    
                    
                    try1_2 = Gallows.create_rectangle(150+25,520, 401+25,602,
                                                     width = 0,
                                                     fill = '#B3EE3A') # Label über rectangle platzieren sonst verdeckt
                    galgen_elements.append(try1_2)
                    
                    all_letters.place(x= 40, y=550)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    if draw_counter >= 2:
                        try2 = Gallows.create_rectangle(260+25,485, 290+25,80,
                                                 fill = '#8B5A2B',
                                                 width = 0)
                        galgen_elements.append(try2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                        
                        if draw_counter >= 3:
                            try3 = Gallows.create_rectangle(260+25,80, 515+25,110,
                                                     fill = '#8B5A2B',
                                                     width = 0)
                            galgen_elements.append(try3)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                            
                            if draw_counter >= 4:
                                try4 = Gallows.create_line(370+25,90, 270+25,190,
                                                    width = 30,
                                                    fill ='#8B5A2B')
                                galgen_elements.append(try4)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                
                                if draw_counter >= 5:
                                    try5 = Gallows.create_line(500+25,110, 500+25,220,
                                                        width = 6,
                                                        fill = '#B5B5B5')
                                    galgen_elements.append(try5)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
############################### PERSON ##################################                                    
#                                 ---------- KOPF ---------                                    
                                    if draw_counter >= 6 and hangm.more_tries == False:
                                        try6_1 = Gallows.create_oval(465+25,220, 535+25,290,
                                                                   width = 0,
                                                                   fill = '#FFE4C4') # '#FAEBD7'
                                        galgen_elements.append(try6_1)
                                        
                                        
                                        try6_2 = Gallows.create_line(482+25,236, 495+25,248,
                                                                     width = 4,
                                                                     fill = '#e50000')
                                        galgen_elements.append(try6_2)
                                        
                                        
                                        try6_3 = Gallows.create_line(482+25,248, 495+25,236,
                                                                     width = 4,
                                                                     fill = '#e50000')
                                        galgen_elements.append(try6_3)
                                        

                                        try6_4 = Gallows.create_line(505+25,236, 518+25,248,
                                                                     width = 4,
                                                                     fill = '#e50000')
                                        galgen_elements.append(try6_4)
                                        
                                        try6_5 = Gallows.create_line(505+25,248, 518+25,236,
                                                                     width = 4,
                                                                     fill = '#e50000')
                                        galgen_elements.append(try6_5)
                                        
                                        try6_6 = Gallows.create_line(489+25,270, 512+25,270,
                                                                     width = 4,
                                                                     fill = 'black')
                                        galgen_elements.append(try6_6)
                                        
                                    
                                    elif draw_counter >= 6 and hangm.more_tries: #wenn mehr als 11 Versuche ursprünglich
                                        try6_1 = Gallows.create_oval(465+25,220, 535+25,290,
                                                                   width = 0,
                                                                   fill = '#FFE4C4') # '#FAEBD7'
                                        galgen_elements.append(try6_1)
                                        
                                        if draw_counter >= 7:
                                            try6_2 = Gallows.create_line(482+25,236, 495+25,248,
                                                                         width = 4,
                                                                         fill = '#e50000')
                                            galgen_elements.append(try6_2)
                                        
                                        
                                            try6_3 = Gallows.create_line(482+25,248, 495+25,236,
                                                                         width = 4,
                                                                         fill = '#e50000')
                                            galgen_elements.append(try6_3)
                                            
                                            if draw_counter >= 8:
                                                try6_4 = Gallows.create_line(505+25,236, 518+25,248,
                                                                             width = 4,
                                                                             fill = '#e50000')
                                                galgen_elements.append(try6_4)
                                                
                                                try6_5 = Gallows.create_line(505+25,248, 518+25,236,
                                                                             width = 4,
                                                                             fill = '#e50000')
                                                galgen_elements.append(try6_5)
                                                
                                                if draw_counter >= 9:
                                                    try6_6 = Gallows.create_line(489+25,270, 512+25,270,
                                                                                 width = 4,
                                                                                 fill = 'black')
                                                    galgen_elements.append(try6_6)
                                                    
                                                    if draw_counter >= 10:
                                                        try7 = Gallows.create_oval(465+25,285, 535+25,395,
                                                                                   width = 0,
                                                                                   fill = '#FFE4C4')
                                                        galgen_elements.append(try7)
                                                        
                                                        if draw_counter >= 11:
                                                            try8_1 = Gallows.create_line(472+25,315, 432+25,258,
                                                                                         width = 6,
                                                                                         fill = '#FFE4C4')
                                                            galgen_elements.append(try8_1)
                                                            
                                                            try8_2 = Gallows.create_oval(424+25,250, 440+25,266,
                                                                                         width = 0,
                                                                                         fill = '#FFE4C4')
                                                            galgen_elements.append(try8_2)
                                                            
                                                            if draw_counter >= 12:
                                                                try9_1 = Gallows.create_line(528+25,315, 568+25,258,
                                                                                             width = 6,
                                                                                             fill = '#FFE4C4')
                                                                galgen_elements.append(try9_1)
                                                                try9_2 = Gallows.create_oval(560+25,250, 576+25,266,
                                                                                             width = 0,
                                                                                             fill = '#FFE4C4')
                                                                galgen_elements.append(try9_2)
                                                                
                                                                if draw_counter >= 13:
                                                                    try10_1 = Gallows.create_line(478+25,380, 458+25,455,
                                                                                                 width = 6,
                                                                                                 fill = '#FFE4C4')
                                                                    galgen_elements.append(try10_1)
                                                                    
                                                                    try10_2 = Gallows.create_oval(437+25,447, 461+25,463,
                                                                                                 width = 0,
                                                                                                 fill = '#FFE4C4')
                                                                    galgen_elements.append(try10_2)
                                                                    
                                                                    if draw_counter >= 14:
                                                                        try11_1 = Gallows.create_line(522+25,380, 542+25,455,
                                                                                                      width = 6,
                                                                                                      fill = '#FFE4C4')
                                                                        galgen_elements.append(try11_1)
                                                                        
                                                                        try11_2 = Gallows.create_oval(563+25,447, 539+25,463,
                                                                                                      width = 0,
                                                                                                      fill = '#FFE4C4')
                                                                        galgen_elements.append(try11_2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                        
            if draw_counter >= 7 and not(hangm.more_tries):
                try7 = Gallows.create_oval(465+25,285, 535+25,395,
                                          width = 0,
                                          fill = '#FFE4C4')
                galgen_elements.append(try7)              
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                         --------- ARME ---------
                if draw_counter >= 8 and not(hangm.more_tries):
                    try8_1 = Gallows.create_line(472+25,315, 432+25,258,
                                                 width = 6,
                                                 fill = '#FFE4C4')
                    galgen_elements.append(try8_1)
                    
                    try8_2 = Gallows.create_oval(424+25,250, 440+25,266,
                                                 width = 0,
                                                 fill = '#FFE4C4')
                    galgen_elements.append(try8_2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                                
                    if draw_counter >= 9 and not(hangm.more_tries):
                        try9_1 = Gallows.create_line(528+25,315, 568+25,258,
                                                   width = 6,
                                                   fill = '#FFE4C4')
                        galgen_elements.append(try9_1)
                        try9_2 = Gallows.create_oval(560+25,250, 576+25,266,
                                                     width = 0,
                                                     fill = '#FFE4C4')
                        galgen_elements.append(try9_2)
#                     ------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                             -------- BEINE --------
                        if draw_counter >= 10 and not(hangm.more_tries):
                            try10_1 = Gallows.create_line(478+25,380, 458+25,455,
                                                         width = 6,
                                                         fill = '#FFE4C4')
                            galgen_elements.append(try10_1)
                            
                            try10_2 = Gallows.create_oval(437+25,447, 461+25,463,
                                                         width = 0,
                                                         fill = '#FFE4C4')
                            galgen_elements.append(try10_2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                                        
                            if draw_counter == 11 and not(hangm.more_tries):
                                try11_1 = Gallows.create_line(522+25,380, 542+25,455,
                                                              width = 6,
                                                              fill = '#FFE4C4')
                                galgen_elements.append(try11_1)
                                
                                try11_2 = Gallows.create_oval(563+25,447, 539+25,463,
                                                              width = 0,
                                                              fill = '#FFE4C4')
                                galgen_elements.append(try11_2)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    
                    
#                 hangm.set_check_loose_lttr_visual()
                
            if hangm.win_counter == len(hangm.choose_words[hangm.r_value]) or hangm.tries <= 0:
                running = False
                print(not(hangm.win_counter != len(hangm.choose_words[hangm.r_value])))
                
                print('running = False')
                
                continue_btn.place(x=17, y=16)
            
        
        if running == False:
            print('if-Abzweigung')
            while len(letter_eingabe.get()) != 0:
                letter_eingabe.delete(0, 'end')
            hangm.win_or_loose()
            
            letter_eingabe.place_forget()
            letter_button.place_forget()
            if hangm.game_over == True:
                output_word.place_forget()
                reveal_btn.place(x= 180, y=12)
    
#     text_storage[13] = hangm.tries
            
#             if hangm.victory == True:
#                 pass 
#             elif hangm.game_over == True:
#                 Gallows.configure(bg = '#323232')
#                 
#                 for f in elements:
#                     f.place_forget()

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    print(used_letters)
    print(hangm.entered_letters)
    print()

def weiter():
    global galgen_elements, elements  ,game_over_counter, vict_counter
    
    while len(galgen_elements) != 0 or len(elements) != 0:
        for s in galgen_elements:
            Gallows.delete(s)
            galgen_elements.remove(s)
        for u in elements:
            u.place_forget()
            elements.remove(u)

            
    elements = [output_word, reveal_btn, Letter_Enter_Rahmen, tries_label, warning_label, all_letters, continue_btn]
    
    if hangm.game_over == True:
        Gallows.configure(bg = '#221e1d') #342d2c #524949
        reveal_btn.configure(fg = '#1E49A4',
                             font = ('Arial', 14))
        
        restart_btn.configure(bg = '#6c504a')
        restart_btn.place(x=285, y=330)
        quit_btn.configure(bg = '#6c504a')
        quit_btn.place(x=427, y=330)
        
        vict_loose_label.configure(text = 'GAME OVER',
                                   bg = '#221e1d',
                                   fg = '#cf290f',
                                   font = ('Arial 50 bold'))
        vict_loose_label.place(x=190, y=230)
        
        game_over_counter += 1
        text_storage[23] = f'{game_over_counter}'
        
        number_of_victs.configure(bg = '#221e1d',
                                  fg = '#eaecd9',
                                  text = f'{text_storage[20]} {text_storage[21]}')
        number_of_victs.place(x=40, y=540)
        
        number_of_losses.configure(bg = '#221e1d',
                                   fg = '#eaecd9',
                                   text = f'{text_storage[22]} {text_storage[23]}')
        number_of_losses.place(x=280, y=540)
    
    elif hangm.victory == True:
        Gallows.configure(bg = '#ffe803')
        
        restart_btn.configure(bg = '#faba75')
        restart_btn.place(x=285, y=330)
        quit_btn.configure(bg = '#faba75')
        quit_btn.place(x=427, y=330)
        
        vict_loose_label.configure(text = text_storage[24],
                                   bg = '#ffe803', #ffe803
                                   fg = '#2ddc1f',
                                   font = ('Arial 30 bold'))
        vict_loose_label.place(x=65, y=220)
        
        vict_counter += 1
        text_storage[21] = f'{vict_counter}'
        
        number_of_victs.configure(bg = '#ffe803',
                                  fg = 'black',
                                  text = f'{text_storage[20]} {text_storage[21]}')
        number_of_victs.place(x=40, y=540)
        
        number_of_losses.configure(bg = '#ffe803',
                                   fg = 'black',
                                   text = f'{text_storage[22]} {text_storage[23]}')
        number_of_losses.place(x=280, y=540)
        
    

def restart():
    global undersc_word, used_letters,\
           counter, running, draw_counter
    
    hangm.retry = 1
    hangm.retry_game()
    undersc_word = ''
    used_letters = ''
    counter = 0
    running = True
    draw_counter = 0
    
    reveal_btn.configure(text = text_storage[30])
    
    all_letters.configure(text = text_storage[16])
#     print(hangm.option)
    vict_loose_label.place_forget()
    restart_btn.place_forget()
    quit_btn.place_forget()
    number_of_victs.place_forget()
    number_of_losses.place_forget()
    
    Galgenmännchen.configure(bg = '#FFB90F')
    Gallows.configure(bg = '#FFB90F')
    Choice_Rahmen.configure(bg = '#FFB90F')#FFB90F
    Choice_Rahmen.place(x=50, y=50)
    
    btn_choice1.place(x=270, y=295)
    btn_choice2.place(x=270, y=155)
    
    settings_btn.place(x=14, y=557) 
    credits.place(x=707, y=557)
    
    tries_label.configure(fg = 'black',
                          text = f'{text_storage[12]} {text_storage[13]}')
    
    
    print(hangm.choose_words)
    print(hangm.final_word)
    
    text_storage[13] = hangm.tries
    
       
def quit_game():
    exit()
    
def settings():
    Galgenmännchen.configure(bg = '#FFD700')
    Gallows.configure(bg = '#FFD700')
    Choice_Rahmen.configure(bg = '#FFD700')
    explain_label.configure(bg = '#FFD700',
                            text = text_storage[29],
                            font = ('Arial 24 underline'))
    explain_label.place(x=0, y=0)
    reveal_btn.configure(text = text_storage[30]) #text_storage[30]
    
    radiobtn_german.place(x=0, y=50)
    radiobtn_english.place(x=0, y=100)
    radiobtn_français.place(x=0, y=150)
    radiobtn_italiano.place(x=0, y=200)
    radiobtn_latein.place(x=0, y=250)
    
    amount_tries_label.place(x=0, y=320)
    amount_11_tries_rdbtn.place(x=0, y=380)
    amount_14_tries_rdbtn.place(x=100, y=380)
    
    quit_label.place(x=360, y=320)
    quit_btn2.place(x=360, y=390)
    
    file_word_storage_label.place(x=360, y=0)
    seperate_yes_rdbtn.place(x=370, y=100)
    seperate_no_rdbtn.place(x=490, y=100)

    btn_choice1.place_forget()
    btn_choice2.place_forget()
    
    settings_btn.place_forget() 
    credits.place_forget()
    back_btn.place(x=20, y=555)
    
def show_credits():
    Galgenmännchen.configure(bg = '#FFD700')
    Gallows.configure(bg = '#FFD700')
    Choice_Rahmen.configure(bg = '#FFD700')
    
    explain_label.place_forget()
    btn_choice1.place_forget()
    btn_choice2.place_forget()
    
    settings_btn.place_forget() 
    credits.place_forget()
    back_btn.place(x=20, y=555)
    
    developer_label.place(x=20, y=40)
    release_label.place(x=20, y=100)
    version_label.place(x=20, y=160)
    language_label.place(x=20, y=220)
    translation_aids.place(x=20, y=280)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    


############ HAUPTFENSTER #############
Galgenmännchen = Tk()
Galgenmännchen.title(text_storage[0])
Galgenmännchen.geometry('800x600')
Galgenmännchen.configure(bg = '#FFB90F') #B3EE3A
Galgenmännchen.resizable(width = False, height = False)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

rdbtn_mode = StringVar()   #'deutsch' # 'englisch'
rdbtn_mode.set('deutsch')

amount_tries = IntVar()
amount_tries.set(11)

seperate_word_storage = StringVar()
seperate_word_storage.set('yes')

############### CANVAS ################
Gallows = Canvas(Galgenmännchen,
                         width = 802,
                         height = 602,
                         bg = '#FFB90F') #B3EE3A
Gallows.place(x=-2, y=-2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

########## FRAME IN CANVAS ############
Choice_Rahmen = Frame(master = Galgenmännchen,
                              bg = '#FFB90F',
                              width = 800,
                              height = 500)
Choice_Rahmen.place(x=50, y=50)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

####### 1.HÄLFTE - VOR DEM RATEN ########

#+++++++++++++ LABEL - ERKLÄRUNG ++++++++++++++
explain_label = Label(Choice_Rahmen,
                              bg = '#FFB90F', 
                              font = ('Arial', 24),
                              text = text_storage[1])
explain_label.place(x=127, y=0)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#+++++++++++++ BUTTON AUSWAHL +++++++++++++++
btn_choice1 = Button(Choice_Rahmen,
                             bg = '#EED5B7',
                             width = 11,
                             text = text_storage[4],
                             command = choice1)
btn_choice1.configure(font = ('Arial', 18))
btn_choice1.place(x=270, y=295)

btn_choice2 = Button(Choice_Rahmen,
                             bg = '#EED5B7',
                             width = 11,
                             text = text_storage[3],
                             font = ('Arial', 18),
                             command = choice2)
# btn_choice2.configure(font = ('Arial', 18))
btn_choice2.place(x=270, y=155)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

back_btn = Button(Gallows,
                          bg = '#EED5B7', #e8e89d #dae89d #e8cc9d
                          font = ('Arial', 12),
                          text = text_storage[8],
                          command = back)

#++++++++++++++++ 1.EIGENES WORT +++++++++++++++++++
word_entry = Entry(Choice_Rahmen,
                           width = 10,
                           bg = '#FFE7BA',#cde150 #FFE7BA
                           font = ('Arial', 22)) # x=228, y=200

enter_word_btn = Button(Choice_Rahmen,
                                bg = '#EED5B7', #e8cc9d #f8ff23 #e2bc22 #f0b840 #fecaa3
                                text = 'ENTER',
                                font = ('Arial', 15),
                                command = enter_own_word) # x=298, y=280
word_warning = Label(Choice_Rahmen,
                             bg = '#FFD700',
                             fg = '#6800c0', #red
                             text = text_storage[10],
                             font = ('Arial', 14))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#++++++++++++++ 2.WORTSPEICHER AUSWHAL ++++++++++++++
leicht_btn = Button(Choice_Rahmen,
                            text = text_storage[5],
                            width = 8,
                            bg = '#EED5B7',
                            font = ('Arial', 18),
                            command = leicht)  # x=260, y=130

mittel_btn = Button(Choice_Rahmen,
                            text = text_storage[6],
                            width = 8,
                            bg = '#EED5B7',
                            font = ('Arial', 18),
                            command = mittel)  # x= 260, y=250

schwer_btn = Button(Choice_Rahmen,
                            text = text_storage[7],
                            width = 8,
                            bg = '#EED5B7',
                            font = ('Arial', 18),
                            command = schwer)  # x=260, y=370
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

######### FRAME 2. HÄLFTE DES GAMES ##########
Letter_Enter_Rahmen = Frame(master = Galgenmännchen,
                       bg = '#B3EE3A', 
                       width = 800,
                       height = 75)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

############ BUCHSTABENEINGABE ##############
letter_eingabe = Entry(Letter_Enter_Rahmen,
                               bg = '#EEE8CD',  #FFFFE0
                               font = ('Arial'),
                               width = 3)

letter_button = Button(Letter_Enter_Rahmen,
                               text = 'ENTER',
                               bg = '#EEDD82',
                               font = ('Arial', 14),
                               command = enter_letter)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

############## AUSGABE WORT etc. ################
output_word = Label(Letter_Enter_Rahmen,
                            width = 29, # len(gewähltes Wort)
                            bg = '#B3EE3A',
                            fg = '#1E49A4',
                            font = ('Arial', 14))

reveal_btn = Button(Letter_Enter_Rahmen,
                            width = 24,
                            text = text_storage[30],
                            bg = '#B3EE3A',#B3EE3A
                            fg = '#1E49A4',
                            font = ('Arial', 14),
                            command = reveal_word)


all_letters = Label(Gallows,
                            bg = '#B3EE3A',
                            width = 45,
                            text = text_storage[16],
                            font = ('Arial', 14))

warning_label = Label(Gallows,
                              bg = '#B3EE3A',
                              fg = 'red',
                              text = text_storage[14],
                              font = ('Arial', 10)) # x=0, y=80

tries_label = Label(Gallows,
                            bg = '#B3EE3A',
                            text = f'{text_storage[12]} {text_storage[13]}',
                            font = ('Arial', 15))

continue_btn = Button(Letter_Enter_Rahmen,
                              bg = '#EEDD82',
                              text = text_storage[17],
                              font = ('Arial', 14),
                              command = weiter)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vict_loose_label = Label(Gallows,
                                 bg = '#221e1d',
                                 fg = '#cf290f',
                                 font = ('Arial 50 bold'))
number_of_victs = Label(Gallows,
                                bg = '#ffe803',
                                text = f'{text_storage[20]} {text_storage[21]}',
                                font = ('Ariral', 14))

number_of_losses = Label(Gallows,
                                 bg = '#221e1d',
                                 text = f'{text_storage[22]} {text_storage[23]}',
                                 font = ('Ariral', 14))

restart_btn = Button(Gallows,
                             bg = '#6c504a',
                             font = ('Arial', 14),
                             text = text_storage[18],
                             width = 8,
                             command = restart)

quit_btn = Button(Gallows,
                          bg = '#6c504a',
                          font = ('Arial', 14),
                          text = text_storage[19],
                          width = 8,
                          command = quit_game)
#~~~~~~~~~~~~~~~~ EINSTELLUNGEN ~~~~~~~~~~~~~~~~~~
settings_btn = Button(Gallows,
                              bg = '#EED5B7',
                             font = ('Arial', 12),
                             text = 'SETTINGS',
                             command = settings)
settings_btn.place(x=14, y=557)

radiobtn_german = Radiobutton(Choice_Rahmen,
                                      text='deutsch',
                                      anchor='w',
                                      value= 'deutsch',
                                      variable = rdbtn_mode,
                                      bg = '#FFD700',
                                      font = ('Arial', 15),
                                      command = mode)

radiobtn_english = Radiobutton(Choice_Rahmen,
                                       text = 'english',
                                       anchor = 'w',
                                       value = 'english',
                                       variable = rdbtn_mode,
                                       bg = '#FFD700',
                                       font = ('Arial', 15),
                                       command = mode)

radiobtn_français = Radiobutton(Choice_Rahmen,
                                        text = 'français',
                                        anchor = 'w',
                                        value = 'français',
                                        variable = rdbtn_mode,
                                        bg = '#FFD700',
                                        font = ('Arial', 15),
                                        command = mode)

radiobtn_italiano = Radiobutton(Choice_Rahmen,
                                        text = 'italiano',
                                        anchor = 'w',
                                        value = 'italiano',
                                        variable = rdbtn_mode,
                                        bg = '#FFD700',
                                        font = ('Arial', 15),
                                        command = mode)

radiobtn_latein = Radiobutton(Choice_Rahmen,
                                      text = text_storage[32],
                                      anchor = 'w',
                                      value = 'latein',
                                      variable = rdbtn_mode,
                                      bg = '#FFD700',
                                      font = ('Arial', 15),
                                      command = mode)


amount_tries_label = Label(Choice_Rahmen,
                                   bg = '#FFD700',
                                   text = text_storage[31],
                                   font = ('Arial 24 underline'))
                                   

amount_11_tries_rdbtn = Radiobutton(Choice_Rahmen,
                                            text = '11',
                                            anchor = 'w',
                                            value = 11,
                                            variable = amount_tries,
                                            bg = '#FFD700',
                                            font = ('Arial', 18),
                                            command = more_tries)

amount_14_tries_rdbtn = Radiobutton(Choice_Rahmen,
                                            text = '14',
                                            anchor = 'w',
                                            value = 14,
                                            variable = amount_tries,
                                            bg = '#FFD700',
                                            font = ('Arial', 18),
                                            command = more_tries)

quit_label = Label(Choice_Rahmen,
                           bg = '#FFD700',
                           text = text_storage[33],
                           font = ('Arial 24 underline'))
quit_btn2 = Button(Choice_Rahmen,
                           bg = '#EED5B7',
                           font = ('Arial', 14),
                           text = text_storage[19],
                           width = 8,
                           command = quit_game)

file_word_storage_label = Label(Choice_Rahmen,
                                        bg = '#FFD700',
                                        text = text_storage[34],
                                        font = ('Arial 24 underline'))
seperate_yes_rdbtn = Radiobutton(Choice_Rahmen,
                                         text = text_storage[35],
                                         anchor = 'w',
                                         value = 'yes',
                                         variable = seperate_word_storage,
                                         bg = '#FFD700',
                                         font = ('Arial', 18),
                                         command = storage)

seperate_no_rdbtn = Radiobutton(Choice_Rahmen,
                                        text = text_storage[36],
                                        anchor = 'w',
                                        value = 'no',
                                        variable = seperate_word_storage,
                                        bg = '#FFD700',
                                        font = ('Arial', 18),
                                        command = storage)
#~~~~~~~~~~~~~~~~~ CREDITS ~~~~~~~~~~~~~~~~~~~~~
credits = Button(Gallows,
                         bg = '#EED5B7',
                         font = ('Arial', 12),
                         text = 'CREDITS',
                         command = show_credits)
credits.place(x=707, y=557)

developer_label = Label(Choice_Rahmen,
                                bg = '#FFD700',
                                text = text_storage[25],
                                font = ('Arial', 22))

language_label = Label(Choice_Rahmen,
                               bg = '#FFD700',
                               text = text_storage[26],
                               font = ('Arial', 22))

release_label = Label(Choice_Rahmen,
                              bg = '#FFD700',
                              text = text_storage[27],
                              font = ('Arial', 22))

version_label = Label(Choice_Rahmen,
                              bg = '#FFD700',
                              text = text_storage[28],
                              font = ('Arial', 22))

translation_aids = Label(Choice_Rahmen,
                              bg = '#FFD700',
                              text = text_storage[38],
                              font = ('Arial', 22))

galgen_elements = []
elements = [output_word, reveal_btn, Letter_Enter_Rahmen, tries_label, warning_label, all_letters, continue_btn]





Galgenmännchen.mainloop()
