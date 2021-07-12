from django.db import models


class Question1(models.Model):
    userid = models.fields.IntegerField()
    q1_result1 = models.fields.IntegerField()
    q1_result2 = models.fields.IntegerField()
    q1_result3 = models.fields.IntegerField()
    q1_result4 = models.fields.IntegerField()
    q1_result5 = models.fields.IntegerField()


class Question2(models.Model):
    userid = models.fields.IntegerField()
    q2_result1 = models.fields.IntegerField()
    q2_result2 = models.fields.IntegerField()
    q2_result3 = models.fields.IntegerField()
    q2_result4 = models.fields.IntegerField()
    q2_result5 = models.fields.IntegerField()


class Question3(models.Model):
    userid = models.fields.IntegerField()
    q3_result1 = models.fields.IntegerField()
    q3_result2 = models.fields.IntegerField()
    q3_result3 = models.fields.IntegerField()
    q3_result4 = models.fields.IntegerField()
    q3_result5 = models.fields.IntegerField()


class Question4(models.Model):
    userid = models.fields.IntegerField()
    q4_result1 = models.fields.IntegerField()
    q4_result2 = models.fields.IntegerField()
    q4_result3 = models.fields.IntegerField()
    q4_result4 = models.fields.IntegerField()
    q4_result5 = models.fields.IntegerField()


class Question5(models.Model):
    userid = models.fields.IntegerField()
    q5_result1 = models.fields.IntegerField()
    q5_result2 = models.fields.IntegerField()
    q5_result3 = models.fields.IntegerField()
    q5_result4 = models.fields.IntegerField()
    q5_result5 = models.fields.IntegerField()

