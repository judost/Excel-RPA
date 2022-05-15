import pandas as pd

def findNearNum(F_List, Val):
    Num = [0 for _ in range(2)] # Num 리스트 0으로 초기화

    minVal = min(F_List, key=lambda x:abs(x-Val))
    minIndex = F_List.index(minVal)
    Num[0] = minIndex
    Num[1] = minVal
    
    return Num

def Num_seq(F_List):
    
    NumL = []
    
     # Num 리스트 0으로 초기화
    trigger = 1
    now = 0
    last_F = 0
    for i in range(0, len(F_List)-1):
        if trigger == 1:
            Num = [0 for _ in range(2)]
            Cal = F_List.iloc[i+1] - F_List.iloc[i]
            
            if Cal > 0.5: # 차이 기준값 ★☆★☆★☆★☆★☆★☆★☆  
                F_Index = F_List.iloc[now]
                L_Index = F_List.iloc[i+1]
                
                Num[0] = F_Index
                Num[1] = L_Index
                NumL.append(Num)
                now = i+2
                last_F = now+1
                trigger = 0 # for문 한 차례 날리기 용 // 하나 하고 다음 그룹은 한차례 건너 뛰고 해야하기 때문에
        else:
            trigger = 1
            
    Num = [0 for _ in range(2)]
    Num[0] = F_List.iloc[last_F]   
    Num[1] = F_List.iloc[-1]
    NumL.append(Num)
    
    return NumL
    

def remover(x):
    x = x['Time'].str.extract(r'(\d+:\d+:\d+.\d+)')
    x.columns = ['Time']
    x = x['Time'].str.replace(':','')
    
    x = pd.to_numeric(x)
    return x


def Pickup_df1():
    data = pd.read_csv('samsample.txt', sep='\t', index_col=False) # csv 파일로 변환
    temp_df = pd.DataFrame(data) # DataFrame화
    df = temp_df.iloc[:,[0,1,2,6,7,8]] # 원하는 칼럼 인덱싱
    # print(df.head())
    
    return df

def Pickup_df2(df):
    df_10 = df[df['this'] > 10]   # this 열에서 10 보다 큰 수
    # print(df_10)
    Col0 = df_10.iloc[:,[0]]
    Col0 = remover(Col0)
   
    return Col0

    
df = Pickup_df1() 
df = Pickup_df2(df)
print(Num_seq(df))

# try:   
#     df = Pickup_df2(df)
# except:
#     pass