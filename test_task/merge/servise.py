import json

class Merge:

    def action(self, text):
        data1=json.loads(text[0])
        data2=json.loads(text[1])
        result=''
                
        for key, value in data1.items():
            find=0
            for key2, value2 in data2.items():
                if(key==key2):
                    find=1
                    if(value==value2):
                        result+=key+':'+str(value)+','
                    else:
                        result+='-'+key+':'+str(value)+','
                        result+='+'+key2+':'+str(value2)+','
            if(find==0):
                result+='-'+key+':'+str(value)+','
        
        for key, value in data2.items():
            find=0
            for key2, value2 in data1.items():
                if(key==key2):
                    find=1
            if(find==0):
                result+='+'+key+':'+str(value)+','


        
        print(result)
        return result