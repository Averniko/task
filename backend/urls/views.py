import logging

from django.http import HttpResponseRedirect
from rest_framework import generics, permissions, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.settings import r
from urls.models import Url
from urls.serializers import UrlSerializer


class UrlView(generics.ListCreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    pagination_class = PageNumberPagination
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(session_key=request.session.session_key)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        data["session_key"] = request.session.session_key
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class RedirectView(APIView):
    def get(self, request, path, *args, **kwargs):
        session_key = request.session.session_key
        cache = r.hmget(session_key, keys=[path]) or {}
        if cache and cache[0] is not None:
            redirect = cache[0].decode("utf-8")
            logging.info(
                f"Url get from cache. session_key={session_key} subpart={path} redirect={redirect}"
            )
        else:
            try:
                url = Url.objects.get(session_key=session_key, subpart=path)
                redirect = url.redirect
                old_cache = r.hgetall(session_key) or {}
                old_cache[url.subpart] = url.redirect
                r.hmset(session_key, old_cache)
                logging.info(
                    f"Url added to cache. session_key={session_key} subpart={path} redirect={redirect}"
                )
            except Url.DoesNotExist:
                logging.error(
                    f"Requested url does not exist. session_key={session_key} subpart={path}"
                )
                return Response(status=400)
        return HttpResponseRedirect(redirect_to=redirect)
