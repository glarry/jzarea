# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.utils.timezone import now

class BasePublishModel(models.Model):
	is_publish = models.BooleanField(_(u"發佈"), default=True)
	upload_date = models.DateTimeField(_(u"上傳日期"), auto_now_add=True)
	publish_date = models.DateTimeField(_(u"發佈日期"), blank=True, null=True)
	expiry_date = models.DateTimeField(_(u"到期日期"), blank=True, null=True)

	class Meta:
		abstract = True

	@property
	def is_active(self):
		if not self.is_publish:
			return False

		if (not self.publish_date or self.publish_date <= now()) and (not self.expiry_date or self.expiry_date >= now()):
			return True
		else:
			return False

class Picture(BasePublishModel):
	image = models.ImageField(u'首頁圖片', upload_to='picture_main', max_length=255)

	class Meta:
		verbose_name = u'首頁圖片'
		verbose_name_plural = u'首頁圖片'

	# def __unicode__(self):
	# 	return self.id

	def image_tag(self):
		return '<img style="width:100px;height:100px" src="' + self.image.url + '" />'

	image_tag.short_description = _(u"照片")
	image_tag.allow_tags = True