def check(places,height,row):
    x=row
    y=height
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for j in range(4):
        cur_x=x+dx[j]
        cur_y=y+dy[j]
        if cur_x<0 or cur_y<0 or cur_x>4 or cur_y>4:
            continue
        elif places[cur_y][cur_x]=="X":
            continue
        elif places[cur_y][cur_x]=="O":
            for j in range(4):
                cur2_x=cur_x+dx[j]
                cur2_y=cur_y+dy[j]
                if cur2_x<0 or cur2_y<0 or cur2_x>4 or cur2_y>4:
                    continue
                elif places[cur2_y][cur2_x]=="X":
                    continue
                elif places[cur2_y][cur2_x]=="O":
                    continue
                else:
                    if cur2_x==row and cur2_y==height:
                        continue
                    else:
                        return 0
        else:
            if cur_x==row and cur_y==height:
                continue
            else:
                return 0
    return 1
    
def solution(places):
    answer = []
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for i in range(5):
        end=False
        for height in range(5):
            for row in range(5):
                if places[i][height][row]=="P":
                    a=check(places[i],height,row)
                    if a==0:
                        answer.append(0)
                        end=True
                        break
            if end==True:
                break
        if end==False:
            answer.append(1)
                
    return answer