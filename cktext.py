from wtforms import TextAreaField
from wtforms.widgets import TextArea
 
class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)
 
 
class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()
