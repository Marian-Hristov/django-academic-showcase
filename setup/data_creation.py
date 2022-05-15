from django.contrib.auth.models import User, Permission, Group
from django.dispatch import receiver
from user_management.models import Profile
from django.contrib.contenttypes.models import ContentType
from user_messaging.models import Message
from item_catalog.models import Project, Post, Rating, Comment

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


project1 = Project(name='Todo App', project_type='app', field='Computer Science', keywords='computers, apps, todo', description='Application to keep track of tasks', status='ongoing', user=profile1)
post1 = Post(project=project1, title='Look at my Todo App')
project1.save()
post1.save()

project11 = Project(name='Spongebob the Movie the Play', project_type='play', field='Theatre', keywords='art, spongebob, larry, the, lobster', description='A real time play for our drama class of the movie Spongebob', status='completed', user=profile1)
post11 = Post(project=project11, title="Please don't come to this play unless you have to.")
rating1 = Rating(post=post11, rating_value=6, user=profile1)
rating2 = Rating(post=post11, rating_value=7, user=profile2)
project11.save()
post11.save()
rating1.save()
rating2.save()

project2 = Project(name='Weather App', project_type='app', field='Meteorology', keywords='computers, apps, weather, meteorology', description='Application to retrieve the weather of destinations', status='ongoing', user=profile2)
post2 = Post(project=project2, title='Look at my Weather App')
project2.save()
post2.save()

project12 = Project(name='Linux Tweet App', project_type='app', field='Computer Science', keywords='linux, containers, docker', description='Linux lab to creation a docker image and run it.', status='completed', user=profile2)
post12 = Post(project=project12, title='Check out my Tweet App')
comment1 = Comment(user=profile2, body="I'm really proud of this, I hope you all like it!", post=post12)
comment2 = Comment(user=profile3, body="This is kinda trash ngl fam", post=post12)
project12.save()
post12.save()
comment1.save()
comment2.save()


project3 = Project(name='Facial Detection', project_type='software', field='AI and ML', keywords='computers, apps, AI, ML', description='Facial detection application to uniquely identify faces', status='completed', user=profile3)
post3 = Post(project=project3, title='Check out my Facial Detection application')
project3.save()
post3.save()

project13 = Project(name='Random number generator', project_type='generator', field='Computer Science', keywords='java, generator, random, numbers, math', description='A random number generator that generates a random number to use for all other random things that you may need in ur random life', status='completed', user=profile3)
post13 = Post(project=project13, title="Download random number generator app")
rating1 = Rating(post=post13, rating_value=7, user=profile3)
rating2 = Rating(post=post13, rating_value=3, user=profile4)
project13.save()
post13.save()
rating1.save()
rating2.save()

project4 = Project(name='Auction System', project_type='system', field='Commerce', keywords='computers, apps, auction, business, commerce', description='System to provide an auctioning interface', status='completed', user=profile4)
post4 = Post(project=project4, title='Take a look at my Auctioning System')
project4.save()
post4.save()

project14 = Project(name='The tale of Marian the Great', project_type='Story', field='English', keywords='English, literature, marian', description='A story about the great marian, how slayed thy Python in battle', status='completed', user=profile4)
post14 = Post(project=project14, title='Please read my story, like plz, plz, plz.')
comment1 = Comment(user=profile4, body="I'm really proud of this, I hope you all like it!", post=post14)
comment2 = Comment(user=profile5, body="This is kinda trash ngl fam", post=post14)
project14.save()
post14.save()
comment1.save()
comment2.save()

project5 = Project(name='Academic Performance evaluater', project_type='api', field='education', keywords='computers, apps, education, grading, school', description='API that evaluates a students academic performance', status='completed', user=profile5)
post5 = Post(project=project5, title='Take a look at my Academic Performance evaluater')
project5.save()
post5.save()

project15 = Project(name='My Life Story', project_type='Autobiography', field='Social Studies', keywords='story, autobiography, social, studies', description='The story of my life, I take her home....', status='completed', user=profile5)
post15 = Post(project=project15, title="I hope you enjoy my life story")
rating1 = Rating(post=post15, rating_value=6, user=profile5)
rating2 = Rating(post=post15, rating_value=7, user=profile6)
project15.save()
post15.save()
rating1.save()
rating2.save()

project6 = Project(name='Crime rate predictor', project_type='api', field='Policing', keywords='computers, apps, police, crime', description='API that predicts the crime rate for given area', status='ongoing', user=profile6)
post6 = Post(project=project6, title='Take a look at my Crime Rate Predictor')
project6.save()
post6.save()

project16 = Project(name='Science Fair Volcano', project_type='model', field='Science', keywords='Volcano, project, boom', description='A model of a volcano to present at the science fair', status='ongoing', user=profile6)
post16 = Post(project=project16, title="Please come to the science fair. Bring goggles so the volcano doesn't make a boom boom on your face")
comment1 = Comment(user=profile6, body="I'm really proud of this, I hope you all like it!", post=post16)
comment2 = Comment(user=profile7, body="This is kinda trash ngl fam", post=post16)
project16.save()
post16.save()
comment1.save()
comment2.save()

project7 = Project(name='Model Airplane', project_type='model', field='Aerospace', keywords='aerospace, physics, planes, aviation, models', description='A model mini airiplane that will be made out of a light wood so that it can actually fly', status='ongoing', user=profile7)
post7 = Post(project=project7, title='Please show up to class everyone to see my airplane :(')
project7.save()
post7.save()

project17 = Project(name='Library Management System', project_type='data', field='Computer Science', keywords='library, data, management', description='The system to manage a library', status='completed', user=profile7)
post17 = Post(project=project17, title="Please buy my system, I'm poor")
rating1 = Rating(post=post17, rating_value=8, user=profile7)
rating2 = Rating(post=post17, rating_value=10, user=profile8)
project17.save()
post17.save()
rating1.save()
rating2.save()

project8 = Project(name='UN simulation', project_type='real-life-game', field='Politics', keywords='UN, peace, poilitics, putin, simulation', description='A full on simulation of the united nations', status='ongoing', user=profile8)
post8 = Post(project=project8, title="Let's all do this model UN sim soon")
project8.save()
post8.save()

project18 = Project(name="Raagav's blog", project_type='website', field='English', keywords='web, blog, english', description='A blog where I update you guys on the weekly occurences in my life', status='ongoing', user=profile8)
post18 = Post(project=project18, title="Enjoy my blog!")
comment1 = Comment(user=profile8, body="I'm really proud of this, I hope you all like it!", post=post18)
comment2 = Comment(user=profile9, body="This is kinda trash ngl fam", post=post18)
project18.save()
post18.save()
comment1.save()
comment2.save()

project9 = Project(name='django-academic-showcase', project_type='application', field='Computer Science', keywords='django, compsci, heroku, vscode', description='A django application to showcase academic projects', status='ongoing', user=profile9)
post9 = Post(project=project9, title="Still not done, currently struggling, send help plz!!!!!!")
project9.save()
post9.save()

project19 = Project(name='A forum', project_type='website', field='Computer Science', keywords='forum, reddit, social, compsci', description='A forum similar to reddit', status='completed', user=profile9)
post19 = Post(project=project19, title="I hope you enjoy making fun of little kids on my forum")
rating1 = Rating(post=post19, rating_value=4, user=profile9)
rating2 = Rating(post=post19, rating_value=7, user=profile10)
project19.save()
post19.save()
rating1.save()
rating2.save()

project10 = Project(name='Word Counter', project_type='api', field='Computer Science', keywords='words, counter, english', description='A word counter to count the number of words in a given text', status='ongoing', user=profile10)
post10 = Post(project=project10, title="Enjoy the word counter app!")
project10.save()
post10.save()

project20 = Project(name="Timer", project_type='app', field='Computer Science', keywords='clock, time, asynchronous', description='A digital timer', status='completed', user=profile10)
post20 = Post(project=project20, title="Download my timer")
comment1 = Comment(user=profile10, body="I'm really proud of this, I hope you all like it!", post=post20)
comment2 = Comment(user=profile1, body="This is kinda trash ngl fam", post=post20)
project20.save()
post20.save()
comment1.save()
comment2.save()






















