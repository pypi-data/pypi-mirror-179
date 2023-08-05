from data_idr_access.singleton import AccessorSingleton as DataAccess


def access():
    return DataAccess


def create(db_type, config_json):
    return DataAccess.get_instance(db_type, config_json)


def clean(db_type, config_json):
    DataAccess.clean_instance(db_type, config_json)


def recreate(db_type, config_json):
    DataAccess.clean_instance(db_type, config_json)
    return DataAccess.get_instance(db_type, config_json)


def list_instance_keys():
    return DataAccess.list_keys()


def list_instance():
    return DataAccess.list_instances()


def delete_instance(key):
    return DataAccess.delete_instance(key)
