from django import template

register = template.Library()

@register.filter
def get_token(track_dict, track):
    return track_dict[track].token