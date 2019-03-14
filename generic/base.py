import configparser

config = configparser.ConfigParser()

def get_section_data_from_ini_file(file_name, section_name):

    config.read('./testdata/'+file_name)
    return config.items(section_name)
