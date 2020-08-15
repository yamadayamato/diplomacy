from django.conf import settings
from django.core.mail import send_mail
from django.db.models import signals
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created

from core import models
from core.models.mixins import AutoSlug
from core.utils.models import super_receiver


@receiver(signals.pre_save, sender=models.Turn)
def set_to_current_turn(sender, instance, **kwargs):
    """
    Set game's current turn to `current_turn=False` before creating new turn.
    """
    try:
        old_turn = instance.game.get_current_turn()
        if not old_turn == instance:
            old_turn.current_turn = False
            old_turn.save()
    except models.Turn.DoesNotExist:
        pass


@super_receiver(signals.pre_save, base_class=AutoSlug)
def add_automatic_slug(sender, instance, **kwargs):
    """
    Fill the slug field on models inheriting from AutoSlug on pre-save.
    """
    instance.hydrate_slug()


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens. When a token is created, an e-mail is to
    be sent to the user.

    Args:
        * `sender` - View Class that sent the signal
        * `instance` -  View Instance that sent the signal
        * `reset_password_token` - Token Model Object
    """
    # send an e-mail to the user
    reset_password_url = settings.CLIENT_URL + '/reset-password/'
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(
            reset_password_url,
            reset_password_token.key
        )
    }

    # render email text
    html_template = 'user_reset_password.html'
    text_template = 'user_reset_password.txt'
    email_html_message = render_to_string(html_template, context)
    email_plaintext_message = render_to_string(text_template, context)

    send_mail(
        'Password Reset for {title}'.format(title='diplomacy.gg'),
        email_plaintext_message,
        'noreply@diplomacy.gg',
        ['to@example.com'],
        fail_silently=False,
        html_message=email_html_message,
    )
