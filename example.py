import time

from skiplagged import Skiplagged


if __name__ == '__main__':
    client = Skiplagged()
    
    bounds = (
              (38.818566, -77.447242), # Lower left lat, lng
              (38.837660, -77.434395) # Upper right lat, lng
              ) # Central park, New York City
#     bounds = client.get_bounds_for_address('Central Park, NY')
    
    while 1:
        try:
            # Log in with a Google or Pokemon Trainer Club account
        #     print client.login_with_google('GOOGLE_EMAIL', 'PASSWORD')
            print(client.login_with_pokemon_trainer('Username', 'Password'))
                        
            # Get specific Pokemon Go API endpoint
            print(client.get_specific_api_endpoint())
            
            # Get profile
            print(client.get_profile())
            
            # Find pokemon
            for pokemon in client.find_pokemon(bounds):
                print(pokemon)

            time.sleep(30)
        except Exception as e:
            print("exception:", e)
            time.sleep(1)
            
