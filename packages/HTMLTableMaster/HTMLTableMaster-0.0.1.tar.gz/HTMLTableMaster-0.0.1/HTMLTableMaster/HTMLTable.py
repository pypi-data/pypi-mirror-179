class HTMLTable:
    
    # -*- coding: utf-8 -*-
    """
    Created on Thu Nov 10 09:58:57 2022

    @author: MudithaRajapaksha
    Functionality - This Class reads HTML tables that are in str format and murge rows based on a common field
    """
    
    from bs4 import BeautifulSoup
    import bs4
    
    def __init__(self, htmlTableStr, identifyCol ,hasHeading = True):
        self.htmlTableStr = htmlTableStr
        self.identifyCol = identifyCol
        self.hasHeading = hasHeading
        
        
        self.soup = self.BeautifulSoup(self.htmlTableStr, "html.parser")
        if(hasHeading == True):
            self.tableRows = self.soup.find_all('tr')[1:]
            self.tableRowsWithHeading = self.soup.find_all('tr')[0]
        else:
            self.tableRows = self.soup.find_all('tr')
    

    
    def GetRowsToSpan(self):
        #first find rows pan nmbers
        rowsToSpan = {}
        uniqueCodePrev = ""
        uniqueCodeNow = ""
        skipedRowNo = 0
        rowNo = 0
        
        if(len(self.tableRows) == 1):
            return rowsToSpan
        else:
            
            #for rowNo in range(0 , len(self.tableRows)):
            while(rowNo <= len(self.tableRows)):
                if(isinstance(self.tableRows[rowNo], self.bs4.element.Tag)):
                    cells = self.tableRows[rowNo].find_all("td")
                    uniqueCodeNow = cells[self.identifyCol].get_text()
                    colsPanCounter = 1
                    
                    #default
                    rowsToSpan[skipedRowNo] = 1
                    
                    for nextRowNo in range(rowNo + 1 , len(self.tableRows)):
                        if(isinstance(self.tableRows[nextRowNo], self.bs4.element.Tag)):
                            cells = self.tableRows[nextRowNo].find_all("td")
                            uniqueCodeNext = cells[self.identifyCol].get_text()
                            if(uniqueCodeNow == uniqueCodeNext ):
                                colsPanCounter += 1
                                rowsToSpan[rowNo] =  colsPanCounter
                            else:
                                rowsToSpan[rowNo] =  colsPanCounter
                                break
                
                skipedRowNo = rowNo + rowsToSpan[skipedRowNo]
                rowNo = skipedRowNo
                
                if(skipedRowNo >= len(self.tableRows)):
                    break
            return rowsToSpan
        
    

    
    def SetRowsPan(self , rowsToSpan , colsToPan):
        #colsToPan = [0,1] #which column numners to murge
        spanRowNoList = list(rowsToSpan.keys())
        removeTdRowLst = list(range(0 , len(self.tableRows))) #all rows here for now
        
        
        for rowNo in spanRowNoList:
            if(isinstance(self.tableRows[rowNo], self.bs4.element.Tag)):
                removeTdRowLst.remove(rowNo)
                cells = self.tableRows[rowNo].find_all("td")
                for colNo in colsToPan:
                    cells[colNo]["rowspan"] = rowsToSpan[rowNo]
              
     
       # tableRowsNew = soup.find_all('tr') #only the reference is passed so the original changes
        
       
        for rowNo in removeTdRowLst:
            if(isinstance(self.tableRows[rowNo], self.bs4.element.Tag)):
                cells = self.tableRows[rowNo].find_all("td")
                for colNo in colsToPan:
                    cells[colNo].decompose()
             
        
    
    def removeColumn(self ,removeCol = [] ):
        
        if(len(removeCol) != 0 ):
            #removeCol = [-1]
            for rowNo in range(0 , len(self.tableRows)):
                if(isinstance(self.tableRows[rowNo], self.bs4.element.Tag)):
                    cells = self.tableRows[rowNo].find_all("td")
                    for colNo in removeCol:
                        cells[colNo].decompose()
            
            if(self.hasHeading == True):
                pass
                #remove heading
                cells = self.tableRowsWithHeading.find_all("th")
                for colNo in removeCol:
                    cells[colNo].decompose()
                    
            return self
        else:
            
            return self
        
    
    
    def murgeRows(self , colsToSpan = [0]):
        rowsToMurge = self.GetRowsToSpan()
        if(len(rowsToMurge) == 0):
            return self
        else:
            self.SetRowsPan(rowsToMurge , colsToSpan)
            return self
    
    
    def getString(self):
        return str(self.soup)
        
  

if __name__ == "__main__":    
    file = open("new 34.html" , "r")
    htmlTable = HTMLTable(file.read() , -1 , hasHeading=(True)).murgeRows([0 ,1, 2 ,3 ,4 ,5 ,6]).removeColumn([-1]).getString()
    #htmlTable = HTMLTable(file.read() , -1 , hasHeading=(True)).removeColumn([-1]).getString()
    print(htmlTable)
    
    fileNew = open("hh.html" , "w")
    fileNew.write(htmlTable)
    fileNew.close()
   
