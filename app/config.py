from environ import config, to_config, var

@config
class Config:
    PLACE: str = var(default=None)
    
CONFIG: Config = to_config(Config)
