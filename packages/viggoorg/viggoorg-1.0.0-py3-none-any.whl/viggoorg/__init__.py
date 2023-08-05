import os
import viggocore
import viggolocal

from flask_cors import CORS

from viggocore import System
# from viggolocal.subsystem.sysadmin import ibge_sync
# from viggolocal.subsystem.parametrizacao.localidade \
#     import regiao, uf, mesorregiao, microrregiao, municipio

from viggoorg.subsystem.sysadmin import domain_org
from viggoorg.resources import SYSADMIN_EXCLUSIVE_POLICIES, \
    SYSADMIN_RESOURCES, USER_RESOURCES


system = System('viggoorg',
                [domain_org.subsystem],
                USER_RESOURCES,
                SYSADMIN_RESOURCES,
                SYSADMIN_EXCLUSIVE_POLICIES)


class SystemFlask(viggocore.SystemFlask):

    def __init__(self):
        super().__init__(system, viggolocal.system)

    def configure(self):
        origins_urls = os.environ.get('ORIGINS_URLS', '*')
        CORS(self, resources={r'/*': {'origins': origins_urls}})

        self.config['BASEDIR'] = os.path.abspath(os.path.dirname(__file__))
        self.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        viggoorg_database_uri = os.getenv('VIGGOORG_DATABASE_URI', None)
        if viggoorg_database_uri is None:
            raise Exception('VIGGOORG_DATABASE_URI not defined in enviroment.')
        else:
            # URL os enviroment example for MySQL
            # export VIGGOORG_DATABASE_URI=
            # mysql+pymysql://root:mysql@localhost:3306/viggoorg
            self.config['SQLALCHEMY_DATABASE_URI'] = viggoorg_database_uri
