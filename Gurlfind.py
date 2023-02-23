import os
import argparse

try:
    from googlesearch import search
except ImportError:
    print("Error: the 'googlesearch' module is not installed. Please install it and try again.")
    quit()

def clear_screen():
    """Clears the console screen based on OS type"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_banner():
    """Prints the banner message"""
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

def search_query(query, num_results):
    """Searches Google for the given query and returns the top 'num_results' results"""
    results = []
    for result in search(query, tld='com', lang='en', num=num_results, start=0, stop=None, pause=2.0):
        results.append(result)
    return results

def save_results(results, output_file):
    """Saves the search results to the specified output file"""
    with open(output_file, 'w') as file:
        for result in results:
            file.write(result + '\n')

def main():
    parser = argparse.ArgumentParser(description='Search Google for the given query and save the results to a file.')
    parser.add_argument('-u', '--query', type=str, required=True, help='The query to search for.')
    parser.add_argument('-o', '--output', type=str, required=True, help='The output file to save the results to.')
    parser.add_argument('-n', '--num_results', type=int, default=10, help='The number of search results to retrieve (default: 10).')
    args = parser.parse_args()

    clear_screen()
    print_banner()

    query = args.query
    num_results = args.num_results
    output_file = args.output

    results = search_query(query, num_results)
    save_results(results, output_file)

if __name__ == '__main__':
    main()
