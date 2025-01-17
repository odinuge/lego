from rest_framework import (
    decorators,
    exceptions,
    permissions,
    renderers,
    status,
    viewsets,
)
from rest_framework.response import Response

from lego.apps.files.exceptions import UnknownFileType

from .models import File
from .serializers import FileUploadSerializer
from .utils import prepare_file_upload
from .validators import KEY_REGEX_RAW


class FileViewSet(viewsets.GenericViewSet):

    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [renderers.JSONRenderer]
    queryset = File.objects.all()
    serializer_class = FileUploadSerializer
    lookup_field = "key"
    lookup_value_regex = KEY_REGEX_RAW

    def create(self, request, *args, **kwargs):
        """
        Upload new file. This method returns instructions to the client on how to upload the file.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        key = serializer.validated_data["key"]
        public = serializer.validated_data.get("public", None)

        try:
            file_key, url, fields, token = prepare_file_upload(
                key, request.user, public
            )
        except UnknownFileType as e:
            raise exceptions.ParseError from e

        return Response(
            {"url": url, "file_key": file_key, "file_token": token, "fields": fields},
            status=status.HTTP_201_CREATED,
        )

    @decorators.action(
        detail=True,
        methods=["GET"],
        permission_classes=[permissions.AllowAny],
        authentication_classes=[],
    )
    def upload_success(self, request, *args, **kwargs):
        """
        The client is redirected to this view when a upload succeeds. This view will inform the
        client with necessary data to change a file on a instance.
        """
        instance = self.get_object()
        instance.upload_done()
        return Response({})
