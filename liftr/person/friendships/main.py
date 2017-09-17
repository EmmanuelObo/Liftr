from friendship.models import Friend, FriendshipRequest

def send_request(curr_user, recipient, msg="{} wants to partner with you!"):
    try:
        # if(FriendshipRequest.objects.get(to_user=curr_user) != None):
        msg.format(curr_user.username)
        Friend.objects.add_friend(curr_user,recipient,msg)

    except:
        print("Already Exists")

def accept_request(curr_user):
     FriendshipRequest.objects.get(to_user=curr_user).accept()

def reject_request(curr_user):
     FriendshipRequest.objects.get(to_user=curr_user).reject()
