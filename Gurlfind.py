import argparse
import os

try:
    from googlesearch import search
except ImportError:
    print("Error: the 'googlesearch' module is not installed. Please install it and try again.")
    quit()

# Define the command-line arguments
parser = argparse.ArgumentParser(description='Google search script')
parser.add_argument('-q', '--query', type=str, required=True, help='The search query')
parser.add_argument('-o', '--output', type=str, required=True, help='The output file name')

args = parser.parse_args()

# clear the console screen
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

# Get the search query from the command-line argument
query = args.query

# Open the output file for writing
with open(args.output, 'w') as f:
    # Perform the search and write the results to the output file
    for j in search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0):
        f.write(j + '\n')
        print(j)

print(f"Results saved to {args.output}")
