from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = ('title', 'content',)

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'
		read_only_fields = ('article',)			# article 정보는 따로 입력하지 않겠다. 
		# 즉 사용자가 입력하는게 아니라 자동으로 처리되게끔 해달라


class ArticleSerializer(serializers.ModelSerializer):
	# comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	comment_set = CommentSerializer(many=True, read_only=True)
	comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
	class Meta:
		model = Article
		fields = '__all__'

