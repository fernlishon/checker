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
        #保存到txt
        file = open('errorNum.txt','w')
        for path in self._result:
            print(path)
            result = self._result[path]
            for r in result:
                if not r[1][0]:
                    print(f"    |_{r[0]} match:{r[1][0]} file number:{r[1][1]}") 
                    file.write(f"    |_{r[0]} match:{r[1][0]} file number:{r[1][1]}\n")
        file.flush()#结束之前将缓冲区内容添加到位
        file.close()
        return self

def checkTheErrorFile(results):
    for key,valueList in results.items():#results.items(),字典不能直接遍历
        #print(key)
        keyDir = key.split('\\')
        dir = keyDir[4]       
        for listItem in valueList:
            if listItem[1][0] == False:
                nameOfError = listItem[0]
                yield dir,nameOfError #循环一次后return，再循环下一次，。yield后续用法与list相同
                

def matchTheErrorFile (originPath,string,errorDir,NameError):
    text = open('nameErrorList.txt','w')
    for file in os.listdir(originPath):
        str = file.split("_")
        if NameError == str[-1]:
            print(f"origin Path:{originPath},  num:{str[-2]},  name: {NameError}")
            text.write(f"origin Path:{originPath},  num:{str[-2]},  name: {NameError}\n")
            
    text.flush()
    text.close()#使用text = open('.txt')打开后必须关闭text.close()，才能写入内容；使用with open则不需要

def theFileTOcheck(path,string):
    for dir in os.listdir(path):
        if string in dir:
            yield os.path.join(path,dir)

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
    numOfFiles = [1,2,120,4992,24,11438,4300,4300,4300,4300,3]
    originPath = r"F:\201804athletes\athletes_data"
    string = "separate"
    checker = Checker(pathFile,numOfFiles)
    results = checker.check(pathAthlete).dumps().getResult()
    subOriginPath = theFileTOcheck(originPath,string)
    for originItem in subOriginPath:
        for errorPath,NameError in checkTheErrorFile(results):
            lastPath = os.path.join(originItem,errorPath) 
            matchTheErrorFile(lastPath,string,errorPath,NameError)