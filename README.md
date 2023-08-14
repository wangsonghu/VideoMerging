# VideoMerging

## 简介

用以合并下载的视频

## `bilibili`
### 用到的镜像和材料

+ harbor.hosts.songhu.wang:8443/apps/python:alpine3.18_v2023-08-09
+ harbor.hosts.songhu.wang:8443/apps/linuxserver/ffmpeg:amd64-version-6.0-cli_v2023-08-09
+ 生成ffmpeg合成命令的脚本：番剧：`parse_file_name.py`；up上传的合集：`parse_file_name_page.py`
+ bilibili下载的视频：

    ```
    s_6038/
    ├── 103591
    │   ├── 80
    │   │   ├── audio.m4s
    │   │   ├── index.json
    │   │   └── video.m4s
    │   ├── danmaku.xml
    │   └── entry.json
    ├── 289640
    │   ├── 112
    │   │   ├── audio.m4s
    │   │   ├── index.json
    │   │   └── video.m4s
    │   ├── danmaku.xml
    │   └── entry.json
    ```

### 使用方法
0. 将bilibili下载的视频文件拷贝到工作目录
具体可以参考[bilibili缓存视频目录](https://gitea.hosts.songhu.wang/songhu.wang/Vedio-Download/src/branch/main/BiliBili%E8%A7%86%E9%A2%91)

1. 生成ffmpeg命令

如果是番剧使用：

```
sudo docker run -it --rm --name parse_file_name -v .:/work -w /work harbor.hosts.songhu.wang:8443/apps/python:alpine3.18_v2023-08-09 python parse_file_name.py .
```

如果是up上传的合集，则使用:

```
sudo docker run -it --rm --name parse_file_name -v .:/work -w /work harbor.hosts.songhu.wang:8443/apps/python:alpine3.18_v2023-08-09 python parse_file_name_page.py .
```

> 生成的命令在`ffmpeg_cmd_list`

2. 执行生成ffmpeg视频合并命令

```
sudo docker run -it --rm --name ffmpeg -v .:/config -w /config harbor.hosts.songhu.wang:8443/apps/linuxserver/ffmpeg:amd64-version-6.0-cli_v2023-08-09 -i s_6038/103591/80/audio.m4s -i s_6038/103591/80/video.m4s -vcodec copy -acodec copy "[1.][BV1wx411Q7kh][风灵玉秀·夜探][1080P].mkv"
```


> 如果文件很多，可以
```
bash ffmpeg_cmd_list
```

## 腾讯视频

[腾讯视频合并](https://gitea.hosts.songhu.wang/songhu.wang/Vedio-Download/src/branch/main/%E8%85%BE%E8%AE%AF%E8%A7%86%E9%A2%91)
