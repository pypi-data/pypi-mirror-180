import importlib
import traceback

from poe import aspect
from poe.logger import logger
from poe.utility import load_config


@aspect.log
class Locators(object):

    def __init__(self):
        self.config = load_config()
        try:
            self.locators_package_path = self.config['LOCATORS']['path']
        except KeyError:
            raise KeyError(
                'Can locate package with locators. "locators_package_path" is not set in LOCATORS section in [poe.ini]')
        except Exception as e:
            logger.error('\n'.join([str(e), traceback.format_exc()]))
            raise e

    def __get__(self, obj, owner):
        """Gets the page locators"""
        module_name = obj.__module__.split('.')[-1]
        locators_class = getattr(importlib.import_module(f'{self.locators_package_path}.{module_name}_locators'),
                                 f'{owner.__name__}Locators')
        return locators_class()


@aspect.log
class AllLocators(object):
    def __get__(self, obj, owner):
        """Gets the page locators"""
        lista_locatora = []
        with os.scandir(
                r'C:\Users\milan.ranisavljevic\PycharmProjects\test-automation-vdi\consts\lensapps\locators') as entries:
            for entry in entries:
                module = (entry.name)[:-3]
                classname = ''.join(list(map(lambda word: word.capitalize(), module.split('_'))))
                print(classname)
                if ('EulaPopupLocators' == classname or classname == 'Init' or module == '__pycach'):
                    continue
                print(len(lista_locatora))
                print(lista_locatora)
                locator_class = getattr(importlib.import_module(f'consts.lensapps.locators.{module}'), f'{classname}')
                lista_locatora.append(locator_class(obj.driver.capabilities.get("platformName").lower()))
        return lista_locatora
