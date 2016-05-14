from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, StringField, validators, TextAreaField


class Reg(Form):
    name = StringField('姓名', [validators.required()], description="你的姓名")
    stucode = StringField('学号', [validators.required()], description="你的学号")
    qq = StringField('QQ', [validators.required()], description="留下QQ便于我们联系")
    phone = StringField('手机', [validators.required()], description="我们将用短信通知您最新信息!")
    button = SubmitField('提交')


class RegWithTeam(Form):
    name = StringField('组长姓名', [validators.required()], description="你的姓名")
    stucode = StringField('组长学号', [validators.required()], description="你的学号")
    qq = StringField('组长QQ', [validators.required()], description="留下QQ便于我们联系")
    phone = StringField('组长手机', [validators.required()], description="我们将用短信通知您最新信息!")
    team = TextAreaField('队员信息', description="组队参加请按照\"姓名 学号\"一人一行填写在文本框内 如: 王尼玛 22150xxxx")
    button = SubmitField('提交')


class UploadFile(Form):
    homework = FileField('你的作品', validators=[
        FileRequired(message='请选择文件'),
        FileAllowed(['zip','rar'], '请使用zip或rar压缩格式提交')
    ])
    button = SubmitField('提交')


class Login(Form):
    user = StringField('姓名', [validators.required()], description="就是你的名字")
    pwd = StringField('密码', [validators.required()], description="学号")
    button = SubmitField('提交')


class TeamModify(Form):
    team = TextAreaField('队员信息', description="组队参加请按照\"姓名 学号\"一人一行填写在文本框内 如: 王尼玛 22150xxxx")
    button = SubmitField('提交')