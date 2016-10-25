from rest_framework import routers

from lego.apps.articles.views.articles import ArticlesViewSet
from lego.apps.comments.views import CommentViewSet
from lego.apps.events.views import EventViewSet, PoolViewSet, RegistrationViewSet
from lego.apps.feed.views import NotificationFeedViewSet
from lego.apps.flatpages.views import PageViewSet
from lego.apps.meetings.views import MeetingInvitationViewSet, MeetingViewSet
from lego.apps.oauth.views import AccessTokenViewSet, ApplicationViewSet
from lego.apps.quotes.views import QuoteViewSet
from lego.apps.reactions.views import ReactionTypeViewSet, ReactionViewSet
from lego.apps.search.views import AutocompleteViewSet, SearchViewSet
from lego.apps.users.views.abakus_groups import AbakusGroupViewSet
from lego.apps.users.views.users import UsersViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticlesViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'events', EventViewSet)
router.register(r'events/(?P<event_pk>\d+)/pools', PoolViewSet)
router.register(r'events/(?P<event_pk>\d+)/registrations',
                RegistrationViewSet, base_name='registrations')
router.register(r'groups', AbakusGroupViewSet)
router.register(r'meetings', MeetingViewSet)
router.register(r'meetings/(?P<meeting_pk>[^/]+)/invitations',
                MeetingInvitationViewSet, base_name='meeting-invitations')
router.register(r'notifications', NotificationFeedViewSet, base_name='feed-notifications')
router.register(r'oauth2/access-tokens', AccessTokenViewSet)
router.register(r'oauth2/applications', ApplicationViewSet)
router.register(r'pages', PageViewSet)
router.register(r'search/autocomplete', AutocompleteViewSet, base_name='autocomplete')
router.register(r'quotes', QuoteViewSet)
router.register(r'search/search', SearchViewSet, base_name='search')
router.register(r'users', UsersViewSet)
router.register(r'reactions', ReactionViewSet)
router.register(r'reaction_types', ReactionTypeViewSet)
