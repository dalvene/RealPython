"""
This is an assignment from RealPython fundamentals, titled 'Cats with hats'. 
"""

def create_dict():
    # Create a dictionary object of 100 key:value pairs.
    # Set keys as sequential integers and all values as False.
    return {n:False for n in range(1,101)}

def hat_swap(hat_status:dict):
    # Loop 100 times. Each time, check every key to see if the loop number is a factor.
    # If it is then swap the cat's hat status.
    for n in range(1,101):
        for key in hat_status.keys():
            if key % n == 0:
                if hat_status[key] == False:
                    hat_status[key] = True
                else:
                    hat_status[key] = False
    return hat_status

def print_hats(hat_status:dict):
    # Print out a list of cats that have a hat at the end.
    for n in range(1, 101):
        if hat_status[n]:
            print(f"Cat {n} has a hat")

def main():
    empty_dict = create_dict()
    hat_status = hat_swap(empty_dict)
    print_hats(hat_status)

if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print(f"runtime: --- {round(time.time() - start_time,2)}s seconds ---")
