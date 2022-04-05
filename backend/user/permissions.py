from rest_framework import permissions

class EditOwnProfile(permissions.BasePermission):
     
     def has_ojbect_permission(self, request, view, obj):
          
          if request.method in permissions.SAFE_METHODS:
               return True
          
          return obj.id == request.user.id