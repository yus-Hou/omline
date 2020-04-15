"""
Django settings for my_blog project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
from django.db.backends.mysql.base import DatabaseWrapper
DatabaseWrapper.data_types['DateTimeField'] = 'datetime' # fix for MySQL 5.5
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%x#u%3slfv*v53rrmg6=2zgffdq3ensa_iaclxh#d($6(luckl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#允许的服务器
ALLOWED_HOSTS = ['*']

# 静态文件收集目录
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'WARNING',
            # 'class': 'logging.FileHandler',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'backupCount': 30,
            'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file', 'mail_admins'],
            'level': 'WARNING',
            'propagate': False,
        },
    }
}
# Application definition


INSTALLED_APPS = [
    #simpleui
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'article',
    'userprofile',
    'password_reset',#三方库用于密码找回
    'comment',
    'taggit',#标签
    'ckeditor',#富文本编辑器
    'mptt',#多级评论
    'notifications',#消息通知
    'notice',#处理回复消息模块
    #提供第三方登录
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #添加需要的第三方
    'allauth.socialaccount.providers.weixin',
    'allauth.socialaccount.providers.weibo',
    'allauth.socialaccount.providers.github',



]
#simple基本配置
SIMPLEUI_HOME_QUICK = False
SIMPLEUI_HOME_INFO = False
SIMPLEUI_HOME_TITLE = '人才交流网'


import time
SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menu_display': ['站点首页', '帖子管理','用户评论管理','用户信息维护','权限认证', '动态菜单测试'],      # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'dynamic': True,    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'menus': [{
        'name': '站点首页',
        'icon': 'fas fa-paper-plane',
        'url': 'http://127.0.0.1:8000/'
    }, {
        'app': 'auth',
        'name': '权限认证',
        'icon': 'fas fa-user-shield',
        'models': [{
            'name': '用户管理',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }]
    }, {
        'app' : 'article',
        'name': '帖子管理',
        'icon': '',
        'models': [{
            'name': '所有帖子',
            'url': 'article/article',
            'icon': 'fas fa-newspaper'
        },{
            'name' : '文章栏目',
            'url' : 'article/articlecolumn',
            'icon' : 'fas fa-columns',
        }],

    },


        {
            'app' : 'comment',
            'name' : '用户评论管理',
            'icon' : 'fas fa-comments',
            'models' : [{
                'name' : '评论',
                'url' : 'comment/comment',
                'icon' : '',
            }]
        },
        {
            'app' : 'userprofile',
            'name': '用户信息维护',
            'icon':'',
            'models' : [{
                'name' : '用户信息',
                'url' : 'auth/user',
                'icon' :'',
            }]

        },

    ]
}












SITE_ID = 1

#登录成功后重定向地址
LOGIN_REDIRECT_URL = '/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'article.context_processor.show_avatar',


            ],
            'libraries' : {
                'mytags' : 'article.templatetags.my_filters_and_tags',
            }
        },
    },
]



AUTHENTICATION_BACKENDS = (
    # Django 后台可独立于 allauth 登录
    'django.contrib.auth.backends.ModelBackend',

    # 配置 allauth 独有的认证方法，如 email 登录
    # 'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'my_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "my_blog",
        'USER': "root",
        'PASSWORD': "root",
        'HOST': "LocalHost",
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'ASIA/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False  #默认为True使用的时UTC时间改为False

#富文本编辑器
CKEDITOR_CONFIGS = {
    # django-ckeditor默认使用default配置
    'default': {
        # 编辑器宽度自适应
        'width':'auto',
        'height':'250px',
        # tab键转换空格数
        'tabSpaces': 4,
        # 工具栏风格
        'toolbar': 'Custom',
        # 工具栏按钮
        'toolbar_Custom': [
            # 表情 代码块
            ['Smiley', 'CodeSnippet'],
            # 字体风格
            ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
            # 字体颜色
            ['TextColor', 'BGColor'],
            # 链接
            ['Link', 'Unlink'],
            # 列表
            ['NumberedList', 'BulletedList'],
            # 最大化
            ['Maximize']
        ],
        # 'removePlugins':'stylesheetparser',
        # 加入代码块插件
        'extraPlugins': ','.join(['codesnippet',]),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT= os.path.join(BASE_DIR, 'media/')
# SMTP服务器
EMAIL_HOST = 'smtp.qq.com'

EMAIL_HOST_USER = '1174935071@qq.com'
# 邮箱授权码
EMAIL_HOST_PASSWORD = 'iljncsgjragujcjb'
# 发送邮件的端口
EMAIL_PORT = 25
# 是否使用 TLS
EMAIL_USE_TLS = True
# 默认的发件人
DEFAULT_FROM_EMAIL = 'Hys的个人博客 <1174935071@qq.com>'