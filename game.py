from fighter import character, jedi, wizard, ninja, kitty

###################################### AVAILABLE CHARACTERS SETUP #
# JEDIS #
yoda = jedi("Yoda")
ren = jedi("Ren")
vader = jedi("Darth Vader")
luke = jedi("Luke")

# WIZARDS #
hermione = wizard("Hermione")
harry = wizard("Harry")
tonks = wizard("Tonks")

# NINJAS #
george = ninja("George")
cody = ninja("Cody")
bryanna = ninja("Bryanna")

# EASTER EGG #
nick = kitty()

###################################################### GAME SETUP #
game_over = False
round_count = 1
char_select = ""
characters = [yoda, ren, luke, hermione, harry, tonks, george, cody, bryanna]
player = yoda
enemy = vader
winner = False

###################################################### GAME INTRO #
print("""
WELCOME TO 
 ______   _______ _________ _______    _______ _________ _______          _________ _______  _______ 
(  __  \ (  ___  )\__    _/(  ___  )  (  ____ \\__   __/(  ____ \|\     /|\__   __/(  ____ \(  ____ )
| (  \  )| (   ) |   )  (  | (   ) |  | (    \/   ) (   | (    \/| )   ( |   ) (   | (    \/| (    )|
| |   ) || |   | |   |  |  | |   | |  | (__       | |   | |      | (___) |   | |   | (__    | (____)|
| |   | || |   | |   |  |  | |   | |  |  __)      | |   | | ____ |  ___  |   | |   |  __)   |     __)
| |   ) || |   | |   |  |  | |   | |  | (         | |   | | \_  )| (   ) |   | |   | (      | (\ (   
| (__/  )| (___) ||\_)  )  | (___) |  | )      ___) (___| (___) || )   ( |   | |   | (____/\| ) \ \__
(______/ (_______)(____/   (_______)  |/       \_______/(_______)|/     \|   )_(   (_______/|/   \__/
                                                                                                     

follow the promts to play, or type "help" for help.

Choose your fighter:
    1) Yoda the Jedi
    2) Ren the Jedi
    3) Luke the Jedi
    4) Hermione the Wizard
    5) Harry the Wizard
    6) Tonks the Wizard
    7) George the Ninja
    8) Cody the Ninja
    9) Bryanna the Ninja
""")

# CHARACTER SELECT #
character_selected = False

while(not character_selected):
    char_select = input()
    if(char_select=="help"):
        print("""
        You can choose between Jedi, Wizard or Ninja Characters:

            JEDI: 
                Has low health and high damage. 
                Once per fight they can use their special to do MEGA DAMAGE

            WIZARD: 
                Has average health and average damage. 
                They can use their special to deal a low amount of damage and heal themselves.

            NINJA: 
                Has high health and low damage.  
                They can use their special to buff their future attacks
        """)
        continue
    if(char_select == "1337"):
        player = nick
        break
    # Check to see if input is a number
    if(char_select.isdigit()):
        int_char = int(char_select) 
        # Check to see if valid option
        if(int_char >=1 and int_char <= 9):
            player = characters[int_char-1]
            print(f"You selected {player.name}")
            character_selected = True
            break
    print("Please enter a value between 1 and 9")


print(f"You({player.name}) are fighting ({enemy.name})")


####################################################### GAME LOOP #
while(not game_over):
    action = ""
    print(f"""
    
~~~~~~~~~ Round {round_count} BEGIN! ~~~~~~~~~
    
    """)
    # Player chooses action
    print(f"What does {player.name} want to do?")
    while(action != "1" and action != "2"):
        print("""
            1: Attack!
            2: Use Special
        """)
        action = input()
    if(action == "1"):
        player.attack(enemy)
    else:
        player.special(enemy)
    # Enemy attacks and display round info
    enemy.attack(player)
    print()
    player.info()
    enemy.info()

    round_count+=1
    # Check to see if either player in knocked out
    if(player.health<=0 or enemy.health <= 0):
        game_over = True
        if(player.health<=0):
            winner = False
        else:
            winner = True
        break

####################################################### GAME OVER #
if(winner):
    if(char_select != "1337"):
        print("""
   ____     __   ,-----.      ___    _         .--.      .--..-./`) ,---.   .--. 
   \   \   /  /.'  .-,  '.  .'   |  | |        |  |_     |  |\ .-.')|    \  |  | 
    \  _. /  '/ ,-.|  \ _ \ |   .'  | |        | _( )_   |  |/ `-' \|  ,  \ |  | 
     _( )_ .';  \  '_ /  | :.'  '_  | |        |(_ o _)  |  | `-'`"`|  |\_ \|  | 
 ___(_ o _)' |  _`,/ \ _/  |'   ( \.-.|        | (_,_) \ |  | .---. |  _( )_\  | 
|   |(_,_)'  : (  '\_/ \   ;' (`. _` /|        |  |/    \|  | |   | | (_ o _)  | 
|   `-'  /    \ `"/  \  ) / | (_ (_) _)        |  '  /\  `  | |   | |  (_,_)\  | 
 \      /      '. \_/``".'   \ /  . \ /        |    /  \    | |   | |  |    |  | 
  `-..-'         '-----'      ``-'`-''         `---'    `---` '---' '--'    '--' """)
    else:
        print("""
       \`*-.                    
        )  _`-.                 
       .  : `. .                
       : _   '  \               
       ; *` _.   `*-._          
       `-.-'          `-.       
         ;       `       `.     
         :.       .        \    
         . \  .   :   .-'   .   
         '  `+.;  ;  '      :   
         :  '  |    ;       ;-. 
         ; '   : :`-:     _.`* ;
      .*' /  .*' ; .*`- +'  `*' 
      `*-*   `*-*  `*-*'
______ _   ___________________ _____ _____ _____ _____ _____ _   _ _ 
| ___ \ | | | ___ \ ___ \  ___|  ___/  __ \_   _|_   _|  _  | \ | | |
| |_/ / | | | |_/ / |_/ / |_  | |__ | /  \/ | |   | | | | | |  \| | |
|  __/| | | |    /|    /|  _| |  __|| |     | |   | | | | | | . ` | |
| |   | |_| | |\ \| |\ \| |   | |___| \__/\ | |  _| |_\ \_/ / |\  |_|
\_|    \___/\_| \_\_| \_\_|   \____/ \____/ \_/  \___/ \___/\_| \_(_)
                                
        """)
else:
    print("""          .-.
                      |_:_|
                     /(_Y_)\\
.                   ( \/M\/ )
 '.               _.'-/'-'\-'._
   ':           _/.--'[[[[]'--.\_
     ':        /_'  : |::"| :  '.\\
       ':     //   ./ |oUU| \.'  :\\
         ':  _:'..' \_|___|_/ :   :\\
           ':.  .'  |_[___]_|  :.': |
            [::\ |  :  | |  :   ; : |
             '-'   \/'.| |.' \  .;.' |
             |\_    \  '-'   :       |
             |  \    \ .:    :   |   |
             |   \    | '.   :    \  |
             /       \   :. .;       |
            /     |   |  :__/     :  \\
           |  |   |    \:   | \   |   ||
          /    \  : :  |:   /  |__|   /|
         |     : : :_/_|  /'._\  '--|_
          /___.-/_|-'   \  
                         '-'
 (        (      (  `          ( /(               )\ )  
 )\ )     )\     )\))(   (     )\()) (   (   (   (()/(  
(()/(  ((((_)(  ((_)()\  )\   ((_)\  )\  )\  )\   /(_)) 
 /(_))_ )\ _ )\ (_()((_)((_)    ((_)((_)((_)((_) (_))   
(_)) __|(_)_\(_)|  \/  || __|  / _ \\\ \ / / | __|| _ \  
  | (_ | / _ \  | |\/| || _|  | (_) |\ V /  | _| |   /  
   \___|/_/ \_\ |_|  |_||___|  \___/  \_/   |___||_|_\   """)