import os
import shutil
import glob


def mk_video_dir():
    path1 = './'
    list1 = os.listdir(path1)
    player_list = []
    for dir_ in list1:
        if os.path.isdir(path1 + dir_):
            player_list.append(path1+str(dir_))
    player_list = sorted(player_list)
    # [["0"],[0,1,2,3...],["2"],[0,1,2,3...]]]
    player_num = 0
    finalPlayerListAndVideo = []
    for player in player_list:
        player_num+=1
        video_path = []
        for video_dir in os.listdir(player):
            if os.path.isdir(player+"/"+video_dir):
                video_path.append(player+"/"+video_dir)
        video_path = sorted(video_path)
        finalPlayerListAndVideo.append(video_path)

    #     目前已把選手1的底下所有資料夾位置抓出來，且 預設mp4檔名都是us.mp4固可直接設定路徑+us.mp4
    player_num = [str(i) for i in range(player_num)]
    finalPlayerListAndVideo = list(zip(player_num,finalPlayerListAndVideo))
    # 已得到[("選手編號",[該選手的所有影片路徑])]
    tendon_name_and_move = ["肩胛下肌_等長","肩胛下肌_等張","棘上肌_等長",'棘上肌_等張',"棘下肌_等長","棘下肌_等張"]
    for _ in finalPlayerListAndVideo:
        counter = 0
        os.mkdir(_[0])
        os.mkdir("./"+_[0]+"/Totel_Res")
        for tendon in tendon_name_and_move:
            os.mkdir("./"+_[0]+"/"+tendon)
        # input()
        for video_path in _[1]:
            copt_to_path = "./"+(_[0])+"/"+str(counter)+".mp4"
            shutil.copy(video_path+"/us.mp4",copt_to_path)
            # 創建所有影片的對應結果
            os.mkdir("./"+(_[0])+"/"+str(counter)+"_res")
            counter+=1






mk_video_dir()
# list1 = ['20210114-case3_2021011423939','20210114-case1_2021011412153','20210114-case2_2021011421009']
# print(sorted(list1))