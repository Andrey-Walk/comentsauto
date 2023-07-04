from rest_framework.permissions import BasePermission

class LookPermission(BasePermission):
    def has_permission(self, request, view):
        token = request.query_params.get('token')

        if token == "avtotoken":
            return True
        else:
            return False


class TokenPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD']:
            return True
        elif request.method == 'POST':
            token = request.META.get('HTTP_AUTHORIZATION')
            if token and token.startswith('Bearer '):
                return token.decode('utf-8') == 'avtotoken'
            else:
                return False
        else:
            return False