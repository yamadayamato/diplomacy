from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path(
        'game-filter-choices',
        views.GameFilterChoicesView.as_view(),
        name='game-filter-choices'
    ),
    path(
        'games',
        views.ListGames.as_view(),
        name='list-games'
    ),
    path(
        'games/create',
        views.CreateGameView.as_view(),
        name='create-game'
    ),
    re_path(
        r'game/(?P<slug>[_\-\w]+)/join',
        views.ToggleJoinGame.as_view(),
        name='toggle-join-game'
    ),
    re_path(
        r'game/finalize/(?P<pk>[0-9]+)',
        views.ToggleFinalizeOrdersView.as_view(),
        name='toggle-finalize-orders'
    ),
    re_path(
        r'game/(?P<slug>[_\-\w]+)/order$',
        views.CreateOrderView.as_view(),
        name='order'
    ),
    re_path(
        r'game/(?P<pk>[0-9]+)/orders$',
        views.ListOrdersView.as_view(),
        name='orders'
    ),
    re_path(
        r'game/(?P<slug>[_\-\w]+)$',
        views.GameStateView.as_view(),
        name='game-state'
    ),
    path(
        'variants',
        views.ListVariants.as_view(),
        name='list-variants'
    ),
    re_path(
        r'game/surrender/(?P<pk>[0-9]+)',
        views.ToggleSurrenderView.as_view(),
        name='toggle-surrender',
    ),
    path(
        'password_reset/',
        include('django_rest_passwordreset.urls', namespace='password_reset')
    ),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
]
