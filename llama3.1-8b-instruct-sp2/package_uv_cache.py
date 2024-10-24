import bentoml
import shutil


with bentoml.models.create( name='uv_cache') as model_ref:
    shutil.copytree('uv_cache', model_ref.path, dirs_exist_ok=True, symlinks=True)
    
