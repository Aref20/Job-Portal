from rest_framework import permissions

class IsAuthProfile(permissions.BasePermission):



    def has_permission(self, request, view):
        # Authenticated users only can see list view
        if request.user.is_authenticated:
            return True
        return False



    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request so we'll always
        # allow GET, HEAD, or OPTIONS requests
        #if request.method in permissions.SAFE_METHODS:
        #    return True
       # Write permissions are only allowed to the user of a userprofile
        return obj.id == request.user.id


class IsAdminOrReadOnlyJob(permissions.BasePermission):


    def has_permission(self, request, view):
        # Authenticated users only can see list view

            return True
 



    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request so we'll always
        # allow GET, HEAD, or OPTIONS requests
        

        #if view.action in ['update', 'partial_update','destroy','create','perform_create']:
      #      return  True
      # Writeelif view.action in ['retrieve','list'] :
        #    return True
       if request.method in ['POST']:
            return False