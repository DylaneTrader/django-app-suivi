from .models import Notification

def notifications_processor(request):
    """Add notifications to template context"""
    if request.user.is_authenticated:
        recent_notifications = Notification.objects.filter(user=request.user)[:5]
        unread_count = Notification.objects.filter(user=request.user, is_read=False).count()
        return {
            'recent_notifications': recent_notifications,
            'unread_notifications_count': unread_count,
        }
    return {}
