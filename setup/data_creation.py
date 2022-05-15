from django.contrib.auth.models import User, Permission, Group
from django.dispatch import receiver
from user_management.models import Profile
from django.contrib.contenttypes.models import ContentType
from user_messaging.models import Message

new_user = User.objects.create_user(username='scott',email='scott@scott.com',password='welovedirk123')
new_user.first_name = 'scott'
new_user.last_name = 'murrell'
profile1 = Profile(user=new_user)
ct = ContentType.objects.get_for_model(Profile)
permission = Permission.objects.get(content_type=ct, codename='can_interact')
new_user.user_permissions.add(permission)
members, _ = Group.objects.get_or_create(name='Members')
new_user.save()
profile1.save()
members.user_set.add(new_user)

new_user = User.objects.create_user(username='barrett',email='barrett@barrett.com',password='welovedirk123')
new_user.first_name = 'barrett'
new_user.last_name = 'brumfield'
profile2 = Profile(user=new_user)
ct = ContentType.objects.get_for_model(Profile)
permission = Permission.objects.get(content_type=ct, codename='can_interact')
new_user.user_permissions.add(permission)
members, _ = Group.objects.get_or_create(name='Members')
new_user.save()
profile2.save()
members.user_set.add(new_user)

Message(body='Hey scott', receiver=profile1, sender=profile2).save()
Message(body='Wassup barret', receiver=profile2, sender=profile1).save()


new_user = User.objects.create_user(username='matthew',email='matthew@matthew.com',password='welovedirk123')
new_user.first_name = 'matthew'
new_user.last_name = 'tucker'
profile3 = Profile(user=new_user)
ct = ContentType.objects.get_for_model(Profile)
permission = Permission.objects.get(content_type=ct, codename='can_interact')
new_user.user_permissions.add(permission)
members, _ = Group.objects.get_or_create(name='Members')
new_user.save()
profile3.save()
members.user_set.add(new_user)

new_user = User.objects.create_user(username='carlos',email='carlos@carlos.com',password='welovedirk123')
new_user.first_name = 'carlos'
new_user.last_name = 'cary'
profile4 = Profile(user=new_user)
ct = ContentType.objects.get_for_model(Profile)
permission = Permission.objects.get(content_type=ct, codename='can_interact')
new_user.user_permissions.add(permission)
members, _ = Group.objects.get_or_create(name='Members')
new_user.save()
profile4.save()
members.user_set.add(new_user)

Message(body='Hey matthew', receiver=profile3, sender=profile4).save()
Message(body='Wassup carlos', receiver=profile4, sender=profile3).save()

new_user = User.objects.create_user(username='charles',email='charles@charles.com',password='welovedirk123')
new_user.first_name = 'charles'
new_user.last_name = 'forman'
profile5 = Profile(user=new_user)
ct = ContentType.objects.get_for_model(Profile)
permission = Permission.objects.get(content_type=ct, codename='can_interact')
new_user.user_permissions.add(permission)
members, _ = Group.objects.get_or_create(name='Members')
new_user.save()
profile5.save()
members.user_set.add(new_user)

new_user = User.objects.create_user(username='tobias',email='tobias@tobias.com',password='welovedirk123')
new_user.first_name = 'tobias'
new_user.last_name = 'dover'
profile6 = Profile(user=new_user)
ct = ContentType.objects.get_for_model(Profile)
permission = Permission.objects.get(content_type=ct, codename='can_interact')
new_user.user_permissions.add(permission)
members, _ = Group.objects.get_or_create(name='Members')
new_user.save()
profile6.save()
members.user_set.add(new_user)

Message(body='Hey charles', receiver=profile5, sender=profile6).save()
Message(body='Wassup tobias', receiver=profile6, sender=profile5).save()

new_user = User.objects.create_user(username='wilfredo',email='wilfredo@wilfredo.com',password='welovedirk123')
new_user.first_name = 'wilfredo'
new_user.last_name = 'wagoner'
profile7 = Profile(user=new_user)
ct = ContentType.objects.get_for_model(Profile)
permission = Permission.objects.get(content_type=ct, codename='can_interact')
new_user.user_permissions.add(permission)
members, _ = Group.objects.get_or_create(name='Members')
new_user.save()
profile7.save()
members.user_set.add(new_user)

new_user = User.objects.create_user(username='layton',email='layton@layton.com',password='welovedirk123')
new_user.first_name = 'layton'
new_user.last_name = 'loyd'
profile8 = Profile(user=new_user)
ct = ContentType.objects.get_for_model(Profile)
permission = Permission.objects.get(content_type=ct, codename='can_interact')
new_user.user_permissions.add(permission)
members, _ = Group.objects.get_or_create(name='Members')
new_user.save()
profile8.save()
members.user_set.add(new_user)

Message(body='Hey wilfredo', receiver=profile7, sender=profile8).save()
Message(body='Wassup layton', receiver=profile8, sender=profile7).save()

new_user = User.objects.create_user(username='brenden',email='brenden@brenden.com',password='welovedirk123')
new_user.first_name = 'brenden'
new_user.last_name = 'graves'
profile9 = Profile(user=new_user)
ct = ContentType.objects.get_for_model(Profile)
permission = Permission.objects.get(content_type=ct, codename='can_interact')
new_user.user_permissions.add(permission)
members, _ = Group.objects.get_or_create(name='Members')
new_user.save()
profile9.save()
members.user_set.add(new_user)

new_user = User.objects.create_user(username='micheal',email='micheal@micheal.com',password='welovedirk123')
new_user.first_name = 'micheal'
new_user.last_name = 'epps'
profile10 = Profile(user=new_user)
ct = ContentType.objects.get_for_model(Profile)
permission = Permission.objects.get(content_type=ct, codename='can_interact')
new_user.user_permissions.add(permission)
members, _ = Group.objects.get_or_create(name='Members')
new_user.save()
profile10.save()
members.user_set.add(new_user)

Message(body='Hey brenden', receiver=profile9, sender=profile10).save()
Message(body='Wassup micheal', receiver=profile10, sender=profile9).save()

new_user = User.objects.create_user(username='varun',email='varun@varun.com',password='welovedirk123')
new_user.first_name = 'varun'
new_user.last_name = 'jonas'
profile = Profile(user=new_user)
ct = ContentType.objects.get_for_model(Profile)
permission = Permission.objects.get(content_type=ct, codename='can_interact')
new_user.user_permissions.add(permission)
members, _ = Group.objects.get_or_create(name='Admin_user_gp')
new_user.save()
profile.save()
members.user_set.add(new_user)

new_user = User.objects.create_user(username='denis',email='denis@denis.com',password='welovedirk123')
new_user.first_name = 'denis'
new_user.last_name = 'mcclelland'
profile = Profile(user=new_user)
ct = ContentType.objects.get_for_model(Profile)
permission = Permission.objects.get(content_type=ct, codename='can_interact')
new_user.user_permissions.add(permission)
members, _ = Group.objects.get_or_create(name='Admin_user_gp')
new_user.save()
profile.save()
members.user_set.add(new_user)

new_user = User.objects.create_user(username='andre',email='andre@andre.com',password='welovedirk123')
new_user.first_name = 'andre'
new_user.last_name = 'hirsch'
profile = Profile(user=new_user)
ct = ContentType.objects.get_for_model(Profile)
permission = Permission.objects.get(content_type=ct, codename='can_interact')
new_user.user_permissions.add(permission)
members, _ = Group.objects.get_or_create(name='Admin_item_gp')
new_user.save()
profile.save()
members.user_set.add(new_user)

new_user = User.objects.create_user(username='melvin',email='melvin@melvin.com',password='welovedirk123')
new_user.first_name = 'melvin'
new_user.last_name = 'raines'
profile = Profile(user=new_user)
ct = ContentType.objects.get_for_model(Profile)
permission = Permission.objects.get(content_type=ct, codename='can_interact')
new_user.user_permissions.add(permission)
members, _ = Group.objects.get_or_create(name='Admin_item_gp')
new_user.save()
profile.save()
members.user_set.add(new_user)

new_user = User.objects.create_user(username='Instructor',email='Instructor@Instructor.com',password='Python420')
new_user.first_name = 'Instructor'
new_user.last_name = 'Iubois'
profile = Profile(user=new_user)
ct = ContentType.objects.get_for_model(Profile)
permission = Permission.objects.get(content_type=ct, codename='can_interact')
new_user.user_permissions.add(permission)
members, _ = Group.objects.get_or_create(name='Admin_gp')
new_user.save()
profile.save()
members.user_set.add(new_user)

new_user = User.objects.create_user(username='jericho',email='jericho@jericho.com',password='welovedirk123')
new_user.first_name = 'jericho'
new_user.last_name = 'thompson'
profile = Profile(user=new_user)
ct = ContentType.objects.get_for_model(Profile)
permission = Permission.objects.get(content_type=ct, codename='can_interact')
new_user.user_permissions.add(permission)
members, _ = Group.objects.get_or_create(name='Admin_gp')
new_user.save()
profile.save()
members.user_set.add(new_user)















