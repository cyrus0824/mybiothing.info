# -*- coding: utf-8 -*-
# Simple template example used to instantiate a new biothing API
from biothings.www.index_base import main
from ${src_package}.settings.${src_package}_settings import ${settings_class}

${src_package}_settings = ${settings_class}()

if __name__ == '__main__':
    main(${src_package}_settings.return_applist())