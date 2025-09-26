from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Post

@registry.register_document
class PostDocument(Document):
    """
    Elasticsearch document for Post model.
    This defines how Post objects are indexed and searched.
    """
    
    # Custom field definitions for better search
    title = fields.TextField(
        analyzer='standard',  # Built-in analyzer for full-text search
        fields={
            'raw': fields.KeywordField(),  # For exact matches
            'suggest': fields.TextField(analyzer='simple'),  # For suggestions
        }
    )
    
    body = fields.TextField(
        analyzer='standard',
        fields={
            'raw': fields.KeywordField(),
        }
    )
    
    # Index the author's username
    author = fields.TextField(
        attr='author.username',  # Django relationship traversal
        fields={
            'raw': fields.KeywordField(),
        }
    )
    
    # Index tags as text for searching
    tags = fields.TextField(
        attr='tags_indexing',  # Custom method we'll add to Post model
        fields={
            'raw': fields.KeywordField(),
        }
    )

    class Index:
        name = 'blog_posts'  # Elasticsearch index name
        settings = {
            'number_of_shards': 1,    # Single shard for development
            'number_of_replicas': 0   # No replicas for development
        }

    class Django:
        model = Post  # The Django model to index
        fields = [
            'slug',
            'publish',
            'created',
            'updated',
            'status',
        ]
        
        # Index in batches of 50 for better performance
        queryset_pagination = 50

    def get_queryset(self):
        """Only index published posts"""
        return super().get_queryset().filter(status='published')