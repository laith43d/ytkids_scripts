import youtube_dl


keywords = [
    'god',
    'evil',
    'devil',
    'hell',
    'death',
    'outrageous',
    'horror',
    'chainsaw',
    'sex',
    'porn',
    'gay',
    'love',
    'lesbian',
    'tranny',
    'transgender',
    'labor',
    'miscourage',
    'punch',
    'kill',
    'killer',
    'oddities',
    'killing',
    'killed',
    'dead',
    'scar',
]

ydl_opts = {
    'ignoreerrors': True,
    'quiet': True,
    'geo_bypass': True,
    'geo_bypass_country': 'us',

}

with open("playlists.txt") as input_file:
    with open('video.json', 'a+') as output:
        for playlist in input_file:
            # print(playlist)
            print(f'playlist ({playlist}) is started!')

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:

                playlist_dict = ydl.extract_info(playlist, download=False)
                # print(playlist_dict['entries'])
                for video in playlist_dict['entries']:

                    # print(video)

                    if not video:
                        # print('ERROR: Unable to get info. Continuing...')
                        continue
                    for k in keywords:
                        if k in str(video.get('title').lower()):
                            print(video.get('id'),video.get('title'))
                            continue
                    output.write('{\n')
                    output.write(f'\tvideoID: \"{video.get("id")}\", videoTitle: \"{video.get("title")}\"\n')
                    output.write('},\n')
                print(f'playlist ({playlist}) is finished!')