from flask import render_template
from wtforms.widgets.core import HTMLString, html_params, escape
from wtforms import StringField,TextField,Field
from wtforms.compat import text_type, string_types, iteritems

class WysiwygWidget(object):

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        html=''
        html+='<div class=\"btn-toolbar\" data-role=\"editor-toolbar\" data-target=\"#editor\">'
        html+='      <div class=\"btn-group\">'
        html+='        <a class=\"btn dropdown-toggle\" data-toggle=\"dropdown\" title=\"Font\"><i class=\"icon-font\"></i><b class=\"caret\"></b></a>'
        html+='          <ul class=\"dropdown-menu\">'
        html+='          </ul>'
        html+='        </div>'
        html+='      <div class=\"btn-group\">'
        html+='        <a class=\"btn dropdown-toggle\" data-toggle=\"dropdown\" title=\"Font Size\"><i class=\"icon-text-height\"></i>&nbsp;<b class=\"caret\"></b></a>'
        html+='          <ul class=\"dropdown-menu\">'
        html+='          <li><a data-edit=\"fontSize 5\"><font size=\"5\">Huge</font></a></li>'
        html+='          <li><a data-edit=\"fontSize 3\"><font size=\"3\">Normal</font></a></li>'
        html+='          <li><a data-edit=\"fontSize 1\"><font size=\"1\">Small</font></a></li>'
        html+='          </ul>'
        html+='      </div>'
        html+='      <div class=\"btn-group\">'
        html+='        <a class=\"btn\" data-edit=\"bold\" title=\"Bold (Ctrl/Cmd+B)\"><i class=\"icon-bold\"></i></a>'
        html+='        <a class=\"btn\" data-edit=\"italic\" title=\"Italic (Ctrl/Cmd+I)\"><i class=\"icon-italic\"></i></a>'
        html+='        <a class=\"btn\" data-edit=\"strikethrough\" title=\"Strikethrough\"><i class=\"icon-strikethrough\"></i></a>'
        html+='        <a class=\"btn\" data-edit=\"underline\" title=\"Underline (Ctrl/Cmd+U)\"><i class=\"icon-underline\"></i></a>'
        html+='      </div>'
        html+='      <div class=\"btn-group\">'
        html+='        <a class=\"btn\" data-edit=\"insertunorderedlist\" title=\"Bullet list\"><i class=\"icon-list-ul\"></i></a>'
        html+='        <a class=\"btn\" data-edit=\"insertorderedlist\" title=\"Number list\"><i class=\"icon-list-ol\"></i></a>'
        html+='        <a class=\"btn\" data-edit=\"outdent\" title=\"Reduce indent (Shift+Tab)\"><i class=\"icon-indent-left\"></i></a>'
        html+='        <a class=\"btn\" data-edit=\"indent\" title=\"Indent (Tab)\"><i class=\"icon-indent-right\"></i></a>'
        html+='      </div>'
        html+='      <div class=\"btn-group\">'
        html+='        <a class=\"btn\" data-edit=\"justifyleft\" title=\"Align Left (Ctrl/Cmd+L)\"><i class=\"icon-align-left\"></i></a>'
        html+='        <a class=\"btn\" data-edit=\"justifycenter\" title=\"Center (Ctrl/Cmd+E)\"><i class=\"icon-align-center\"></i></a>'
        html+='        <a class=\"btn\" data-edit=\"justifyright\" title=\"Align Right (Ctrl/Cmd+R)\"><i class=\"icon-align-right\"></i></a>'
        html+='        <a class=\"btn\" data-edit=\"justifyfull\" title=\"Justify (Ctrl/Cmd+J)\"><i class=\"icon-align-justify\"></i></a>'
        html+='      </div>'
        html+='      <div class=\"btn-group\">'
        html+='        <a class=\"btn\" title=\"Insert picture (or just drag & drop)\" id=\"pictureBtn\"><i class=\"icon-picture\"></i></a>'
        html+='        <input type=\"file\" data-role=\"magic-overlay\" data-target=\"#pictureBtn\" data-edit=\"insertImage\" />'
        html+='      </div>'
        html+='      <div class=\"btn-group\">'
        html+='        <a class=\"btn\" data-edit=\"undo\" title=\"Undo (Ctrl/Cmd+Z)\"><i class=\"icon-undo\"></i></a>'
        html+='        <a class=\"btn\" data-edit=\"redo\" title=\"Redo (Ctrl/Cmd+Y)\"><i class=\"icon-repeat\"></i></a>'
        html+='      </div>'
        html+='      <input type=\"text\" data-edit=\"inserttext\" id=\"voiceBtn\" x-webkit-speech=\"\">'
        html+='    </div> '
        html+='    <div id=\"editor\" class=\"bootstrap-wysiwyg\" %s>%s</div> '  

        return HTMLString(html % (html_params(name=field.name, **kwargs), escape(text_type(field._value()))))

       
    
 


class WysiwygField(TextField):
    widget = WysiwygWidget()