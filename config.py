def config():
    
    config = open("photobooth_config.txt",'r')
    config_array = config.readlines()
    VERBOSE= config_array[18].split(' ')[-1].lower().strip("\n")
    wait_time = config_array[19].split(' ')[-1].lower().strip("\n")
    run_time = config_array[20].split(' ')[-1].lower().strip("\n")
    fixed_dim = config_array[21].split(' ')[-1].lower().strip("\n")
    Hostname = config_array[22].split(' ')[-1].lower().strip("\n")
    Venue = config_array[6].split(' ')[-2].upper().strip("\n")
    return VERBOSE,int(wait_time),run_time,fixed_dim,Hostname,Venue
