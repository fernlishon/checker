#neaten2：check the num of the files
# 单一职责
# 封装层次
import os
def checkNumOfFilesInDirs(dirPath,numOfFiles):
    fileNum = len(os.listdir(dirPath))
    if fileNum != numOfFiles:
        return [False,fileNum]
    else:
        return [True,fileNum]

def checkAllDirs(path,numOfFiles):
    dirs = [ (dir,os.path.join(path,dir)) for dir in os.listdir(path) ]
    return [(dir,checkNumOfFilesInDirs(wholeDir,numOfFiles)) for dir,wholeDir in dirs ]

def check(dir,numOfFile,path):
    results = {}
    for dirs,numOfFile in zip(dir,numOfFile):
        wholeDirs = os.path.join(pathAthlete,dirs)
        results[wholeDirs] = checkAllDirs(wholeDirs,numOfFile)
    return results

def dumps(results):
    for path in results:
        print(path)
        result = results[path]
        for r in result:
            print(f"    |_{r[0]} match:{r[1][0]} file number:{r[1][1]}")

class Checker:
    def __init__(self,dirsToCheck,num):
        self._dirsToCheck = dirsToCheck
        self._num = num
        self._result = {}
        
    
    def checkNumOfFilesInDirs(self,dirPath,numOfFiles):
        fileNum = len(os.listdir(dirPath))
        if fileNum != numOfFiles:
            return [False,fileNum]
        else:
            return [True,fileNum]

    def checkAllDirs(self,path,numOfFiles):
        dirs = [ (dir,os.path.join(path,dir)) for dir in os.listdir(path) ]
        return [(dir,checkNumOfFilesInDirs(wholeDir,numOfFiles)) for dir,wholeDir in dirs ]

    def check(self,path):
        for dirs,numOfFile in zip(self._dirsToCheck,self._num):
            wholeDirs = os.path.join(pathAthlete,dirs)
            self._result[wholeDirs] = checkAllDirs(wholeDirs,numOfFile)
        return self

    def getResult(self):
        return self._result
    
    def dumps(self):
        file = open('F:\codes\pycodes\checker\errorNum.txt','w')
        for path in self._result:
            print(path)
            result = self._result[path]
            for r in result:
                if not r[1][0]:
                    print(f"    |_{r[0]} match:{r[1][0]} file number:{r[1][1]}")
                    #保存到txt
                    file.write(f"    |_{r[0]} match:{r[1][0]} file number:{r[1][1]}\n")
        file.flush()#结束之前将缓冲区内容添加到位
        file.close()
        return self


if __name__ == "__main__":
    # pathAthlete = r"F:\201804athletes\athletes_data\collation_201804ath"  
    # pathHc = r"F:\201804athletes\athletes_data\collation_201804hc"
    # pathFile = ["3DT1","3PlT2FGRE","AssetCalibration","DTI","OAxT2FLAIR","rest","run1","run2","run3","run4","ScreenSave"]
    # numOfFiles = [2,2,3,4,1,2,1,1,1,1,2]

    # for pathFileName,detachNumOfFile in zip(pathFile,numOfFiles):#将两数组列表打包方式
    #     subPath = os.path.join(pathAthlete,pathFileName)
    #     for file in os.listdir(subPath):
    #         print("pathName:  %s"%pathFileName,end=',  ') #不换行的方式
    #         match,fileNum = checkNumOfFilesInDirs(subPath,detachNumOfFile)
    #         print("match?   %s,  fileNumbers： %s"%(match,fileNum),end = ",  ")#函数返回数组的解包方式
    #         print("name:  %s"%file)

    pathAthlete = r"F:\201804athletes\athletes_data\collation_201804ath"  
    pathHC = r"F:\201804athletes\athletes_data\collation_201804hc" 
    pathFile = ["3DT1","3PlT2FGRE","AssetCalibration","DTI","OAxT2FLAIR","rest","run1","run2","run3","run4","ScreenSave"]
    numOfFiles = [159,18,120,4992,24,11438,4300,4300,4300,4300,3]

    checker = Checker(pathFile,numOfFiles)
    results = checker.check(pathAthlete).dumps().getResult()
    



    