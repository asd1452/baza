from django.db import models


class Clanak(models.Model):
    naslov = models.CharField(max_length=255)
    kratki_opis = models.CharField(max_length=255, null=True, blank=True)
    sadrzaj = models.TextField()
    vrijeme_objave = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.naslov

    class Meta:
        verbose_name_plural = 'Novosti / događaji itd.'


class Slika(models.Model):
    slika = models.ImageField(upload_to='slike')
    clanak = models.ForeignKey(Clanak, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Slike'


class Dokument(models.Model):
    naziv = models.CharField(max_length=255)
    datoteka = models.FileField(upload_to='dokumenti')

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name_plural = 'Dokumenti (izvješća itd.)'


AKTIVNOSTI_PARTNERA = (
    ('NA', 'Napajanje'),
    ('MJ', 'Mjerenje'),
    ('RR', 'RR'),
    ('PA', 'Pasivna'),
    ('TE', 'Terminalna'),
    ('PR', 'Pristup'),
    ('SO', 'Software'),
    ('RA', 'Racunala'))


class Partner(models.Model):
    ime = models.CharField(max_length=255)
    opis = models.CharField(max_length=255, null=True, blank=True)
    web = models.URLField(null=True, blank=True)
    aktivnost = models.CharField(max_length=2, choices=AKTIVNOSTI_PARTNERA)

    class Meta:
        verbose_name_plural = 'Partneri'

    def __str__(self):
        return self.ime


TIPOVI_KORISNIKA = (
    ('OP', 'Operater'),
    ('EP', 'Elektroprivreda'),
    ('PO', 'Posta'),
    ('JI', 'Javna institucija'))


class Korisnik(models.Model):
    ime = models.CharField(max_length=255)
    web = models.URLField(null=True, blank=True)
    tip = models.CharField(max_length=2, choices=TIPOVI_KORISNIKA)

    def __str__(self):
        return self.ime

    class Meta:
        verbose_name_plural = 'Korisnici'


TIPOVI_GRANDSTREAM = (
    ('ATA', 'ATA Adapteri'),
    ('BIP', 'Basic IP Telefoni'),
    ('HIP', 'High-End IP Telefoni'),
    ('WIP', 'Bezicni IP Telefoni'),
    ('ICP', 'IP Audio konferencijski telefon'),
    ('AIV', 'Android IP Video Telefoni'),
    ('VCU', 'Video konferencijski uredaji'))


class Grandstream(models.Model):
    naziv = models.CharField(max_length=255)
    web = models.URLField(null=True, blank=True)
    tip = models.CharField(max_length=3, choices=TIPOVI_GRANDSTREAM)

    def __str__(self):
        return self.naziv


class TekstMarketing(models.Model):
    naslov = models.CharField(max_length=255)
    naslov_eng = models.CharField(max_length=255, blank=True)
    sadrzaj_eng = models.TextField(blank=True)
    sadrzaj = models.TextField()

    def __str__(self):
        return self.naslov

    class Meta:
        verbose_name_plural = 'Filler tekstovi'


class Kontakt(models.Model):
    naslov = models.CharField(max_length=255)
    sadrzaj = models.TextField()
    email_adresa = models.EmailField()

    class Meta:
        verbose_name_plural = 'Ostavljene poruke'

    def __str__(self):
        return f'{self.naslov}, {self.email_adresa}'


KATEGORIJA_ZAPOSLENIH = (
    ('MA', 'Menadžment'),
    ('PR', 'Prodaja i računovodstvo'),
    ('TP', 'Tehnička podrška'))


class Zaposlenik(models.Model):
    kategorija = models.CharField(max_length=2, choices=KATEGORIJA_ZAPOSLENIH)
    uloga = models.CharField(max_length=255)
    uloga_eng = models.CharField(max_length=255, blank=True)
    ime_prezime = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Zaposlenici'

    def __str__(self):
        return f'{self.ime_prezime}, {self.uloga}'
