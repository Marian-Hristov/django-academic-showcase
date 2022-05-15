from cmath import exp
from unicodedata import name
from django.apps import AppConfig
from psycopg2 import ProgrammingError


class WebAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web_admin'

    def ready(self):
        try:
            from django.contrib.auth.models import Group, Permission, User
            from django.contrib.contenttypes.models import ContentType

            # Permissons
            admin_projects = Permission.objects.filter(codename='administrate_projects').first()
            content_type = ContentType.objects.get_for_model(Group)

            administrate_all_members , _= Permission.objects.get_or_create(
                codename='administrate_members',
                name='Can administrate members',
                content_type=content_type
            )

            administrate_all_users , _= Permission.objects.get_or_create(
                codename='administrate_users',
                name='Can administrate all users',
                content_type=content_type
            )

            # Create groups
            def create_member_group():
                members, _ = Group.objects.get_or_create(name='Members')
                members.save()

            def create_admin_user_group():
                admin_user, _= Group.objects.get_or_create(name='Admin_user_gp')
                admin_user.permissions.clear()
                admin_user.permissions.add(administrate_all_members)
                admin_user.save()

            # This admin should be able to move and remove users from the various groups
            def create_admin_item_group():
                admin_item, _= Group.objects.get_or_create(name='Admin_item_gp')
                admin_item.permissions.clear()
                admin_item.permissions.add(administrate_all_members, admin_projects)
                admin_item.save()

            def create_admin_group():
                admin_group , _ = Group.objects.get_or_create(name='Admin_gp')
                admin_group.permissions.clear()
                admin_group.permissions.add(administrate_all_members, admin_projects, administrate_all_users)
                user, created = User.objects.get_or_create(username='Instructor')
                if created:
                    user.set_password("Python419")
                    user.save()
                admin_group.user_set.add(user)
                admin_group.save()

            create_admin_user_group()
            create_admin_item_group()
            create_member_group()
            create_admin_group()
        except:
            pass
