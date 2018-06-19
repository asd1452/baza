from rest_framework.generics import ListAPIView  # read-only endpoint
from rest_framework.generics import CreateAPIView  # za kontakt formu
from .serializers import *
from .models import *


class DokumentView(ListAPIView):
    queryset = Dokument.objects.all()
    serializer_class = DokumentSerializer


class TekstMarketingView(ListAPIView):
    queryset = TekstMarketing.objects.all()
    serializer_class = TekstMarketingSerializer


class GrandstreamView(ListAPIView):
    queryset = Grandstream.objects.all()
    serializer_class = GrandstreamSerializer


class KorisnikView(ListAPIView):
    queryset = Korisnik.objects.all()
    serializer_class = KorisnikSerializer


class PartnerView(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class SlikaView(ListAPIView):
    queryset = Slika.objects.all()
    serializer_class = SlikaSerializer


class ClanakView(ListAPIView):
    queryset = Clanak.objects.all()
    serializer_class = ClanakSerializer


class KontaktView(CreateAPIView):
    serializer_class = KontaktSerializer
    # queryset


class ZaposlenikView(ListAPIView):
    queryset = Zaposlenik.objects.all()
    serializer_class = ZaposlenikSerializer
