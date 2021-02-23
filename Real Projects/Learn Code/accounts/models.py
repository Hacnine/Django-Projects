from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

SUBSCRIPTION = {
    ('F', 'FREE'),
    ('M', 'MONTHLY'),
    ('Y', 'YEARLY'),
}


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_pro = models.BooleanField(default=False)
    pro_expiry_date = models.DateField(null=True, blank=True)
    subscription_type = models.CharField(max_length=100, choices=SUBSCRIPTION, default='FREE')

    def __str__(self):
        return self.user


class Course(models.Model):
    course_name = models.CharField(max_length=200, null=True)
    course_description = RichTextField(null=True)
    is_premium = models.BooleanField(default=False, null=True)
    course_image = models.ImageField(default="profile.png", null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.course_name)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.course_name


class CourseModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    course_module_name = models.CharField(max_length=100, null=True)
    course_description = RichTextField(null=True)
    video_url = models.URLField(max_length=300, null=True)
    can_view = models.BooleanField(default=False, null=True)



# MEMBERSHIP_CHOICES = {
#     ('Enterprise', 'ent'),
#     ('Professional', 'pro'),
#     ('Free', 'free')
# }
#
#
# class Membership(models.Model):
#     slug = models.SlugField()
#     membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, max_length=30,
#                                        default='Free')
#     price = models.IntegerField(default=15, null=True)
#     stripe_plan_id = models.CharField(max_length=40, null=True)
#
#     def __str__(self):
#         return self.membership_type
#
#
# class UserMembership(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     stripe_customer_id = models.CharField(max_length=40)
#     membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
#
#     def __str__(self):
#         return self.user.username
#
#
# def post_save_membership_create(sender, instance, created, *args, **kwargs):
#     if created:
#         UserMembership.objects.get_or_create(user=instance)
#     user_membership, created = UserMembership.objects.get_or_create(user=instance)
#     if user_membership.stripe_customer_id is None or user_membership.stripe_customer_id == '':
#         new_customer_id = stripe.Customer.create(email=instance.email)
#         user_membership.stripe_customer_id = new_customer_id['id']
#         user_membership.save()
#
#
# class Subscription(models.Model):
#     user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
#     stripe_subscription_id = models.CharField(max_length=40)
#     active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.user_membership.user.username
