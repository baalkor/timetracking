from django import template


register = template.Library()


@register.filter
def duration(td):
    seconds = td
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)


    return "%d:%02d:%02d" % (hours, minutes, seconds)