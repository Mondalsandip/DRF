from rest_framework import permissions

# class AdminOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         print('obj :', obj)
#         print('hello')
#         return obj.owner == request.user
    
class ReviewOrReadOnly(permissions.IsAuthenticated):
    #def has_object_permission(self, request, view, obj):
        # if request.method not in permissions.SAFE_METHODS:
            # print('obj: ', obj.owner)
            # return True
        #return obj.owner == request.user

    # def has_permission(self, request, view):
    #     return False

    def has_permission(self, request, view):
        #print('request: ',  request.method)
        #print('request: ',  request.user)
        #print('request: ',  request.user)
        #return   request.method == 'GET' or  super().has_permission(request,view)
        return  super().has_permission(request,view)
    
        
