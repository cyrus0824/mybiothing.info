# -*- coding: utf-8 -*-
# Simple template example used to instantiate a new biothing API
from mybiothing.www.index_base import main
from myexample.settings.example_settings import MyExampleSettings

myexample_settings = MyExampleSettings()

if __name__ == '__main__':
    main(myexample_settings.return_applist())