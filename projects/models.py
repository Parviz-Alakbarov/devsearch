import uuid

from django.db import models
from django.db.transaction import on_commit

from users.models import Profile


class Porject(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-vote_ratio', '-vote_total']

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset
    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        vote_count = reviews.count()
        total_vote = 0
        for vote in ('5', '4', '3', '2', '1'):
            vote_value = int(vote)
            count = reviews.filter(value=vote).count()
            total_vote += vote_value * count
        vote_ratio = (total_vote / (vote_count * 5)) * 100
        self.vote_ratio = vote_ratio
        self.vote_total = vote_count
        self.save()


class Review(models.Model):
    VOTE_TYPE = (
        ('1', 'Bad'),
        ('2', 'Not Bad'),
        ('3', 'Not Good'),
        ('4', 'Good'),
        ('5', 'Perfect')
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Porject, on_delete=models.SET_NULL, null=True)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        unique_together = [['owner', 'project']]

    def __str__(self):
        return self.VOTE_TYPE[int(self.value) - 1][1]


class Tag(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return self.name
