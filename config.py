def config():
    config = open("Slideshow_Config.txt",'r')
    config_array = config.readlines()
    VERBOSE= config_array[4].split(' ')[-1].lower().strip("\n")
    wait_time = config_array[5].split(' ')[-1].lower().strip("\n")
    run_time = config_array[6].split(' ')[-1].lower().strip("\n")
    fixed_dim = config_array[7].split(' ')[-1].lower().strip("\n")
    Hostname = config_array[8].split(' ')[-1].lower().strip("\n")
    name_code = config_array[9].split(' ')[-3].upper().strip("\n")
    return VERBOSE,wait_time,run_time,fixed_dim,Hostname,name_code
