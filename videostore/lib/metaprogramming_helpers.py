

class LeafSubclassRetriever:
    """
    http://code.activestate.com/recipes/577858-concrete-class-finder/
    """

    def __init__(self, base_class):
        self.base_class = base_class

    def value(self):
        direct_subclasses = self.base_class.__subclasses__()
        leaf_subclasses = list()
        for klass in direct_subclasses:
          if( len(klass.__subclasses__()) > 0 ):
                leaf_subclasses += LeafSubclassRetriever(klass).value()
          else:
                leaf_subclasses.append(klass)

        return leaf_subclasses


def leaf_subclasses(klass):
    return LeafSubclassRetriever(klass).value()


def import_from_string(full_name):
    """
    Used to obtain various objects (classes, variables, functions...) from
    string paths.
    Usage:
        import_from_string('dspmobi_backend.models.Campaign')
        import_from_string('dspmobi_backend.models.campaign.query.CAMPAIGN_STATUSES')
    """
    import importlib

    module, obj_name = full_name.rsplit('.', 1)
    obj = getattr(importlib.import_module(module), obj_name)

    return obj
