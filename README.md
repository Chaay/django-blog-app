# Django Blog with Elasticsearch

A feature-rich blog application built with Django, featuring full-text search capabilities powered by Elasticsearch.

## 🚀 Features

### Core Functionality
- **Post Management**: Create, edit, and publish blog posts with rich content
- **Tagging System**: Categorize posts with tags and filter by tag
- **Comment System**: Engage with readers through post comments
- **Email Sharing**: Share posts via email with friends
- **Similar Posts**: Recommend related content based on shared tags

### Advanced Search
- **Full-Text Search**: Powerful search functionality using Elasticsearch
  - Multi-field search (title, body, author, tags)
  - Relevance ranking with field boosting (title 3x, author/tags 2x)
  - Fuzzy matching for typo tolerance
  - AND operator for precise multi-word queries
  - Real-time search results

### SEO & Performance
- **SEO Optimization**: XML sitemap generation for better search indexing
- **Markdown Support**: Write content in Markdown format with custom filters
- **Custom Template Tags**: Reusable components for latest posts, statistics
- **Pagination**: Efficient content loading with pagination

## 🛠 Tech Stack

- **Backend**: Django 4.2
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Search Engine**: Elasticsearch 8.x with django-elasticsearch-dsl
- **Tagging**: django-taggit for flexible tagging system
- **Content Formatting**: Markdown with custom template filters
- **Containerization**: Docker (for Elasticsearch)
- **Environment Management**: python-dotenv for configuration

## 📋 Prerequisites

- Python 3.9+
- Docker Desktop (for Elasticsearch)
- Git

## ⚙️ Installation

### 1. Clone and Setup Project
```bash
# Clone the repository
git clone <your-repository-url>
cd django-blog

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
### 2. Environment Configuration

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3

# Email Configuration (for sharing feature)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True

# Elasticsearch Configuration
ELASTICSEARCH_HOST=http://localhost:9200
```
### 3. Database Setup
```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load sample data (optional)
python manage.py loaddata sample_data.json
```
### 4. Elasticsearch Setup
```bash
# Start Elasticsearch with Docker
docker run -d --name elasticsearch \
  -p 9200:9200 -p 9300:9300 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  elasticsearch:8.11.0

# Verify Elasticsearch is running
curl http://localhost:9200
# Should return cluster information

# Build search index
python manage.py search_index --rebuild
# Type 'y' when prompted
```

### 5. Start Development Server
```bash
python manage.py runserver
```

## 🌐 Application URLs

| URL Pattern | Description | Example |
|-------------|-------------|---------|
| `/blog/` | Main blog homepage with all posts | `http://localhost:8000/blog/` |
| `/blog/search/` | Search functionality page | `http://localhost:8000/blog/search/` |
| `/blog/tag/<slug>/` | Posts filtered by specific tag | `http://localhost:8000/blog/tag/django/` |
| `/blog/YYYY/MM/DD/post-slug/` | Individual post detail page | `http://localhost:8000/blog/2024/09/27/my-first-post/` |
| `/blog/<post-id>/share/` | Email sharing form for specific post | `http://localhost:8000/blog/1/share/` |
| `/admin/` | Django admin interface | `http://localhost:8000/admin/` |
| `/sitemap.xml` | SEO sitemap for search engines | `http://localhost:8000/sitemap.xml` |

### URL Patterns Breakdown

- **Homepage**: Lists all published posts with pagination
- **Search**: Full-text search across posts using Elasticsearch
- **Tag Filtering**: Shows posts tagged with specific keywords
- **Post Detail**: Individual post with comments and sharing options
- **Email Sharing**: Form to share posts via email
- **Admin**: Content management interface
- **Sitemap**: XML sitemap for SEO optimization

### URL Configuration

The blog uses Django's `app_name = 'blog'` for URL namespacing:

```python
# In blog/urls.py
app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/', views.PostListView.as_view(), name='post_list_by_tag'),
    path('search/', views.post_search, name='post_search'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]
```
## 📁 Project Structure

```markdown
## 📁 Project Structure

```text
django-blog/
├── config/                  # Project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
│
├── blog/                    # Main blog app
│   ├── models.py            # Post, Comment models
│   ├── views.py             # View logic & search
│   ├── urls.py              # Blog URL patterns
│   ├── admin.py             # Admin customization
│   ├── forms.py             # Comment & sharing forms
│   ├── documents.py         # Elasticsearch mappings
│   ├── sitemaps.py          # XML sitemap generator
│   │
│   ├── templatetags/        # Custom template tags
│   │   ├── __init__.py
│   │   └── blog_tags.py     # Markdown filter, stats
│   │
│   └── templates/blog/      # HTML templates
│       ├── base.html        # Base template
│       ├── pagination.html  # Pagination component
│       └── post/
│           ├── list.html    # Post listing
│           ├── detail.html  # Post detail & comments
│           ├── search.html  # Search interface
│           └── share.html   # Email sharing form
│
├── requirements.txt         # Python dependencies
├── manage.py                # Django management
└── README.md                # Documentation
```