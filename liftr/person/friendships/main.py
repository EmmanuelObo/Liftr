from friendship.models import Friend, FriendshipRequest

def send_request(curr_user, recipient, msg="{} wants to partner with you!"):
    msg.format(curr_user.username)
    Friend.objects.add_friend(curr_user,recipient,msg)

 def accept_request():
    FriendshipRequest.objects.filter(to_user=jon)




# def reject_request():


