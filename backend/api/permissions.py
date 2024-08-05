from rest_framework import permissions

class isStaffEditorPermission(permissions.DjangoModelPermissions):
    
    def has_permission(self, request, view):
        # user = request.user
        # if not user.is_staff:
        #     return False
        return super().has_permission(request, view)
    
    
    
    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm('api.change_product'):
    #             return True
    #         if user.has_perm('api.add_product'):
    #             return True
    #         if user.has_perm('api.delete_product'):
    #             return True
    #         if user.has_perm('api.view_product'):
    #             return True
    #         return True
    #     return False