from rest_framework.permissions import BasePermission, SAFE_METHODS

class isOwnerOrReadOnly(BasePermission):
    message = 'Only organizer can create and edit events.'
    def has_object_permission(self ,request  ,view ,obj):
        if request.method in SAFE_METHODS and obj.owner.profile.role == "Attendee":
            return True
        else:
            return (request.user == obj.owner) and (obj.owner.profile.role == "Organizer")
    
class isOrganizer(BasePermission):
    def has_permission(self ,request,view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return (request.user.profile.role == "Organizer")
    
