from django.db import models
from django.db.models import PROTECT
from django.utils import timezone
from django.contrib.auth.models import User

choose_from_categories = (
    ('creative', (
        ('comics', 'comics'),
        ('art', 'art'),
    )),
    ('tech', (
        ('education', 'education'),
        ('phones', 'phones'),
    )),
    ('community', (
        ('environment', 'environment'),
        ('culture', 'culture'),
    ))
)
# choose_from_categories = (
#     ('creative', 'creative'),
#     ('tech', 'tech'),
#     ('community', 'community'),
# )


# class CampaignStatus(models.Model):
#     class Meta:
#         verbose_name_plural = 'Campaign Status'
#     status = models.TextField(max_length=65)


class Campaign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign_Title = models.CharField(max_length=200)
    campaign_Tagline = models.CharField(max_length=200)
    campaign_Card_Image = models.ImageField(blank=True, null=True)
    campaign_Category = models.CharField(
        max_length=20,
        choices=choose_from_categories,
    )
    country = models.CharField(max_length=50, default='India')
    city = models.CharField(max_length=50)
    image = models.FileField()
    tags = models.CharField(max_length=200, blank=True, null=True)
    overview = models.TextField(max_length=500)
    story = models.TextField(max_length=500, blank=True, null=True)
    goal = models.FloatField()
    start_Date = models.DateField()
    end_Date = models.DateField()
    pledged = models.FloatField(default=0.0)
    people_pledged = models.IntegerField(default=0)
#    campaign_Status = models.ForeignKey(CampaignStatus, on_delete=models.PROTECT)

    def __str__(self):
        return self.campaign_Title

#
# class CampaignStatusHistory(models.Model):
#     class Meta:
#         verbose_name_plural = 'Campaign Status History'
#     campaign_ID = models.ForeignKey(Campaign, on_delete=models.CASCADE)
#     campaign_Status = models.ForeignKey(Campaign, on_delete=models.CASCADE)


class FAQs(models.Model):
    class Meta:
        verbose_name_plural = 'FAQs'
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    question = models.TextField(max_length=100, blank=True)
    answer = models.TextField(max_length=200, blank=True)
