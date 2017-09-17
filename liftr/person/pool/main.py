from geopy.distance import vincenty

def filter(curr_user, preference, users):
    filtered = []
    for user in users:
        if (user in curr_user.reject_list or
            user in curr_user.pending_list or
            user in curr_user.awaiting_list or
            user in curr_user.friends):
            # vincenty((user.person.longitude, user.person.latitude),(curr_user.longitude, curr_user.latitude)).miles > preference.distance):
            print('Filtered out user {}'.format(user.username))


        else:
            filtered.append(user)

    return filtered
