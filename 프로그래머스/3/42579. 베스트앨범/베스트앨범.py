from collections import defaultdict
def solution(genres, plays):
    
    playlist=defaultdict(list)
    play_count=defaultdict(int)

    #장르별로 음악 재생 횟수 합산
    for idx,(genre,play) in enumerate(zip(genres,plays)):
        playlist[genre].append((play,idx))
        play_count[genre]+=play
        
    #음악 재생 횟수를 기반으로 정렬
    sorted_genres=sorted(play_count.keys(),key=lambda g:play_count[g],reverse=True)
    
    #각 장르별 곡 정렬 후 최대 2개 선택
    answer=[]
    for genre in sorted_genres:
        songs=sorted(playlist[genre],key=lambda x:(-x[0],x[1]))
        answer.extend([idx for _, idx in songs[:2]])
        
    return answer