# clear
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

def banner():
    print("\033[32;1m")
    print("""

  ________             .__   _____.__            .___
 /  _____/ __ _________|  |_/ ____\__| ____    __| _/
/   \  ___|  |  \_  __ \  |\   __\|  |/    \  / __ | 
\    \_\  \  |  /|  | \/  |_|  |  |  |   |  \/ /_/ | 
 \______  /____/ |__|  |____/__|  |__|___|  /\____ | 
        \/                                \/      \/ 

                                                                   
""")
    print("\033[33;1m MADE BY CYBERXEAL")

banner()


qu = input("Enter your query: ")

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# to search
query = qu

for j in search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0):
    print(j)