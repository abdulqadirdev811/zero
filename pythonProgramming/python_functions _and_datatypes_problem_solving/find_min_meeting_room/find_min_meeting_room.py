time_intervals_list = [[3, 4],[2, 8], [3, 9], [5, 11], [8, 20], [11, 15]]

def verify_data(input_list):
    for time_intervel in input_list:
        if time_intervel[0] > time_intervel[1]:
            return False
    return True 

def sort_list_on_index_base(input_list):
    flag = False
    sorted_list = []
    if verify_data(input_list):
        sorted_list =  sorted(input_list,key = lambda x : x[0])
        flag = True
    
    return (flag,sorted_list)   
    

def get_min_required_meeting_room(sorted_list):
        pq = [sorted_list[0]]
        for current_time_interval in sorted_list[1:]:
            print("pq >>",pq)
            prev = pq.pop(0)
            
            if prev[1] > current_time_interval[0]:
                pq.append(prev)
                pq.append(current_time_interval)
            else:
                 prev = current_time_interval
                 pq.append(prev)
        return len(pq)               


sorted_result = sort_list_on_index_base(time_intervals_list)
rslt = get_min_required_meeting_room(sorted_result[1])

print(rslt)
