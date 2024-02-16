from django.db import models
from django_quill.fields import QuillField

# Create your models here.
class PT(models.Model):
    id_pt = models.IntegerField(unique=True, auto_created=True)
    nama_pt = models.TextField()
    logo = models.ImageField(upload_to='productionfiles/uploaded_image/logo/')

class Tentang(models.Model):
    id_tentang = models.IntegerField(unique=True, auto_created=True)
    detail = models.TextField(max_length=255)
    visi = models.TextField(max_length=255)
    misi = QuillField()
    
class Sejarah(models.Model):
    id_sejarah = models.IntegerField(unique=True, auto_created=True)
    tahun = models.DateField()
    deskripsi = models.TextField(max_length=255)
    
class Greeting(models.Model):
    id_greeting = models.IntegerField(unique=True, auto_created=True)
    teks = models.TextField(max_length=500)
    
class Services(models.Model):
    id_sejarah = models.IntegerField(unique=True, auto_created=True)
    nama_service = models.TextField(max_length=255)
    deskripsi_service = QuillField()
    
class Project(models.Model):
    id_project = models.IntegerField(unique=True, auto_created=True)
    nama_project = models.TextField(max_length=255)
    service = models.TextField(max_length=255)
    nama_client = models.TextField(max_length=255)
    foto_client = models.ImageField(upload_to='productionfiles/uploaded_image/client/')

class Jabatan(models.Model):
    id_jabatan = models.IntegerField(unique=True, auto_created=True)
    nama_jabatan = models.TextField(max_length=255)
    
class Team(models.Model):
    id_team = models.IntegerField(unique=True, auto_created=True)
    nama = models.TextField(max_length=255)
    jabatan = models.TextField(max_length=255)
    foto_tim = models.ImageField(upload_to='productionfiles/uploaded_image/tim/')
    
class Testimoni(models.Model):
    id_testimoni = models.IntegerField(unique=True, auto_created=True)
    nama = models.TextField(max_length=255)
    deskripsi = models.TextField(max_length=255)