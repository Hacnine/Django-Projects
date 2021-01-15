from django.apps import AppConfig


class CodeBlogConfig(AppConfig):
    name = 'code_blog'

    def ready(self):
        import code_blog.signals
