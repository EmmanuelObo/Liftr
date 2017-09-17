from friendship.models import Friend

def send_request(curr_user, recipient, msg):
    msg="{} wants to partner with you!".format(curr_user.username)
    Friend.objects.add_friend(curr_user,recipient,msg)

def accept_request():
    # Code

def reject_request():
    # Code

