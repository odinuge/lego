
from lego.apps.notifications.constants import ANNOUNCEMENT
from lego.apps.notifications.notification import Notification


class AnnouncementNotification(Notification):

    name = ANNOUNCEMENT

    def generate_mail(self):
        announcement = self.kwargs['announcement']

        return self._delay_mail(
            to_email=self.user.email_address,
            context={
                'name': self.user.full_name,
                'created_by': announcement.created_by,
                'message': announcement.message
            },
            subject=f'Viktig melding fra {announcement.created_by.full_name}',
            plain_template='notifications/email/announcement.txt',
            html_template='notifications/email/announcement.html',
        )

    def generate_push(self):
        announcement = self.kwargs['announcement']

        return self._delay_push(
            template='notifications/push/announcement.txt',
            context={
                'created_by': announcement.created_by,
            },
            instance=announcement
        )