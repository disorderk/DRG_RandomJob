# encoding in utf-8
import os
import json


def config():
    if os.path.exists('config.json'):
        with open('./config.json', 'r') as configFile:
            text = configFile.read()
            obj = json.loads(text)
            # print(obj["playerList"]) # 输出读取的玩家列表

            import random

            # 假设有一个列表
            list_to_sort = ["Engineer", "Gunner", "Dirller", "Scotter"]
            # 随机排序列表
            random.shuffle(list_to_sort)
            # 转换为字典，键值为序号
            job_Sorts = {index + 1: item for index, item in enumerate(list_to_sort)}
            print(job_Sorts)  # 输出随机的职业排序

            playList = {}
            for i in obj["playerList"]:
                random_int = random.randint(1, 4)
                # print(f"{i}:{random_int}") # 每个玩家分配一个1-4内的值
                playList[i] = job_Sorts[random_int]  # 根据玩家随机到的值与随机排序的职业表对应，以得到玩家所随机的职业
            # output = "Rabbit:{rabbit},\nRainbow:{rainbow},\nShark:{shark},\nEleven:{eleven},\nDisorder:{disorder},\nNobody:{nobody}\n".format(
            #     **playList)
            output = ',\n'.join([f"{key}: {value}" for key, value in playList.items()])
            print(output)  # output result/输出骰子结果

            os.system("pause")

            configFile.close()
    else:
        with open('./config.json', 'w+') as configFile:
            configFile.close()
            # obj = {}
            # print("1.How many people to play DRG？")

            # playerNum = int(input("1.How many people to play DRG？"))  # 输入列表的长度
            # playerList = []  # 初始化一个空列表
            # for i in range(playerNum):
            #     item = input("The " + str(i + 1) + " player\'s name is: ")  # 输入每个元素
            #     playerList.append(item)  # 将元素添加到列表中
            # print("playerList:", playerList)
            # for i in playerList:
            #     playerListJson = json.dumps(i)
            #     configFile.write(playerListJson + '\n')
            # configFile.close()

            # # 用户手动输入键值对创建字典
            # player_dict = {}
            # while True:
            #     key = input("请输入键（输入'q'退出）: ")
            #     if key == 'q':
            #         break
            #     value = input(f"请输入{key}对应的值: ")
            #     player_dict[key] = value
            # print(player_dict)


if __name__ == '__main__':
    config()
