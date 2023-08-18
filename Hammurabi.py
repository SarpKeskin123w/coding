def print_intro():
    intro_message = """Congrats, you are the newest ruler of ancient Samaria, elected for a ten year term
    of office. Your duties are to distribute food, direct farming, and buy and sell land
    as needed to support your people. Watch out for rat infestations and the resultant
    plague! Grain is the general currency, measured in bushels. The following will help
    you in your decisions:
    (a) Each person needs at least 20 bushels of grain per year to survive.
    (b) Each person can farm at most 10 acres of land.
    (c) It takes 2 bushels of grain to farm an acre of land.
    (d) The market price for land fluctuates yearly.
    Rule wisely and you will be showered with appreciation at the end of your term. Rule
    poorly and you will be kicked out of office!"""
    print(intro_message)

def ask_to_buy_land(bushels, cost):
    """
    Ask user how many bushels to spend buying land.
    """
    acres = int(input("How many acres will you buy? "))
    while acres * cost > bushels:
        print("O great Hammurabi, we have but", bushels, "bushels of grain!")
        acres = int(input("How many acres will you buy? "))
    return acres

def ask_to_sell_land(acres):
    """
    Ask user how much land they want to sell.
    """
    acres_to_sell = int(input("How many acres will you sell? "))
    while acres_to_sell > acres:
        print("O great Hammurabi, we have only", acres, "acres of land!")
        acres_to_sell = int(input("How many acres will you sell? "))
    return acres_to_sell

def ask_to_feed(bushels):
    """
    Ask user how many bushels they want to use for feeding.
    """
    bushels_to_feed = int(input("How many bushels will you use for feeding? "))
    while bushels_to_feed > bushels:
        print("O great Hammurabi, we have but", bushels, "bushels of grain!")
        bushels_to_feed = int(input("How many bushels will you use for feeding? "))
    return bushels_to_feed

def ask_to_cultivate(acres, population, bushels):
    """
    Ask user how much land they want to plant seed in.
    """
    acres_to_cultivate = int(input("How many acres will you plant with seed? "))
    while acres_to_cultivate > acres or acres_to_cultivate > (population * 10) or (acres_to_cultivate * 2) > bushels:
        print("O great Hammurabi, we have limitations!")
        if acres_to_cultivate > acres:
            print("We have only", acres, "acres of land!")
        elif acres_to_cultivate > (population * 10):
            print("Each person can farm at most 10 acres of land!")
        elif (acres_to_cultivate * 2) > bushels:
            print("We have but", bushels, "bushels of grain!")
        acres_to_cultivate = int(input("How many acres will you plant with seed? "))
    return acres_to_cultivate
import random

def plague():
    
    return random.random() < 0.15

def num_starving(population, bushels):

    num_starved = max(0, population * 0.45 - bushels / 20)
    return int(num_starved)

def num_immigrants(land, bushels, population, num_starved):

    if num_starved > 0:
        return 0
    else:
        num_immigrants = (20 * land + bushels) // ((100 * population) + 1)
        return int(num_immigrants)

def get_harvest(acres_to_cultivate):

    return acres_to_cultivate * random.randint(1, 8)

def do_rats_infest():

    return random.random() < 0.4

def percent_destroyed():
    return random.uniform(0.1, 0.3)

def price_of_land():

    return random.randint(16, 22)

def Hammurabi():
    starved = 0
    immigrants = 5
    population = 100
    harvest = 3000  # total bushels harvested
    bushels_per_acre = 3  # amount harvested for each acre planted
    rats_ate = 200  # bushels destroyed by rats
    bushels_in_storage = 2800
    acres_owned = 1000
    cost_per_acre = 19  # each acre costs this many bushels
    plague_deaths = 0

    print_intro()

    for year in range(1, 11):
        print("O great Hammurabi!")
        print(year)
        print("You are in year", year, "of your ten-year rule.")
        print("In the previous year", starved, "people starved to death.")
        print("In the previous year", immigrants, "people entered the kingdom.")
        print("The population is now", population, ".")
        print("We harvested", harvest, "bushels at", bushels_per_acre, "bushels per acre.")
        print("Rats destroyed", rats_ate, "bushels, leaving", bushels_in_storage, "bushels in storage.")
        print("The city owns", acres_owned, "acres of land.")
        print("Land is currently worth", cost_per_acre, "bushels per acre.")
        print("There were", plague_deaths, "deaths from the plague.")

        acres_to_buy = ask_to_buy_land(bushels_in_storage, cost_per_acre)
        acres_owned += acres_to_buy
        bushels_in_storage -= acres_to_buy * cost_per_acre

        if acres_to_buy == 0:
            acres_to_sell = ask_to_sell_land(acres_owned)
            acres_owned -= acres_to_sell
            bushels_in_storage += acres_to_sell * cost_per_acre

        bushels_to_feed = ask_to_feed(bushels_in_storage)
        bushels_in_storage -= bushels_to_feed

        population -= num_starving(population, bushels_to_feed)

        acres_to_cultivate = ask_to_cultivate(acres_owned, population, bushels_in_storage)
        bushels_in_storage -= acres_to_cultivate * 2

        if plague():
            plague_deaths = int(population / 2)
            population -= plague_deaths
        else:
            plague_deaths = 0

        starved = num_starving(population, bushels_to_feed)
        if starved > population * 0.45:
            print("O great Hammurabi, you have been overthrown! Game over.")
            break

        immigrants = num_immigrants(acres_owned, bushels_in_storage, population, starved)
        population += immigrants
        harvest = get_harvest(acres_to_cultivate)
        if do_rats_infest():
            rats_ate = int(harvest * percent_destroyed())
            bushels_in_storage -= rats_ate
        else:
            rats_ate = 0

        bushels_in_storage += harvest - rats_ate
        cost_per_acre = price_of_land()

    # Final summary
    print("\n--- Final Summary ---")
    print("Total population:", population)
    print("Total acres owned:", acres_owned)
    print("Total bushels in storage:", bushels_in_storage)

    if starved > population * 0.45:
        print("\nYou have been overthrown! Your rule was a disaster.")
    else:
        if acres_owned >= 1000 and population >= 100 and bushels_in_storage >= 200:
            print("\nCongratulations, great Hammurabi!")
            print("You have successfully ruled the kingdom for ten years.")
            print("Your people are happy and prosperous.")
        else:
            print("\nYour rule was average, but there is room for improvement.")

Hammurabi()
