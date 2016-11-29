class Test:
    FOO = 'test'


class Development:
    FOO = 'development'


class Production:
    FOO = 'production'


environments = {
    'test': Test,
    'development': Development,
    'production': Production,
}
