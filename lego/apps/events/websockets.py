from datetime import datetime

from djangorestframework_camel_case.render import camelize

from lego.apps.events.models import Event
from lego.apps.events.serializers import EventReadDetailedSerializer, RegistrationReadSerializer
from lego.apps.permissions.filters import filter_queryset
from lego.apps.websockets.groups import group_for_event, group_for_user
from lego.apps.websockets.notifiers import notify_group


def find_event_groups(user):
    """
    Find all channels groups the user belongs to as a result
    of being signed up to future events.
    """
    queryset = Event.objects.filter(start_time__gt=datetime.now())
    if not user.has_perm('/sudo/admin/events/list/'):
        queryset = filter_queryset(user, queryset)
    groups = []
    for event in queryset.all():
        groups.append(group_for_event(event))

    return groups


def notify_event_registration(type, registration, from_pool=None):
    group = group_for_event(registration.event)
    notify_registration(group, type, registration, from_pool)


def notify_failed_registration(type, registration):
    group = group_for_user(registration.user)
    notify_registration(group, type, registration)


def notify_registration(group, type, registration, from_pool=None):
    payload = RegistrationReadSerializer(registration).data
    if from_pool:
        payload['from_pool'] = from_pool

    notify_group(group, {
        'type': type,
        'payload': camelize(payload)
    })


def event_updated_notifier(event):
    group = group_for_event(event)
    serializer = EventReadDetailedSerializer(event)
    notify_group(group, {
        'type': 'EVENT_UPDATED',
        'payload': serializer.data
    })