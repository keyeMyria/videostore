from .test import Test
from .development import Development
from .production import Production


environments = {
    'test': Test,
    'development': Development,
    'production': Production,
}
