from rest_framework.permissions import BasePermission

class TokenPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD']:
            return True
        elif request.method == 'POST':
            token = request.query_params.get('token')

            if token == "avtotoken":
                return True
            else:
                return False