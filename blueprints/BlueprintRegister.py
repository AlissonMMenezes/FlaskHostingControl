from flask import Flask
from collections import Counter
import os, re, imp

#To dynamic load works, file and main var need to have same name
class BlueprintRegister:

    def init_app(self, app_context, file_to_ignore):
        base_path = os.path.dirname(__file__)
        mask_fle_path = "{}\\{}.py"
        files_to_import = [re.sub('.pyc|.py','',file) for file in os.listdir(base_path)]
        files_counter = Counter(files_to_import)
        files_to_import = [f for f in files_counter if f not in file_to_ignore]

        for file in files_to_import:
            try:
                if os.path.isfile(mask_fle_path.format(base_path, file)):
                    module = imp.load_source(file, mask_fle_path.format(base_path, file))
                    blueprint_load = getattr(module, file.lower())
                    app_context.register_blueprint(blueprint_load)
                               
            except Exception as e:
                print e        
                 