from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, News, NewsCategory
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView


def department_query():
    return db.session.query(Department)


class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    #base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department':  QuerySelectField('Department',
                                query_factory=department_query,
                                widget=Select2Widget(extra_classes="readonly"))}


    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']

class MenuItemView(ModelView):
    datamodel = SQLAInterface(MenuItem)
    list_columns = ['id', 'name', 'link', 'menu_category_id']

class MenuCategoryView(ModelView):
    datamodel = SQLAInterface(MenuCategory)
    list_columns = ['id', 'name']

class NewsView(ModelView):
    datamodel = SQLAInterface(News)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']

class NewsCategoryView(ModelView):
    datamodel = SQLAInterface(NewsCategory)
    list_columns = ['id', 'name']

class NewsPageView(BaseView):
    default_view = 'local_news'

    @expose('/local_news/')
    def local_news(self):
        param1 = 'Local News'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)

    @expose('/global_news/')
    def global_news(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)
        
    @expose('/error_page/')
    def error_page(self):
        param1 = 'error'
        self.update_redirect()
        return self.render_template('404.html', param1=param1)


db.create_all()

""" Page View """
appbuilder.add_view(NewsPageView, 'Local News', category="News")
appbuilder.add_link("Global News", href="/newspageview/global_news/", category="News")



appbuilder.add_link("Projects", href="/newspageview/error_page/", category="Resources")
appbuilder.add_link("Challenges", href="/newspageview/error_page/", category="Resources")
appbuilder.add_link("Docs", href="/newspageview/error_page/", category="Resources")
appbuilder.add_link("Cheatsheets", href="/newspageview/error_page/", category="Resources")
appbuilder.add_link("Articles", href="/newspageview/error_page/", category="Resources")
appbuilder.add_link("Videos", href="/newspageview/error_page/", category="Resources")
appbuilder.add_link("Blog", href="/newspageview/error_page/", category="Resources")
appbuilder.add_link("Career_Center", href="/newspageview/error_page/", category="Resources")


appbuilder.add_link("Forums", href="/newspageview/error_page/", category="Community")
appbuilder.add_link("Chat", href="/newspageview/error_page/", category="Community")
appbuilder.add_link("Chapters", href="/newspageview/error_page/", category="Community")
appbuilder.add_link("Events", href="/newspageview/error_page/", category="Community")
appbuilder.add_link("Learner Stories", href="/newspageview/error_page/", category="Community")







""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")

