import pathlib
import json
import sys
import os

file_path = sys.argv[1]
#file_path = '/home/songhu/todo/s_6038'
path = pathlib.Path(file_path)
file_list = path.glob('**/entry.json')
ffmpeg_cmd_list= 'ffmpeg_cmd_list'
if __name__ == '__main__':
    with open(ffmpeg_cmd_list, 'a+') as file:
        file.truncate(0)
    for item in file_list:
        with open(item, encoding='utf-8', mode='r') as f:
            jdata = json.load(f)
            title = jdata['title'].replace('/', '')
            video_quality = str(jdata['video_quality'])
            quality_pithy_description = jdata['quality_pithy_description']
            ep_index = jdata['ep']['index']
            ep_index_title = jdata['ep']['index_title']
            ep_bvid = jdata['ep']['bvid']
            media_file_path = os.path.dirname(item)
            audio_file = media_file_path+'/'+video_quality+'/'+'audio.m4s'
            video_file = media_file_path+'/'+video_quality+'/'+'video.m4s'
            with open(ffmpeg_cmd_list, encoding='utf-8', mode='a+') as fp:
                print('sudo docker run -it --rm --name ffmpeg -v `pwd`:/config -w /config harbor.hosts.songhu.wang:8443/apps/linuxserver/ffmpeg:amd64-version-6.0-cli_v2023-08-09 -i %s -i %s -vcodec copy -acodec copy "[%s.][%s][%s·%s][%s].mkv"' % (audio_file, video_file, ep_index, ep_bvid, title, ep_index_title, quality_pithy_description), file=fp)
