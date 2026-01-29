
import logging
from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver, Signal
from django.core.cache import cache

from .models import Topic, TopicActivity

logger = logging.getLogger(__name__)


topic_changed = Signal()



@receiver(m2m_changed, sender=Topic.subscribers.through)
def topic_subscribers_changed(sender, instance, action, pk_set, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        for user_id in pk_set:
            cache.delete(f"user:{user_id}:topics")



@receiver(post_save, sender=Topic)
def topic_post_save(sender, instance, created, **kwargs):
    if created:
        TopicActivity.objects.create(
            topic=instance,
            action="created",
        )
        topic_changed.send(
            sender=sender,
            topic_id=instance.id,
            action="created",
        )



@receiver(post_delete, sender=Topic)
def topic_post_delete(sender, instance, **kwargs):
    TopicActivity.objects.create(
        topic=instance,
        action="deleted",
    )
    topic_changed.send(
        sender=sender,
        topic_id=instance.id,
        action="deleted",
    )



@receiver(topic_changed)
def handle_topic_changed(sender, topic_id, action, **kwargs):
    logger.info(f"Topic {topic_id} changed: {action}")

    topic = Topic.objects.filter(id=topic_id).first()
    if not topic:
        return

    for user in topic.subscribers.all():
        cache.delete(f"user:{user.id}:topics") 
            
