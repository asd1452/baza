from rest_framework import serializers
from .models import *


class KorisnikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korisnik
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class SlikaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slika
        fields = '__all__'


class TekstMarketingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TekstMarketing
        fields = '__all__'


class ClanakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clanak
        fields = '__all__'


class DokumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dokument
        fields = '__all__'


class GrandstreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grandstream
        fields = '__all__'


class KontaktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kontakt
        fields = '__all__'

class ZaposlenikSerializer(serializers.ModelSerializer):
    class Meta:
        model=Zaposlenik
        fields='__all__'
