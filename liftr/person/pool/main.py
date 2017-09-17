from geopy.distance import vincenty

def filter(curr_user, preference, users):
    filtered = []
    try:
        for user in users:
            # if ((curr_user.reject_list & ( for user == curr_user.reject_list[0].from_user) or
            #     user == curr_user.pending_list[0].from_user or
            #     user == curr_user.awaiting_list[0].from_user or
            #     user in curr_user.friends):

            if(curr_user.awaiting_list):
                if( user == curr_user.awaiting_list[0].from_user):
                # vincenty((user.person.longitude, user.person.latitude),(curr_user.longitude, curr_user.latitude)).miles > preference.distance):
                    print('Filtered out user {}'.format(user.username))
            else:
                filtered.append(user)



    except:
        print("Index Out of Bounds")

    return filtered
