from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from django.http import JsonResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from django.db.models import Count
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from .models import *
from .serializers import *
import sys

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from rest_framework.decorators import action


# Create your views here.

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def post(self, request, format=None):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(obj.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def get_home_score (self, request, pk=None):
        match = self.get_object()
        players = match.matchplayer_set.filter(team = match.homeTeamId)
        points = 0
        for p in players:
            points += (1 * match.event_set.filter(player1=p, event_type="1P").count()) + (
                        2 * match.event_set.filter(player1=p, event_type="2P").count()) + (
                        3 * match.event_set.filter(player1=p, event_type="3P").count())
        result = {"home_score":points}
        return JsonResponse(result)
    
    @action(detail=True, methods=['get'])
    def get_away_score (self, request, pk=None):
        match = self.get_object()
        players = match.matchplayer_set.filter(team = match.awayTeamId)
        points = 0
        for p in players:
            points += (1 * match.event_set.filter(player1=p, event_type="1P").count()) + (
                        2 * match.event_set.filter(player1=p, event_type="2P").count()) + (
                        3 * match.event_set.filter(player1=p, event_type="3P").count())
        result = {"away_score":points}
        return JsonResponse(result)
        

    @action(detail=True, methods=['get'])
    def pdf_gen(self, request, pk=None):
        match = self.get_object()

        response = HttpResponse(content_type='application/pdf')
        response[
            'Content-Disposition'] = f'attachment; filename="Protokoll {match.homeTeamId.name} vs {match.awayTeamId}"'

        doc = SimpleDocTemplate(response, pagesize=letter)

        def point_sum(player):
            # helper function to sum points total for player
            points = 0
            points += (1 * match.event_set.filter(player1=player, event_type="1P").count()) + (
                        2 * match.event_set.filter(player1=player, event_type="2P").count()) + (
                                  3 * match.event_set.filter(player1=player, event_type="3P").count())
            print(points, sys.stderr)
            return str(points)

            # Helper function to get foul sum of player

        def foul_sum(player):
            fouls = 0
            fouls += (match.event_set.filter(player1=player, event_type="FO").count() + match.event_set.filter(
                player1=player, event_type="FP").count())
            return str(fouls)

        def populate_data(team):
            data = [['#', 'Namn', 'Poäng', 'Foul'], ]
            for p in match.matchplayer_set.all().filter(team=team):
                templst = [p.number, f"{p.player.givenName} {p.player.surname}", point_sum(p), foul_sum(p)]
                data.append(templst)

            return data

        def populate_event_chain():
            data = [["Typ", "Spelare 1", "Spelare 2", "Tid"], ]

            for e in match.event_set.all():
                fullNameP1 = f"{e.player1.player.givenName} {e.player1.player.surname}"
                fullNameP2 = f"{e.player2.player.givenName} {e.player2.player.surname}"

                templst = [e.event_type, fullNameP1, fullNameP2, str(e.time)]
                data.append(templst)
            return data

        LIST_STYLE = TableStyle()

        styles = getSampleStyleSheet()
        title_style = styles['Heading1']
        matchTimeStyle = styles['Heading2']
        titleHomeT = Paragraph(f"Hemmalag: {match.homeTeamId.name}", title_style)
        titleAwayT = Paragraph(f"Bortalag: {match.awayTeamId.name}", title_style)
        titleEvents = Paragraph(f"Händelser", title_style)
        titleMain = Paragraph(f"{match.homeTeamId.name} VS {match.awayTeamId.name}", title_style)
        titleMatchTime = Paragraph(f"Starttid: {match.startTime}", matchTimeStyle)
        # titleMatchId = Paragraph(f"Match nr: {match.Id}")

        homeT_data = populate_data(match.homeTeamId)
        awayT_data = populate_data(match.awayTeamId)
        event_chain_data = populate_event_chain()

        tableHomeT = Table(homeT_data)
        tableAwayT = Table(awayT_data)
        tableEvent = Table(event_chain_data)

        tableHomeT.setStyle(LIST_STYLE)
        LIST_STYLE.alignment = 0
        title_style.alignment = 1
        matchTimeStyle.alignment = 0
        # matchIdStyle.alignment = 2

        spacer = Spacer(1, 12)

        doc.build([titleMain, titleMatchTime, spacer, titleHomeT, tableHomeT, spacer, titleAwayT, tableAwayT, spacer,
                   titleEvents, tableEvent])

        return response


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class MatchPlayerViewSet(viewsets.ModelViewSet):
    queryset = MatchPlayer.objects.all()
    serializer_class = MatchPlayerSerializer


class MatchAdminViewSet(viewsets.ModelViewSet):
    queryset = MatchAdmin.objects.all()
    serializer_class = MatchAdminSerializer
