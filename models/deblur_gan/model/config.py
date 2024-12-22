from pydantic import BaseModel


class DeBlurConfig(BaseModel):
    norm_layer:str = 'instance'
    weight_path:str = 'fpn_inception.h5'
