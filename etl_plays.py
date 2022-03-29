def cleaning_df(file_name):
    #extract
    data_frame = pd.read_csv(file_name, error_bad_lines=False)
    
    #transform
    data_frame = data_frame.drop(columns=['city', 'utm_campaign', 'utm_source', 'utm_medium', 'genre_name', 'film_title', 'season_name', 
                           'hash_film_id', 'app_version', 'stream_type'])
    data_frame = data_frame.dropna(subset=['referrer', 'average_bitrate', 'player_name', 'os_version'])
    data_frame.browser_version = data_frame.browser_version.fillna('79.0.3945')
    data_frame.completed = data_frame.completed.fillna('False')
    data_frame.autoplay = data_frame.autoplay.fillna('False')
    data_frame.category_name = data_frame.category_name.fillna('Entertainment')
    data_frame.flash_version = data_frame.flash_version.fillna('0,0,0')
    data_frame.browser_name = data_frame.browser_name.fillna('Chrome Mobile')
    data_frame.os_name = data_frame.os_name.fillna('Android')
    
    #load
    data_frame.to_excel('sampling2clean.xlsx', index=True, index_label=False)
        #mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
    engine = sqlalchemy.create_engine("mysql+pymysql://root:281042810128Mm-@localhost/sampling1plays?charset=utf8mb4")
    comn = engine.connect()
    data_frame.to_sql('sampling_clean', if_exists='replace', con=comn)

if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    import openpyxl
    
    cleaning_df('plays.csv')